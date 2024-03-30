from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import datetime
import json

# Criar tela principal
root = ctk.CTk()
root.title("GK PDV")
root._set_appearance_mode("light")
root.geometry("1366x768")
root.state('zoomed')


#Cores
azul = "#172635"    # Hexadecimal para um tom escuro de azul
preto= "#1B1816"    # Hexadecimal para um tom escuro de preto
cinza= "#202124"    # Hexadecimal para um tom escuro de cinza
ciano= "#0DCBEF"    # Hexadecimal para um tom escuro de ciano

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
    finalizar_compra_window.geometry("1200x700")
    finalizar_compra_window.grab_set()  # Torna a janela de finalizar compra modal
    
    # Frame Cadastro de Produto
    frame_finalizar = ctk.CTkFrame(master=finalizar_compra_window, width=2000, height=100, fg_color=azul, bg_color=azul)
    frame_finalizar.place(x=0, y=0)
    
    # Labels
    ctk.CTkLabel(finalizar_compra_window, text="R$ SUB TOTAL", font=("Arial Bold", 18), bg_color="white", text_color="black").place(x=100, y=150)
    ctk.CTkLabel(finalizar_compra_window, text="R$ TOTAL A PAGAR", font=("Arial Bold", 18), bg_color="white", text_color="black").place(x=1000, y=100)
    ctk.CTkLabel(finalizar_compra_window, text="XXXX", font=("Arial Bold", 30), bg_color="white", text_color="black").place(x=1000, y=200)
    btn_dinheiro = ctk.CTkButton(master=finalizar_compra_window, text="DINHEIRO",width=250, height=70, fg_color=azul, text_color="white",font=("Arial Bold",18),corner_radius=5)
    btn_dinheiro.place(x=100, y=450)



# Código e Descrição
entry_barra_codigo = ctk.CTkEntry(root, width=1500, height=50, placeholder_text="Código/Descrição")
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

    #Frame Cadastro de Produto

    frame_topcadastro= ctk.CTkFrame(master=cadastro_window, width=2000, height=100, fg_color=azul)
    frame_topcadastro.place(x=0, y=0)

    frame_cadastro= ctk.CTkFrame(cadastro_window,width=1400,height=700)
    frame_cadastro.place(x=250,y=230)

    btn_salvar = ctk.CTkButton(master=frame_cadastro, text="Salvar",width=450,height=50, command=salvar_json, fg_color=azul,corner_radius=20,text_color="white",font=("Arial Bold",18))
    btn_salvar.place(x=475,y=550)

    # Entry Nome do Produto
    entry_nome_produto = ctk.CTkEntry(master=frame_cadastro, width=450,height=50,placeholder_text="Nome do Produto")
    entry_nome_produto.place(x=475,y=50)

    # Entry Codigo do Produto
    entry_codigoproduto = ctk.CTkEntry(master=frame_cadastro, width=450,height=50, placeholder_text="Codigo do Produto")
    entry_codigoproduto.place(x=475,y=150)

    # Entry Quantidade
    entry_quantidade = ctk.CTkEntry(master=frame_cadastro,width=450,height=50,placeholder_text="Quantidade")
    entry_quantidade.place(x=475,y=250)

    # Entry Valor Unitário
    entry_valor_unitario = ctk.CTkEntry(master=frame_cadastro,width=450,height=50,placeholder_text="Valor Unitário")
    entry_valor_unitario.place(x=475,y=350)

    # Entry Imposto
    entry_imposto= ctk.CTkEntry(master=frame_cadastro,width=450,height=50, placeholder_text="Imposto")
    entry_imposto.place(x=475,y=450)

    # Botão para voltar à página anterior
    btn_voltar = ctk.CTkButton(master=frame_topcadastro, text="Voltar à página anterior", command=lambda: voltar_pagina_anterior(cadastro_window),width=100, height=70, fg_color=azul, text_color="white",font=("Arial Bold",18),corner_radius=20)
    btn_voltar.place(x=475, y=20)

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
