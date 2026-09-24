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
            print(f"ID: {product['id']}\n"
                f"Nome: {product['name']}\n"
                f"Preço: {product['price']}\n"
                f"Quantidade: {product['amount']}\n"
                f"Categoria: {product['category']}\n"
                f"{'-' * 30}")

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
        print(f"Id: {product['id']} | Nome: {product['name']} | Preço: {product['price']} | Quantidade: {product['amount']} | Categoria: {product['category']}")
    elif found3:
        for product in category_found:
            print(f"Id: {product['id']} | Nome: {product['name']} | Preço: {product['price']} | Quantidade: {product['amount']} | Categoria: {product['category']}")
    elif not found1 and not found2 and not found3:
        print('Produto não encontrado!')

def stock_report(products):
    print('=' * 30)
    print('RELATÓRIO DE ESTOQUE'.center(30))
    print('=' * 30)
    print('\n')

    found = True
    counter = 0
    total_amount = 0
    total_price = 0
    if len(products) > 0:
        max_amount = products[0]
        min_amount = products[0]
    else:
        print('Não há produtos cadastrados!')
        return
    for product in products:
        counter += 1
        total_amount += product['amount']
        total_price += product['price'] * product['amount']
        if product['amount'] > max_amount['amount']:
            max_amount = product
        elif product['amount'] < min_amount['amount']:
            min_amount = product
    if found:
        print(f'Produtos cadastrados: {counter}')
        print(f'Quantidade total em estoque: {total_amount}')
        print(f'Valor total do estoque: {total_price}')
        print('\n\n')
        print(f"Produto com maior estoque:\n{max_amount['name']} - {max_amount['amount']} unidades\n\n")
        print(f"Produto com menor estoque:\n{min_amount['name']} - {min_amount['amount']} unidades")

def low_stock(products):
    user = int(input('Digite o limite de estoque: '))
    print('=' * 30)
    print('ESTOQUE BAIXO'.center(30))
    print('=' * 30)
    print('\n')
    print('Produtos com estoque baixo:\n' \
    '\n')
    if len(products) == 0:
        print('Não há produtos cadastrados!')
        return
    found = False
    for product in products:
        if product['amount'] <= user:
            print(f'ID {product['id']} | {product['name']} | {product['amount']} unidades\n'
            '\n'
            '-' * 30)
            found = True
    if not found:
        print('Nenhum produto com estoque baixo!')

def sort_products(products):
    user = int(input('Escolha a ordem\n' \
    '1 - Menor -> Maior\n' \
    '2 - Maior -> Menor\n' \
    '0 - Voltar ao menu\n' \
    'Escolha: '))
    if len(products) == 0:
        print('Não há produtos cadastrados!')
        return
    elif user == 0:
        return
    elif user == 1:
        products = sorted(products, key=lambda product: product['price'])
    elif user == 2:
        products = sorted(products, key=lambda product: product['price'], reverse = True)
    for product in products:
        print(f'{product['name']} - R$ {product['price']}')

def product_value(products):
    user = int(input('Digite o ID de um produto: '))
    found = False
    if len(products) == 0:
        print('Não há produtos cadastrados!')
        return
    for product in products:
        if user == product['id']:
            print(f'Produto: {product['name']}\n'
                  f'Preço unitário: R$ {product['price']}\n'
                  f'Quantidade: {product['amount']}\n'
                  f'Valor em estoque: R$ {product['price'] * product['amount']:.2f}')
            found = True
            break
    if not found:
        print('Produto não encontrado!')

def update_stock(products):
    user = int(input('Digite o ID do produto a ser alterado: '))
    if len(products) == 0:
        print('Não há produtos cadastrados!')
        return
    found = False
    for product in products:
        if user == product['id']:
            found = True
            print(f'Quantidade atual: {product['amount']}')
            new_amount = int(input('Digite a nova quantidade: '))
            product['amount'] = new_amount
            print('Produto atualizado!')
            break
    if not found:
        print('Produto não encontrado!')

def filter_price(products):
    user1 = int(input('Preço mínimo: '))
    user2 = int(input('Preço máximo: '))
    if len(products) == 0:
        print('Não há produtos cadastrados!')
        return
    print('=' * 30)
    print('FILTRO DE PREÇO'.center(30))
    print('=' * 30)
    print('\n'
    'Produtos encontrados:\n'
    '\n')
    found = False
    for product in products:
        if user1 <= product['price'] <= user2:
            print(f'ID: {product['id']} | {product['name']} | R$ {product['price']:.2f}')
            found = True
    if not found:
        print('Nenhum produto se encaixa no requisito!')

def menu(products):
    while True:
        user = int(input(
            '=' * 30 + '\n'
            + 'GERENCIADOR DE PRODUTOS'.center(30) + '\n'
            + '=' * 30 + '\n\n'
            + '1 - Cadastrar produto\n'
            + '2 - Listar produto(s)\n'
            + '3 - Buscar produto\n'
            + '4 - Remover produto\n'
            + '5 - Relatório de estoque\n'
            + '6 - Verificar estoque por quantidade'
            + '7 - Ordenar produtos pelo valor\n'
            + '8 - Valor total de um produto\n'
            + '9 - Atualizar produto\n'
            + '10 - Filtrar por faixa de preço\n'
            + '0 - Sair\n'
            + 'Escolha uma opção: '
        ))

        if user == 1:
            add_product(products)
        elif user == 2:
            show_products(products)
        elif user == 3:
            search_product(products)
        elif user == 4:
            remove_product(products)
        elif user == 5:
            stock_report(products)
        elif user == 6:
            low_stock(products)
        elif user == 7:
            sort_products(products)
        elif user == 8:
            product_value(products)
        elif user == 9:
            update_stock(products)
        elif user == 10:
            filter_price(products)
        elif user == 0:
            break