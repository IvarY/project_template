import pandas as pd


def write_console(output):
    """Write output to the console

    Args:
        output (any): The output to write to the console
    """
    print(output)


def write_file(file_path, output):
    """Write output to a file

    Args:
        file_path (str): The path to the file
        output (str): The output to write to the file
    """
    with open(file_path, 'w') as file:
        file.write(output)


def write_file_pandas(file_path, output):
    """Write output to a JSON or CSV file using pandas

    Notes:
        The file format is determined by the file extension in the file_path

    Args:
        file_path (str): The path to the file
        output (pandas.DataFrame): The output to write to the file

    Raises:
        ValueError: If the file format is not supported
    """
    file_extension = file_path.split('.')[-1]

    if file_extension == 'csv':
        output.to_csv(file_path, index=False)
    elif file_extension == 'json':
        output.to_json(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and JSON files are supported.")