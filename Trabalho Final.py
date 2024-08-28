import os
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')

TotalVisitas = 0
Clientes = 0
Masculino = 0
Feminino = 0
Visitas = 0
MelhorFonte = 0
TotalIdade = 0
TotalCristal = 0
ValorEntrega = 0
Rubis = 0
Esmeraldas = 0
Quartzos = 0
ValorRubis = 0
ValorEsmeraldas = 0
ValorQuartzos = 0
Brasilia = 0
Florianopolis = 0
Salvador = 0
DecisaoCompra = 'sim'

#---------------------INFO CLIENTE-------------

print ("#-----------------------INFO CLIENTE--------------------")

Vendedor = input("Com qual vendedor você esta comprando? Pierre, Paulo, Leticia, Nicolas.\n ").lower()

while True:

	NumeroTelefone = (input("Informe seu número de contato (XX) 9XXXX-XXXX (Somente números): "))

	if len(NumeroTelefone) != 11 or NumeroTelefone[3] != '9':
		input("Infome seu número de contato novamente: ")
	else:
		break

NomeCompleto =  input("Informe seu nome completo: ")
print("\nGostariamos de fazer algumas perguntas sobre você.")
Idade = int(input("Infome sua idade por favor: "))
Genero = input("Por favor digite se você é do sexo feminino ou masculino: ").lower()

Instagram = 0
Facebook = 0
Amigos = 0

FonteTrafego = input("Infome por qual meio chegou em nós (Instagram, Facebook, Amigos): ").lower()

if FonteTrafego == 'Instagram':
	Instagram += 1

elif FonteTrafego == 'Amigos':
	Amigos += 1

elif FonteTrafego == 'Facebook':
	Facebook += 1


Entradas = input("É a primeira vez que você entra no nosso site?: ").lower()

if Entradas == 'sim':
	Visitas += 1

else:
	Visitas = int(input("Quantas vezes já visitou nosso site?: "))

TotalVisitas += Visitas

Clientes += 1
TotalIdade = TotalIdade + Idade

if Genero == 'Masculino':
	Masculino += 1

elif Genero == 'Feminino':
	Feminino += 1

#---------------------DECISÃO DE COMPRA----------------



print ("\n#---------------------DECISÃO DE COMPRA----------------\n")

while True:

		if DecisaoCompra.lower() == 'sim':
			CristalEscolhido = input("Temos 3 opções de cristais, escolha um: Rubi, Esmeralda e Quartzo. ")

			if CristalEscolhido.lower() == "rubi":
				print("Certo, o valor do seu cristal é de R$120,00. ")
				Rubis += 1
			
			elif CristalEscolhido.lower() == "esmeralda":
				print("Certo, o valor do seu cristal é de R$220,00. ")
				Esmeraldas += 1

			elif CristalEscolhido.lower() == "quartzo":
				print("Certo, o valor do seu cristal é de R$45,00. ")
				Quartzos += 1

			else:
				print("Infelizmente no momento só temos aquelas 3 opções. Porém esperamos ampliar nosso estoque no futuro!")
				break

			DecisaoCompra = input('Você gostaria de comprar mais alguma coisa? Sim ou não?: ')

		elif DecisaoCompra.lower() == 'nao':
			print("Certo, continuaremos para o frete agora.")
			break

		else:
			print("Por favor, responda com 'sim' ou 'não'.")
			continue

if Quartzos > 0:
		ValorQuartzos = 45 * Quartzos

if Esmeraldas > 0:
		ValorEsmeraldas = 220 * Esmeraldas

if Rubis > 0:
		ValorRubis = 120 * Rubis

TotalCristal = ValorQuartzos + ValorEsmeraldas + ValorRubis

	#--------------------VALOR FRETE--------------------

print ("#--------------------VALOR FRETE------------------------")

if ValorEntrega == 0:

		Entrega = input("Você gostaria de pedir para entregar? Sim ou não?: ")

		if Entrega.lower() == 'sim':
				
			while True:
					CidadeEntrega = input("No momento só enviamos para 3 cidades, sendo: Brasília(DF), Florianópolis(SC) e Salvador(BA), qual seria seu destino? ")
							
					if CidadeEntrega.lower() == "brasilia":
						print("Certo, o valor da entrega em Brasília(DF) é de R$35,00. ")
						Brasilia += 1
						ValorEntrega = 35
						break
								
					elif CidadeEntrega.lower() == "florianopolis":
						print("Certo, o valor da entrega em Florianópolis(SC) é de R$23,00. ")
						Florianopolis += 1
						ValorEntrega = 23
						break
								
					elif CidadeEntrega.lower() == "salvador":
						print("Certo, o valor da entrega em Salvador(BA) é de R$47,00. ")
						Salvador += 1	
						ValorEntrega = 47
						break

					else:
						print("Desculpe, no momento só podemos entregar para Brasília(DF), Florianópolis(SC) ou Salvador(BA). Por favor, escolha um desses destinos.")
						continue	

		elif Entrega == 'nao':
			print("\nCerto, nosso endereço fica na rua Av. Cel. Procópio Gomes do bairro Bucarein com o número 911.")

		else:
			print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")

		ValorFinal = TotalCristal + ValorEntrega 

	#--------------------IMPRESSÃO VALORES-------------------	

print ("#--------------------VALORES TOTAIS-------------------")

print("Número de contato: ", NumeroTelefone)
print("Nome: ", NomeCompleto)
print("Os cristais comprados ficaram no valor total de:", TotalCristal)

print("Os cristais comprados foram: ")

if Rubis > 0:
		print(f"\nForam comprados {Rubis} Rubis.")

if Esmeraldas > 0:
		print(f"Foram comprados {Esmeraldas} Esmeraldas.")

if Quartzos > 0:
		print(f"Foram comprados {Quartzos} Quartzos.")

if ValorEntrega > 0:
		print("\nO valor total do seu cristal com entrega fica em:", ValorFinal, "\n")

#--------------------DADOS DO CLIENTE-------------------	
	
print ("#--------------------DADOS MÉDIA DE CLIENTES-------------------")

Faixa_Etaria = TotalIdade / Clientes

if Faixa_Etaria > 20:
	Faixa_Etaria = 'Adultos'

else:
	Faixa_Etaria = 'Adolescentes'

if Feminino > Masculino:
	Genero_Alvo = 'Femininos'

else:
	Genero_Alvo = 'Masculinos'

print("O gênero que mais compra conosco é: ", Genero_Alvo)
print("A faixa etária que mais compra conosco é de: ", Faixa_Etaria)
print("No total tivemos ", Visitas, "Visitas no nosso site. ")

MelhorRegiao = Brasilia
NomeMelhorRegiao = 'Brasilia'

if Salvador > MelhorRegiao:
    MelhorRegiao = Salvador
    NomeMelhorRegiao = 'Salvador'

if Florianopolis > MelhorRegiao:
    MelhorRegiao = Florianopolis
    NomeMelhorRegiao = 'Florianopolis'

print("A região que mais entregamos é para: ", NomeMelhorRegiao)

#--------------------HORÁRIO DE VENDA-------------------	

def get_current_datetime():
    # Obtém a data e hora atuais
    now = datetime.now()

    formatted_now = now.strftime("%Y/%m/%d %H:%M:%S")

    print(f"A venda foi feita em: {formatted_now}")

    return now

if __name__ == "__main__":
    current_datetime = get_current_datetime()

#--------------------RESULTADO-------------------	
	
print ("#--------------------CONSULTAR VENDEDOR-------------------")

if Vendedor == "pierre":
    print ("\nO vendedor foi: Pierre Vargas")
    print ("O nome de seus clientes: ", NomeCompleto)
    print ("O total em vendas foi: ", TotalCristal)
    print ("Os Cristais vendidos e suas quantidades foram: ")

elif Vendedor == "paulo":
        print ("\nO vendedor foi: Paulo Ricardo")
        print ("O nome de seus clientes: ", NomeCompleto)
        print ("O total em vendas foi: ", TotalCristal)
        print ("Os Cristais vendidos e suas quantidades foram: ")

elif Vendedor == "leticia":
        print ("\nO vendedor foi: Leticia Vieira")
        print ("O nome de seus clientes: ", NomeCompleto)
        print ("O total em vendas foi: ", TotalCristal)
        print ("Os Cristais vendidos e suas quantidades foram: ")
	
elif Vendedor == "nicolas":
        print ("\nO vendedor foi: Nicolas Giovanni")
        print ("O nome de seus clientes: ", NomeCompleto)
        print ("O total em vendas foi: ", TotalCristal)
        print ("Os Cristais vendidos e suas quantidades foram: ")

if Rubis > 0:
	print(f"\nForam comprados {Rubis} Rubis na sua venda.")

if Esmeraldas > 0:
	print(f"Foram comprados {Esmeraldas} Esmeraldas na sua venda.")

if Quartzos > 0:
	print(f"Foram comprados {Quartzos} Quartzos na sua venda.")
		
#--------------------NOME DO VENDEDOR-------------------	

if Vendedor == "pierre":
    print ("\nVocê consultou o vendedor: Pierre Vargas\n")
if Vendedor == "paulo":
    print ("\nVocê consultou o vendedor: Paulo Ricardo\n")
if Vendedor == "leticia":
    print ("\nVocê consultou a vendedora: Leticia Vieira\n")
if Vendedor == "nicolas":
    print ("\nVocê consultou o vendedor: Nicolas Giovanni\n")

#--------------------PREÇO PLATARFORMA-------------------

PlataForma = (input("Digite a plataforma que será anunciada: "))
PrecoDia = float(input("Digite o preço cobrado pela plataforma por cada dia: "))
QuantHoras = int(input("Digite quantas horas esse anúncio rodara por dia: "))
QuantDias = int(input("Informe a quantidade dias esse anúncio ficara rodando: "))

print("O preço cobrado por dia é: ", PrecoDia)

PrecoHora = PrecoDia / QuantHoras
print("O preço por hora e: ", PrecoHora)

PrecoSemana = PrecoDia * 7 
print("O preço por semana e: ", PrecoSemana)

QuantSemanas = QuantDias / 7
print("O anúncio rodara por ", QuantSemanas, "semanas.")
