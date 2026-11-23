from database.connection import get_connection
from entities.entity import Entity


class DAOEntity:

    def create(self, aluno):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "INSERT INTO aluno (nome, idade, ativo, casaMagica) VALUES (?, ?, ?, ?)",
                (aluno.nome, aluno.idade, int(aluno.ativo), aluno.casaMagica),
            )
            connection.commit()
            aluno.id = cursor.lastrowid
            return aluno
        finally:
            connection.close()

    def find_all(self):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "SELECT id, nome, idade, ativo, casaMagica FROM aluno"
            )
            rows = cursor.fetchall()
            return [
                Entity(
                    nome=row[1],
                    idade=row[2],
                    ativo=bool(row[3]),
                    casaMagica=row[4],
                    id=row[0],
                )
                for row in rows
            ]
        finally:
            connection.close()

    def find_by_id(self, aluno_id):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "SELECT id, nome, idade, ativo, casaMagica FROM aluno WHERE id = ?",
                (aluno_id,),
            )
            row = cursor.fetchone()
            if row is None:
                return None
            return Entity(
                nome=row[1],
                idade=row[2],
                ativo=bool(row[3]),
                casaMagica=row[4],
                id=row[0],
            )
        finally:
            connection.close()

    def update(self, aluno):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "UPDATE aluno SET nome = ?, idade = ?, ativo = ?, casaMagica = ? WHERE id = ?",
                (
                    aluno.nome,
                    aluno.idade,
                    int(aluno.ativo),
                    aluno.casaMagica,
                    aluno.id,
                ),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()

    def delete(self, aluno_id):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "DELETE FROM aluno WHERE id = ?",
                (aluno_id,),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()