import re
import csv

def processar_lista(caminho_arquivo):
    cpf_cnpj_lista = []

    # Ler o arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        # Ler cada linha do arquivo
        for linha in arquivo:
            # Extrair CPFs e CNPJs usando expressão regular
            cpfs_cnpjs = re.findall(r'\d{11}|\d{14}', linha)

            # Adicionar CPFs e CNPJs à lista
            cpf_cnpj_lista.extend(cpfs_cnpjs)

    # Remover caracteres indesejados e duplicados
    cpf_cnpj_lista = [re.sub(r'\D', '', item) for item in cpf_cnpj_lista]
    cpf_cnpj_lista = list(set(cpf_cnpj_lista))

    return cpf_cnpj_lista

def gerar_arquivo_txt(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(item + '\n')

    print('Arquivo TXT gerado com sucesso!')

def gerar_arquivo_excel(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['CPF/CNPJ'])

        for item in lista:
            writer.writerow([item])

    print('Arquivo Excel gerado com sucesso!')

# Exemplo de uso
caminho_arquivo_entrada = 'caminho/do/arquivo.txt'
caminho_arquivo_saida_txt = 'caminho/do/arquivo_processado.txt'
caminho_arquivo_saida_excel = 'caminho/do/arquivo_processado.xlsx'

lista_processada = processar_lista(caminho_arquivo_entrada)

# Gerar arquivo TXT
gerar_arquivo_txt(lista_processada, caminho_arquivo_saida_txt)

# Gerar arquivo Excel
gerar_arquivo_excel(lista_processada, caminho_arquivo_saida_excel)
