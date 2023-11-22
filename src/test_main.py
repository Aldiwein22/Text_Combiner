import os
from unittest import TestCase, mock
from main import merge_files
import unittest

class TestMergeFiles(TestCase):
    def test_merge_files_with_text_files(self):
        directory = "/path/to/directory"
        output_file = "/path/to/output.txt"

        # Create some dummy text files
        text_files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in text_files:
            with open(os.path.join(directory, file), "w") as f:
                f.write("This is some text.")

        merge_files(directory, output_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(output_file))

        # Check if the contents of the output file are correct
        with open(output_file, "r") as f:
            contents = f.read()
            expected_contents = "Chapter: file1\n\nThis is some text.\n\nChapter: file2\n\nThis is some text.\n\nChapter: file3\n\nThis is some text.\n\n"
            self.assertEqual(contents, expected_contents)

        # Clean up the dummy text files
        for file in text_files:
            os.remove(os.path.join(directory, file))

        # Clean up the output file
        os.remove(output_file)

    def test_merge_files_with_rtf_files(self):
        directory = "/path/to/directory"
        output_file = "/path/to/output.txt"

        # Create some dummy RTF files
        rtf_files = ["file1.rtf", "file2.rtf", "file3.rtf"]
        for file in rtf_files:
            with open(os.path.join(directory, file), "w") as f:
                f.write("{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0\\fnil\\fcharset0 Arial;}}\n\\viewkind4\\uc1\\pard\\lang1031\\f0\\fs20 This is some text.\\par}\n")

        merge_files(directory, output_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(output_file))

        # Check if the contents of the output file are correct
        with open(output_file, "r") as f:
            contents = f.read()
            expected_contents = "Chapter: file1\n\nThis is some text.\n\nChapter: file2\n\nThis is some text.\n\nChapter: file3\n\nThis is some text.\n\n"
            self.assertEqual(contents, expected_contents)

        # Clean up the dummy RTF files
        for file in rtf_files:
            os.remove(os.path.join(directory, file))

        # Clean up the output file
        os.remove(output_file)

    def test_merge_files_with_pdf_files(self):
        directory = "/path/to/directory"
        output_file = "/path/to/output.txt"

        # Create some dummy PDF files
        pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
        for file in pdf_files:
            with open(os.path.join(directory, file), "wb") as f:
                f.write(b"%PDF-1.7\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT\n/F1 12 Tf\n100 100 Td\n(Hello, world!) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000074 00000 n\n0000000178 00000 n\n0000000456 00000 n\ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n548\n%%EOF\n")

        merge_files(directory, output_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(output_file))

        # Check if the contents of the output file are correct
        with open(output_file, "r") as f:
            contents = f.read()
            expected_contents = "Chapter: file1\n\nHello, world!\n\nChapter: file2\n\nHello, world!\n\nChapter: file3\n\nHello, world!\n\n"
            self.assertEqual(contents, expected_contents)

        # Clean up the dummy PDF files
        for file in pdf_files:
            os.remove(os.path.join(directory, file))

        # Clean up the output file
        os.remove(output_file)


if __name__ == "__main__":
    unittest.main()