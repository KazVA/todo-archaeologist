import re, subprocess, sys
from datetime import datetime
from pathlib import Path

PATTERN = re.compile(r"\b(TODO|FIXME|HACK|XXX)\b[:\s]*(.*)")

def git(path, *args):
    return subprocess.run(["git", "-C", path, *args], capture_output=True,
                          text=True, errors="replace")

def blame(path, file, line):
    r = git(path, "blame", "-L", f"{line},{line}", "--porcelain", "--", file)
    author = ts = None
    for l in r.stdout.splitlines():
        if l.startswith("author "):
            author = l[7:]
        elif l.startswith("author-time "):
            ts = int(l[12:])
    return author, ts

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    files = git(path, "ls-files").stdout.splitlines()
    if not files:
        sys.exit("Not a git repo, or no tracked files.")
    found = []
    for f in files:
        if Path(f).name == Path(__file__).name:
            continue
        try:
            lines = (Path(path) / f).read_text(errors="ignore").splitlines()
        except OSError:
            continue
        for i, text in enumerate(lines, 1):
            m = PATTERN.search(text)
            if m:
                author, ts = blame(path, f, i)
                if ts:
                    age = (datetime.now() - datetime.fromtimestamp(ts)).days
                    found.append((age, m.group(1), f, i, author, m.group(2).strip()))

    found.sort(reverse=True)
    print(f"\n🏺 Found {len(found)} forgotten notes\n")
    for age, kind, f, i, author, note in found[:15]:
        print(f"{age:>4} days old | {kind:<5} | {f}:{i} | {author}")
        print(f"             \"{note[:70]}\"")
    if found:
        avg = sum(x[0] for x in found) // len(found)
        print(f"\nOldest: {found[0][0]} days. Average age: {avg} days.\n")

if __name__ == "__main__":
    main()