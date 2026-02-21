from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import hashlib
import os
import psycopg
import json

from prompts import DOCSTRING_MAP_PROMPT, README_PROMPT
from ast_docstring_inserter import insert_docstrings

load_dotenv()

# LM CONFIG

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# 🗄️ Neon DB CONFIG

DB_URL = os.getenv("NEON_DB_URL")


def get_connection():
    return psycopg.connect(DB_URL)


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS llm_cache (
                    hash TEXT PRIMARY KEY,
                    prompt TEXT,
                    response TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()


init_db()

# 🔑 HASHING (CACHE KEY)

def get_cache_key(text):
    return hashlib.sha256(text.encode()).hexdigest()

# CACHE LOOKUP

def get_cached_response(prompt):

    key = get_cache_key(prompt)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT response FROM llm_cache WHERE hash=%s",
                (key,)
            )
            row = cur.fetchone()

    if row:
        return row[0], True

    return None, False

# SAVE TO CACHE

def save_response(prompt, response):

    key = get_cache_key(prompt)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO llm_cache (hash, prompt, response)
                VALUES (%s, %s, %s)
                ON CONFLICT (hash) DO NOTHING
                """,
                (key, prompt, response)
            )
        conn.commit()

# LLM CALL (CACHE-AWARE)

def call_openai(prompt, use_cache=True):

    if use_cache:
        cached_response, is_cached = get_cached_response(prompt)
        if is_cached:
            return cached_response, True

    response = llm.invoke(prompt)
    output = response.content

    if use_cache:
        save_response(prompt, output)

    return output, False

# FILE DOCUMENTATION USING AST INSERTION

def generate_file_documentation(chunks, python_files):

    # Use TRUE original files
    original_map = {
        f["filename"]: f["content"]
        for f in python_files
    }

    updated_files = {}
    cache_flags = {}
    validation_flags = {}
    retry_counts = {}  # kept for compatibility with app UI

    for filename, original_code in original_map.items():

        prompt = DOCSTRING_MAP_PROMPT.format(code=original_code)

        response, cached = call_openai(prompt)

        try:
            # Parse JSON docstring map
            doc_map = json.loads(response)

            # ⭐ Insert docstrings safely via AST
            updated_code = insert_docstrings(original_code, doc_map)

            is_safe = True

        except Exception:
            # Fallback to original if anything fails
            updated_code = original_code
            is_safe = False

        updated_files[filename] = updated_code
        cache_flags[filename] = cached
        validation_flags[filename] = is_safe
        retry_counts[filename] = 0  # no retries in AST mode

    return updated_files, cache_flags, validation_flags, retry_counts

# PROJECT README GENERATION

def generate_project_readme(chunks):

    sample = "\n\n".join(c["chunk"] for c in chunks[:5])

    prompt = README_PROMPT.format(code=sample)

    return call_openai(prompt)