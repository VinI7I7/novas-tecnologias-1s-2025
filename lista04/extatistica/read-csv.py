import csv


def read_csv(base_folder):
    with open(base_folder, newline="", encoding="utf-8") as file:
        l = csv.DictReader(file)
        dados = []
        for linha in l:
            for chave, valor in linha.items():
                if chave != "nome":
                    linha[chave] = float(valor)
            dados.append(linha)
        return dados

