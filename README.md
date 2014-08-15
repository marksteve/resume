# My resume

## Export to PDF

### Requires

- [grip](https://github.com/joeyespo/grip) - Markdown to HTML with GitHub styling
- [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf) - PDF conversion

### Exporting

```sh
grip resume.md --wide --export - > resume.html
# Edit resume.html to remove container divs
wkhtmltopdf resume.html resume.pdf
```

## TODO

- [ ] Make a one-liner command to export to pdf
