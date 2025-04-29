import subprocess
import os
import argparse

def convert_ebook(input_file, output_format, output_dir=None):
    # Set default input path if only filename is provided
    if not os.path.dirname(input_file):
        input_file = os.path.join(r'C:\Users\ASUS\Downloads', input_file)
    
    # Normalize file path, handle special characters and spaces
    input_file = os.path.abspath(input_file)

    # Verify if input file exists
    if not os.path.exists(input_file):
        print(f"Searching for file: {input_file}")
        # Try to list files in directory for comparison
        dir_path = os.path.dirname(input_file)
        files = os.listdir(dir_path)
        for file in files:
            if file.endswith('.epub'):
                print(f"Found file: {file}")
        raise FileNotFoundError(f"Input file {input_file} does not exist")

    # Set default output directory if none specified
    if not output_dir:
        output_dir = r'C:\Users\ASUS\Downloads'

    # Verify if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")

    # Set output filename and path (using os.path.basename to preserve Chinese characters)
    base_name = os.path.splitext(os.path.basename(input_file))[0]  # Get filename part from full path, preserve original encoding
    output_ext = output_format.lower()  # Remove extension
    output_file = f"{base_name}.{output_ext}"  # Create new filename using original name with new extension
    
    if output_dir:
        output_file = os.path.join(output_dir, output_file)

    # Check if output format is supported
    supported_formats = ['azw3', 'mobi']
    if output_ext not in supported_formats:
        raise ValueError(f"Unsupported output format: {output_ext}, supported formats: {', '.join(supported_formats)}")

    try:
        # Execute conversion command
        subprocess.run([
            'ebook-convert',
            input_file,
            output_file,
            '--output-profile', 'kindle_pw3'  # Optimize for Kindle devices
        ], check=True)
        print(f"Conversion successful! Output file: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {str(e)}")
        return False
    except FileNotFoundError:
        print("ebook-convert command not found, please ensure Calibre is installed and added to PATH environment variable")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='EPUB to AZW3/MOBI conversion tool')
    parser.add_argument('input', help='Input EPUB file path')
    parser.add_argument('--format', required=True, choices=['azw3', 'mobi'], 
                       help='Target format (azw3 or mobi)')
    parser.add_argument('--output', help='Output directory (optional)')

    args = parser.parse_args()

    convert_ebook(
        input_file=args.input,
        output_format=args.format,
        output_dir=args.output
    )