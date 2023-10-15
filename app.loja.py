from matrix_banco import Database

class App:
    def __init__(self):
        
        self.loja = Database('Loja_Alpha&Eletronicos.db')
        
        while True:
            print('''\n\n
            =======================================================
                            CADASTRO DE CLIENTES
            =======================================================
                        1 - Incluir cliente
                        2 - Alterar cliente 
                        3 - Excluir cliente
                        4 - Consultar cliente Nome
                        5 - Consultar cliente Status
                        6 - Consultar cliente Id
                        7 - Consultar Todos Clientes
                        8 - Encerrar aplicação
            ========================================================
            /////////////////////Sistema & Co.//////////////////////   
            ======================================================== 
            ''')
            op = int(input('Escolha uma opção ==> '))

            match op:
                case 1:
                    self.inc_cli()
                case 2:
                    self.alt_cli()
                case 3:
                    self.exc_cli()
                case 4:
                    self.con_cliente_nome()
                case 5:
                    self.con_cliente_status()
                case 6:
                    self.con_cliente_id()
                case 7 :
                    self.con_todos_do_banco()
                case 8:
                    print('[SAINDO DO SISTEMA....................]')
                    break
                case _:
                    print('[ERRO] Opção inválida!')

# AQUI A FUNÇÃO DE INCLUIR
  
    def inc_cli(self):
        print('---------------------[INCLUIR O CLIENTE]---------------------- ')
        id_cliente= int(input('Id do cliente   ? '))
        nome = input('Nome do cliente ? ').upper()
        email  = input('Email do cliente  ? ').upper()
        data_cadastro = input('Data do Cadastro do cliente ?      ')
        status = input('Digite o Status do Cliente A[Ativo]/ I[Inativo]:       ').upper()
        self.loja.inserir_dados_clientes(id_cliente, nome, email, data_cadastro, status)
        print('---------------------------------------------------------------')

# AQUI A FUNÇÃO DE ATUALIZAR 

    def alt_cli(self): 
        print('------------[ATUALIZAR O DADOS STATUS DO CLIENTE]-------------- ')
        id_cliente = int(input('Digite Id do cliente   ? '))
        print('='*60)
        print(self.loja.consultar_clientes_id_cliente(id_cliente))
        print('----------------------------------------------------------------')
        print('--------------------DADOS PARA ATUALIZAR------------------------')   
        id_cliente = int(input('Digite Id do cliente   ? '))
        nome = input('Nome do cliente ? ').upper()
        email  = input('Email do cliente  ? ').upper()
        data_cadastro = input('Data do Cadastro do cliente ?      ')
        status = input('Digite o Status do Cliente A[Ativo]/ I[Inativo]:       ').upper()
        n_id_cliente = id_cliente
        n_nome = nome
        n_email = email
        n_data_cadastro = data_cadastro
        n_status = status  
        self.loja.atualizar_dados_clientes_status(n_id_cliente,n_nome,n_email,n_data_cadastro,n_status)           
        print('============================================')        
        self.loja.consultar_todos_clientes() 
        print('============================================')


# AQUI FUNÇÃO DE DELETAR CLIENTE         
        
    def exc_cli(self):
        print('--------------------[DELETAR O CLIENTE]--------------------')
        id_cliente = int(input('Qual o Id_do_Cliente quer DELETAR ?:   '))
        print('-----------------------------------------------------------') 
        id_cliente = self.loja.deletar_cliente(id_cliente)
        print('---------------------------------------------------------- ')       
        
        
# AQUI A FUNÇÃO DE CONSULTAR CLIENTE

    def con_cliente_nome(self):
        print('--------------------[CONSULTAR O NOME CLIENTE]-----------------')
        nome = input('Nome do cliente ? ').upper()
        print('='*60)      
        for n in self.loja.consultar_clientes_nome(nome):
            print (n)
        print('='*60)
        
    def con_cliente_status(self):
        print('-----------------[CONSULTAR O STATUS CLIENTE]-------------------')
        status = input('Digite o Status do Cliente A[Ativo]/ I[Inativo]:       ').upper()
        print('='*60)
        for linha in self.loja.consultar_clientes_status(status):
           print(linha)
        print('='*60) 

    def con_cliente_id(self):
        print('-----------------[CONSULTAR O ID CLIENTE]-----------------------')
        id_cliente = int(input('Digite o ID do Cliente : '))
        print('='*60)
        for linha in self.loja.consultar_clientes_id_cliente(id_cliente):
           print(linha)
        print('='*60) 
     
    def con_todos_do_banco(self):
        print('----------------[CONSULTAR TODOS OS CLIENTES]--------------------')
        print('='*60)
        for linha in self.loja.consultar_todos_clientes():
            print(linha)
        print('='*60)
     
# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    aplicacao = App()