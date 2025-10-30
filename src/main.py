
from models.loja import Loja
from models.equipamento import Equipamento
from models.garantia import Garantia
from models.documento import Documento
from models.usuario import Usuario

def main():
    print("=== SISTEMA DE GARANTIAS ===\n")

    # Criando lojas
    loja1 = Loja(1, "Tech Store", "mumbuca, 123")
    loja2 = Loja(2, "InfoWorld", "Avenida Marica, 45")

    # Criando usuários
    usuario1 = Usuario(1, "123.456.789-00")
    usuario2 = Usuario(2, "987.654.321-00")

    # Criando documentos (notas fiscais)
    doc1 = Documento(1, "NF-2025-001")
    doc2 = Documento(2, "NF-2025-002")

    # Criando equipamentos
    equip1 = Equipamento(1, "Notebook Lenovo", 3500.00, loja1.id_loja)
    equip2 = Equipamento(2, "Smartphone Samsung", 2500.00, loja1.id_loja)
    equip3 = Equipamento(3, "Monitor LG 27\"", 1200.00, loja2.id_loja)

    # Criando garantias
    garantia1 = Garantia(1, equip1.id_equipamento, "2024-10-01", "2025-10-01")
    garantia2 = Garantia(2, equip2.id_equipamento, "2024-12-15", "2025-12-15")

       # Exibindo informações formatadas
    print(loja1)
    print(loja2)
    print(usuario1)
    print(usuario2)
    print(doc1)
    print(doc2)
    print(equip1)
    print(equip2)
    print(equip3)
    print(garantia1)
    print(garantia2)


    print("\n=== FIM DA EXECUÇÃO ===")

if __name__ == "__main__":
    main()
