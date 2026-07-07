from pathlib import Path

# Generates the tree structure for the project

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}

IGNORE_FILES = {
    ".DS_Store",
}


def build_tree(path: Path, prefix: str = "", lines=None):
    if lines is None:
        lines = []

    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    items = [
        item
        for item in items
        if item.name not in IGNORE_DIRS
        and item.name not in IGNORE_FILES
    ]

    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "

        lines.append(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if index == len(items) - 1 else "│   "
            build_tree(item, prefix + extension, lines)

    return lines

root = Path(__file__).resolve().parent.parent

tree_lines = [root.name]
tree_lines.extend(build_tree(root))

tree_text = "\n".join(tree_lines)

status_file = root / "STATUS.md"

content = status_file.read_text(encoding="utf-8")

start = "<!-- PROJECT_TREE_START -->"
end = "<!-- PROJECT_TREE_END -->"

before = content.split(start)[0] + start + "\n"
after = "\n" + end + content.split(end)[1]

updated = before + "```text\n" + tree_text + "\n```\n" + after

status_file.write_text(updated, encoding="utf-8")

print("STATUS.md updated.")