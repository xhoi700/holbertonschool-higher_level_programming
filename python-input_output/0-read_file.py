#!/usr/bin/python3
''' module about to read a file'''
def read_file(filename=""):  
    """
    Reads a text file and prints its content to the standard output.
    
    Parameters:
    filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, "r", encoding="UTF8") as file:  # Opens the file in read mode with UTF-8 encoding
        content = file.read()  
        print(content, end="") 
