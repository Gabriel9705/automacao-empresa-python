# Automação de Pedidos para TecnoLuz Soluções
# Este programa permite que os clientes façam pedidos de produtos relacionados à iluminação

produtos = {
    "lampada LED 9W": {"preco": 25.0, "estoque": 10},
    "soquete comum": {"preco": 8.0, "estoque": 15},
    "fita isolante": {"preco": 5.5, "estoque": 20},
    "chave de fenda": {"preco": 12.0, "estoque": 8},
}


def mostrar_produtos():
    print("\nProdutos disponíveis para venda:")
    print("--------------------------------")
    for nome, dados in produtos.items():
        print(f"{nome:<20} - R$ {dados['preco']:.2f} - Estoque: {dados['estoque']}")
    print()


def solicitar_pedido():
    pedido = {}
    while True:
        item = input("Digite o nome do produto (ou ENTER para finalizar): ").strip()
        if item == "":
            break
        if item not in produtos:
            print("Produto não encontrado. Tente novamente.")
            continue

        try:
            quantidade = int(input("Quantidade desejada: "))
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")
            continue

        if quantidade <= 0:
            print("Informe uma quantidade maior que zero.")
            continue

        if quantidade > produtos[item]["estoque"]:
            print(f"Não há estoque suficiente. Disponível: {produtos[item]['estoque']}")
            continue

        pedido[item] = pedido.get(item, 0) + quantidade

    return pedido


def calcular_total(pedido):
    total = 0.0
    for nome, quantidade in pedido.items():
        total += quantidade * produtos[nome]["preco"]
    return total


def atualizar_estoque(pedido):
    for nome, quantidade in pedido.items():
        produtos[nome]["estoque"] -= quantidade


def imprimir_relatorio(pedido):
    if not pedido:
        print("Nenhum produto foi pedido.")
        return

    print("\nResumo do pedido:")
    print("-----------------")
    for nome, quantidade in pedido.items():
        preco = produtos[nome]["preco"]
        subtotal = quantidade * preco
        print(f"{quantidade} x {nome} - R$ {preco:.2f} cada - Subtotal: R$ {subtotal:.2f}")

    total = calcular_total(pedido)
    print("-----------------")
    print(f"Valor total do pedido: R$ {total:.2f}")


def main():
    print("Bem-vindo à automação de pedidos da TecnoLuz Soluções")
    mostrar_produtos()

    pedido = solicitar_pedido()
    imprimir_relatorio(pedido)

    if pedido:
        atualizar_estoque(pedido)
        print("\nEstoque atualizado com sucesso.")
        mostrar_produtos()


if __name__ == "__main__":
    main()
