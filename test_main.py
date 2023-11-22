import os
import unittest
import tempfile
from main import merge_files

class TestMergeFiles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory
        cls.test_dir = tempfile.mkdtemp()

        # Create mock text file
        with open(os.path.join(cls.test_dir, "test1.txt"), "w") as file:
            file.write("Hello from text file")

        # Create mock RTF file
        with open(os.path.join(cls.test_dir, "test2.rtf"), "w") as file:
            file.write(r"{\rtf1\ansi\deff0 {\fonttbl {\f0 Courier;}} {\colortbl;\red0\green0\blue0;\red255\green0\blue0;} This is some {\b bold} text in an RTF file.}")

        # Create mock PDF file
        # We'll use a simple text-based PDF for testing
        from reportlab.pdfgen import canvas
        pdf_path = os.path.join(cls.test_dir, "test3.pdf")
        c = canvas.Canvas(pdf_path)
        c.drawString(100, 750, "Hello from PDF")
        c.save()

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary directory and its contents
        for filename in os.listdir(cls.test_dir):
            os.remove(os.path.join(cls.test_dir, filename))
        os.rmdir(cls.test_dir)

    def test_merge_text_files(self):
        output_file = os.path.join(self.test_dir, "output.txt")
        merge_files(self.test_dir, output_file)
        with open(output_file, "r") as file:
            content = file.read()
        self.assertIn("Hello from text file", content)

    def test_merge_rtf_files(self):
        output_file = os.path.join(self.test_dir, "output.txt")
        merge_files(self.test_dir, output_file)
        with open(output_file, "r") as file:
            content = file.read()
        self.assertIn("bold", content)  # Assuming RTF content is stripped to plain text

    def test_merge_pdf_files(self):
        output_file = os.path.join(self.test_dir, "output.txt")
        merge_files(self.test_dir, output_file)
        with open(output_file, "r") as file:
            content = file.read()
        self.assertIn("Hello from PDF", content)

    def test_output_file_creation(self):
        output_file = os.path.join(self.test_dir, "output.txt")
        merge_files(self.test_dir, output_file)
        self.assertTrue(os.path.exists(output_file))

    def test_content_integrity(self):
        # This test ensures that all files are merged correctly
        output_file = os.path.join(self.test_dir, "output.txt")
        merge_files(self.test_dir, output_file)
        with open(output_file, "r") as file:
            content = file.read()
        self.assertIn("Hello from text file", content)
        self.assertIn("bold", content)
        self.assertIn("Hello from PDF", content)

    def test_invalid_input_handling(self):
        with self.assertRaises(Exception):
            merge_files("non_existent_directory", "output.txt")

if __name__ == '__main__':
    unittest.main()
