def solicitar_dados_usuario():
    print("Por favor, digite suas informações:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))  # Converte para inteiro
    email = input("E-mail: ")

    # Retorna os dados como uma tupla
    return (nome, idade, email)


# Função principal
def main():
    lista_usuarios = []  # Inicializa a lista vazia

    # Loop para adicionar dados de vários usuários
    while True:
        dados = solicitar_dados_usuario()
        lista_usuarios.append(dados)  # Adiciona os dados à lista

        continuar = input("Deseja adicionar outro usuário? (s/n): ")
        if continuar.lower() != 's':
            break  # Sai do loop se a resposta não for 's'

    # Mostra os dados armazenados
    print("\nDados armazenados:")
    for idx, usuario in enumerate(lista_usuarios, start=1):
        print(f"Usuário {idx}:")
        print(f"Nome: {usuario[0]}")
        print(f"Idade: {usuario[1]}")
        print(f"E-mail: {usuario[2]}")
        print()  # Linha em branco para separar os usuários


if __name__ == "__main__":
    main()