from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())

print(soup.title, "\n")

print(soup.title.string, "\n")

print(soup.p.b, "\n")

print(soup.p['class'], "\n")

print(soup.a, "\n")

print(soup.find(class_="story"), "\n")
print(soup.find(href="http://example.com/lacie"), "\n")

print(soup.find_all("a"), "\n")

print(soup.find_all(["a", "title"]), "\n")


p = soup.find(class_="story")


print(p.contents, "\n")

for child in p.children:
    print(child)
print("\n")


body = soup.find("body")
print(body.contents, "\n")
print(len(body.contents), "\n")

print(list(body.descendants))
print(len(list(body.descendants)), "\n")



print(soup.a.parent, "\n")


for p in soup.a.parents:
    print(p.name)
print("\n")


a = soup.a
print(a.next_sibling)
print(a.next_sibling.next_sibling)
print(a.next_sibling.previous_sibling)
print()
