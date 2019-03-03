import xml.etree.ElementTree
import csv

def joinXMLWithCSV(XMLFileName, csvFileName):
    products = extractProductsFromXMLFile(XMLFileName)
    products_and_prices_csv_writer = createCSVWriter('prices_and_products.csv');
    addFirstRow(products_and_prices_csv_writer, ['customer','Local code','Name','Price','Description','URL','LEN Code'])
    compareCodesAndWriteProducts(products, csvFileName, products_and_prices_csv_writer)

def extractProductsFromXMLFile(XMLFileName):
    return xml.etree.ElementTree.parse(XMLFileName).getroot().findall('Products')[0]

def createCSVWriter(csvToCreateName):
    products_and_prices_csv_writer = csv.writer(open(csvToCreateName, 'w', newline='', encoding='utf-8'),
                                                delimiter='|')
    return products_and_prices_csv_writer

def addFirstRow(products_and_prices_csv_writer, firstRow):
    products_and_prices_csv_writer.writerow(firstRow)

def compareCodesAndWriteProducts(products, csvFileName, csvWriter):
    for product in products.findall('Product'):
        code = product.attrib.get('LocalCode')
        name = product.findall('Name')[0].text

        with open(csvFileName) as csvFile:
            pricesCSV = csv.reader(csvFile, delimiter=';')
            for row in pricesCSV:
                if row[1] == code:
                    csvWriter.writerow([row[0], row[1], name, row[5], row[3], row[4], row[2]])
                    break

