# PDF Downloader and Merger

This Python script downloads PDF files from a website and merges them into a single PDF file using the PyPDF2 library.

## Requirements

- Python 3.x
- Dependencies: `beautifulsoup4`, `PyPDF2`, and `requests` (specified in `requirements.txt`)

## Installation

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies using `pip` with the following command:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Update the `url` variable in the script with the URL of the HTML page that contains the PDF files you want to download and merge.
2. Run the script using the following command:
    ```
    python pdf_downloader_merger.py
    ```
3. The script will download the PDF files from the specified URL and save them locally.
4. It will then merge the downloaded PDF files into a single PDF file named `merged.pdf` in the project directory.
5. You can open the merged PDF file to verify the merged contents.

Note: If the downloaded PDF files are not fully downloaded or corrupted, the script will skip them during the merging process.

## Contributing

If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This script is licensed under the [MIT License](LICENSE).

