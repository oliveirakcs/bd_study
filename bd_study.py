import psycopg2
import pandas as pd

# Parâmetros de conexão

param = {
    "host": "127.0.0.1",
    "database": "TestDB",
    "user": "postgres",
    "password": "admin"
}


def connect(param):
    '''Realiza a conexão no Postgre'''
    conn = None
    try:
        print('Conectando no servidor...')
        conn = psycopg2.connect(**param)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)

    print('Conectado com sucesso!')

    return conn


def pg_to_df(conn, query, column_names):
    '''Converte o SELECT em um DF Pandas'''
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    tupples = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(tupples, columns=column_names)
    return df


def get_data(conn, query):
    '''Retorna todos os dados no formato de Tuplas'''
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    tupples = cursor.fetchall()
    cursor.close()

    return tupples


def insert_data(conn, query):
    '''Insere '''
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    conn.commit()
    cursor.close()


conn = connect(param)

conn.autocommit = True

query1 = '''SELECT * FROM vendas'''

query2 = '''INSERT INTO vendas (id, data, funcionario, vendas, dia_semana) VALUES (5,'24/08/2021', 'Carlos', 10, 'Quinta' )'''

result = get_data(conn, query1)

print(result)

insert_data(conn, query2)

result = get_data(conn, query1)

print(result)

query3 = ''' SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'vendas' '''

result = get_data(conn, query3)

print(result)
