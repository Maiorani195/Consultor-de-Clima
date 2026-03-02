from clima_api import buscar_clima, mostrar_clima

def main(): #Função principal do programa o que vai aparecer para o usuário
    print("Bem-vindo ao consultor de clima!\n")

    while True:
        print("[1] Consultar clima")
        print("[2] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cidade = input("Digite o nome da cidade: ")
            data = buscar_clima(cidade)
            if data:
                mostrar_clima(data)
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()