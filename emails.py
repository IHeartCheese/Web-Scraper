import re

def email_search(content):
    """Runs an email search using regex on the passed string"""
    # Regex searches for standard email format, including "mailto:" if present
    emails = re.findall(r"(?:mailto:)?\w*[.-]?\w+@\w+[.-]?\w*\.?\w+\.?\w+", content)
    mailto = [x for x in emails if "mailto:" in x]
    emails = [x for x in emails if x not in mailto]
    return emails, mailto
