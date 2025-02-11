#!/usr/bin/python3


"""Module that contains the function write_file."""


def write_file(filename="", text=""):
    """write a text file (UTF8) and prints it to stdout."""
    with open(filename, "w", encoding="UTF8") as f:
        content = f.write(text)
        return content
