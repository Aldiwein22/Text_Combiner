import os
from striprtf.striprtf import rtf_to_text
from PyPDF2 import PdfReader

def merge_files(directory, output_file):
    # Open the output file in write mode
    
    with open(output_file, "w") as outfile:
        # Loop through each directory, subdirectory, and file in the directory
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                print(f"Processing file: {filename}")
                
                # Full path to the file
                full_path = os.path.join(dirpath, filename)
                
                # Check if the file is a text, rtf, or PDF file
                if filename.endswith(".txt"):
                    # Open the text file in read mode
                    with open(full_path, "r") as infile:
                        # Write the file name as a chapter title
                        chapter_title = filename.replace(".txt", "")
                        outfile.write(f"Chapter: {chapter_title}\n\n")
                        print(f"Writing chapter title for {filename}")
                        # Write the contents of the file to the output file
                        contents = infile.read()
                        if contents:
                            outfile.write(contents)
                            print(f"Writing contents of {filename}")
                        else:
                            print(f"No contents in {filename}")
                        # Add a new line after each file
                        outfile.write("\n\n")
                        print(f"Adding new line after {filename}")
                elif filename.endswith(".rtf"):
                    # Open the rtf file in read mode
                    with open(full_path, "r") as infile:
                        # Convert rtf to plain text
                        rtf_content = infile.read()
                        plain_text = rtf_to_text(rtf_content)
                        # Write the file name as a chapter title
                        chapter_title = filename.replace(".rtf", "")
                        outfile.write(f"Chapter: {chapter_title}\n\n")
                        print(f"Writing chapter title for {filename}")
                        # Write the plain text contents to the output file
                        if plain_text:
                            outfile.write(plain_text)
                            print(f"Writing contents of {filename}")
                        else:
                            print(f"No contents in {filename}")
                        # Add a new line after each file
                        outfile.write("\n\n")
                        print(f"Adding new line after {filename}")
                elif filename.endswith(".pdf"):
                    # Open the PDF file in read mode
                    pdf = PdfReader(full_path)
                    # Write the file name as a chapter title
                    chapter_title = filename.replace(".pdf", "")
                    outfile.write(f"Chapter: {chapter_title}\n\n")
                    print(f"Writing chapter title for {filename}")
                    # Loop through each page in the PDF
                    for page_num in range(len(pdf.pages)):
                        # Extract the text from the page
                        page = pdf.pages[page_num]
                        text = page.extract_text()
                        # Write the page contents to the output file
                        if text:
                            outfile.write(text)
                            print(f"Writing contents of page {page_num + 1} in {filename}")
                        else:
                            print(f"No contents in page {page_num + 1} in {filename}")
                        # Add a new line after each page
                        outfile.write("\n\n")
                        print(f"Adding new line after page {page_num + 1} in {filename}")

def main():
    # Define the directory containing the text files and PDF files
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text_files")

    # Define the output file name
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "merged.txt")

    merge_files(directory, output_file)

    print("Merging complete!")

if __name__ == "__main__":
    main()