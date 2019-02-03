"""convert md to rtf"""

#!/usr/bin/env python

import argparse
import pypandoc


def convert_text(input_file, output_file, output_format="docx"):

    output = pypandoc.convert_file( input_file,
                                    output_format,
                                    outputfile=output_file)

    return output


def main():
    convert_text("./test_conversion.md", "./converted.docx")


if __name__ == "__main__":
    main()
