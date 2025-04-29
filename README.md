# epub2azw

# EPUB to AZW3/MOBI Converter

A Python script for converting EPUB files to AZW3 or MOBI format using Calibre's command-line tools.

## Prerequisites

- Python 3.x
- Calibre (must be installed and added to system PATH)
- Windows operating system

## Installation

1. Install Calibre from [Calibre's official website](https://calibre-ebook.com/download)
2. Add Calibre to your system PATH
3. Save the script `epub2azw.py` to your desired location

## Usage

### Installation and Usage

#### Method 1: Using GitHub
1. Clone the repository:
```bash
git clone https://github.com/yourusername/epub-converter.git
cd epub-converter

### Relative Path Usage

When running the script from the same directory as your EPUB file:
```bash
# Basic usage with file in current directory
python epub2azw.py "book.epub" --format azw3

# With Chinese filename in current directory
python epub2azw.py "三体.epub" --format azw3

# Specify output directory (relative path)
python epub2azw.py "book.epub" --format azw3 --output "output_folder"

### Absolute Paths Usage

# Windows absolute path with quotes (recommended for paths with spaces)
python epub2azw.py "C:\Users\ASUS\Downloads\book.epub" --format azw3

# With custom output directory
python epub2azw.py "C:\Users\ASUS\Downloads\book.epub" --format azw3 --output "D:\ebooks\kindle"

# With Chinese filename (absolute path)
python epub2azw.py "C:\Users\ASUS\Downloads\三体.epub" --format azw3 --output "D:\ebooks\kindle"
