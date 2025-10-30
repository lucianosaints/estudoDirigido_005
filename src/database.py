# database.py
import psycopg2
from psycopg2 import OperationalError, Error

class Database:
    def __init__(self, host="localhost", database="postgres", user="luciano", password="1234"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        """Estabelece conexão com o PostgreSQL."""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            print("✅ Conexão com PostgreSQL estabelecida com sucesso!")
        except OperationalError as e:
            print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
            raise

    def execute(self, query, params=None):
        """Executa comandos SQL (INSERT, UPDATE, DELETE)."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Error as e:
            print(f"❌ Erro ao executar a query: {e}")
            self.conn.rollback()
            raise

    def fetchall(self, query, params=None):
        """Executa SELECT e retorna todas as linhas."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao buscar dados: {e}")
            raise

    def fetchone(self, query, params=None):
        """Executa SELECT e retorna apenas uma linha."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Error as e:
            print(f"❌ Erro ao buscar dado: {e}")
            raise

    def close(self):
        """Fecha a conexão com o banco."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("🔒 Conexão com PostgreSQL encerrada.")


# Exemplo de uso
if __name__ == "__main__":
    db = Database()
    db.connect()

    # Teste simples: listar as tabelas existentes
    try:
        db.execute("SET search_path TO public;")
        db.cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """)
        tabelas = db.cursor.fetchall()
        print("\n📋 Tabelas encontradas:")
        for t in tabelas:
            print("-", t[0])
    except Exception as e:
        print("Erro ao listar tabelas:", e)

    db.close()
