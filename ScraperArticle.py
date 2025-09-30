import urllib.request
import re
from html.parser import HTMLParser

# Custom HTML parser to extract title and paragraphs
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_paragraph = False
        self.title = ""
        self.paragraphs = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        elif tag == "p":
            self.in_paragraph = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "p":
            self.in_paragraph = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()
        elif self.in_paragraph:
            self.paragraphs.append(data.strip())

# Get Wikipedia page content
def get_Wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"Failed to fetch the page: {e}")
        return None

# Extract data using custom parser
def parse_html(content):
    parser = MyHTMLParser()
    parser.feed(content)
    return parser.title, parser.paragraphs

# Extract headings using regex
def get_headings(content):
    headings = re.findall(r'<h2.*?>(.*?)</h2>', content)
    return [re.sub(r'<.*?>', '', heading).strip() for heading in headings]

# Extract related links using regex
def get_related_links(content):
    links = re.findall(r'href="/wiki/([^":#]+)"', content)
    return [f"https://en.wikipedia.org/wiki/{link}" for link in set(links)][:5]

# Main program
def main():
    topic = input("Enter a topic: ").strip()
    page_content = get_Wikipedia_page(topic)

    if page_content:
        title, paragraphs = parse_html(page_content)
        headings = get_headings(page_content)
        related_links = get_related_links(page_content)

        print("\n--- Wikipedia Article ---")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {paragraphs[0] if paragraphs else 'No content found'}")
        print("\nHeadings:")
        for heading in headings[:5]:
            print(f"- {heading}")

        print("\nRelated Links:")
        for link in related_links:
            print(f"- {link}")

# Run the program
if __name__ == "__main__":
    main()
