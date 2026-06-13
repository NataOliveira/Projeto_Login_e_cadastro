import sys
import customtkinter as ctk
import bcrypt
from tkinter import messagebox
from PIL import Image
from datetime import datetime

# Adiciona a pasta ao caminho do banco de dadosd
sys.path.append(r"C:\Users\natan\OneDrive\Documentos\MyDB")

# Importa as funções da conexão
from conexao_db import conectar_banco, encerrar_conectar_banco

app = None
usuario = None
senha = None
label_resultado = None
conexao = None

def menulogin():
    
    global usuario, senha, label_resultado, lbl_image

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("350x450")

    imagem_pil = Image.open(r"C:\Users\natan\OneDrive\Documentos\GitHub\Projeto_Login_e_cadastro\2.png")
    labelimg = ctk.CTkImage(light_image=imagem_pil, size=(150,150))
    lbl_image = ctk.CTkLabel(master=app, image=labelimg,text='')
    lbl_image.pack(pady=(20,0))

    label_usuario = ctk.CTkLabel(app,text="Usuário: ", font=('Arial', 16))
    label_usuario.pack(pady=(10,0))
    usuario = ctk.CTkEntry(app,placeholder_text='Usuário')
    usuario.pack(pady=(0,0))

    label_senha = ctk.CTkLabel(app, text="Senha: ", font=('Arial', 16))
    label_senha.pack(pady=(0,0))
    senha = ctk.CTkEntry(app,placeholder_text='password', show ="*")
    senha.pack(pady=(0,0))

    botao_entrar = ctk.CTkButton(app, text="Entrar",command=(login))
    botao_entrar.pack(pady=20)

    botao_cadastro = ctk.CTkButton(app, text="Cadastrar-se",command=(cadastro))
    botao_cadastro.pack(pady=0)

    label_resultado = ctk.CTkLabel(app,text='',font=('Arial', 16,"bold"))
    label_resultado.pack(pady=20)

def login():
#recebe o input do usuário
    usuario_entry = usuario.get().strip()
    senha_input = senha.get().strip()
    conexao = None
    cliente = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        #faz um select where no banco de dados usando o input inserido pelo usuário
        cursor.execute('SELECT * FROM clientes WHERE usuario = %s', (usuario_entry,))
        cliente = cursor.fetchone()

        #validação da senha
        if cliente and bcrypt.checkpw(senha_input.encode('utf-8'),cliente[3].encode('utf-8')):
         label_resultado.configure(text='Logado com Sucesso',text_color='green')
            
        else:
            label_resultado.configure(text='Usuário ou Senha inválios',text_color='red')

    except Exception as erro:
        label_resultado.configure(text='Sistema offline', text_color='red')
        print(erro)
        return

    finally:
        if cursor:
            cursor.close()
            encerrar_conectar_banco(conexao)
               
def cadastro():

    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("600x750")

    imagem_pil = Image.open(r"C:\Users\natan\OneDrive\Documentos\GitHub\Projeto_Login_e_cadastro\2.png")
    labelimg = ctk.CTkImage(light_image=imagem_pil, size=(150,150))
    lbl_image = ctk.CTkLabel(master=app, image=labelimg,text='')
    lbl_image.pack(pady=(20,0))
    
    frame_grid = ctk.CTkFrame(app, fg_color='transparent')
    frame_grid.pack(pady=20)

    # Linha 1 - Usuário
    entry_label_usuario = ctk.CTkLabel(frame_grid, text="Usuário: ", font=('Arial', 16))
    entry_label_usuario.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_usuario = ctk.CTkEntry(frame_grid, placeholder_text='Usuario', width=300)
    entry_usuario.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Linha 2 - Nome
    entry_label_nome = ctk.CTkLabel(frame_grid, text="Nome completo: ", font=('Arial', 16))
    entry_label_nome.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_grid, placeholder_text='Nome', width=300)
    entry_nome.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Linha 3 - Senha
    entry_label_senha = ctk.CTkLabel(frame_grid, text="Senha: ", font=('Arial', 16))
    entry_label_senha.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entry_senha = ctk.CTkEntry(frame_grid, placeholder_text='******', show="*", width=300)
    entry_senha.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
    # Linha 4 - CPF
    entry_label_cpf = ctk.CTkLabel(frame_grid, text="CPF: ", font=('Arial', 16))
    entry_label_cpf.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    entry_cpf = ctk.CTkEntry(frame_grid, placeholder_text='000.000.000-00', width=300)
    entry_cpf.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Linha 5 - Email
    entry_label_email = ctk.CTkLabel(frame_grid, text="Email: ", font=('Arial', 16))
    entry_label_email.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    entry_email = ctk.CTkEntry(frame_grid, placeholder_text='Email', width=300)
    entry_email.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # Linha 6 - Data de Nascimento
    entry_label_data_de_nascimento = ctk.CTkLabel(frame_grid, text="Data de Nascimento: ", font=('Arial', 16))
    entry_label_data_de_nascimento.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    data_bruta = ctk.CTkEntry(frame_grid, placeholder_text='DD/MM/AAAA', width=300)
    data_bruta.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    # Linha 7 - Logradouro
    entry_label_logradouro = ctk.CTkLabel(frame_grid, text="Logradouro: ", font=('Arial', 16))
    entry_label_logradouro.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    entry_logradouro = ctk.CTkEntry(frame_grid, placeholder_text='Rua, Av., Estr.', width=300)
    entry_logradouro.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    # Linha 8 - Número
    entry_label_numero_casa = ctk.CTkLabel(frame_grid, text="Número: ", font=('Arial', 16))
    entry_label_numero_casa.grid(row=8, column=0, padx=5, pady=5, sticky="w")
    entry_numero_casa = ctk.CTkEntry(frame_grid, placeholder_text='Nº', width=300)
    entry_numero_casa.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    # Linha 9 - Bairro
    entry_label_bairro = ctk.CTkLabel(frame_grid, text="Bairro: ", font=('Arial', 16))
    entry_label_bairro.grid(row=9, column=0, padx=5, pady=5, sticky="w")
    entry_bairro = ctk.CTkEntry(frame_grid, placeholder_text='Bairro', width=300)
    entry_bairro.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    # Linha 10 - Cidade
    entry_label_cidade = ctk.CTkLabel(frame_grid, text="Cidade: ", font=('Arial', 16))
    entry_label_cidade.grid(row=10, column=0, padx=5, pady=5, sticky="w")
    entry_cidade = ctk.CTkEntry(frame_grid, placeholder_text='Cidade', width=300)
    entry_cidade.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    # Linha 11 - Estado
    entry_label_estado = ctk.CTkLabel(frame_grid, text="Estado: ", font=('Arial', 16))
    entry_label_estado.grid(row=11, column=0, padx=5, pady=5, sticky="w")
    entry_estado = ctk.CTkEntry(frame_grid, placeholder_text='UF', width=50)
    entry_estado.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # Linha 12 - CEP
    entry_label_cep = ctk.CTkLabel(frame_grid, text="CEP: ", font=('Arial', 16))
    entry_label_cep.grid(row=12, column=0, padx=5, pady=5, sticky="w")
    entry_cep = ctk.CTkEntry(frame_grid, placeholder_text='00000-000', width=300)
    entry_cep.grid(row=12, column=1, padx=5, pady=5, sticky="w")

    # Linha 13 - Telefone
    entry_label_telefone = ctk.CTkLabel(frame_grid, text="Telefone: ", font=('Arial', 16))
    entry_label_telefone.grid(row=13, column=0, padx=5, pady=5, sticky="w")
    entry_telefone = ctk.CTkEntry(frame_grid, placeholder_text='+55 (0) 00000-0000', width=300)
    entry_telefone.grid(row=13, column=1, padx=5, pady=5, sticky="w")

    def commit():

        usuario_get = entry_usuario.get().strip()
        nome_get = entry_nome.get().strip()
        senha_digitada = entry_senha.get().strip()
        cpf_get = entry_cpf.get().strip()
        email_get = entry_email.get().strip()
        data_get = data_bruta.get().strip()
        logradouro_get = entry_logradouro.get().strip()
        numero_get = entry_numero_casa.get().strip()
        bairro_get = entry_bairro.get().strip()
        cidade_get = entry_cidade.get().strip()
        estado_get = entry_estado.get().strip()
        cep_get = entry_cep.get().strip()
        telefone_get = entry_telefone.get().strip()     
        
        if usuario_get == '' or nome_get == '' or senha_digitada == ''or data_get == '' or cpf_get == '' or email_get == '' or logradouro_get == '' or numero_get == '' or bairro_get == ''or cidade_get == '' or estado_get == '' or cep_get == '' or telefone_get == '':
            messagebox.showwarning("Campos Obrigatórios","Todos os campos devem ser preenchidos !") 
            return
        
        senha_get = bcrypt.hashpw(senha_digitada.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 
 
        data_limpa = data_bruta.get().strip().replace('/','').replace('-','').replace('_','').replace('.','')
        try:
            data_nascimento_get = datetime.strptime(data_limpa,'%d%m%Y').date()
                
        except ValueError:
            messagebox.showerror('Data Inválida','Formato de data incorreto! Digite uma data válida (DD/MM/AAA)')
            return
     
        Q_sql_insert_tudo = "INSERT INTO clientes (usuario,nome,senha,cpf,email,data_nascimento,logradouro,numero,bairro,cidade,estado,cep,telefone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (usuario_get, nome_get, senha_get, cpf_get, email_get, data_nascimento_get,logradouro_get, numero_get, bairro_get, cidade_get, estado_get, cep_get, telefone_get)
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        try:
            cursor.execute(Q_sql_insert_tudo, valores)
            conexao.commit()
            messagebox.showinfo('Cadastro concluido','Usuário Cadastrado com sucesso!')
            menulogin()
            
        except Exception as erro:
            print(f'Erro: {erro}')

        finally:
            cursor.close()
            encerrar_conectar_banco(conexao)

    #Botão Submite
    
    botao_voltar_commit = ctk.CTkButton(frame_grid, text="Voltar", command=menulogin)
    botao_voltar_commit.grid(row=15, column=0, padx=5, pady=15, sticky="w")
    
    botao_cadastro_commit = ctk.CTkButton(frame_grid, text="Cadastrar-se", command=commit)
    botao_cadastro_commit.grid(row=15, column=1, padx=5, pady=15, sticky="e")

 #Definindo App
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.iconbitmap(r"C:\Users\natan\OneDrive\Documentos\GitHub\Exercicios\projeto ctk\logo.ico")
app.title('Dreyfus Bank')

menulogin()
app.mainloop()
