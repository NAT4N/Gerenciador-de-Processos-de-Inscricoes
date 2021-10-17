usuarios = []

getData = {
  "Nome": "",
  "E-mail": ""
}

def menu():
    print("============================================\n")
    print("1- Cadastrar novos usuários\n")
    print("2- Listar usuários (ordem de cadrasto)\n")
    print("3- Listar usuário (ordem alfabética)\n")
    print("4- Verificar se o usuário está na lista\n")
    print("5- Remover usuário\n")
    print("6- Alterar o nome de um usuário\n")
    print("0- Fechar o Menu\n")
    print("============================================\n")
    choice = int(input(""))

    if(choice == 1):
        print("\n ========================= \n")
        print("Cadastrar Usuário\n")
        print("Digite o nome completo\n")
        nomeCompleto = input("").upper()
        print("Digite o E-mail\n")
        email = input("").upper()
        cadastrarUsuarios(nomeCompleto, email)
    elif(choice == 2):
        print("\n ========================= \n")
        print("Listar Usuário (ordem de cadastro)\n")
        listarUsuariosOrdemCadastro()
    elif(choice == 3):
        print("\n ========================= \n")
        print("Listar Usuário (ordem de alfabética)\n")
        listarUsuariosOrdemAlfabetica()
    elif(choice == 4):
        print("\n ========================= \n")
        print("Verificar Usuário na Lista\n")
        print("Digite o nome do usuário: \n")
        nome = input("").upper()
        verificarLista(nome)
    elif(choice == 5):
        print("\n ========================= \n")
        print("Remover usuário\n")
        print("Digite o e-mail do usuário: \n")
        email = input("").upper()
        removerUsuarios(email)
    elif(choice == 6):
        print("\n ========================= \n")
        print("Alterar o nome de um Usuário\n")
        print("Digite o e-mail do usuário:\n")
        email = input("").upper()
        alterarUsuario(email)
    elif(choice == 0):
        print("\n ========================= \n")
        print("Encerrando...\n")
    else:
        print("Escolha uma opção valida")
        continuarMenu()
        
def continuarMenu():
  print("1 - Continuar\n")
  print("2 - Encerrar\n")
  choice = int(input(""))
  if (choice == 1):
    menu()
  elif(choice == 2):
    print("Encerrando...")
    pass
  else:
    print("Opção inválida!")
    continuarMenu()
      
def cadastrarUsuarios(nomeCompleto, email):
    getData["Nome"] = nomeCompleto
    getData["E-mail"] = email
    usuarios.append([getData["Nome"], getData["E-mail"]])
    continuarMenu()
  
def listarUsuariosOrdemCadastro():
    for getUser in usuarios:
        getData["Nome"] = getUser[0]
        getData["E-mail"] = getUser[1]
        print("\n=========================")
        print("Nome: ", getData["Nome"])   
        print("E-mail: ", getData["E-mail"])
        print("=========================")    
    continuarMenu()
  
def listarUsuariosOrdemAlfabetica():
    usuarios.sort()
    for getUser in usuarios:
        getData["Nome"] = getUser[0]
        getData["E-mail"] = getUser[1]
        print("\n=========================")
        print("Nome: ", getData["Nome"])   
        print("E-mail: ", getData["E-mail"])
        print("=========================")
    usuarios.reverse()
    continuarMenu()
  
def verificarLista(nome):
    for search in usuarios:
        if search[0] == nome:
            print ("O usuário está na lista\n")
            return continuarMenu()
    print("O usuário não está na lista\n")
    continuarMenu()
    
def removerUsuarios(email):
    flag = 0
    for search in usuarios:
        if search[1] == email:
            del(usuarios[flag])
            print("Usuário removido\n")
            return listarUsuariosOrdemCadastro()
        flag += 1 

    print("E-mail não encontrado.\n")
    listarUsuariosOrdemCadastro()

def alterarUsuario(email): 
    flag = 0
    for search in usuarios:
        if search[1] == email:
            getData["Nome"] = input("Digite o novo nome: ").upper()
            getData["E-mail"] = search[1]
            usuarios[flag][0] = getData["Nome"]
            print("Usuário alterado\n")
            return listarUsuariosOrdemCadastro()
        flag += 1
    print("E-mail não encontrado.\n")
    continuarMenu()

def main():
    menu()
        
if __name__ == "__main__":
    main()
