"""Command-line interface for the ``sandhi`` package.

The CLI is a thin wrapper around :class:`sandhi.Sandhi`.  It forms sandhi
between two input words and prints all possible results.
"""

import argparse
import sys

from .sandhi import Sandhi


def build_parser():
    """Create and return the argument parser for the sandhi CLI."""
    parser = argparse.ArgumentParser(
        prog="sandhi",
        description="Form Sanskrit sandhi between two words.",
    )
    parser.add_argument(
        "first",
        help="First word (default input scheme: Devanagari).",
    )
    parser.add_argument(
        "second",
        help="Second word.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Only print resulting forms (omit sutra and sandhi type).",
    )
    return parser


def main(argv=None):
    """Console entry point for the ``sandhi`` command."""
    parser = build_parser()
    args = parser.parse_args(argv)

    engine = Sandhi()
    results = engine.sandhi(args.first, args.second)

    if not results:
        print("No sandhi forms found.", file=sys.stderr)
        return 1

    for index, (form, sutra, sandhi_type) in enumerate(results, start=1):
        if args.quiet:
            print(form)
            continue

        parts = [form]
        if sutra:
            parts.append(sutra)
        if sandhi_type:
            parts.append(sandhi_type)

        print(f"{index}. " + " | ".join(parts))

    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
