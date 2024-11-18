import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import os

# Dicionário para armazenar os produtos
estoque = {}

# Função para cadastrar um produto
def cadastrar_produto():
    id_produto = entry_id.get()
    nome_produto = entry_nome.get()
    preco_produto = float(entry_preco.get())
    quantidade_produto = int(entry_quantidade.get())
    estoque[id_produto] = {
        'nome': nome_produto,
        'preco': preco_produto,
        'quantidade': quantidade_produto
    }
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    atualizar_lista()
    limpar_campos()

# Função para consultar um produto
def consultar_produto():
    id_produto = entry_id.get()
    if id_produto in estoque:
        produto = estoque[id_produto]
        messagebox.showinfo("Produto Encontrado", f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")
    else:
        messagebox.showerror("Erro", "Produto não encontrado.")

# Função para gerar relatório em Excel
def gerar_relatorio():
    if not estoque:
        messagebox.showerror("Erro", "Nenhum produto cadastrado.")
        return

    df = pd.DataFrame.from_dict(estoque, orient='index')
    df['valor_total'] = df['preco'] * df['quantidade']
    df.to_excel('relatorios/relatorio_estoque.xlsx')
    messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

# Função para atualizar a lista de produtos
def atualizar_lista():
    listbox_produtos.delete(0, tk.END)
    for id_produto, produto in estoque.items():
        listbox_produtos.insert(tk.END, f"ID: {id_produto}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")

# Função para criar a interface gráfica principal
def criar_interface(is_admin):
    root = tk.Tk()
    root.title("Sistema de Estoque")
    root.geometry("800x600")  # Aumenta o tamanho da tela
    root.configure(bg="#2C3E50")  # Fundo cinza escuro

    style = ttk.Style()
    style.configure("TLabel", background="#2C3E50", foreground="white", font=("Arial", 14))
    style.configure("TButton", background="#2980B9", foreground="black", font=("Arial", 14))
    style.configure("TEntry", font=("Arial", 14))
    style.configure("TListbox", font=("Arial", 14))

    global entry_id, entry_nome, entry_preco, entry_quantidade, listbox_produtos, label_img

    ttk.Label(root, text="ID do Produto").grid(row=0, column=0, padx=10, pady=10)
    entry_id = ttk.Entry(root, width=30)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="Nome do Produto").grid(row=1, column=0, padx=10, pady=10)
    entry_nome = ttk.Entry(root, width=30)
    entry_nome.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="Preço do Produto (R$)").grid(row=2, column=0, padx=10, pady=10)
    entry_preco = ttk.Entry(root, width=30)
    entry_preco.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(root, text="Quantidade do Produto").grid(row=3, column=0, padx=10, pady=10)
    entry_quantidade = ttk.Entry(root, width=30)
    entry_quantidade.grid(row=3, column=1, padx=10, pady=10)

    ttk.Button(root, text="Cadastrar Produto", command=cadastrar_produto).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    ttk.Button(root, text="Consultar Produto", command=consultar_produto).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    if is_admin:
        ttk.Button(root, text="Gerar Relatório", command=gerar_relatorio).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        # Atualiza a imagem para o administrador
        label_img.configure(image=img_adm)
        label_img.image = img_adm  # Mantém referência da imagem para evitar garbage collection

    ttk.Label(root, text="Produtos Cadastrados").grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    listbox_produtos = tk.Listbox(root, width=80, height=10, font=("Arial", 14), bg="#34495E", fg="white")
    listbox_produtos.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Função para criar a interface de login
def criar_interface_login():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.configure(bg="#2C3E50")  # Fundo cinza escuro

    style = ttk.Style()
    style.configure("TLabel", background="#2C3E50", foreground="white", font=("Arial", 14))
    style.configure("TButton", background="#2980B9", foreground="black", font=("Arial", 14))
    style.configure("TEntry", font=("Arial", 14))

    ttk.Label(login_window, text="Usuário").grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = ttk.Entry(login_window, width=30)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(login_window, text="Senha").grid(row=1, column=0, padx=10, pady=10)
    entry_senha = ttk.Entry(login_window, show="*", width=30)
    entry_senha.grid(row=1, column=1, padx=10, pady=10)

    global img_adm, img_user, label_img

    def login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "adm" and senha == "11042003":
            login_window.destroy()
            criar_interface(True)
        elif usuario == "padrao" and senha == "1234":
            login_window.destroy()
            criar_interface(False)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    ttk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Adiciona uma imagem para diferenciar o administrador do usuário comum
    img_adm_path = os.path.join(os.path.dirname(__file__), 'adm.png')
    img_user_path = os.path.join(os.path.dirname(__file__), 'padrao.png')

    img_adm = Image.open(img_adm_path)
    img_adm = img_adm.resize((100, 100), Image.LANCZOS)
    img_adm = ImageTk.PhotoImage(img_adm)

    img_user = Image.open(img_user_path)
    img_user = img_user.resize((100, 100), Image.LANCZOS)
    img_user = ImageTk.PhotoImage(img_user)

    label_img = ttk.Label(login_window, image=img_user)
    label_img.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    login_window.mainloop()

if __name__ == "__main__":
    criar_interface_login()
