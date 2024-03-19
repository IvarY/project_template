import pandas as pd


def read_console():
    """Read input from the console

    Returns:
        str: The input from the console
    """
    return input()


def read_file(file_path):
    """Read input from a file

    Args:
        file_path (str): The path to the file

    Returns:
        str: The input from the file
    """
    with open(file_path, 'r') as file:
        return file.read()


def read_file_pandas(file_path):
    """Read input from a JSON or CSV file using pandas

    Args:
        file_path (str): The path to the file

    Returns:
        pandas.DataFrame: The input from the file

    Raises:
        ValueError: If the file format is not supported
    """
    file_extension = file_path.split('.')[-1]

    if file_extension == 'csv':
        data = pd.read_csv(file_path)
    elif file_extension == 'json':
        data = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and JSON files are supported.")

    return data

