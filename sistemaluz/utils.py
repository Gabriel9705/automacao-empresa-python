"""Módulo com funções utilitárias para a automação de pedidos."""

import tkinter as tk


# Variáveis globais para acessar os widgets
produtos_text = None
pedido_text = None
total_var = None


def calcular_total(produtos, pedido):
    """Calcula o total do pedido."""
    return sum(quantidade * produtos[nome]["preco"] for nome, quantidade in pedido.items())


def atualizar_estoque(produtos, pedido):
    """Atualiza o estoque após a finalização do pedido."""
    for nome, quantidade in pedido.items():
        produtos[nome]["estoque"] -= quantidade


def atualizar_produtos_display(produtos):
    """Atualiza a exibição de produtos disponíveis."""
    global produtos_text
    produtos_text.config(state="normal")
    produtos_text.delete("1.0", tk.END)
    for nome, dados in produtos.items():
        estoque = dados.get("estoque", 0)
        preco = dados.get("preco", 0.0)
        produtos_text.insert(
            tk.END,
            f"{nome:<20} - R$ {preco:.2f} - Estoque: {estoque}\n",
        )
    produtos_text.config(state="disabled")


def atualizar_pedido_display(pedido):
    """Atualiza a exibição do pedido atual."""
    global pedido_text
    pedido_text.config(state="normal")
    pedido_text.delete("1.0", tk.END)
    if not pedido:
        pedido_text.insert(tk.END, "Nenhum item no pedido.\n")
    else:
        for nome, quantidade in pedido.items():
            pedido_text.insert(tk.END, f"{quantidade} x {nome}\n")
    pedido_text.config(state="disabled")


def atualizar_total_label(produtos, pedido):
    """Atualiza o label do total do pedido."""
    global total_var
    total = calcular_total(produtos, pedido)
    total_var.set(f"Total: R$ {total:.2f}")


def set_widgets(prods_text, ped_text, tot_var):
    """Define referências aos widgets globais."""
    global produtos_text, pedido_text, total_var
    produtos_text = prods_text
    pedido_text = ped_text
    total_var = tot_var
