# Automação de Pedidos - TecnoLuz Soluções

Sistema de automação para controle de pedidos e estoque de uma empresa de material elétrico.

## 📋 Descrição

Este projeto implementa uma solução completa de automação para uma pequena empresa, demonstrando como a programação pode otimizar processos de negócio. Inclui:

- **Interface gráfica** para gerenciamento de pedidos
- **Controle automático de estoque**
- **Cálculo de valores** em tempo real
- **Validação de dados** e tratamento de erros

## 🚀 Funcionalidades

### Sistema de Pedidos
- ✅ Seleção de produtos do catálogo
- ✅ Controle de quantidade disponível
- ✅ Cálculo automático de valores
- ✅ Resumo detalhado do pedido
- ✅ Atualização automática do estoque

### Interface Gráfica
- ✅ Design intuitivo com Tkinter
- ✅ Validação em tempo real
- ✅ Mensagens de erro claras
- ✅ Layout responsivo

## 📁 Estrutura do Projeto

```
python/
├── .gitignore
├── df/
│   └── desafio_empreeder.py    # Cálculo de lâmpadas por área
├── sistemaluz/
│   ├── automacao_empresa.py    # Versão console do sistema
│   ├── automacao_empresa_front.py  # Interface gráfica
│   ├── pedido.py               # Funções de gerenciamento de pedidos
│   ├── produtos.py             # Catálogo de produtos
│   └── utils.py                # Funções utilitárias
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Tkinter** (interface gráfica)
- **Git** (controle de versão)

## 📦 Instalação e Uso

### Pré-requisitos
- Python 3.14 ou superior
- Git

### Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USERNAME/SEU_REPOSITORIO.git
   cd python
   ```

2. **Execute a versão gráfica:**
   ```bash
   python sistemaluz/automacao_empresa_front.py
   ```

3. **Ou execute a versão console:**
   ```bash
   python sistemaluz/automacao_empresa.py
   ```

## 🎯 Como usar o sistema

1. **Selecionar produto:** Escolha um item do catálogo
2. **Definir quantidade:** Digite a quantidade desejada
3. **Adicionar ao pedido:** Clique em "Adicionar ao pedido"
4. **Finalizar:** Clique em "Fechar pedido" para confirmar
5. **Sair:** Use "Fechar programa" para encerrar

## 📊 Produtos Disponíveis

- Lâmpada LED 9W - R$ 25,00
- Soquete comum - R$ 8,00
- Fita isolante - R$ 5,50
- Chave de fenda - R$ 12,00
- E outros produtos elétricos

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Usuario** - *Desenvolvimento inicial*

## 🙏 Agradecimentos

- Projeto desenvolvido como exemplo de automação empresarial
- Demonstra integração entre programação e processos de negócio
- Base para expansão com novos recursos (banco de dados, web, etc.)