from matrix_banco import Database

loja = Database('Loja_Alpha&Eletronicos.db')

loja.create_table()
#============================================================================================================ 

#METODO DE INSERIR 

loja.inserir_dados_clientes( 1, 'FABRICIO PAIM', 'fabricio001devenloper@gmail.com', '10-03-2023', 'ATIVO' )
loja.inserir_dados_clientes( 2, 'ANA PAULA', 'anapaula@hotmail.com', '12-03-2023', 'ATIVO' )
loja.inserir_dados_clientes( 3, 'VINICIUS AMORIM', 'vini_001_amorim@gmail.com', '05-01-2023', 'INATIVO' )
loja.inserir_dados_clientes( 4, 'SANDRA LOUISA', 'SL_@gmail.com', '20-01-2023', 'ATIVO' )
loja.inserir_dados_clientes( 5, 'LAURA SILVA', 'LS_@gmail.com', '4-09-2023', 'INATIVO' )
loja.inserir_dados_clientes( 6, 'FERNANDA SILVA', 'fernandasilva_@hotmail.com', '11-04-2023', 'ATIVO' )
loja.inserir_dados_clientes( 7, 'MICAEL LEVI', 'micael007levi_@gmail.com', '01-01-2023', 'INATIVO' )
#============================================================================================================

#METODO DE CONSULTA  STATUS 

#for linha in loja.consultar_clientes_status('ativo'):
#    print (linha)

#METODO DE CONSULTA  NOME 

#for linha in loja.consultar_clientes_nome('FABRICIO PAIM'):
#    print (linha)

#METODO DE CONSULTA  ID_CLIENTE

#for linha in loja.consultar_clientes_id_cliente(7):
#    print (linha)

#============================================================================================================    

#METODO DE ATUALIZAR DADOS 

#loja.atualizar_dados_clientes_status('inativo', 2)
#============================================================================================================

#METODO DE DELETAR 

#loja.deletar_dados_clientes('inativo')
#============================================================================================================
