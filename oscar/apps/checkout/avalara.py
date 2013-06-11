import datetime
import requests


class DocType:
    SalesOrder = "SalesOrder"
    SalesInvoice = "SalesInvoice"
    ReturnOrder = "ReturnOrder"
    ReturnInvoice = "ReturnInvoice"


class DetailLevel:
    Summary = 'Summary'
    Document = 'Summary'
    Line = "Line"
    Tax = 'Tax'
    Diagnostic = 'Diagnostic'


def get_tax(basket, addresses):
    assert basket.total_excl_tax > 0
    assert len(addresses) > 0
    payload = {
        'DocType': DocType.SalesOrder,
        'DocDate': datetime.date.today().strftime('%Y-%m-%d'),
        'DetailLevel': DetailLevel.Document,
        'Addreses': [],
        'Lines': []}
    for address in addresses:
        payload['Addresses'].append({
            'AddressCode': address.id,
            'Line1': address.line1,
            'Line2': address.line2,
            'City': address.city,
            'Region': address.state,
            'PostalCode': address.postcode,
        })
    for line in basket.all_lines():
        payload['Lines'].append({
            'LineNo': line.id,
            'DestinationCode': addresses[0].id,  # use first address by default
            'OriginCode': '',
            'Quantity': line.qty,
            'Amount': line.total_excl_tax,
        })

    username, password = '', ''
    headers = {
        'Authorization': ''
    }
    url = 'https://development.avalara.net/1.0/tax/'
    response = requests.get(url, payload, headers=headers)


