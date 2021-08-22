from webpage import *  # Web Content Functionality
from emails import *  # Email Functionality
from files import *  # File Functionality
from md5 import *  # md5 hash Functionality

import re, os

url = "http://www.google.com/" # URL to scan
output_file = "output.txt"
html_content = get_page(url)

def output(title, elements, elements2=None):
    with open(output_file, "a") as f:
        f.writelines("[*] " + str(len(elements)) + " " + title + "\n\n")
        for element in elements:
            f.writelines("- " + element + "\n")
        if elements2 is not None:
            f.writelines("\n" + str(len(elements2)) + " Mailto: E-mails found\n\n")
            for element in elements2:
                f.writelines("- " + element + "\n")
        f.writelines("\n")

def link_search(content):
    """Runs a web link search using regex on the passed string"""
    # Regex looks for protocol://link until reaching the closing "
    links = re.findall(r"\w+://[0-9a-zA-Z./\-_?=]+", content)
    return links

def phone_search(content):
    """Runs a phone number search using regex on the passed string"""
    # Regex searches for all formats of phone numbers, question marks needed to accommodate all varieties
    numbers = re.findall(r"\+?\d{2}\s?\(?0?\)?[\d\-\s]{7,}\S\b", content)
    return numbers

if os.path.isfile("output.txt"):
    os.system("del output.txt")

emails, mailto = email_search(html_content)
output("E-mails", emails, mailto)
output("Phone Numbers", phone_search(html_content))
output("Hyperlinks", link_search(html_content))

files = file_search(html_content)
output("Files", files)
output("Failed Downloads", file_download(files, url))

hashes = md5_search(html_content)
output("MD5 Hashes", hashes)
output("Cracked MD5 Hashes", crack_md5(hashes))
