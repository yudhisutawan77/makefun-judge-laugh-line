"""Make the Judge Laugh in One Line.

Writes one original one-line joke to the output entry file.
Standard library only; no network, no dependencies.
"""

import os


ENTRY_TEXT = (
    "The judge has read 965 one-liners today, so this one brought "
    "its own laugh track, just in case his ran out."
)


def pick_output_dir():
    """Return the directory entry.txt should live in, or None.

    ENTRY_OUT wins when it names a directory; MAKEFUN_OUTPUT_DIR
    is next; otherwise the default is /output.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out and os.path.isdir(entry_out):
        return entry_out

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return out_dir

    return "/output"


def resolve_entry_path():
    """Work out the full path of the entry file.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    -> /output/entry.txt, falling back to ./entry.txt if /output
    is not writable (e.g. read-only grader filesystem).
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out and not os.path.isdir(entry_out):
        return entry_out

    return os.path.join(pick_output_dir(), "entry.txt")


def emit_entry(path):
    """Write ENTRY_TEXT byte-identically, with no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


def main():
    destination = resolve_entry_path()
    try:
        emit_entry(destination)
    except OSError:
        # /output may be read-only; last resort is the current directory.
        if destination != "entry.txt":
            emit_entry("entry.txt")


if __name__ == "__main__":
    main()
