import re
import ast
from typing import List, Tuple


def extract_python_regexes_ast(python_script_path: str) -> List[Tuple[int, str, str]]:
    """
    Alternative implementation using AST parsing for more robust extraction.
    This version can handle more complex cases like multi-line statements and variables.

    Args:
        python_script_path (str): Path to the Python script file

    Returns:
        List[Tuple[int, str, str]]: List of tuples containing:
            - Line number (1-indexed)
            - Original line content
            - Extracted regex pattern
    """
    regexes = []

    try:
        with open(python_script_path, "r", encoding="utf-8") as file:
            content = file.read()
            lines = content.splitlines()

        # Parse the Python file into an AST
        tree = ast.parse(content)

        class RegexVisitor(ast.NodeVisitor):
            def visit_Call(self, node):
                # Check if this is a re.match call
                if (
                    isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "re"
                    and (node.func.attr == "search" or node.func.attr == "match")
                ):

                    # Extract the first argument (the regex pattern)
                    if node.args and isinstance(node.args[0], ast.Constant):
                        # Get the string value
                        regex_pattern = node.args[0].value

                        if isinstance(regex_pattern, str):
                            line_num = node.lineno
                            # Skip commented lines
                            if line_num <= len(lines):
                                original_line = lines[line_num - 1]
                                if not re.match(r"^\s*#", original_line):
                                    regexes.append(
                                        (line_num, original_line, regex_pattern)
                                    )

                # Continue visiting child nodes
                self.generic_visit(node)

        visitor = RegexVisitor()
        visitor.visit(tree)

    except FileNotFoundError:
        raise FileNotFoundError(f"Python script not found: {python_script_path}")
    except SyntaxError as e:
        raise SyntaxError(f"Syntax error in Python script: {e}")
    except Exception as e:
        raise Exception(f"Error parsing Python script: {e}")

    return regexes


def extract_perl_regexes(perl_script_path: str) -> List[Tuple[int, str, str]]:
    """
    Extract regex patterns from a Perl script, skipping commented lines.

    Args:
        perl_script_path (str): Path to the Perl script file

    Returns:
        List[Tuple[int, str, str]]: List of tuples containing:
            - Line number (1-indexed)
            - Original line content
            - Extracted regex pattern
    """
    regexes = []

    # Common Perl regex patterns to look for
    regex_patterns = [r"/(.*?)/"]

    with open(perl_script_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            original_line = line.rstrip()

            # Skip empty lines
            if not original_line.strip():
                continue

            # Skip commented lines (lines starting with # after optional whitespace)
            if re.match(r"^\s*#", original_line):
                continue

            # Remove inline comments (but be careful with # inside strings/regexes)
            # This is a simplified approach - full Perl parsing would be more complex
            working_line = original_line

            # Look for regex patterns in the line
            for pattern in regex_patterns:
                matches = re.finditer(pattern, working_line)
                for match in matches:
                    regex_pattern = match.group(1)  # The actual regex pattern
                    flags = match.group(2) if len(match.groups()) > 1 else ""
                    assert flags == ""
                    regexes.append((line_num, original_line, regex_pattern))

    return regexes


def print_regexes(regexes: List[Tuple[int, str, str]], filename: str) -> None:
    """
    Helper function to print extracted regexes in a readable format.

    Args:
        regexes: Extracted regexes
        filename: file name
    """
    print(f"Found {len(regexes)} re.match() pattern(s) in {filename}:")
    print("-" * 60)

    for line_num, original_line, regex_pattern in regexes:
        print(f"Line {line_num}: {repr(regex_pattern)}")
        print(f"  Context: {original_line.strip()}")


def test_compare_regexes():
    perl_script = "../perl/apavAxa_any.pl"
    perl_regexes = extract_perl_regexes(perl_script)
    # print_regexes(perl_regexes, perl_script)
    _, _, r = zip(*perl_regexes)
    perl_set = set(r)

    python_script = "../sandhi/apavaada.py"
    python_regexes = extract_python_regexes_ast(python_script)
    _, _, r = zip(*python_regexes)
    python_set = set(r)

    assert python_set == perl_set

    # from pprint import pprint
    # pprint(f"{(perl_set - python_set)=}")
    # pprint(f"{(python_set - perl_set)=}")


if __name__ == "__main__":
    test_compare_regexes()
