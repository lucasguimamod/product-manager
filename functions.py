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

def remove_product(products):
    user = int(input('1 - Remover pelo id\n'
                     '2 - Remover pelo nome\n'
                     '0 - Voltar ao menu\n'
                     'Escolha: '))
    found = False
    if user == 1:
        id_user = int(input('Digite o id do produto a ser removido: '))
        for product in products:
            if id_user == product['id']:
                found = True
                products.remove(product)
    elif user == 2:
        name_user = str(input('Digite o nome do produto a ser removido: ')).upper().strip()
        for product in products:
            if name_user == product['name'].upper():
                found = True
                products.remove(product)
    elif user == 0:
        return
    if not found:
        print('Produto não encontrado!')

def update_product(products):
        user = int(input('1 - Atualizar pelo id\n'
                     '2 - Atualizar pelo nome\n'
                     '0 - Voltar ao menu\n'
                     'Escolha: '))
    found = False
    if user == 1:
        id_user = int(input('Digite o id do produto a ser atualizado: '))
    elif user == 2:
        name_user = str(input('Digite o nome do produto a ser atualizado: ')).upper().strip()
    elif user == 0:
        return
    for product in products:
        if user == 1:
            if id_user == product['id']:
                found = True
                break
        if user == 2:
            if name_user == product['name'].upper():
                found = True
                break
    if found:
        product['name'] = str(input('Digite o nome atualizado do produto: '))
        product['price'] = float(input('Digite o preço atualizado do produto: '))
        product['amount'] = int(input('Digite a quantidade atualizada do produto: '))
        product['category'] = str(input('Digite a categoria atualizada do produto: '))
    
    if not found:
        print('Produto não encontrado!')

def menu(products):
    while True:
        user = int(input(f'{'=' * 30}\n'
                         f'{'GERENCIADOR DE PRODUTOS'.center(30)}\n'
                         f'{'=' * 30}\n'
                         f'\n'
                         f'1 - Cadastrar produto\n'
                         f'2 - Listar produto(s)\n'
                         f'3 - Remover produto\n'
                         f'0 - Sair\n'
                         f'\n'
                         f'Escolha uma opção: '))

        if user == 1:
            add_product(products)
        elif user == 2:
            show_products(products)
        elif user == 3:
            remove_product(products)
        elif user == 0:
            break