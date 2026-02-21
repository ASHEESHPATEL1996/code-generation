import ast


def insert_docstrings(original_code, docstrings):

    tree = ast.parse(original_code)

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            name = node.name

            if name in docstrings:

                if not ast.get_docstring(node):

                    doc_node = ast.Expr(
                        value=ast.Constant(value=docstrings[name])
                    )

                    node.body.insert(0, doc_node)

    return ast.unparse(tree)