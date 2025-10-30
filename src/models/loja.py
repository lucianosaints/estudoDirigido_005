class Loja:
    def __init__(self, id_loja, nome_loja, endereco):
        self.id_loja = id_loja
        self.nome_loja = nome_loja
        self.endereco = endereco

    def __str__(self):
        return f"Loja(ID: {self.id_loja}, Nome: {self.nome_loja}, Endereço: {self.endereco})"
