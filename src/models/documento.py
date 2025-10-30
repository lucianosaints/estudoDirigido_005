class Documento:
    def __init__(self, id_doc, numero_nota):
        self.id_doc = id_doc
        self.numero_nota = numero_nota

    def __str__(self):
        return f"Documento(ID: {self.id_doc}, Número da Nota: {self.numero_nota})"
