from entities.entity import Entity
from repository.DAO_entity import DAOEntity
from service.services import Services


class Ui:

    def __init__(self):
        self.services = Services(DAOEntity())
        self.MENU_OPTIONS = [
            (1, "Aluno", self.menu_entity_one),
        ]

    def _ler_id(self, prompt="Informe o ID do aluno: "):
        valor = input(prompt).strip()
        if not valor.isdigit():
            raise ValueError("Identificador inválido. Informe um número inteiro positivo.")
        return int(valor)

    def _ler_idade(self, prompt="Idade (inteiro): "):
        valor = input(prompt).strip()
        try:
            numero = int(valor)
        except ValueError:
            raise ValueError("Idade inválida. Informe um número inteiro.")
        if numero < 0:
            raise ValueError("A idade não pode ser negativa.")
        return numero

    def _ler_ativo(self, prompt="Aluno ativo? (S/N ou True/False): "):
        valor = input(prompt).strip().lower()
        if valor in ("s", "sim", "true", "1"):
            return True
        if valor in ("n", "nao", "não", "false", "0"):
            return False
        raise ValueError("Valor booleano inválido. Informe S/N ou True/False.")

    def _solicitar_dados_aluno(self):
        nome = input("Nome do aluno: ")
        idade = self._ler_idade()
        ativo = self._ler_ativo()
        opcoes = ", ".join(Entity.CASAS_PERMITIDAS)
        casaMagica = input(f"Casa Mágica ({opcoes}): ")
        return nome, idade, ativo, casaMagica

    def _cadastrar(self):
        nome, idade, ativo, casaMagica = self._solicitar_dados_aluno()
        aluno = self.services.create(nome, idade, ativo, casaMagica)
        print(f"Aluno cadastrado com sucesso! ID atribuído: {aluno.id}")

    def _listar(self):
        alunos = self.services.list()
        if not alunos:
            print("Nenhum registro disponível.")
            return
        print("\n--- LISTA DE ALUNOS ---")
        for aluno in alunos:
            print(aluno)

    def _consultar_por_id(self):
        aluno_id = self._ler_id()
        aluno = self.services.get(aluno_id)
        status_ativo = "Sim" if aluno.ativo else "Não"
        print("\n--- DETALHES DO ALUNO ---")
        print(f"ID: {aluno.id}")
        print(f"Nome: {aluno.nome}")
        print(f"Idade: {aluno.idade}")
        print(f"Ativo: {status_ativo}")
        print(f"Casa Mágica: {aluno.casaMagica}")

    def _atualizar(self):
        aluno_id = self._ler_id()
        self.services.get(aluno_id)
        nome, idade, ativo, casaMagica = self._solicitar_dados_aluno()
        self.services.update(aluno_id, nome, idade, ativo, casaMagica)
        print("Aluno atualizado com sucesso!")

    def _excluir(self):
        aluno_id = self._ler_id()
        aluno = self.services.get(aluno_id)
        print(f"Registro selecionado: {aluno}")
        confirmacao = input("Confirma a exclusão? (S/N): ").strip().upper()
        if confirmacao == "S":
            self.services.delete(aluno_id)
            print("Aluno excluído com sucesso!")
        else:
            print("Operação cancelada.")

    def show(self):
        while True:
            print("\n===== ESCOLA DE MAGIA =====")

            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ").strip()

            if option == "0":
                print("Encerrando...")
                break

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break

            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        while True:
            print("\n===== ESCOLA DE MAGIA =====")
            print("== Aluno ==")
            print("1 - Cadastrar Aluno")
            print("2 - Listar Alunos")
            print("3 - Procurar Aluno por ID")
            print("4 - Atualizar Aluno por ID")
            print("5 - Excluir Aluno por ID")
            print("0 - Voltar")

            option = input("Escolha uma opção: ").strip()

            try:
                if option == "0":
                    print("Voltando ao menu principal...")
                    break
                elif option == "1":
                    self._cadastrar()
                elif option == "2":
                    self._listar()
                elif option == "3":
                    self._consultar_por_id()
                elif option == "4":
                    self._atualizar()
                elif option == "5":
                    self._excluir()
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError as e:
                print(f"Aviso: {e}")
                    
                    

