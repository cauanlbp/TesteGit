from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import datetime
from pymongo import MongoClient

# Criar conexão com o MongoDB
uri = "mongodb+srv://cauanlbp:<password>@cluster0.953cqto.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Substitua '<password>' com sua senha MongoDB Atlas
uri = uri.replace("<password>", "Ov0qooNRoxHkcOHP")

client = MongoClient(uri)
db = client['Cluster0']  # substitua 'seu_banco_de_dados' pelo nome do seu banco
collection = db['produtos']  # nome da coleção onde os produtos serão armazenados

# Criar tela principal
root = ctk.CTk()
root.title("GK PDV")
root._set_appearance_mode("light")
root.geometry("1366x765")
root.state('zoomed')

#Cores
azul = "#172635"  # Hexadecimal para um tom escuro de vermelho
preto= "#1B1816"
cinza= "#202124"
ciano= "#0DCBEF"

def login():
    # Criar a janela de login
    login_window = ctk.CTkToplevel(root, fg_color=azul)
    login_window.geometry("800x700")
    login_window.maxsize(width=800, height=700)
    login_window.minsize(width=800, height=700)
    login_window.resizable(width=False, height=False)
    login_window.title("Login")

#Frame
    frame_login=ctk.CTkFrame(master=login_window, width=500, height=480,fg_color=preto,border_width=3,corner_radius=20,border_color=ciano)
    frame_login.pack(pady=100)

    #Logo
    logo_image = Image.open("./simbolo.png")
    logo = ImageTk.PhotoImage(logo_image.resize((200, 100)))
    ctk.CTkLabel(frame_login, text=None, image=logo, bg_color=preto).place(x=160, y=60)
        
    # Campos de entrada para nome de usuário e senha

    username_entry = ctk.CTkEntry(master=frame_login, width=300,placeholder_text="nome do usuário",fg_color=cinza,height=50)
    username_entry.place(x=100,y=200)


    password_entry = ctk.CTkEntry(master=frame_login, width=300, placeholder_text="sua senha",show="*",fg_color=cinza,height=50 )  # Show="*" oculta a senha
    password_entry.place(x=100,y=280)

    # Função de verificação de login
    def verificar_login():
        # Aqui você pode adicionar a lógica para verificar as credenciais
        # Por exemplo, verificar se o nome de usuário e a senha estão corretos
        # Se estiverem corretos, feche a janela de login e abra a janela principal
        if username_entry.get() == "" and password_entry.get() == "":
            login_window.destroy()  # Fechar janela de login
            root.deiconify()  # Restaurar janela principal

    # Botão de login
    login_button = ctk.CTkButton(master=frame_login, text="ENTRAR", command=verificar_login, fg_color=azul, width=300, height=50,font=("Arial Bold",20))
    login_button.place(x=100,y=360)

    # Você pode adicionar mais elementos à sua tela de login conforme necessário
    # Por exemplo, links para redefinir senha, registrar, etc.

# Função para abrir a tela de login
def abrir_login():   
    root.iconify()  # Minimizar a janela principal
    login()  # Chamar a função de login

# Chamar a função para abrir a tela de login
abrir_login()

# Função para atualizar a hora
def atualizar_horario():
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    label_horario.config(text=hora_formatada)
    label_horario.after(1000, atualizar_horario)  # Atualiza a cada 1000ms (1 segundo)

# Criar o rótulo para exibir a hora
label_horario = Label(root, font=("Arial", 18),fg="gray")
label_horario.place(x=1600, y=170)

# Iniciar a função para atualizar o horário
atualizar_horario()

def finalizar_compra():
    finalizar_compra_window = ctk.CTkToplevel(root, fg_color="white")
    finalizar_compra_window.geometry("800x700")
    finalizar_compra_window.grab_set()  # Torna a janela de finalizar compra modal
    
    #Frame Cadastro de Produto

    frame_finalizar= ctk.CTkFrame(master=finalizar_compra_window, width=2000, height=100, fg_color=azul, bg_color=azul)
    frame_finalizar.place(x=0, y=0)
    
    #Label
    ctk.CTkLabel(finalizar_compra_window, text="R$ SUB TOTAL",font=("Arial Bold",18),bg_color="gray",text_color="gray").place(x=390, y=200)


# Código e Descrição
entry_barra_codigo = ctk.CTkEntry(root, width=1370, height=50, placeholder_text="Código/Descrição")
entry_barra_codigo.place(x=199, y=200)

# Quantidade
entry_quantidade = ctk.CTkEntry(root, width=150, height=50, placeholder_text="Quantidade")
entry_quantidade.place(x=199, y=400)

# Valor Unitario
entry_unitario = ctk.CTkEntry(root, width=150, height=50, placeholder_text="Valor Unitário")
entry_unitario.place(x=199, y=500)

# Valor Total
entry_total = ctk.CTkEntry(root, width=150, height=50, placeholder_text="Valor Total")
entry_total.place(x=199, y=600)

def pesquisar_produto():
    codigo_produto = entry_barra_codigo.get()

    # Consultar o MongoDB para encontrar o produto pelo código
    produto_encontrado = collection.find_one({"codigo_produto": codigo_produto})

    if produto_encontrado:
        # Limpar o frame antes de exibir o novo produto
        for widget in frame_right.winfo_children():
            widget.destroy()

        # Exibir os detalhes do produto no frame
        ctk.CTkLabel(master=frame_right, text=f"Nome: {produto_encontrado['nome_produto']}", font=("Arial", 18), bg_color=azul, text_color="white").pack()
        ctk.CTkLabel(master=frame_right, text=f"Valor Unitário: {produto_encontrado['valor_unitario']}", font=("Arial", 18), bg_color=azul, text_color="white").pack()
        ctk.CTkLabel(master=frame_right, text=f"Quantidade: {produto_encontrado['quantidade']}", font=("Arial", 18), bg_color=azul, text_color="white").pack()
        ctk.CTkLabel(master=frame_right, text=f"Imposto: {produto_encontrado['imposto']}", font=("Arial", 18), bg_color=azul, text_color="white").pack()
    else:
        # Limpar o frame se nenhum produto for encontrado
        for widget in frame_right.winfo_children():
            widget.destroy()

        # Exibir uma mensagem se nenhum produto for encontrado
        ctk.CTkLabel(master=frame_right, text="Produto não encontrado", font=("Arial", 18), bg_color=azul, text_color="white").pack()

# Botão de pesquisa
btn_pesquisar = ctk.CTkButton(master=root, text="Pesquisar", command=pesquisar_produto, width=100, height=50, fg_color=azul,corner_radius=20, bg_color=azul,text_color="white",font=("Arial Bold",18))
btn_pesquisar.place(x=1570, y=200)


# Frames

frame_top= ctk.CTkFrame(master=root, width=2000, height=100, fg_color=azul)
frame_top.place(x=0, y=0)

frame_down = ctk.CTkFrame(master=root, width=500, height=330, fg_color=azul)
frame_down.place(x=0, y=920)

frame_rightdown = ctk.CTkFrame(master=root, width=1000, height=330, fg_color=azul)
frame_rightdown.place(x=1000, y=920)

frame_right = ctk.CTkFrame(master=root, width=5000, height=400, fg_color=azul)
frame_right.place(x=500, y=400)

# Logo
logo_image = Image.open("./Logo 2.png")
logo = ImageTk.PhotoImage(logo_image.resize((192, 100)))
ctk.CTkLabel(master=frame_top, text=None, image=logo, bg_color=azul).place(x=40, y=0)

# Labels Root Principal
ctk.CTkLabel(master=frame_top, text="Suporte (11) 99999-9999", font=("Arial", 18), bg_color=azul, text_color="white").place(x=1600, y=40)
ctk.CTkLabel(root, text="Código/Descrição", font=("Arial", 18), bg_color="white", text_color="gray").place(x=199, y=170)
ctk.CTkLabel(root, text="Quantidade", font=("Arial", 22), bg_color="white", text_color="gray").place(x=199, y=370)
ctk.CTkLabel(root, text="Valor Unitário", font=("Arial", 22), bg_color="white", text_color="gray").place(x=199, y=470)
ctk.CTkLabel(root, text="Valor Total", font=("Arial", 22), bg_color="white", text_color="gray").place(x=199, y=570)
ctk.CTkLabel(root, text="Você está sendo atendido por: xxxxxxx", font=("Arial", 22), bg_color="white", text_color="gray").place(x=199, y=260)
ctk.CTkLabel(master=frame_down, text="AVISO", font=("Arial Bold", 30), bg_color=azul, text_color="white").place(x=60, y=50) 
ctk.CTkLabel(master=frame_down, text="CAIXA ABERTO", font=("Arial Bold", 30), bg_color=azul, text_color="white").place(x=200, y=50) 
ctk.CTkLabel(master=frame_rightdown, text="SUB TOTAL", font=("Arial Bold", 30), bg_color=azul, text_color="white").place(x=60, y=50) 
ctk.CTkLabel(master=frame_rightdown, text="R$", font=("Arial Bold", 50), bg_color=azul, text_color="white").place(x=400, y=40) 

# Função para fechar a janela de cadastro e restaurar a janela principal
def voltar_pagina_anterior(cadastro_window):
    cadastro_window.destroy()  # Fecha a janela de cadastro
    root.deiconify()  # Restaura a janela principal

# Criando nova janela de cadastro
def cadastro():

    root.iconify()  # Minimiza a janela principal

    cadastro_window = ctk.CTkToplevel(root, fg_color="white")
    cadastro_window.geometry("800x700")
    cadastro_window.state('zoomed')  # Maximiza a nova janela

    def salvar_mongodb():
        codigo_produto = entry_codigoproduto.get()
        nome_produto = entry_nome_produto.get()
        valor_unitario = entry_valor_unitario.get()
        quantidade = entry_quantidade.get()
        imposto = entry_imposto.get()

        if codigo_produto and nome_produto and valor_unitario and quantidade and imposto:
            produto = {
                "codigo_produto": codigo_produto,
                "nome_produto": nome_produto,
                "valor_unitario": valor_unitario,
                "quantidade": quantidade,
                "imposto": imposto
            }

            # Insere o produto na coleção do MongoDB
            collection.insert_one(produto)

            messagebox.showinfo("Sucesso", "Produto salvo no MongoDB!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos antes de salvar!")

    #Frame Cadastro de Produto

    frame_topcadastro= ctk.CTkFrame(master=cadastro_window, width=2000, height=100, fg_color=azul)
    frame_topcadastro.place(x=0, y=0)

    frame_cadastro=ctk.CTkFrame(cadastro_window,width=1400,height=700)
    frame_cadastro.place(x=250,y=230)

    # OptionMenu Categoria
    #ctk.CTkLabel(cadastro_window, text="Categoria", font=("arial bold", 14), text_color="black").pack()
    #categoria = ctk.CTkOptionMenu(master=frame_cadastro, values=["Alimentos", "Bebidas", "Higiene Pessoal", "Hortifruti", "Congelados", "Frios", "Vestuário", "Pets", "Outros..."])
    #categoria.pack(pady=20)
    #categoria.set("Escolha a categoria")

    # Entry Valor Unitário
    entry_valor_unitario = ctk.CTkEntry(master=frame_cadastro, width=200, placeholder_text="Valor Unitário")
    entry_valor_unitario.place(x=0,y=200)

    # Codigo do Produto
    entry_codigoproduto = ctk.CTkEntry(master=frame_cadastro, width=200, placeholder_text="Codigo do Produto")
    entry_codigoproduto.place(x=0,y=0)

    btn_salvar = ctk.CTkButton(master=frame_cadastro, text="Salvar", width=100, command=salvar_mongodb, height=70, fg_color=azul,corner_radius=20,text_color="white",font=("Arial Bold",18))
    btn_salvar.place(x=200, y=20)

    # Entry Nome do Produto
    entry_nome_produto = ctk.CTkEntry(master=frame_cadastro, width=200, placeholder_text="Nome do Produto")
    entry_nome_produto.place(x=0,y=400)

    # Entry Quantidade
    entry_quantidade = ctk.CTkEntry(master=frame_cadastro, width=200, placeholder_text="Quantidade")
    entry_quantidade.place(x=0,y=300)

    # Entry Imposto
    entry_imposto= ctk.CTkEntry(master=frame_cadastro, width=200, placeholder_text="Imposto")
    entry_imposto.place(x=0,y=100)

    # Botão para voltar à página anterior
    btn_voltar = ctk.CTkButton(master=frame_topcadastro, text="Voltar à página anterior", command=lambda: voltar_pagina_anterior(cadastro_window),width=100, height=70, fg_color=azul, text_color="white",font=("Arial Bold",18),corner_radius=20)
    btn_voltar.place(x=500, y=20)

   #Logo dentro do Cadastro
    logo_image = Image.open("./Logo 2.png")
    logo = ImageTk.PhotoImage(logo_image.resize((192, 100)))
    ctk.CTkLabel(frame_topcadastro, text=None, image=logo, bg_color=azul).place(x=40, y=0)

# Botão para abrir a janela de cadastro
btn_cadastro = ctk.CTkButton(master=frame_top, text="Cadastrar Produto", command=cadastro, width=100, height=70, fg_color=azul,corner_radius=20, bg_color=azul,text_color="white",font=("Arial Bold",18))
btn_cadastro.place(x=500, y=20)

btn_cancelar = ctk.CTkButton(master=frame_top, text="Cancelar Compra", width=100, height=70, fg_color=azul,corner_radius=20,text_color="white",font=("Arial Bold",18))
btn_cancelar.place(x=800, y=20)

btn_fechar = ctk.CTkButton(master=frame_top, text="Fechar Compra", command=finalizar_compra, width=100, height=70, fg_color=azul,corner_radius=20,text_color="white",font=("Arial Bold",18))
btn_fechar.place(x=1100, y=20)

root.mainloop()  # Executa o loop principal
