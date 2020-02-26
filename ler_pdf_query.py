import pdfquery
from lxml import etree


PDF_FILE = 'C:/testes/email_download/DARE.pdf'

pdf = pdfquery.PDFQuery(PDF_FILE)
pdf.load(1,5)

with open('xmltree.xml','wb') as f:
    f.write(etree.tostring(pdf.tree, pretty_print=True))

product_info = []
page_count = len(pdf._pages)
for pg in range(page_count):
    data = pdf.extract([
        ('with_parent', 'LTPage[pageid="{}"]'.format(pg+1)),
        ('with_formatter', None),
        ('product_name', 'LTTextLineHorizontal:in_bbox("89.904, 757.502, 265.7, 770.83")'),
        ('product_details', 'LTTextLineHorizontal:in_bbox("223, 100, 737, 1114")'),
    ])
    for ix, pn in enumerate(sorted([d for d in data['product_name'] if d.text.strip()], key=lambda x: x.get('y0'), reverse=True)):
        product_info.append({'Manufacturer': pn.text.strip(), 'page': pg, 'y_start': float(pn.get('y1')), 'y_end': float(pn.get('y1'))-150})
        if ix > 0:
            product_info[-2]['y_end'] = float(pn.get('y0'))
    for product in [p for p in product_info if p['page'] == pg]:
        details = []
        for d in sorted([d for d in data['product_details'] if d.text.strip()], key=lambda x: x.get('y0'), reverse=True):
            if  product['y_start'] > float(d.get('y0')) > product['y_end']:
                details.append(d.text.strip())
        product['Details'] = ' '.join(details)
pdf.file.close()

for p in product_info:
    print('Manufacturer: {}\r\nDetail Info:{}...\r\n\r\n'.format(p['Manufacturer'], p['Details'][0:100]))