import pandas as pd


def read_console_input():
    """
    Function to get text input from console.

    Returns:
        string: input from the console.
    """
    return input("Enter some text: ")


def read_file(path):
    """
    Function to read from file using built-in Python functions.

    Args:
        path (string): Path to file.

    Returns:
        string: data from file.
    """
    try:
        with open(path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found")
        return None


def read_file_pandas(path):
    """
    Function to read from file using pandas library.

    Args:
        path (string): Path to file.

    Returns:
        string: data from file.
    """
    try:
        content = pd.read_csv(path, sep=" ")
        return content
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception:
        print("Some error with panda read")
        return None
