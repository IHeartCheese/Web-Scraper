import hashlib, re

wordlist = "rockyou.txt"

def md5_search(content):
    """Runs an md5 hash search using regex on the passed string"""
    # Regex searches for a string of 32 hex characters
    hashes = re.findall(r"\b[\dabcdef]{32}\b", content)
    hashes = list(set(hashes))
    return hashes

def crack_md5(hashes):
    """Attempts to crack the md5 hashes passed in with the popular rockyou.txt word list"""
    cracked = []
    file = open(wordlist, "r", encoding="latin-1")
    for line in file:
        temp = hashlib.md5(line.strip().encode('latin-1')).hexdigest()
        if temp in hashes:
            cracked.append(temp + " : " + line.strip('\n').strip())
    file.close()
    cracked = list(set(cracked))
    return cracked
