class Garantia:
    def __init__(self, id_garantia, id_equipamento, data_inicio, data_validade):
        self.id_garantia = id_garantia
        self.id_equipamento = id_equipamento
        self.data_inicio = data_inicio
        self.data_validade = data_validade

    def __str__(self):
        return (f"Garantia(ID: {self.id_garantia}, EquipamentoID: {self.id_equipamento}, "
                f"Início: {self.data_inicio}, Validade: {self.data_validade})")
