from entities.professor import Professor


class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome):
        if not nome or not nome.strip():
            raise ValueError("O nome é obrigatório e não pode ser vazio.")

        especialidade_limpo = especialidade.strip() if especialidade else ""
        professor = Professor(nome=nome.strip(), experiencia=experiencia.strip(), especialidade=especialidade_limpo, ativo=True)

        return self.repository.create(professor)

    def list(self):
        return self.repository.find_all()

    def get(self, professor_id):
        professor = self.repository.find_by_id(professor_id)
        if professor is None:
            raise ValueError("Professor não encontrado.")
        return professor

    def update(self, professor_id, nome, especialidade=""):
        professor_existe = self.repository.find_by_id(professor_id)
        if professor_existe is None:
            raise ValueError("Professor não encontrado.")

        if not nome or not nome.strip():
            raise ValueError("O nome é obrigatório e não pode ser vazio.")

        professor_existe.nome = nome.strip()
        professor_existe.especialidade = especialidade.strip() if especialidade else ""
        self.repository.update(professor_existe)
        return professor_existe

    def delete(self, professor_id):
        professor_existe = self.repository.find_by_id(professor_id)
        if professor_existe is None:
            raise ValueError("Professor não encontrado.")
        return self.repository.delete(professor_id)

    def ativar(self, professor_id):
        professor_existe = self.repository.find_by_id(professor_id)
        if professor_existe is None:
            raise ValueError("Professor não encontrado.")
        self.repository.update_status(professor_id, True)
        professor_existe.ativo = True
        return professor_existe

    def desativar(self, professor_id):
        professor_existe = self.repository.find_by_id(professor_id)
        if professor_existe is None:
            raise ValueError("Professor não encontrado.")
        self.repository.update_status(professor_id, False)
        professor_existe.ativo = False
        return professor_existe