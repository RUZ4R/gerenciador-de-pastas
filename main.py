import os
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image

def selecionar_pasta():  
    caminho_entry.delete(0, "end") 
    # Abre o navegador de pastas e guarda o caminho
    caminho_base = filedialog.askdirectory(title="Selecione a Pasta")
    caminho_entry.insert(index=0, string=caminho_base)


def apagar_pastas_vazias():
    caixa_msg.delete("0.0", "end")
    try:
        caminho_base = caminho_entry.get()
        # Listar todas as pastas dentro do caminho base
        for nome_pasta in os.listdir(caminho_base):
            caminho_completo = os.path.join(caminho_base, nome_pasta)
            # Apaga as pastas vazias se existir
            if os.path.isdir(caminho_completo):
                with os.scandir(caminho_completo) as entries:
                    if os.path.exists(caminho_completo) and not any(entries):
                            os.rmdir(caminho_completo)
                            caixa_msg.insert("0.0", f"{nome_pasta} >>> A pasta foi deletada.\n")                         
        caixa_msg.insert("0.0", f"Permaneceram as pastas não vazias.\n\n")
    except OSError as e:
         caixa_msg.insert("0.0", f'Erro ao apagar pastas: {e}\n\n')

def criar_pastas():
    caixa_msg.delete("0.0", "end")
    try:
        numero = int(qtde_pastas.get())
        caminho_base = caminho_entry.get()
        if os.path.exists(caminho_base):
            if numero > 0:
                for i in range(numero):
                    nome_pasta = f"nova pasta ({i})"
                    caminho_completo = os.path.join(caminho_base, nome_pasta)
                    os.makedirs(caminho_completo, exist_ok=True)
                    caixa_msg.insert("0.0", f"{nome_pasta} >>> A pasta foi criada com sucesso.\n")
        else:
            messagebox.showinfo("Aviso", "Selecione o caminho da pasta!!!")
    except:
        messagebox.showinfo("Aviso", "Digite a quantidade de pastas que quer criar.\n\n")

def nome_pasta_maiusculas():
    caixa_msg.delete("0.0", "end")
    caminho_base = caminho_entry.get()
    # Listar todas as pastas dentro do caminho base
    for nome_pasta in os.listdir(caminho_base):
        caminho_completo = os.path.join(caminho_base, nome_pasta)
        
        # Verificar se é realmente uma pasta (e não um arquivo)
        if os.path.isdir(caminho_completo):
            # Criar o novo nome em maiúsculas
            novo_nome = nome_pasta.upper()
            novo_caminho = os.path.join(caminho_base, novo_nome)
            
            # Renomear se o nome for diferente
            if nome_pasta != novo_nome:
                try:
                    os.rename(caminho_completo, novo_caminho)
                    caixa_msg.insert("0.0", f"Pasta renomeada: {nome_pasta} >>> {novo_nome}\n")
                except OSError as e:
                    caixa_msg.insert("0.0", f'{nome_pasta} >>> Erro ao renomear: {e}\n\n')

def nome_pasta_minusculas():
    caixa_msg.delete("0.0", "end")
    caminho_base = caminho_entry.get()
    # Listar todas as pastas dentro do caminho base
    for nome_pasta in os.listdir(caminho_base):
        caminho_completo = os.path.join(caminho_base, nome_pasta)
        
        # Verificar se é realmente uma pasta (e não um arquivo)
        if os.path.isdir(caminho_completo):
            # Criar o novo nome em maiúsculas
            novo_nome = nome_pasta.lower()
            novo_caminho = os.path.join(caminho_base, novo_nome)
            
            # Renomear se o nome for diferente
            if nome_pasta != novo_nome:
                try:
                    os.rename(caminho_completo, novo_caminho)
                    caixa_msg.insert("0.0", f'Pasta renomeada: {nome_pasta} >>> "{novo_nome}"\n')
                except OSError as e:
                    caixa_msg.insert("0.0", f'{nome_pasta} >>> Erro ao renomear: {e}\n\n')


def renomear_pastas():
    caixa_msg.delete("0.0", "end")
    caminho_base = caminho_entry.get()
    nome_novo = novo_nome_entry.get()
    try:
        if os.path.exists(caminho_base):
            if nome_novo:
                # Listar pastas
                for i, nome_pasta in enumerate(os.listdir(caminho_base)):
                    caminho_completo = os.path.join(caminho_base, nome_pasta)

                # Renomear as pastas com nome novo
                    if os.path.isdir(caminho_completo):
                        novo_nome = nome_novo.title()
                        novo_nome = f"{str(i)}.{novo_nome}"
                        novo_caminho = os.path.join(caminho_base, novo_nome)
                        os.rename(caminho_completo, novo_caminho)
                caixa_msg.insert("0.0", "As pastas foram renomeadas com sucesso!!!")
            else:
                messagebox.showinfo("Aviso", "Digite um novo nome para as pastas!!!")
        else:
            messagebox.showinfo("Aviso", "Selecione o caminho da pasta!!!")          
    except OSError as e:
        caixa_msg.insert("0.0", f'Algun erro ocorreu:  {e}\n\n')

def ajuda():
    messagebox.showinfo("Ajuda", "Se o nome da pasta já existir, ele será sobrescrito automaticamente.")

#CONFIGURANDO A JANELA CUSTOMTKINTER
janela = ctk.CTk()
janela.geometry("700x500")
janela.resizable(False, False)
janela.title("Gerenciador de Pastas  v.0.1.0")
janela._set_appearance_mode('Dark')
janela.iconbitmap('ico.ico')

#BOTOES
buton_vazias = ctk.CTkButton(janela, text='APAGAR PASTAS VAZIAS', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=apagar_pastas_vazias, corner_radius=5).place(x=30, y=80)

buton_criar = ctk.CTkButton(janela, text='CRIAR PASTAS', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=criar_pastas, corner_radius=5).place(x=30, y=120)

buton_ajuda = ctk.CTkButton(janela, text='?', bg_color='transparent', fg_color="#FF7043", text_color="black",
                              font=('arial black', 12), width=10, height=10,
                              command=ajuda, corner_radius=5).place(x=375, y=123)

buton_maiusculas = ctk.CTkButton(janela, text='NOME DAS PASTAS EM MAIUSCULAS', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=nome_pasta_maiusculas, corner_radius=5).place(x=30, y=160)

buton_minusculas = ctk.CTkButton(janela, text='NOME DAS PASTAS EM MINUSCULAS', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=nome_pasta_minusculas, corner_radius=5).place(x=30, y=200)

buton_renomear = ctk.CTkButton(janela, text='RENOMEAR PASTAS', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=renomear_pastas, corner_radius=5).place(x=490, y=240)

buton_caminho = ctk.CTkButton(janela, text='PROCURAR', bg_color='transparent', fg_color='teal',
                              font=('arial black', 14), width=100, height=30,
                              command=selecionar_pasta, corner_radius=5).place(x=490, y=40)

# ENTRADAS
caminho_entry  = ctk.CTkEntry(janela, bg_color='transparent', width=450, height=30, corner_radius=5)
caminho_entry.place(x=30, y=40)

novo_nome_entry  = ctk.CTkEntry(janela, bg_color='transparent', width=450, height=30, corner_radius=5, placeholder_text="Digite aqui o novo nome para as pastas...")
novo_nome_entry.place(x=30, y=240)

qtde_pastas = ctk.CTkEntry(janela, bg_color='transparent', width=30, height=30, corner_radius=5)
qtde_pastas.place(x=167, y=120)

# CAIXA DE MENSAGENS
caixa_msg = ctk.CTkTextbox(janela, width=450, height=200, corner_radius=5)
caixa_msg.place(x=30, y=280) 
caixa_msg.insert("0.0", "Porque esse é meu caminho ninja!!!!!  [criado por Endrio].\n\n")

# LABELS
caminho_text = ctk.CTkLabel(janela, text='Selecione o caminho da pasta:', bg_color='transparent', text_color='#fff',
                           font=('arial black', 15)).place(x=30, y=10)

qtde_text = ctk.CTkLabel(janela, text='Digite a quantidade', bg_color='transparent', text_color='#fff',
                           font=('arial black', 15)).place(x=205, y=120)

img = ctk.CTkImage(dark_image=Image.open("./imagem.png"), size=(200,200))
img_label = ctk.CTkLabel(janela, text=None, bg_color='transparent',
                           image=img).place(x=470, y=280)


janela.mainloop()