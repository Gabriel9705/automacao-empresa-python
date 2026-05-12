
"""Módulo de funções relacionadas a pedidos."""

from tkinter import messagebox


def adicionar_item(produto_var, quantidade_var, produtos, pedido, atualizar_pedido_display, atualizar_total_label):
    """Adiciona um item ao pedido."""
    item = produto_var.get()
    try:
        quantidade = int(quantidade_var.get())
    except ValueError:
        messagebox.showwarning("Quantidade inválida", "Digite um número inteiro para a quantidade.")
        return

    if quantidade <= 0:
        messagebox.showwarning("Quantidade inválida", "Informe uma quantidade maior que zero.")
        return

    if item not in produtos:
        messagebox.showwarning("Produto inválido", "Selecione um produto válido.")
        return

    if quantidade > produtos[item]["estoque"]:
        messagebox.showwarning(
            "Estoque insuficiente",
            f"Não há estoque suficiente para {item}. Disponível: {produtos[item]['estoque']}",
        )
        return

    pedido[item] = pedido.get(item, 0) + quantidade
    atualizar_pedido_display()
    atualizar_total_label()


def finalizar_pedido(pedido, produtos, calcular_total, atualizar_estoque, atualizar_produtos_display, atualizar_pedido_display, atualizar_total_label):
    """Finaliza o pedido e atualiza o estoque."""
    if not pedido:
        messagebox.showinfo("Nenhum pedido", "Nenhum produto foi adicionado ao pedido.")
        return

    total = calcular_total()
    resumo = "Resumo do pedido:\n\n"
    for nome, quantidade in pedido.items():
        preco = produtos[nome]["preco"]
        subtotal = quantidade * preco
        resumo += f"{quantidade} x {nome} - R$ {preco:.2f} cada - Subtotal: R$ {subtotal:.2f}\n"
    resumo += f"\nValor total: R$ {total:.2f}"

    messagebox.showinfo("Pedido finalizado", resumo)
    atualizar_estoque()
    pedido.clear()
    atualizar_produtos_display()
    atualizar_pedido_display()
    atualizar_total_label()


def atualizar_estoque():
    for nome, quantidade in pedido.items():
        produtos[nome]["estoque"] -= quantidade


def atualizar_produtos_display():
    produtos_text.config(state="normal")
    produtos_text.delete("1.0", tk.END)
    for nome, dados in produtos.items():
        produtos_text.insert(
            tk.END,
            f"{nome:<20} - R$ {dados['preco']:.2f} - Estoque: {dados['estoque']}\n",
        )
    produtos_text.config(state="disabled")


def atualizar_pedido_display():
    pedido_text.config(state="normal")
    pedido_text.delete("1.0", tk.END)
    if not pedido:
        pedido_text.insert(tk.END, "Nenhum item no pedido.\n")
    else:
        for nome, quantidade in pedido.items():
            pedido_text.insert(tk.END, f"{quantidade} x {nome}\n")
    pedido_text.config(state="disabled")


def atualizar_total_label():
    total = calcular_total()
    total_var.set(f"Total: R$ {total:.2f}")