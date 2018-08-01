.PHONE: clean

resume.pdf: resume.md
	grip resume.md --wide --export - | \
		python3 format.py | \
		wkhtmltopdf - resume.pdf
clean:
	rm resume.pdf
