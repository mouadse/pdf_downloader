import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from PyPDF2 import PdfMerger

# Define the URL of the HTML page
url = "https://www.your_website.com/page.html"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract all <a> tags that contain PDF files
    pdf_links = [a["href"]
                 for a in soup.find_all("a") if a["href"].endswith(".pdf")]

    # Loop through each PDF link
    for pdf_link in pdf_links:
        # Combine the PDF link with the base URL to get the absolute URL
        absolute_url = urljoin(url, pdf_link)

        # Send a GET request to download the PDF file
        pdf_response = requests.get(absolute_url)

        # Extract the filename from the PDF link
        filename = os.path.basename(urlparse(pdf_link).path)

        # Check if the PDF file was downloaded successfully
        if pdf_response.status_code == 200:
            # Save the PDF file locally
            with open(filename, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"{filename} downloaded successfully.")

            # Verify the file size to ensure the download is complete
            if os.path.getsize(filename) == 0:
                os.remove(filename)
                print(f"{filename} is empty and has been deleted.")
            else:
                print(f"{filename} is valid.")
        else:
            print(f"Failed to download {filename}.")
else:
    print("Failed to retrieve HTML content.")

# Create a PdfMerger object to merge PDF files
merger = PdfMerger()

# Loop through each downloaded PDF file and add it to the merger
for pdf_link in pdf_links:
    filename = os.path.basename(urlparse(pdf_link).path)
    merger.append(filename)

# Define the output PDF filename
output_filename = "merged.pdf"

# Merge the PDF files and save the output file
merger.write(output_filename)
merger.close()

print(f"All PDF files have been merged into {output_filename}.")
