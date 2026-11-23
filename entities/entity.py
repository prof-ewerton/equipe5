class Entity:
    CASAS = ("Corvinal", "Grifinória", "Sonserina", "Lufa-Lufa")

    def __init__(self, nome, idade, ativo, casaMagica, id=None):
        self.id = id
        self.nome = nome
        self.idade = int(idade)
        self.ativo = bool(ativo)
        self.casaMagica = casaMagica
        
    def __str__(self):
        status_ativo = "Sim" if self.ativo else "Não"
        return (
            f"ID: {self.id} | Nome: {self.nome} | Idade: {self.idade} | "
            f"Ativo: {status_ativo} | Casa Mágica: {self.casaMagica}"
        )