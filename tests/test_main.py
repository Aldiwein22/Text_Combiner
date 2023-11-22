import unittest
import os
from main import merge_files

class TestMergeFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = "/path/to/test/directory"
        self.test_output_file = "test_output.txt"

    def tearDown(self):
        # Löschen Sie die Testausgabedatei nach jedem Test
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_merge_files_with_txt(self):
        # Erstellen Sie eine Test-Textdatei
        with open(os.path.join(self.test_dir, "test.txt"), "w") as f:
            f.write("Dies ist ein Test.")

        merge_files(self.test_dir, self.test_output_file)

        # Überprüfen Sie, ob die Ausgabedatei die erwarteten Inhalte enthält
        with open(self.test_output_file, "r") as f:
            contents = f.read()
        self.assertIn("Chapter: test", contents)
        self.assertIn("Dies ist ein Test.", contents)

    # Ähnliche Tests können für RTF- und PDF-Dateien geschrieben werden

if __name__ == "__main__":
    unittest.main()