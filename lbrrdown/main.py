import argparse

from collections.abc import Sequence

from pathlib import Path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument("path", type=Path)
    parser.add_argument("-f", "--format", default="HTML", type=str)

    args = parser.parse_args(argv)

    # Check if path exists
    # Check if path is a library
    # Create the build dir
    # Check if @param exists for all parameters
    # Support for Functions and Classes
    # Support for @title, @description, @param, @returns, @example
    # Future support for @inheritsFrom, @importsFrom
    # Generate HTML

    print(args.path)
    print(args.format)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
