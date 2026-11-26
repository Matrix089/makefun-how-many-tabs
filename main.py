"""How Many Tabs Do You Have Open? entry.

Writes one number in digits and nothing else to /output/entry.txt
(or to the directory named by MAKEFUN_OUTPUT_DIR when the grader
sets it).

47: high enough to surprise, low enough to read as a real, lived-in
answer from someone who works across a dozen projects at once. A
triple-digit count would read as exaggeration; a single digit would
not surprise anyone. The gate allows 1 to 5 digits, and this entry
is 2 digits.
"""

import os

ENTRY = "47"


def main():
    entry = ENTRY.strip()
    if not (entry.isdigit() and 1 <= len(entry) <= 5):
        raise SystemExit(f"Entry must be 1 to 5 digits, got {entry!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
