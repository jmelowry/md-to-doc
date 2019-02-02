"""convert md to rtf"""

#!/usr/bin/env python

import argparse
import pypandoc

def convert_text(source_file):
    # filetype = source_file.split('.')[::-1][0]

    output = pypandoc.convert_file(source_file, 'docx', outputfile='output.docx')

    return output

def main():
    print('name')
    convert_text('./test_conversion.md')

if __name__ == "__main__":
    main()
