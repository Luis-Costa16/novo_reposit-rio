import pymysql as pms
import matplotlib.pyplot as plt

conexao = pms.connect(
    host='localhost',
    user='root',
    password='',
    db='Loja',
)

cursor = conexao.cursor() #Iniciando a conexão com o banco

cursor.execute("SELECT * FROM produtos") #Executando a query para pegar todos os produtos
produtos = cursor.fetchall() #Guarda todos os resultados organizados

nomes = [coluna[1] for coluna in produtos] #Uma lista que percorre os nomes de produtos da loja
quantidade = [coluna[2] for coluna in produtos] #Uma lista que percorre a quantidades de produtos da loja


plt.bar(nomes,quantidade)
plt.xlabel('Produtos')
plt.ylabel('Quantidade')
plt.title('Relação de quantidade de produtos')
plt.show() #Mostra o gráfico