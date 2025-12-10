import re
import os
from pathlib import Path
from typing import List


def extract_perl_rules_array(perl_script_path: str | Path) -> List[str]:
    """
    Extract the @rules array from a Perl script, skipping commented lines.

    Args:
        perl_script_path (str): Path to the Perl script file

    Returns:
        List[str]: List of array elements as strings
    """
    with open(perl_script_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Remove commented lines and empty lines
    clean_lines = []
    for line in lines:
        stripped_line = line.strip()
        # Skip empty lines and lines starting with #
        if stripped_line and not stripped_line.startswith("#"):
            clean_lines.append(line.rstrip())

    content = "\n".join(clean_lines)

    # Extract the @rules array using regex
    pattern = r"@rules\s*=\s*\((.*?)\);"

    array_content = None
    # Use DOTALL flag to match across newlines
    match = re.search(pattern, content, re.DOTALL)
    if match:
        array_content = match.group(1)

    if array_content is None:
        return []  # Array not found

    # Parse the array elements
    entries = array_content.strip().split("\n")
    rules = []
    pattern = re.compile(r'"(.*)",')
    for e in entries:
        m = pattern.match(e)
        if m:
            r = m.group(1)
            r = (
                r.strip()
                .replace("dIPAlt", "varNamelana")
                .replace("diPAlt", "varNamelana")
                .replace("dePAlt", "varNamelana")
            )
            rules.append(r)

    return rules


def test_rules():
    path = Path(os.path.dirname(__file__))
    perl_script = path / ".." / "perl" / "any_sandhi.pl"
    perl_rules = extract_perl_rules_array(perl_script)
    from sandhi.niyama import RULES as python_rules

    assert perl_rules == python_rules

    # from pprint import pprint
    # perl_rules = set(perl_rules)
    # python_rules = set(python_rules)
    # pprint(f"{perl_rules - python_rules=}")
    # pprint(f"{python_rules - perl_rules=}")
    # return perl_rules, python_rules


if __name__ == "__main__":
    test_rules()
