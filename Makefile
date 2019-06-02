.PHONE: clean

resume.pdf: resume.md
	grip resume.md --wide --export - | \
		python3 format.py | \
		wkhtmltopdf \
			-T 1in -B 1in -L 1in -R 1in \
			-s A4 \
			--title "Resume - Mark Steve Samson" \
			- resume.pdf
clean:
	rm resume.pdf
