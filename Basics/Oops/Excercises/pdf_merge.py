# merge the pdf using pypdf module
import PyPDF2
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path1 = os.path.join(script_dir, 'New_Adhar.pdf')
file_path2 = os.path.join(script_dir, 'pancard.pdf')

pdf1 = open(file_path1, "rb")
pdf2 = open(file_path2, "rb")

reader1 = PyPDF2.PdfReader(pdf1)
reader2 = PyPDF2.PdfReader(pdf2)

writer = PyPDF2.PdfWriter()

for page in reader1.pages:
    writer.add_page(page)

for page in reader2.pages:
    writer.add_page(page)

output = open(os.path.join(script_dir, "merged.pdf"), "wb")
writer.write(output)

pdf1.close()
pdf2.close()
output.close()

print("Hello I'm Tejas")
