import tempfile
import zipfile
import os


def extract_python_files(uploaded_files):
    python_files = []

    for uploaded_file in uploaded_files:

        if uploaded_file.name.endswith(".py"):
            code = uploaded_file.read().decode("utf-8")

            python_files.append({
                "filename": uploaded_file.name,
                "content": code
            })

        elif uploaded_file.name.endswith(".zip"):

            with tempfile.TemporaryDirectory() as tmpdir:
                zip_path = os.path.join(tmpdir, uploaded_file.name)

                with open(zip_path, "wb") as f:
                    f.write(uploaded_file.read())

                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extractall(tmpdir)

                for root, _, files in os.walk(tmpdir):
                    for file in files:
                        if file.endswith(".py"):
                            path = os.path.join(root, file)

                            with open(path, "r", encoding="utf-8") as f:
                                python_files.append({
                                    "filename": file,
                                    "content": f.read()
                                })

    return python_files