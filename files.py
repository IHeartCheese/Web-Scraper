import re, os, urllib, hashlib

download_dir_path = "downloaded"  # No closing "/"

def file_search(content):
    """Runs a targeted file search using regex on the passed string. re module required"""
    # Regex searches for relative and http file links, only looks for specified extensions due to efficiency
    files = re.findall(r"(?:http://)?[\(\)%\-/.\w]+(?:.docx|.pdf|.png|.gif|.jpg|.bmp|.jpeg)", content)
    return files

def file_download(file_list, url):
    """Attempt to download and store all files found. Download dir resets each time. Handles duplicates"""
    # Delete previous downloaded folder if present
    if os.path.isdir(download_dir_path):
        os.system("rmdir /s /q " + download_dir_path)
    os.system("mkdir " + download_dir_path)

    broken_files = []
    full_links = []
    file_hashes = []

    # Find complete links to files
    for file in file_list:
        if file[0:4] == "http":
            full_links.append(file)
        else:
            full_links.append(os.path.join(url, file))

    # Attempt to download the files from any full links found, else mark the link as broken/not functional
    for file in full_links:
        try:
            urllib.request.urlretrieve(file, os.path.join(download_dir_path, re.findall(r"([%\w\-_]+.\w+$)", file)[-1]))
        except urllib.error.HTTPError:
            broken_files.append(re.findall(r"\/([\w\.\-]+$)", file)[-1])

    # Manage duplicates with file hashes
    for file in os.listdir(download_dir_path):
        with open(os.path.join(download_dir_path, file), "rb") as f:
            content = f.read()
            file_hashes.append(hashlib.md5(content).hexdigest())

    return broken_files
