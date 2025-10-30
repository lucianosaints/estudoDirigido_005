class Usuario:
    def __init__(self, id_usuario, cpf_usuario):
        self.id_usuario = id_usuario
        self.cpf_usuario = cpf_usuario

    def __str__(self):
        return f"Usuário(ID: {self.id_usuario}, CPF: {self.cpf_usuario})"
