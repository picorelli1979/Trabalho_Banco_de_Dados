import sqlite3

class Database():
    def __init__(self, nome_db) -> None:
        self.nome_db = nome_db
        self.conn = None
        self.cursor = None 
        
    def conecta_db(self):
        self.conn = sqlite3.connect(self.nome_db)
        
        self.cursor = self.conn.cursor()        
    
    def desconecta_db(self):
        self.conn.close()
        return (f'DESCONECTADO')     
    
    
    def create_table(self):
        self.conecta_db()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                               id_cliente INTEGER PRIMARY KEY,
                               nome VARCHAR (50), 
                               email VARCHAR (50),
                               data_cadastro INTEGER,
                               status VARCHAR (50)
                              )''')
        
        self.conn.commit()
        self.desconecta_db()
        return(f'BANCO CRIADO COM SUCESSO !!!!')
    
    
# INSERIR DADOS CLIENTE     
    def inserir_dados_clientes(self,id_cliente, nome, email, data_cadastro, status):
        self.conecta_db()
        self.cursor.execute('''INSERT INTO clientes(id_cliente, nome, email, data_cadastro, status) VALUES(?,?,?,?,?);''',
                           (id_cliente, nome, email, data_cadastro,status))
        self.conn.commit()
        self.desconecta_db()
#--------------------------------------------------------------------------        


# CONSULTAR DADOS DO CLIENTE
    def consultar_clientes_nome(self,nome):
        self.conecta_db()
        return self.cursor.execute('''SELECT * FROM clientes WHERE nome = ?;''',(nome,)).fetchall()    
        
    def consultar_clientes_status(self,status):
        self.conecta_db()
        return self.cursor.execute('''SELECT nome , email FROM clientes WHERE status = ?;''',(status,)).fetchall()
    
    def consultar_clientes_id_cliente(self,id_cliente):
        self.conecta_db()
        return self.cursor.execute('''SELECT * FROM clientes WHERE id_cliente = ?;''',(id_cliente,)).fetchall()
    
    def consultar_todos_clientes(self):    
        self.conecta_db()
        return self.cursor.execute('''SELECT * FROM clientes ''').fetchall()
#---------------------------------------------------------------------------    
    
    
# ATUALIZAR DADOS DO CLIENTE 
    
    def atualizar_dados_clientes(self, n_id_cliente, n_nome, n_email, n_data_cadastro, n_status):
        self.conecta_db()
        self.cursor.execute('''UPDATE clientes SET id_cliente = ?,nome =?, email = ?, data_cadastro = ?, status=? WHERE id_cliente =?''',(n_id_cliente, n_nome,n_email,n_data_cadastro,n_status,))
        self.conn.commit()
        self.desconecta_db()
        
         
    def atualizar_dados_clientes_status(self,status, id_cliente):
        self.conecta_db()
        self.cursor.execute('''UPDATE clientes SET status = ? where id_cliente = ?''',(status, id_cliente,))
        self.conn.commit()
        self.desconecta_db()
#------------------------------------------------------------------------------

# DELETAR DADOS DO CLIENTE 
        
    def deletar_cliente(self, id_cliente):        
        self.conecta_db()
        self.cursor.execute('''DELETE FROM clientes WHERE id_cliente = ?;''',(id_cliente,))
        
        print('DELETADO COM SUCESSO !!!!!!')
        self.conn.commit()
        self.desconecta_db()
        return (f'DELETADO COM SEUCESSO....')