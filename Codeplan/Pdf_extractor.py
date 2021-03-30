import PyPDF2
import re


pyfile = open('./Uma Vida com Propositos.pdf', 'rb')    #Abre o PDF
read_pdf = PyPDF2.PdfFileReader(pyfile)                 #Le o PDF

page = read_pdf.getPage(1)                              #Seleciona uma página
page_content = page.extractText()                       #Pega o conteudo da pagina
number_pages = read_pdf.getNumPages()                   #Pega o número de páginas
parsed = ''.join(page_content)                          #Junta as linhas
parsed = re.sub('\n', '', parsed)                       #Remove a quebra de linhas
print(parsed)




