"""Entry program: writes one line of tech-support advice to the output file."""

import os

LINE = (
    "Have you tried turning it off and leaving it off? "
    "The error disappears completely. So does everything else, but one problem at a time."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
