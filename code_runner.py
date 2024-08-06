"""
@Author: poqob
@Date: 2024-08-04 15:00:00
@LastEditTime: 2024-08-06 20:00:00

"""

import os
import re
import configparser

class CodeRunner:
    def remove_custom_imports(self, file_path: str, expression: str) -> None:
        """
        Removes all imports that depend on packages from `src.*` and custom packages
        in the specified file.
        :param expression: custom import keyword.
        :param file_path: Path to the file to be edited.
        """
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            for line in lines:
                pattern = rf"^\s*(from {re.escape(expression)}|import {re.escape(expression)})\."
                # If the line matches the pattern, skip it
                if not re.match(pattern, line):
                    file.write(line)

    def change_words(self,file_path: str, old_word: str, new_word: str) -> None:
        """
        Change all occurrences of `old_word` with `new_word` in the specified file.
        :param file_path: Path to the file to be edited.
        :param old_word: Word to be replaced.
        :param new_word: Word to replace `old_word`.
        """
        with open(file_path, "r") as file:
            content = file.read()

        content = content.replace(old_word, new_word)

        with open(file_path, "w") as file:
            file.write(content)

    def concatenate_files_in_sequence(self,file_names: list, output_file: str) -> None:
        """
        Concatenates files in the specified sequence into a single output file.
        :param file_names: List of filenames in the order to be concatenated.
        :param output_file: Path to the output file where concatenated content will be saved.
        """
        with open(output_file, "w") as outfile:
            for file_name in file_names:
                if os.path.isfile(file_name):
                    with open(file_name, "r") as infile:
                        outfile.write(f"# File: {file_name}\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")
                else:
                    print(f"Warning: File {file_name} does not exist.")

    def read_file_paths(self,conf_file: str) -> list:
        config = configparser.ConfigParser()
        config.read(conf_file)
        file_paths = []
        if 'files' in config:
            for key in config['files']:
                file_paths.append(config['files'][key].strip('"'))
        return file_paths



if __name__ == "__main__":
    runner = CodeRunner()
    conf_file = 'code_runner.conf'  # Path to your .conf file
    file_names = runner.read_file_paths(conf_file)

    output_file = "run.py"
    runner.concatenate_files_in_sequence(file_names, output_file)
    runner.remove_custom_imports(output_file, 'src')
    runner.change_words(output_file, "cv2.Mat", "np.ndarray")
