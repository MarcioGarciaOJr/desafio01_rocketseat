def salvar_novo_contato(contatos, nome, telefone, email):
    if nome != "" and telefone != "" and email != "":
        #Nome, telefone, email, favorito
        novo_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        contatos.append(novo_contato)
        print(f"Contato {nome} salvo com sucesso!")
    else:
        print("Não foi possível salvar contato! (Falta de informação)")
    return

def consultar_contatos(contatos):
    print("\nAgenda - contatos:")    
    for indice, contato in enumerate(contatos, start=1):
        fav = "⭐" if contato["favorito"] else " "
        print(f"{indice}. {fav} Nome: {contato["nome"]} - Telefone: {contato["telefone"]} - Email: {contato["email"]}")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print("Alterações salvas com sucesso!")
    else:
        print("Contato informado não existe!")
    return

def favoritar_desfavoritar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(contatos):
        if contatos[indice_ajustado]["favorito"]:
            contatos[indice_ajustado]["favorito"] = False
            print("Contato removido dos favoritos!")
        else:
            contatos[indice_ajustado]["favorito"] = True
            print("Contato adicionado aos favoritos!")
    else:
        print("Contato informado não existe!")

def consultar_contatos_favoritos(contatos):
    print("\nAgenda - contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. ⭐ Nome: {contato["nome"]} - Telefone: {contato["telefone"]} - Email: {contato["email"]}")
    return

def deletar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1    
    print("\nTem certeza que deseja deletar o contato %s? " % contatos[indice_ajustado]["nome"])
    print("1. SIM")
    print("2. NÃO")
    confirmacao = input()
    if confirmacao == "1":
        if 0 <= indice_ajustado <= len(contatos):
            contatos.remove(contatos[indice_ajustado])
            print("Contato removido!")
        else:
            print("Contato informado não existe!")
    else:
        print("Operação cancelada!")
    return

contatos = []

while True:
    print("\nAgenda:")

    print("1. Salvar novo contato")
    print("2. Consultar contatos")
    print("3. Editar contato")    
    print("4. Favoritar/Desfavoritar contato")
    print("5. Consultar contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair do programa")

    escolha = input("\nDigite a opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o telefone do novo contato: ")
        email = input("Digite o email do novo contato: ")
        salvar_novo_contato(contatos, nome, telefone, email)
    
    elif escolha == "2":
        consultar_contatos(contatos)
    
    elif escolha == "3":
        consultar_contatos(contatos)
        indice = input("\nDigite o número do contato que deseja alterar: ")
        novo_nome = input("Digite o novo nome: ") 
        novo_telefone = input("Digite o novo telefone: ")  
        novo_email = input("Digite o novo email: ")
        editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)  

    elif escolha == "4":
        consultar_contatos(contatos)
        indice = input("\nDigite o número do contato que deseja favoritar/desfavoritar: ")
        favoritar_desfavoritar_contato(contatos, indice)
    
    elif escolha == "5":
        consultar_contatos_favoritos(contatos)

    elif escolha == "6":
        consultar_contatos(contatos)
        indice = input("\nDigite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice)
    
    elif escolha == "7":
        print("\nOperação finalizada")
        break