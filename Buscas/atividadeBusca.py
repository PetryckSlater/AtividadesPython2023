import csv

servidores_dns = []

with open('dns_br.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)  # pula os cabeçalhos
    for row in csv_reader:
        servidor_dns = {
            'ip': row[0],
            'nome': row[1]
        }
        servidores_dns.append(servidor_dns)

def busca_sequencial(chave, vetor=servidores_dns):
    for i in vetor:
        if i['ip'] == chave or i['nome'] == chave:
            return i
    return "Valor não encontrado"
#Professor ESSE For foi responsavel por 3 horas DE ODIO.
# menu
print("Escolha o que você deseja fazer!")
print("Digite 1 para mostrar o banco de dados:")
print("Digite 2 para fazer uma busca sequencial:")
op = int(input("->>"))
if op == 1:
    print(servidores_dns)
elif op == 2:
    valor = str(input('Digite o que você deseja pesquisar:'))
    resultado = busca_sequencial(valor)
    if resultado:
        print("Resultado:")
        print("IP:", resultado['ip'])
        print("Nome:", resultado['nome'])
    else:
        print("Chave não encontrada.")
else:
    print("Opção inválida.")
