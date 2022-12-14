import csv
from xml.etree.ElementTree import Element, ElementTree

def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml')
