from database.connection import get_db_connection


def install():
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                experiencia INTEGER NOT NULL,
                ativo INTEGER NOT NULL,
                especialidade TEXT NOT NULL
            )
        """)

        connection.execute(
            "INSERT INTO professores (nome, experiencia, ativo, especialidade) VALUES (?, ?, ?, ?)",
            ("Carlos Azevedo", 1, 0, "Introdução à magia"),
        )
        connection.execute(
            "INSERT INTO professores (nome, experiencia, ativo, especialidade) VALUES (?, ?, ?, ?)",
            ("João Silva", 5, 1, "Magia de fogo"),
        )
        connection.execute(
            "INSERT INTO professores (nome, experiencia, ativo, especialidade) VALUES (?, ?, ?, ?)",
            ("José Araújo", 10, 1, "Magia Sombria"),
        )
        connection.execute(
            "INSERT INTO professores (nome, experiencia, ativo, especialidade) VALUES (?, ?, ?, ?)",
            ("Lucas Souza", 6, 0, "Magia de defesa"),
        )
        connection.execute(
            "INSERT INTO professores (nome, experiencia, ativo, especialidade) VALUES (?, ?, ?, ?)",
            ("Hugo Almeida", 7, 1, "Varinhas"),
        )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado.")
