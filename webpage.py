import urllib.request

# Scrape and return the content of the webpage
def get_page(url):
    try:
        file = urllib.request.urlopen(url)
        file_bytes = file.read()
        content = file_bytes.decode("utf8")
        file.close()
    except Exception as err:
        print("URL Access Error  - ", err)
        exit(1)
    return content

