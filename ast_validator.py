import ast


def normalize_ast(code):
    """
    Parse code into AST and remove docstrings for comparison.
    """

    tree = ast.parse(code)

    for node in ast.walk(tree):

        # Remove docstrings from functions/classes/modules
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):

            if (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            ):
                node.body = node.body[1:]

    return ast.dump(tree, include_attributes=False)


def is_equivalent(original_code, generated_code):
    """
    Returns True if code is equivalent except for docstrings.
    """

    try:
        return normalize_ast(original_code) == normalize_ast(generated_code)
    except Exception:
        return False