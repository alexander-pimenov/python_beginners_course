# Конвертируем .docx в .pdf с помощью библиотеки docx2pdf
from docx2pdf import convert

# Путь к сохранённому .docx
# input_docx = "/mnt/data/Alexander_Pimenov_CV_Updated.docx"
# output_pdf = "/mnt/data/Alexander_Pimenov_CV_Updated.pdf"
input_docx_1 = "C:\Users\pimal\Documents\Подготовка к интервью\CV\Alexander_Pimenov_CV_Updated.docx"
output_pdf_1 = "C:\Users\pimal\Documents\Подготовка к интервью\CV\Alexander_Pimenov_CV_Updated.pdf"

# Конвертация
convert(input_docx_1, output_pdf_1)

# output_pdf
output_pdf_1
