import PyPDF2

pdFiles = ["1.pdf","2.pdf","sample.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdFiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')