import os
import argparse
from jsmin import jsmin
from csscompressor import compress as cssmin
from htmlmin import minify as htmlmin
from rjsmin import jsmin as rjsmin

def get_filetype(file_path):
    file_type = os.path.splitext(file_path)[1].replace(".", "")
    if file_type == "html":
        return "HTML"
    if file_type == "css":
        return "CSS"
    if file_type == "js":
        return "jsx"
    if file_type == "ejs":
        return "ejs"
    if file_type == "py":
        return "python"
    if file_type == "md":
        return "markdown"

def write_file_contents_to_md(file_path, md_file, minify):
    file_type = get_filetype(file_path)
    md_file.write(f"## {file_path}\n\n")
    with open(file_path, "r", encoding='utf-8') as f:
        file_contents = f.read()
        if minify:
            if file_type == "HTML":
                file_contents = htmlmin(file_contents, remove_comments=True, remove_empty_space=True)
            elif file_type == "CSS":
                file_contents = cssmin(file_contents)
            elif file_type == "jsx":
                file_contents = jsmin(file_contents)
            elif file_type == "python":
                file_contents = rjsmin(file_contents)
        md_file.write(f"```{file_type}\n")
        md_file.write(file_contents)
        if file_contents[-1] == "\n":
            md_file.write('```\n\n')
        else:
            md_file.write('\n```\n\n')

def filterIgnoredFiles(files, ignore_files):
    not_empty_files = [f for f in files if os.stat(f).st_size != 0]
    new_files = []
    for f in not_empty_files:
        file_name = f.split("\\")[-1]
        if file_name not in ignore_files:
            new_files.append(f)
    return new_files

def filterIgnoredDirectories(dirs, ignore_dirs):
    new_dirs = []
    for d in dirs:
        if d not in ignore_dirs:
            new_dirs.append(d)
    return new_dirs

def search_files(start_dir, ignore_dirs, ignore_files, all_types, ext, name, minify):
    markdown_file = f"{name}.md"
    extensions = ext
    if all_types:
        extensions = ['.html', '.css', '.js', '.ejs', '.py', '.txt', '.md', '.json', '.xml', '.yml', '.yaml', '.csv', '.ts', '.tsx', '.jsx', '.php', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.vb', '.vbhtml']
    with open(markdown_file, "w", encoding='utf-8') as md_file:
        md_file.write(f"# {name}\n\n")
        for dirpath, dirs, files in os.walk(start_dir):
            dirs[:] = filterIgnoredDirectories(dirs, ignore_dirs)
            files = filterIgnoredFiles([os.path.join(dirpath, f) for f in files], ignore_files)
            for filename in files:
                if any(filename.endswith(ext) for ext in extensions):
                    write_file_contents_to_md(filename, md_file, minify)
    os.startfile(markdown_file)

def print_help():
    print("Search for files with specific extensions in a directory and its subdirectories.")
    print("Usage: python project_search.py [options]")
    print("Options:")
    print("  -h, --help            show this help message and exit")
    print("  -i ignore [ignore ...], --ignore ignore [ignore ...]")
    print("                        list of directories to ignore")
    print("  -s start_dir, --start_dir start_dir")
    print("                        the directory to start the search from")
    print("  -x ignore_files [ignore_files ...], --ignore_files ignore_files [ignore_files ...]")
    print("                        list of files to ignore")
    print("  -a, --all-types       include all file types")
    print("  -e types [types ...], --extensions types [types ...]")
    print("                        list of file types to include")
    print("  -n name, --name name  name of the markdown file to write to")
    print("  -m, --minify          minify the files")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for files with specific extensions in a directory and its subdirectories.')
    parser.add_argument('-i', '--ignore', metavar='ignore', type=str, nargs='+', help='list of directories to ignore')
    parser.add_argument('-s', '--start_dir', metavar='start_dir', type=str, default='.', help='the directory to start the search from')
    parser.add_argument('-x', '--ignore_files', metavar='ignore_files', type=str, nargs='+', default="['project_search.py']", help='list of files to ignore')
    parser.add_argument('-a', '--all-types', action='store_true', help='include all file types')
    parser.add_argument('-e', '--extensions', metavar='types', type=str, nargs='+', default="['.html', '.css', '.js', '.ejs', '.py']", help='list of file types to include')
    parser.add_argument('-n', '--name', metavar='name', type=str, default='project', help='name of the markdown file to write to')
    parser.add_argument('-m', '--minify', action='store_true', help='minify the files')
    parser.add_argument('-H', '--Help', action='store_true', help='show this help message and exit')
    args = parser.parse_args()

    ignore_dirs = args.ignore if args.ignore else []
    ignore_files = args.ignore_files if args.ignore_files else []
    
    if args.Help:
        parser.print_help()
    else:
        search_files(args.start_dir, ignore_dirs, ignore_files, args.all_types, args.extensions, args.name, args.minify)