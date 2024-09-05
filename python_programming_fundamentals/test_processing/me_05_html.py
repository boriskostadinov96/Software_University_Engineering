title = input()
content = input()
comment = input()
divs = []

while comment != "end of comments":
    divs.append(comment)
    comment = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")

for div in divs:
    print(f"<div>\n    {div}\n</div>")
