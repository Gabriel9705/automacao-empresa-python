"""Front-end gráfico para a automação de pedidos da TecnoLuz Soluções.

Este programa cria uma interface simples em Tkinter para selecionar produtos,
quantidades, ver o pedido e atualizar o estoque.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from produtos import produtos
from pedido import adicionar_item, finalizar_pedido
from utils import (
    calcular_total,
    atualizar_estoque,
    atualizar_produtos_display,
    atualizar_pedido_display,
    atualizar_total_label,
    set_widgets,
)

pedido = {}


def criar_interface():
    # Variáveis globais para os widgets e dados
    global produto_var, quantidade_var, produtos_text, pedido_text, total_var

    janela = tk.Tk()
    janela.title("Luz do Bem - Automação de Pedidos")
    janela.geometry("760x560")
    janela.resizable(False, False)

    titulo = tk.Label(janela, text="Automação de Pedidos - Luz do Bem", font=("Helvetica", 14, "bold"))
    titulo.pack(pady=10)

    frame_principal = ttk.Frame(janela, padding=12)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    frame_produtos = ttk.LabelFrame(frame_principal, text="Produtos disponíveis", padding=10)
    frame_produtos.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

    frame_pedido = ttk.LabelFrame(frame_principal, text="Pedido", padding=10)
    frame_pedido.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

    frame_controle = ttk.LabelFrame(frame_principal, text="Controle de pedido", padding=10)
    frame_controle.grid(row=1, column=0, columnspan=2, padx=8, pady=8, sticky="ew")

    frame_principal.columnconfigure(0, weight=1)
    frame_principal.columnconfigure(1, weight=1)
    frame_principal.rowconfigure(1, weight=0)
    frame_controle.columnconfigure(0, weight=1)
    frame_controle.columnconfigure(1, weight=1)

    produtos_text = tk.Text(frame_produtos, width=34, height=12, state="disabled", wrap="none")
    produtos_text.pack(fill=tk.BOTH, expand=True)

    pedido_text = tk.Text(frame_pedido, width=34, height=12, state="disabled", wrap="none")
    pedido_text.pack(fill=tk.BOTH, expand=True)

    produto_var = tk.StringVar(value=list(produtos.keys())[0])
    quantidade_var = tk.StringVar(value="1")
    total_var = tk.StringVar(value="Total: R$ 0.00")

    # Configura referências aos widgets nas funções de utils
    set_widgets(produtos_text, pedido_text, total_var)

    ttk.Label(frame_controle, text="Produto:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
    selecionar_produto = ttk.Combobox(
        frame_controle,
        textvariable=produto_var,
        values=list(produtos.keys()),
        state="readonly",
        width=30,
    )
    selecionar_produto.grid(row=0, column=1, sticky="ew", padx=4, pady=4)

    ttk.Label(frame_controle, text="Quantidade:").grid(row=1, column=0, sticky="w", padx=4, pady=4)
    quantidade_entry = ttk.Entry(frame_controle, textvariable=quantidade_var, width=10)
    quantidade_entry.grid(row=1, column=1, sticky="w", padx=4, pady=4)

    adicionar_btn = ttk.Button(
        frame_controle, 
        text="Adicionar ao pedido", 
        command=lambda: adicionar_item(produto_var, quantidade_var, produtos, pedido, lambda: atualizar_pedido_display(pedido), lambda: atualizar_total_label(produtos, pedido))
    )
    adicionar_btn.grid(row=2, column=0, columnspan=2, sticky="ew", pady=8, padx=4)

    total_label = ttk.Label(frame_controle, textvariable=total_var, font=("Helvetica", 12, "bold"))
    total_label.grid(row=3, column=0, columnspan=2, pady=4)

    ttk.Separator(frame_controle, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=4)

    frame_botoes = ttk.Frame(frame_controle)
    frame_botoes.grid(row=5, column=0, columnspan=2, sticky="ew", pady=4, padx=4)
    frame_botoes.columnconfigure(0, weight=1)
    frame_botoes.columnconfigure(1, weight=1)

    adicionar_btn2 = ttk.Button(
        frame_botoes, 
        text="Adicionar ao pedido", 
        command=lambda: adicionar_item(produto_var, quantidade_var, produtos, pedido, lambda: atualizar_pedido_display(pedido), lambda: atualizar_total_label(produtos, pedido))
    )
    adicionar_btn2.grid(row=0, column=0, sticky="ew", padx=(0, 4))

    finalizar_btn = ttk.Button(
        frame_botoes, 
        text="Fechar pedido", 
        command=lambda: finalizar_pedido(pedido, produtos, lambda: calcular_total(produtos, pedido), lambda: atualizar_estoque(produtos, pedido), lambda: atualizar_produtos_display(produtos), lambda: atualizar_pedido_display(pedido), lambda: atualizar_total_label(produtos, pedido))
    )
    finalizar_btn.grid(row=0, column=1, sticky="ew", padx=(4, 0))

    sair_btn = ttk.Button(frame_botoes, text="Fechar programa", command=janela.destroy)
    sair_btn.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    atualizar_produtos_display(produtos)
    atualizar_pedido_display(pedido)
    atualizar_total_label(produtos, pedido)

    janela.mainloop()


if __name__ == "__main__":
    criar_interface()

