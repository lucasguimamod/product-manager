products = []

def add_product(products):
    product = {}
    product['id'] = int(input('Digite o id do produto: '))
    product['name'] = str(input('Digite o nome do produto: '))
    product['price'] = float(input('Digite o preço do produto: '))
    product['amount'] = int(input('Digite a quantidade do produto: '))
    product['category'] = str(input('Digite a categoria deste produto: '))
    products.append(product)