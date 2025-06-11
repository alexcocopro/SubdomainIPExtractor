# SubdomainIPExtractor
Subdomain and IP Extractor - Multi-format Support


This program extracts subdomains and IPv4 addresses from various input file formats including TXT, CSV, JSON, Excel (.xlsx), and Word (.docx). It reads the content of the input file, detects valid subdomains and IP addresses using pattern matching, and outputs two separate text files: one with unique subdomains and another with unique IP addresses.

## This tool is ideal for cybersecurity professionals and researchers who need to analyze reconnaissance or enumeration data from diverse sources and file types without manual conversion.

Developed by Alex Cabello Leiva, Cybersecurity Consultant.

# Usage Guide for Subdomain and IP Extractor (Multi-format)

1. Prepare your input file:
   - Supported formats: TXT, CSV, JSON, Excel (.xlsx), Word (.docx).
   - Ensure the file contains textual data with subdomains and/or IP addresses.

2. Run the program:
   - Execute the script from the command line:
     python3 SubdomainIPExtractor.py -i your_input_file.ext

3. Output files:
   - The program generates two files in the current directory:
     * subdomains.txt  - sorted list of unique subdomains found.
     * ips.txt         - sorted list of unique IPv4 addresses found.

4. Notes:
   - The program validates IPv4 addresses and filters out invalid entries.
   - It excludes reverse DNS entries (e.g., *.in-addr.arpa).
   - Works with any text content extracted from supported file formats.
   - Requires necessary Python libraries installed (see requirements).

5. Contact:
   - For support or questions, contact Alex Cabello Leiva, Cybersecurity Consultant.


# Requirements for Subdomain and IP Extractor (Multi-format)

- Python 3.6 or higher
- Python packages:
  * argparse (standard library)
  * re (standard library)
  * colorama (for colored terminal output)
  * openpyxl (to read Excel files)
  * python-docx (to read Word documents)

Install required packages with:
  pip install colorama openpyxl python-docx

Optional:
- Terminal with ANSI color support for best user experience.

The program is cross-platform and runs on any OS with Python 3 installed.
