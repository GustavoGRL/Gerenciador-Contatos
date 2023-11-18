#view_contatos
import Controle_contatos as control

sistema = control.CONTROLE_DE_DADOS()

class GerenciadorContatosCLI:
    # Método para exibir o menu principal
    def exibir_menu_principal(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Pesquisar contato")
            print("2. Ver todos os contatos")
            print("3. Adicionar Contatos")
            print("4. Modificar Contato")
            print("5. Ver Grupos")
            print("6. Sair")
            opcao = input("Escolha uma opção (1/2/3/4/5/6): ")

            if opcao == "1":
                self.Pesquisar_contato()
            elif opcao == "2":
                self.ver_contatos()
            elif opcao == "3":
                self.adicionar_contatos()
            elif opcao == "4":
                self.modificar_contato()
            elif opcao == "5":
                self.ver_grupos()
            elif opcao == "6":
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    # Método para pesquisar um contato pelo nome
    def Pesquisar_contato(self):
        print("Caso deseje sair, digite o número 11.")
        nome = input("Digite o nome e sobrenome do contato: ")
        
        encontrados= sistema.Pesquisar_contato(nome, "nome")
        
        if encontrados == False:
            print("\n==Nenhum contato encontrado==")
        else:
            print("== Contatos encontrados ==")
            for i in encontrados:
                print(f"\n{i['nome']} / {i['numero']} / {i['id']}")
    
    # Método para visualizar todos os contatos
    def ver_contatos(self):
        print("\n=== Lista de Contatos ===")
        
        contatos= sistema.contatos
        for contato in contatos:
            print(f"{contato['nome']} - {contato['numero']} - {contato['id']}")
    
    # Método para adicionar novos contatos
    def adicionar_contatos(self):
        nome = input("Digite o nome do novo contato: ")
        numero = input("Digite o número do novo contato: ")
        email = input("Digite o email do novo contato: ")

        adicionando=sistema.Adicionar_contato(nome, numero, email)
        print(adicionando)

    # Método para modificar um contato existente
    def modificar_contato(self):
        id_contato = int(input("Digite o ID do contato que deseja modificar: "))

        encontrado=sistema.Pesquisar_contato(id_contato, "id")
        
        if encontrado == False:
            print("Contato não encontrado.")
            return 0


        print(f"\nModificando o Contato: {encontrado['nome']} - {encontrado['numero']} - {encontrado['id']}")
        deletar = input("Deseja deletar o contato? (Sim/Não).")

        if deletar.upper() == "SIM":
            sistema.sistema.delete_contato(encontrado["id"])
            print(f"O contato {encontrado['nome']} foi deletado com sucesso!!!")
            return 0
        
        novo_nome = input("Novo nome (pressione Enter para manter o mesmo): ")
        novo_numero = input("Novo número (pressione Enter para manter o mesmo): ")
        novo_email = input("Novo email (pressione Enter para manter o mesmo): ")
        
        if novo_nome:
            encontrado["nome"] = novo_nome
        if novo_numero:
            encontrado["numero"] = novo_numero
        if novo_email:
            encontrado["email"] = novo_email

        confirmacao = input("Deseja realmente salvar as alterações? (S para Sim, qualquer outra coisa para não): ")

        if confirmacao.upper() == "S":
            print(encontrado["nome"], encontrado["numero"], encontrado["email"])
            modficando=sistema.Modificar_contato(encontrado["nome"], encontrado["numero"], encontrado["email"], encontrado["id"])
            if modficando == True:
                print("Contato modificado com sucesso!")
                return 0
            else:
                print(modficando)
        else:
            print("Modificação cancelada.")
            return 0

    # Método para visualizar grupos e realizar ações relacionadas
    def ver_grupos(self):
        print("\n=== Lista de Grupos ===")
        grupos=sistema.grupos
        for grupo in grupos:
            print(f"{grupo['nome']} - {grupo['id']}")

        opcao = input("Deseja:\n (A)dicionar pessoa a um grupo\n (E)xcluir grupo\n (V)er os contatos de um grupo\n (C)riar um grupo\n (A/E/V/C/N): ")
        if opcao.upper() == "A":
            self.adicionar_pessoa_a_grupo()
        elif opcao.upper() == "E":
            self.excluir_grupo()
        elif opcao.upper() == "V":
            self.ver_contatos_grupo()
        elif opcao.upper() == "C":
            self.Criar_grupo()

    # Método para adicionar uma pessoa a um grupo
    def adicionar_pessoa_a_grupo(self):
        id_contato = int(input("Digite o ID do contato que deseja adicionar ao grupo: "))
        id_grupo = int(input("Digite o ID do grupo: "))
        
        adicionando=sistema.Adicionando_contato_grupo(id_grupo, id_contato)
        
        if adicionando == True:
            print("Contato adicionado ao grupo com sucesso!")
        else:
            print("Erro, id do grupo ou id do contato, está ERRADO")
            
    # Método para excluir um grupo
    def excluir_grupo(self):
        id_grupo = int(input("Digite o ID do grupo que deseja excluir: "))
        
        excluindo=sistema.Excluir_grupo(id_grupo)

        if excluindo == False:
            print("\nErro, id do crupo não foi encontrado.")
        else:
            print("Grupo excluído com sucesso!")
    
    # Método para visualizar contatos de um grupo
    def ver_contatos_grupo(self):
        grupo_id=input("Digite o id do grupo: ")
        contatos_grupo, nome_grupo= sistema.Ver_contatos_grupo(grupo_id)
        
        if contatos_grupo == False:
            print("Erro, grupo não encontrado.")
        
        else:
            print(f"=={nome_grupo}==")
            if len(contatos_grupo) == 0:
                print("Nenhum contato foi adicionado no grupo.")
            else:
                for i in contatos_grupo:
                    print(f"{i[0]} - {i[1]}")
    
    # Método para criar um novo grupo
    def Criar_grupo(self):
        nome_grupo=input("Digite o nome do novo grupo: ")
        sistema.sistema.Criar_grupo(nome_grupo)
        print(f"\no grupo {nome_grupo} foi criado com sucesso!!!")

if __name__ == "__main__":
    gerenciador_cli = GerenciadorContatosCLI()
    gerenciador_cli.exibir_menu_principal()