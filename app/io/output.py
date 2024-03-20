import pandas as pd


def output_console(text):
    """
        outputting text to console

        Parameters:
            text (str): text outputted from console

        Returns:
            None
        """
    print(text)


def write_to_file_using_builtin(text, path):
    """
        writing text to a file using  built-in capabilities.

        Parameters:
            text (str): text which needs to be written to the file
            path (str): path of the file where text needs to be written

        Returns:
            None
        """
    with open(path, 'w') as file:
        file.write(text)


def write_to_file_using_pandas(text, path):
    """
        writing text to a file using pandas library for Python

        Parameters:
            text (str): text which needs to be written to the file
            path (str): path of the file where text needs to be written

        Returns:
            None
        """
    df = pd.DataFrame(data={'text_column': [text]})
    df.to_csv(path, index=False)