import os


def generate_index(html_files_directory):
	is_en = html_files_directory.endswith("en")

	html_files = [filename for filename in os.listdir(html_files_directory) if
	              filename.endswith('.html') and not filename.startswith("index")]
	html_files.sort()  # Sort the filenames numerically

	index_content = '<html>\n<head>\n<meta charset="utf-8" />\n<title>Index</title>\n</head>\n<body>\n'

	index_content += '<h1>Аудиториски вежби по Структурно програмирање</h1>\n' if not is_en \
		else '<h1>Auditory exercises in Structural programming</h1>\n'

	index_content += f'<h2>Содржина</h2>\n' if not is_en else "<h2>Content</h2>"

	for filename in html_files:
		index_content += f'<a href="{filename}">{"Аудиториска вежба бр." if not is_en else "Auditory exercise #"} {filename.replace(".html", "")}</a><br>\n'

	index_content += '</body>\n</html>'

	with open(os.path.join(html_files_directory, 'index.html'), 'w') as index_file:
		index_file.write(index_content)


if __name__ == "__main__":
	generate_index(html_files_directory="./output/output_html/en")
	generate_index(html_files_directory="./output/output_html/mk")
