import ast


def chunk_python_files(python_files,
                       max_lines=2000,
                       overlap=50):

    chunks = []

    for file in python_files:

        code = file["content"]
        lines = code.splitlines()

        try:
            tree = ast.parse(code)
        except Exception:
            continue

        segments = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef,
                                 ast.AsyncFunctionDef,
                                 ast.ClassDef)):

                start = node.lineno - 1
                end = getattr(node, "end_lineno", start + 1)

                segment = "\n".join(lines[start:end])
                segments.append(segment)

        if not segments:
            segments = ["\n".join(lines)]

        combined = []
        current = ""

        for seg in segments:
            if len((current + seg).splitlines()) > max_lines:
                combined.append(current)
                current = seg
            else:
                current += "\n\n" + seg

        if current:
            combined.append(current)

        for i, chunk in enumerate(combined):

            if i > 0:
                prev_lines = combined[i-1].splitlines()
                overlap_text = "\n".join(prev_lines[-overlap:])
                chunk = overlap_text + "\n\n" + chunk

            chunks.append({
                "filename": file["filename"],
                "chunk": chunk
            })

    return chunks