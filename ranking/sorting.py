import re

def atoi(text):
    return int(text) if text.isdigit() else text

def nat_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


