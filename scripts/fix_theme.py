import os
import glob
from bs4 import BeautifulSoup

def process_html(input_file, output_file):
    # Read the HTML file
    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # 1) Add lang="ja" to <html>
    if soup.html:
        soup.html["lang"] = "ja"

    # 2) Add Bootstrap link to <head>
    if soup.head:
        link_tag = soup.new_tag("link", href="../bootstrap.min.css", rel="stylesheet")
        if not soup.head.find("link", href="../bootstrap.min.css"):
            soup.head.append(link_tag)

    # 3) Add data-bs-theme="dark" to <body>
    if soup.body:
        soup.body["data-bs-theme"] = "dark"

        # 4) Wrap body content in <div class="container"> if not already
        if not (len(soup.body.contents) == 1 and getattr(soup.body.contents[0], "get", lambda *_: None)("class") == ["container"]):
            container = soup.new_tag("div", **{"class": "container"})
            for child in list(soup.body.contents):
                container.append(child.extract())
            soup.body.append(container)

    # Save modified HTML
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup.prettify()))

def process_all_html():
    # Create output directory "new"
    os.makedirs("new", exist_ok=True)

    # Find all .html files in current directory
    for file in glob.glob("*.html"):
        output_file = os.path.join("new", os.path.basename(file))
        process_html(file, output_file)
        print(f"Processed {file} -> {output_file}")

if __name__ == "__main__":
    process_all_html()