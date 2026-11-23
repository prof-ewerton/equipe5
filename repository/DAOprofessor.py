from database.connection import get_connection
from entities.professor import Professor


class DAOProfessor:

    def create(self, professor):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "INSERT INTO professor (nome, especialidade, experiencia, ativo) VALUES (?, ?, ?, ?)",
                (professor.nome, professor.especialidade, int(professor.experiencia), bool(professor.ativo),
            )
            )
            connection.commit()
            professor.id = cursor.lastrowid
            return professor
        finally:
            connection.close()

    def find_all(self):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "SELECT id, nome, especialidade, experiencia, ativo FROM professor"
            )
            rows = cursor.fetchall()
            return [
                Entity(
                    nome=row[1],
                    especialidade=row[2],
                    experiencia=bool(row[3]),
                    ativo=row[4],
                    id=row[0],
                )
                for row in rows
            ]
        finally:
            connection.close()

    def find_by_id(self, professor_id):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "SELECT id, nome, especialidade, experiencia, ativo FROM professor WHERE id = ?",
                (professor_id,),
            )
            row = cursor.fetchone()
            if row is None:
                return None
            return Professor(
                nome=row[1],
                especialidade=row[2],
                experiencia=bool(row[3]),
                ativo=row[4],
                id=row[0],
            )
        finally:
            connection.close()

    def update(self, professor):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "UPDATE professor SET nome = ?, especialidade = ?, experiencia = ?, ativo = ? WHERE id = ?",
                (
                    professor.nome,
                    professor.especialidade,
                    int(professor.experiencia),
                    professor.ativo,
                    professor.id,
                ),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()

    def delete(self, professor_id):
        connection = get_connection()
        try:
            cursor = connection.execute(
                "DELETE FROM professor WHERE id = ?",
                (professor_id,),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()
