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

def search_product(products):
    print('=' * 30)
    print('BUSCAR PRODUTO'.center(30))
    print('=' * 30)
    print('\n')
    user = int(input('1 - Buscar pelo ID\n' \
    '2 - Buscar pelo nome\n' \
    '3 - Buscar pela categoria\n' \
    '0 - Voltar\n' \
    '\n' \
    'Escolha: '))
    found1 = False
    found2 = False
    found3 = False
    category_found = []
    if user == 1:
        id_user = int(input('Digite o id do produto a ser pesquisado: '))
    elif user == 2:
        name_user = str(input('Digite o nome do produto a ser pesquisado: ')).upper().strip()
    elif user == 3:
         category_user = str(input('Digite o nome da categoria a ser pesquisada: ')).upper().strip()
    elif user == 0:
        return
    for product in products:
        if user == 1:
            if id_user == product['id']:
                found1 = True
                break
        elif user == 2:
            if name_user == product['name'].upper().strip():
                found2 = True
                break
        elif user == 3:
            if category_user == product['category'].upper().strip():
                found3 = True
                category_found.append(product)
    if found1 or found2:
        print(f'Id: {product['id']} | Nome: {product['name']} | Preço: {product['price']} | Quantidade: {product['amount']} | Categoria: {product['category']}')
    elif found3:
        for product in category_found:
            print(f'Id: {product['id']} | Nome: {product['name']} | Preço: {product['price']} | Quantidade: {product['amount']} | Categoria: {product['category']}')
    elif not found1 and not found2 and not found3:
        print('Produto não encontrado!')

def menu(products):
    while True:
        user = int(input(f'{'=' * 30}\n'
                         f'{'GERENCIADOR DE PRODUTOS'.center(30)}\n'
                         f'{'=' * 30}\n'
                         f'\n'
                         f'1 - Cadastrar produto\n'
                         f'2 - Listar produto(s)\n'
                         f'3 - Buscar produto\n'
                         f'4 - Remover produto\n'
                         f'0 - Sair\n'
                         f'\n'
                         f'Escolha uma opção: '))

        if user == 1:
            add_product(products)
        elif user == 2:
            show_products(products)
        elif user == 3:
            search_product(products)
        elif user == 4:
            remove_product(products)
        elif user == 0:
            break