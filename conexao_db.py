import psycopg

from dotenv import load_dotenv
import os

load_dotenv()

def conectar_banco(): 
    try:
        conectar = psycopg.connect (

            password = os.getenv('DB_PASSWORD'),
            host = os.getenv('DB_HOST'),
            dbname = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'), 
        )
        return conectar

    except Exception:
        print('ERRO:Sistema fora do ar')

        return None

#Recebe os dados da conexão
conectado = conectar_banco()

def encerrar_conectar_banco(conexao):
    if conexao:
        conexao.close()


    
