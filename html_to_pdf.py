# import pdfkit
# # Set the options for wkhtmltopdf
# options = {
#     'page-size': 'A4',
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm'
# }

# # Set the URL of the webpage to convert
# url = 'https://www.geeksforgeeks.org/downloading-pdfs-with-python-using-requests-and-beautifulsoup/'

# # Set the filename for the output PDF
# output_filename = 'example.pdf'

# # Convert the webpage to PDF using pdfkit
# pdfkit.from_url(url, output_filename, options=options)W



import pdfkit  
  
# configuring pdfkit to point to our installation of wkhtmltopdf  
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  
  
# converting url to pdf file  
pdfkit.from_url('https://app.grammarly.com/', 'output2.pdf', configuration = config)  