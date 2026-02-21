DOCSTRING_MAP_PROMPT = """
You are an expert Python developer.

Generate high-quality multi-line docstrings for EVERY function
and class in the given code using Google style.

Return ONLY valid JSON mapping names to docstrings.

STRICT RULES:

- Use Google-style docstrings
- Each docstring MUST be multi-line
- Include a short summary line
- Include Args section for parameters
- Include Returns section if applicable
- Include Raises section if exceptions are obvious
- Use correct parameter names and types if inferable
- If type unknown, omit type
- Do NOT include explanations outside JSON
- Do NOT include markdown or code fences
- Return ONLY valid JSON

Example output:

{{
  "load_data": "Load dataset from file.\\n\\nArgs:\\n    path (str): Path to the file.\\n\\nReturns:\\n    pd.DataFrame: Loaded dataset.",
  "Model": "Machine learning model for classification.\\n\\nAttributes:\\n    weights (ndarray): Model parameters."
}}

Code:
{code}
"""

README_PROMPT = """
You are an expert technical writer.

Generate a high-quality README for the following Python project.

Include:

- Project purpose
- Key features
- Main components
- Usage overview
- Dependencies (if identifiable)

Write in clear, professional Markdown.

Code sample:
{code}
"""