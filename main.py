from app.io.input import read_console, read_file, read_file_pandas


def main():
    console_input = read_console()
    file_input = read_file('data\\file_in')
    file_pandas_input = read_file_pandas('data\\cereal.csv')

    with open('data\\console_out', 'w') as file:
        file.write(console_input)
    with open('data\\file_out', 'w') as file:
        file.write(file_input)
    with open('data\\file_pandas_out', 'w') as file:
        file.write(file_pandas_input.to_csv(index=False))

    print('\n')
    print(f'Console input: {console_input}')
    print(f'File input: {file_input}')
    print(f'File pandas input: {file_pandas_input}')


if __name__ == "__main__":
    main()

