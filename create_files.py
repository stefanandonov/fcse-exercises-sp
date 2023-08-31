import os

import pypandoc

source_folders = ['mk', 'en']

HTML_OUTPUT_DIR = './output/output_html'

PDF_OUTPUT_DIR = './output/output_pdf'


def create_folder(path):
	dir_path = os.path.dirname(path)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)


for source_folder in source_folders:
	for doc in os.listdir(f"./src/{source_folder}"):
		doc_path = os.path.join(f"./src/{source_folder}", doc)
		html_path = os.path.join(HTML_OUTPUT_DIR, source_folder, doc.replace("md", "html"))
		create_folder(html_path)
		output = pypandoc.convert_file(
			source_file=doc_path,
			to='html',
			outputfile=html_path,
			extra_args=['-s']
		)

for source_folder in source_folders:
	for doc in os.listdir(f"./src/{source_folder}"):
		doc_path = os.path.join(f"./src/{source_folder}", doc)
		pdf_path = os.path.join(PDF_OUTPUT_DIR, source_folder, doc.replace("md", "pdf"))
		create_folder(pdf_path)
		output = pypandoc.convert_file(
			source_file=doc_path,
			to='pdf',
			outputfile=pdf_path,
			extra_args=['-s', '--pdf-engine=xelatex']
		)
