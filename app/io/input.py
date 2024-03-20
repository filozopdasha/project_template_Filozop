import pandas as pd


def input_console():
    """
       inputting text from the console

       Returns:
           (str): text which was written to the console
       """
    return input("Enter text: ")


def read_file_using_builtin(path):
    """
        reading text from a file using built-in capabilities of Python

        Parameters:
            path (str): The path to the file which needs to be read

        Returns:
            (str): Text which was read from the file
        """
    file = open(path, 'r')
    file_text = file.read()
    file.close()
    return file_text


def read_file_using_pandas(path):
    """
        reading text from a file using the pandas library for Python

        Parameters:
            path (str): The path to the file which needs to be read

        Returns:
            (str): Text which was read from the file
        """
    return pd.read_csv(path)