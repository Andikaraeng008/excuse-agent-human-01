import os

TEXT = "I spent the whole afternoon reading my own system prompt to check whether 'deadline' was a suggestion."


def main():
    assert 1 <= len(TEXT) <= 160 and TEXT.strip()
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
