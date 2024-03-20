from app.io.input import input_console, read_file_using_builtin, read_file_using_pandas
from app.io.output import output_console, write_to_file_using_builtin, write_to_file_using_pandas


def main():
    console_text = input_console()
    output_console(console_text)
    textfile = read_file_using_builtin("data/test1.txt")
    output_console(textfile)

    write_to_file_using_builtin("Just testing function", "data/test_builtin.txt")
    write_to_file_using_pandas("Testing function with pandas", 'data/test2csv')

    file_text_builtin = read_file_using_builtin("data/test_builtin.txt")
    print("Text from built-in file:", file_text_builtin)

    file_text_pandas = read_file_using_pandas("data/test_pandas.csv")
    print("Text from pandas file: \n", file_text_pandas)


if __name__ == "__main__":
    main()