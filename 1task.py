import requests
import re

site = "http://www.mosigra.ru/"
max_depth = 10


def mails(url, visited, depth):
    print(site+url)
    response = requests.get(site + url)
    caught_mails = re.findall(r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)
    urls = re.findall(r"\"/[a-zA-Z0-9/]+\"", response.text)
    for url in urls:
        url = url.replace("\"", "")[1:]
        if url not in visited and depth < max_depth:
            depth = depth + 1
            visited.append(url)
            new_mails = mails(url, visited, depth)
            for mail in new_mails:
                if mail not in caught_mails:
                    caught_mails.append(mail)
    return caught_mails

print(mails("", [], 0))
