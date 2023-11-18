import psycopg2 as psy

#class para gerenciar o banco de dados.
class CONTROLE_BANCO:
    def __init__(self):
        self.connect = psy.connect(dbname="contatos", user="postgres", password="a12955")
        self.cursor= self.connect.cursor()
        
    #função para adicionar um novo contato a tabela.
    def Adicionar_contato(self, nome, numero, email):
        
        self.cursor.execute("SELECT numeros FROM contatos")
        numeros= self.cursor.fetchall()
        numeros=[registro[0] for registro in numeros]
        
        for i in numeros:
            if i == numero:
                return 0
        
        #fasendo a criação de um novo rool de contato
        self.cursor.execute("INSERT INTO contatos (nome, numeros, email) VALUES (%s, %s, %s)", (nome, numero, email))
    
        # confirmando a tranzasão
        self.connect.commit()
        
        return 0
        
    
    
    #função para retornar uma lista dos nomes dos contatos.
    def Carrregar_contatos(self):
        self.cursor.execute("SELECT nome, numeros, email, id FROM contatos")
        
        resultados = self.cursor.fetchall()
        
        return resultados
    
    # Função para pesquisar um contato pelo nome
    def Pesquisar_contato(self, nome):
        
        self.cursor.execute("SELECT nome FROM contatos")
        nomes_contatos= self.cursor.fetchall()
        nomes_contatos=[registro[0] for registro in nomes_contatos]
        
        encontrados=[]
        for i in nomes_contatos:
            if nome in i:
                encontrados.append(i)
                
        return(encontrados)
    
    # Função para criar um novo grupo
    def  Criar_grupo(self, nome_grupo):
        self.cursor.execute("INSERT INTO grupos (nome) VALUES (%s)", (nome_grupo, ) )
        self.connect.commit()
        return True
    
    # Função para adicionar um contato a um grupo
    def Adicionar_contato_grupo(self, contato_id, grupo_id):
        
        self.cursor.execute("INSERT INTO contatos_grupos (contato_id, grupo_id) VALUES (%s, %s)", (contato_id, grupo_id))
        
        self.connect.commit()
        return True
    
    # Função para pesquisar contatos de um grupo
    def Pesquisar_contatos_grupo(self, grupo_id):
    
        self.cursor.execute("""
        SELECT contatos.nome
        FROM contatos_grupos
        JOIN contatos ON contatos_grupos.contato_id = contatos.id
        WHERE contatos_grupos.grupo_id = %s
        """, (grupo_id,))
    
        resultados_nome = [registro[0] for registro in self.cursor.fetchall()]
    
        return resultados_nome
    
    # Função para excluir um contato
    def delete_contato(self, contato_id):
        
        self.cursor.execute("DELETE FROM contatos_grupos WHERE contato_id = %s", (contato_id,))
        self.cursor.execute("DELETE FROM contatos WHERE id = %s", (contato_id,))
        self.connect.commit()
        return True
    
    # Função para modificar um contato existente
    def Modificar_contato(self, nome, numero, email , id):
        self.cursor.execute("UPDATE contatos SET nome=%s, numeros=%s, email=%s WHERE id = %s;", (nome, numero, email, id))
        self.connect.commit()
        
    # Função para carregar a lista de grupos
    def Carregar_grupos(self):
        self.cursor.execute(" SELECT nome, id FROM grupos;")
        grupos=self.cursor.fetchall()
        
        return grupos
    
    # Função para carregar contatos de um grupo específico
    def Carregar_contatos_grupo(self, grupo_id):
        self.cursor.execute("SELECT nome, id FROM contatos INNER JOIN contatos_grupos on contatos.id = contatos_grupos.contato_id where contatos_grupos.grupo_id = %s;", (grupo_id,))
        contatos_grupo=self.cursor.fetchall()
        return contatos_grupo
    
    # Função para excluir um grupo
    def Excluir_grupo(self, grupo_id):
        self.cursor.execute("DELETE FROM contatos_grupos WHERE grupo_id = %s", (grupo_id,))
        self.cursor.execute("DELETE FROM grupos WHERE id = %s", (grupo_id,))
        self.connect.commit()

    # Método chamado quando a instância da classe é destruída
    def __del__(self):
        self.cursor.close()
        self.connect.close()