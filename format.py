import sys

from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(sys.stdin.read(), 'html.parser')

    # Remove script tag
    soup.html.body.script.decompose()

    # Remove unnecessary wrappers
    (soup.html.body
     .select_one('.page')
     .replace_with(soup.html.body.find('article')))

    # Add some styling
    style = soup.new_tag('style')
    style.append('article { width: 40rem; }')
    soup.html.head.append(style)

    sys.stdout.write(soup.prettify())
