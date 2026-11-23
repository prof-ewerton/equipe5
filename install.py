from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                ativo INTEGER NOT NULL DEFAULT 0,
                casaMagica TEXT
            )
        """)

        connection.execute(
            "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
            ("Mateus", 21, 1, "Corvinal"),
        )
        
        connection.execute(
            "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
            ("Vinícius", 19, 0, "Corvinal"),
        )

        connection.execute(
            "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
            ("Carlos", 28, 0, "Grifinória"),
        )
        
        connection.execute(
            "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
            ("Paulo", 20, 1, "Sonserina"),
        )
        
        connection.execute(
            "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
            ("Daniel", 21, 1, "Lufa-Lufa"),
        )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")


