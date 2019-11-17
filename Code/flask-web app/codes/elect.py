from __future__ import print_function

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTPage, LTRect, LTChar
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage

fp = open(r"C:/Users/SAMARTH G VASIST/ceo-kar-roll-scraper/er-test.pdf", "rb")


p=open("electordetails.txt","w+")
parser = PDFParser(fp)
doc = PDFDocument(parser)

parser.set_document(doc)
#doc.set_parser(parser)

#doc.initialize("")

if not doc.is_extractable:
	raise PDFTextExtractionNotAllowed

resmgr = PDFResourceManager()
device = PDFPageAggregator(resmgr, laparams=None)

interpreter = PDFPageInterpreter(resmgr, device)

for page in PDFPage.create_pages(doc):
	interpreter.process_page(page)
	layout = device.get_result()

	# First 2 pages are metadata - we need to parse those separately
	if layout.pageid < 3:
		continue

	first = True
	old_y0 = 0

	for child in layout:
		# Text upto the first LTRect is just a header
		if first:
			if not isinstance(child, LTRect):
				continue
			else:
				first = False

		if isinstance(child, LTRect):
			print("\n----")
			p.write('\n')			
		elif isinstance(child, LTChar):
			# This is used to detect word boundaries
			if old_y0 != child.y0:
				old_y0 = child.y0
				print(" | ", end="")
				p.write(' | ')
			print(child.get_text(), end="")
			p.write(child.get_text())			
            
p.close()            
            
            
