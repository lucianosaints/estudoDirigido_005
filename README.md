# 🛠️ Projeto ED005 - Sistema de Garantia

## 📌 Descrição Geral

Este projeto tem como objetivo modelar e implementar um **sistema de controle de garantias de equipamentos** vendidos por lojas.  
O trabalho aborda as etapas de **modelagem de dados (conceitual, lógico e físico)**, além da execução dos scripts SQL em ambiente de banco de dados.

---

## 🧩 Estrutura do Projeto

```
ed005_garantia_nomeAluno/
│
├── sql/
│   ├── schema.sql          
│   ├── inserts.sql         
│
├── src/
│   ├── main.py             
│   ├── database.py        
│   ├── models/
│   │   ├── equipamento.py
│   │   ├── garantia.py
│   │   ├── loja.py
│   │   ├── documentos.py
│   │   ├── usuarios.py
├── prints/
│   ├── modelo_logico.png           # Diagrama lógico do banco
│   ├── consultas_dbeaver.png       # Resultado da execução no DBeaver
│   ├── execucao_terminal.png       # Evidência de execução no terminal
│
└── README.md
```

---

## 🧠 Modelo de Dados

### Entidades Principais

| Entidade | Descrição | Atributos principais |
|-----------|------------|----------------------|
| **Loja** | Representa uma loja de vendas | `id_loja`, `nome`, `cnpj`, `endereco`, `telefone` |
| **Equipamento** | Produto vendido pela loja | `id_equipamento`, `nome`, `preco`, `data_venda`, `id_loja` |
| **Garantia** | Período de cobertura do equipamento | `id_garantia`, `data_inicio`, `data_fim`, `tipo`, `id_equipamento` |
| **Documentos** | Nota fiscal associada a uma venda | `id_doc`, `numero_nota` |
| **Usuários** | Pessoa ou cliente do sistema | `id_usuario`, `cpf_usuario` |

---

## 🔗 Relacionamentos

- **Loja → Equipamento:** 1:N  
  Uma loja pode vender vários equipamentos.

- **Equipamento → Garantia:** 1:1  
  Cada equipamento possui apenas uma garantia.

- **Documentos** e **Usuários:** tabelas independentes no momento, usadas para controle futuro.

---

## 🧮 Modelo Lógico (Resumo)

```
Loja (id_loja PK, nome, cnpj, endereco, telefone)
Equipamento (id_equipamento PK, nome, preco, data_venda, id_loja FK)
Garantia (id_garantia PK, data_inicio, data_fim, tipo, id_equipamento FK)
Documentos (id_doc PK, numero_nota)
Usuários (id_usuario PK, cpf_usuario)
```

---

## 🖼️ Diagrama Lógico

O diagrama representando as entidades e relações está salvo em:
```
prints/modelo_logico.png
```

---

## ⚙️ Execução dos Scripts

1. Abra o **DBeaver** (ou outro cliente SQL).
2. Execute o script `schema.sql` para criar as tabelas.
3. Execute o script `inserts.sql` para inserir os dados.
4. Faça consultas como:

```sql
SELECT * FROM loja;
SELECT * FROM equipamento;
SELECT * FROM garantia;
SELECT * FROM documentos;
SELECT * FROM usuarios;
```

5. Capture o resultado e salve como `prints/consulta_dbeaver.png`.

---

## 💬 Diferença entre Modelos

| Modelo | Descrição |
|--------|------------|
| **Conceitual** | Mostra as entidades e relacionamentos em alto nível, sem tipos de dados. |
| **Lógico**     | Define tabelas, chaves primárias e estrangeiras, ainda sem detalhes do SGBD. |
| **Físico**     | Implementação real do banco com tipos e restrições específicos. |

---

## 🧾 Créditos

**Autor:** *Luciano_santos*  
**Disciplina:** Engenharia de Dados / Banco de Dados  
**Instituição:** *Curso_BFD_polo_itaipuaçu_maricá*  
**Ferramentas:** DBeaver,PostgreSQL, Draw.io

---

## 🧠 Conclusão

O projeto demonstrou a importância da modelagem de dados para garantir a integridade e clareza do sistema.  
Com o modelo implementado, é possível realizar consultas, filtrar equipamentos por loja e verificar informações de garantia com facilidade.
