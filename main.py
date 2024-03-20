import app.io.input as inp
import app.io.output as outp


def main():

    file_path_1 = "data/someFile1.txt"
    file_path_2 = "data/someFile2.txt"

    file_path_3 = "data/someFile3.txt"
    file_path_4 = "data/someFile4.txt"
    file_path_5 = "data/someFile5.txt"

    text = inp.read_console_input()
    file_content = inp.read_file(file_path_1)
    pandas_content = inp.read_file_pandas(file_path_2)

    outp.write_console(text)
    outp.write_console(file_content)
    outp.write_console(pandas_content)

    outp.write_file(text, file_path_3)
    outp.write_file(file_content, file_path_4)
    outp.write_file(pandas_content.to_string(), file_path_5)


if __name__ == "__main__":
    main()