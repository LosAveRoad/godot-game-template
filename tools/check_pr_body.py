"""Check a pull request body against the sections in the pull request template."""

import re
import sys

REQUIRED = (
    "Summary",
    "Org templates",
    "Templates stay blank",
    "Review bot",
)


def _strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def sections(body: str) -> dict[str, str]:
    found: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current is not None:
                found[current] = "\n".join(buf)
            current = line[3:].strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        found[current] = "\n".join(buf)
    return found


def check(body: str) -> list[str]:
    found = sections(body)
    errors: list[str] = []
    for name in REQUIRED:
        if name not in found:
            errors.append(f"Missing section: {name}")
            continue
        if not _strip_comments(found[name]).strip():
            errors.append(f"Empty section: {name}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/check_pr_body.py BODY_FILE", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="utf-8") as handle:
        body = handle.read()
    errors = check(body)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("PR template check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
