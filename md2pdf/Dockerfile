FROM python:3

LABEL "com.github.actions.name"="Markdown to PDF"
LABEL "com.github.actions.description"="Render a Markdown file to PDF"
LABEL "com.github.actions.icon"="file-text"
LABEL "com.github.actions.color"="purple"

RUN pip install grip
RUN curl -O https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
    dpkg -i ./wkhtmltox_0.12.5-1.stretch_amd64.deb
CMD grip resume.md --wide --export - | \
    python3 format.py | \
    wkhtmltopdf - resume.pdf

