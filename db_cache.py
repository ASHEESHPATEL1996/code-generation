import os
import hashlib
import psycopg
from dotenv import load_dotenv

load_dotenv()

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


def hash_prompt(prompt):
    return hashlib.sha256(prompt.encode()).hexdigest()


def get_cached_response(prompt):

    key = hash_prompt(prompt)

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


def save_response(prompt, response):

    key = hash_prompt(prompt)

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