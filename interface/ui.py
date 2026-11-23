class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Professor", self.menu_entity_one),
        ]

    def show(self):
        while True:
            print("\n===== ESCOLA DE MAGIA =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break
            elif option == "1":
                self.menu_entity_one()

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== ESCOLA DE MAGIA =====")
        print("= Professor ==")
        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Procurar Professor por ID")
        print("4 - Atualizar Professor por ID")
        print("5 - Excluir Professor por ID")
        print("0 - Voltar")
        
        option = input("Escolha uma opção: ").strip()
        
        if option == "0":
                self.show()
        elif option == "1":
                self.menu_entity_one()
