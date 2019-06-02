.PHONE: clean

resume.pdf: resume.md
	grip resume.md --wide --export - | \
		python3 format.py | \
		wkhtmltopdf --title "Resume - Mark Steve Samson" - resume.pdf
clean:
	rm resume.pdf
