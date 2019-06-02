import sys

import pendulum
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
    style.append('''
        * { font-family: "Liberation Sans", sans-serif !important; }
        h1, h2, h3, h4 { margin-top: 3rem !important; }
        footer { margin-top: 6rem; text-align: right; }
    ''')
    soup.html.head.append(style)

    # Add footer
    last_updated = pendulum.now('Asia/Manila').to_day_datetime_string()
    footer = BeautifulSoup(f'''
      <footer>
        <hr />
        <small>
          Automatically built using <a href="https://github.com/marksteve/resume/blob/master/.github/main.workflow">GitHub Actions</a>
          - Last updated on {last_updated}
        </small>
      </footer>
    ''', 'html.parser')
    soup.html.body.append(footer)

    sys.stdout.write(soup.prettify())
