products = []

def add_product(products):
    product = {}
    product['id'] = int(input('Digite o id do produto: '))
    product['name'] = str(input('Digite o nome do produto: '))
    product['price'] = float(input('Digite o preço do produto: '))
    product['amount'] = int(input('Digite a quantidade do produto: '))
    product['category'] = str(input('Digite a categoria deste produto: '))
    products.append(product)

def show_products(products):
    print('=' * 30)
    print('PRODUTOS CADASTRADOS'.center(30))
    print('=' * 30)
    if len(products) == 0:
        print('Nenhum produto cadastrado no sistema!')
        return
    else:
        for product in products:
            print(f'ID: {product['id']}\n'
                  f'Nome: {product['name']}\n'
                  f'Preço: {product['price']}\n'
                  f'Quantidade: {product['amount']}\n'
                  f'Categoria: {product['category']}\n'
                  f'{'-' * 30}')