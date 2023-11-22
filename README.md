# Text_Combiner

This Python script combines multiple text-based files into a single file.

## Requirements
- Python 3.x
- striprtf
- PyPDF2

## Installation
1. Clone the repository: `git clone https://github.com/username/Text_Combiner.git`
2. Navigate to the directory: `cd Text_Combiner`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage
1. Place the files to be combined in the `files` directory.
2. Run the script: `python text_combiner.py`
3. The combined file will be created as `merged.txt` in the current directory.

## Notes
- The script supports combining text files (.txt), RTF files (.rtf), and PDF files (.pdf).
- The content of the combined file will be displayed in the order of the files in the `files` directory.
- Each file or each page in a PDF file will be treated as a separate chapter.
- The chapter headings correspond to the file names without file extensions.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
