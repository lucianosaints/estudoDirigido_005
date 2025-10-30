class Equipamento:
    def __init__(self, id_equipamento, nome_equipamento, preco, id_loja):
        self.id_equipamento = id_equipamento
        self.nome_equipamento = nome_equipamento
        self.preco = preco
        self.id_loja = id_loja

    def __str__(self):
        return f"Equipamento(ID: {self.id_equipamento}, Nome: {self.nome_equipamento}, Preço: R${self.preco:.2f}, LojaID: {self.id_loja})"
