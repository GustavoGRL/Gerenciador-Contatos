import model_contatos as model

sistema=model.CONTROLE_BANCO()


class CONTROLE_DE_DADOS:
    def __init__(self):

        self.sistema=sistema
        # Carregar os contatos do banco
        carregar_contatos = sistema.Carrregar_contatos()
        self.contatos = []

        # Colocando eles em um dicionário
        for i in carregar_contatos:
            aux = {"nome": i[0], "numero": i[1], "email": i[2], "id": i[3]}
            self.contatos.append(aux)

        carregar_grupos = sistema.Carregar_grupos()
        self.grupos = []

        for i in carregar_grupos:
            aux = {"nome": i[0], "id": i[1]}
            self.grupos.append(aux)
       
        
    #pesquisando o nome fornecido no banco.
    def Pesquisar_contato(self, busca, tipo):
        if tipo == "nome":
            encontrados=[]
            for i in self.contatos:
                if busca.lower() in i["nome"].lower():
                    encontrados.append(i)
            
            if len(encontrados) == 0:
                return False
            
            #retornando lista de contatos encontrados.
            else:
                return encontrados
        else:
            posição=self.busca_binaria(self.contatos, busca)
            if posição == -1:
                return False
            else:
                return self.contatos[posição]

    
    #função para validar a entrada e adicionar o contato
    def Adicionar_contato(self, nome, numero, email):
        #validado o numero
        try:
            numero= int(numero)
        except ValueError:
            return "Erro, numero invalido"
        
        if numero < 10000000 or numero > 99999999:
            return "Erro, numero invalido"
        
        #validando o email.
        if not "@" in email or not ".com" in email:
            return "Erro, Email invalido"
            
        
        #adicionando o contato.
        self.sistema.Adicionar_contato(nome, numero, email)
        self.__init__()
        return "Contato adicionado com sucesso!"
    
    def Modificar_contato(self, nome, numero, email, id):
        #validado o numero
        try:
            numero= int(numero)
        except ValueError:
            return "Erro, numero invalido"
        
        if numero < 10000000 or numero > 99999999:
            return "Erro, numero invalido"
        
        #validando o email.
        if not "@" in email or not ".com" in email:
            return "Erro, Email invalido"
        
        self.sistema.Modificar_contato(nome, numero, email, id)
        self.__init__()
        return True
    
    #função para fazer a busca binaria.
    def busca_binaria(self, lista, alvo):
        baixo, alto = 0, len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            valor_meio = lista[meio]["id"]

            if valor_meio == alvo:
                return meio  # Encontrou o alvo, retorna o índice.
            elif valor_meio < alvo:
                baixo = meio + 1
            else:
                alto = meio - 1

        return -1  # Se o alvo não está na lista.
    
    #função para valida entradas e adicionar um contato a um grupo.
    def Adicionando_contato_grupo(self, grupo_id, contato_id):
        #verificando se o id existe.
        validando_id= self.busca_binaria(self.grupos, grupo_id)
        if validando_id == -1:
            return False
        
        validando_id= self.busca_binaria(self.contatos, contato_id)
        
        if validando_id == -1:
            return False
        
        
        sistema.Adicionar_contato_grupo(contato_id, grupo_id)
        return True
        

    def Excluir_grupo(self, grupo_id):
        #verificando se o id do grupo existe.
        validando_id=self.busca_binaria(self.grupos, grupo_id)
        if validando_id == -1:
            return False
        
        sistema.Excluir_grupo(grupo_id)
        self.__init__()
        return True
    
    def Ver_contatos_grupo(self, grupo_id):
        #verificando se o id é valido
        try:
            grupo_id=int(grupo_id)
        except ValueError:
            return False, None
        
        #verificandos se o existe o grupo com este id.
        validando_id=self.busca_binaria(self.grupos, grupo_id)
        
        
        if validando_id == -1:
            return False, None
            
        return sistema.Carregar_contatos_grupo(grupo_id), self.grupos[validando_id]["nome"]
    

        