import tempfile
import os
from git import Repo


def clone_repo(repo_url):

    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(repo_url, temp_dir)

    python_files = []

    for root, _, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    python_files.append({
                        "filename": file,
                        "content": f.read()
                    })

    return python_files