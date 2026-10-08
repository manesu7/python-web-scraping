from bs4 import BeautifulSoup
import requests

# A short test document provided by the Beautiful Soup documentation.
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Create our soup
soup = BeautifulSoup(html_doc)

# Test to ensure it's working
print(soup.title)

print(soup.p)

# Define a custom User-Agent header
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          "AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/140.0.0.0 Safari/537.36" }

# Send the GET request with the 'headers' parameter
response = requests.get("https://www.wikipedia.org/", headers=headers)
print(response.text)