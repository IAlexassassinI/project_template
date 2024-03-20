def write_console(text):
    """
    Function to print text to console.

    Args:
        text (string): Text to print.

    Returns:
        None
    """
    print(text)

def write_file(text, path):
    """
    Function to write to file using built-in Python functions.

    Args:
        text (string): Text to write.
        path (string): Path to file.

    Returns:
        None
    """
    try:
        with open(path, 'w') as file:
            file.write(text)
    except IOError:
        print("Error writing to file")