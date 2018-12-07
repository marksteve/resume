FROM python:3

LABEL "com.github.actions.name"="Markdown to PDF"
LABEL "com.github.actions.description"="Render a Markdown file to PDF"
LABEL "com.github.actions.icon"="file-text"
LABEL "com.github.actions.color"="purple"

RUN pip install grip
RUN apt-get update && apt-get -y install wkhtmltopdf
CMD grip resume.md --wide --export - | \
    python3 format.py | \
    wkhtmltopdf - resume.pdf

