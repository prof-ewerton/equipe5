from entities.entity import Entity


class Services:

    def __init__(self, repository):
        self.repository = repository

    def _validar_dados(self, nome, idade, ativo, casaMagica):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome é obrigatório e não pode conter apenas espaços em branco.")

        if isinstance(idade, bool) or not isinstance(idade, int) or idade < 0:
            raise ValueError("A idade deve ser um número inteiro maior ou igual a zero.")

        if not isinstance(ativo, bool):
            raise ValueError("O status ativo deve ser um valor booleano.")

        if casaMagica not in Entity.CASAS_PERMITIDAS:
            opcoes = ", ".join(Entity.CASAS_PERMITIDAS)
            raise ValueError(f"Casa mágica inválida. Digite exatamente uma das opções: {opcoes}.")

    def create(self, nome, idade, ativo, casaMagica):
        self._validar_dados(nome, idade, ativo, casaMagica)
        aluno = Entity(
            nome=nome.strip(),
            idade=idade,
            ativo=ativo,
            casaMagica=casaMagica,
        )
        return self.repository.create(aluno)

    def list(self):
        return self.repository.find_all()

    def get(self, aluno_id):
        aluno = self.repository.find_by_id(aluno_id)
        if aluno is None:
            raise ValueError("Aluno não encontrado.")
        return aluno

    def update(self, aluno_id, nome, idade, ativo, casaMagica):
        aluno_existente = self.repository.find_by_id(aluno_id)
        if aluno_existente is None:
            raise ValueError("Aluno não encontrado.")

        self._validar_dados(nome, idade, ativo, casaMagica)

        aluno_existente.nome = nome.strip()
        aluno_existente.idade = idade
        aluno_existente.ativo = ativo
        aluno_existente.casaMagica = casaMagica
        self.repository.update(aluno_existente)
        return aluno_existente

    def delete(self, aluno_id):
        aluno_existente = self.repository.find_by_id(aluno_id)
        if aluno_existente is None:
            raise ValueError("Aluno não encontrado.")
        return self.repository.delete(aluno_id)