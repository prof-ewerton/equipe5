class Professor:
    def __init__(self, nome, experiencia, ativo=True, id=None):
        self.id = id
        self.nome = nome
        self.experiencia = experiencia
        self.ativo = bool(ativo)
        self.especialidade = especialidade

    def __str__(self):
        situacao = "Ativo" if self.ativo else "Inativo"
        especialidade_exibicao = self.especialidade if self.especialidade else "Não informado"
        return f"ID: {self.id} | Nome: {self.titulo} | Experiência: {self.experiencia} | Especialidade: {especialidade_exibicao} | Situação: {situacao}"
