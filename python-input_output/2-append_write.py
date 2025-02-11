#!/usr/bin/python3


"""Module that contains the function write_file."""


def append_write(filename="", text=""):
    """write a text file (UTF8) and prints it to stdout."""
    with open(filename, "a", encoding="UTF8") as f:
        content = f.write(text)
        return content
