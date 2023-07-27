import os

#================

def ex_cesar():
	os.system("cls")
	print(" ==================================================== ==========================")	
	print( " | ** Crifra de César ** |")
	imprima(" | |")
	print( " | Criada pelo imperador Cesar, com o intuito de codificar mensagens em su|")	
	print( " | as batalhas, ela é um tipo de cifra de substituição na qual cada letra|")
	print( " | do texto é substituído por outro, que se apresenta no alfabeto abaixo |")
	print( " | dela um numero fixo de vezes. Por exemplo, com uma troca dela um numero|")
	print( " | como exemplo, com uma troca de três posições, A seria substituída por |")	
	print(" | D, B se tornaria E, e assim por diante. |")
	imprima(" | |")
	print( " | ** OBS : O algoritimo consegue decifrar apenas letras |")
	print(" | Caso sejam inseridos números ou caracteres código irá finalizar |")
	print(" ==================================================== ===========================")	
	enter = input("\n * Pressione ENTER para continuar *")
	os.system("cls")

	



#================
def ex_morse():
	os.system("cls")
	print(" ==================================================== ==========================")	
	print(" | ** Código Morse ** |")
	imprima(" | |")
	print( " | Inventado por um pintor e físico Americano Samuel Morse(1791-1872).Sentar|")
	print( " | ua em uma ferramenta de comunicação que representa letras, números e |")
	print( " | sinais de verificação por meio de uma sequência de pontos (.) e traços |")
	print( " | (-) chamados de bits ou dahs, respectivamente. Esses sinais criam uma |")
	print( " | mensagem codificada que é enviada pausadamente, conforme o ritmo e os |")
	print( " | intervalos com que aparecem. |")
	imprima(" | |")
	imprima(" | |")
	print( " | ** OBS : O algoritmo consegue decifrar apenas letras e números |")
	print( " | Caso seja inserido código carctericos irá finalizar |")
	print(" ==================================================== ==========================")
	enter = input("\n * Pressione ENTER para continuar *")
	os.system("cls")

#================
 
def ex_simétrica():
	os.system("cls")
	print(" ==================================================== ===========================")	
	print(" | **Chave Simetrica** |")
	print(" | Considerada a mais simples, na qual remetente e destinatário utilizar a|")	
	print( " | mesma chave para codificar e decodificar a informação . Os lgoritmos de|")
	print( " | chave simétrica mesma chave para codificar e decodificar a informação. |")
	print( " | Os algoritmos de chave simétrica são algoritmos para criptografia que us|")
	print( " | sou a mesma chave criptográfica para encriptação de texto puro e decript|")
	print( " | ação de texto cifrado. A chave, na prática, representa um segredo com |")
	print( " | compartilhado entre duas ou mais partes que pode ser usado para manter uma|")
	print( " | ligação de informação privada |")
	imprima(" | |")
	print( " | Neste algoritmo a criptografia simétrica utiliza o bliblioteca python,|")
	print( " | cryptocode que fornece a execução da função de forma simples e prática |")
	imprima(" | |")
	imprima(" | |")
	imprima(" | |")
	print(" ==================================================== ===========================")
	enter = input("\n * Pressione ENTER para sair *")
	os.system("cls")

#================

def consideração():
	os.system("cls")
	print(" ==================================================== ==========================")
	print( " | O projeto foi desenvolvido pelos alunos do terceiro período do curso |")
	print( " | de Sistemas da Informação da Uniube Uberlândia centro. Os envolvidos |")
	print(" | são os alunos: |")
	imprima(" | |")
	print( " | > Samuel Souto dos Santos |")
	imprima(" | |")
	print( " | O objetivo do projeto é colocar em prática os conhecimentos de Python |")
	print( " | ensinados pela professora Dra. Luciene Chagas de Oliveira |")
	imprima(" | |")
	imprima(" | |")
	imprima(" | |")
	print( " | O projeto foi desenvolvido com base de técnicas de criptografia sendo |")
	print( " | Elas são as Cifra de César, Códigos Morse e Chave Simétrica.Assim ofer|")
	print( " | tando aos usuários do algoritmo a possibilidade a decodificar e codificar-|")
	print(" | carro como mensagens. |")
	print(" ==================================================== ==========================")

#================

# info de cifras
def info_cifras():
	os.system("cls")
	print("\n Para conhecer um pouco mais das criptografia do projeto, selecione : \n")
	print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
	print(" 1 - Crifra de Cesar ")	
	print(" 2 - Codigo Morse ")
	print(" 3 - Chave simetrica ")
	print("\n ** Para sair selecione qualquer outro número ou letra **")
	print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
	op = input(" # Selecione uma opção : ")
	se op == "1":
		ex_cesar()		
	elif op == "2":
		ex_morse()
	elif op == "3":
		ex_simétrica()
	outro :	
		enter = input("\n * Aperte enter para voltar ao menu principal *")

#================

def introdução():
	print("\n Análise criptográfica de mensagens \n")
	print("= = = = = = = = = = = = = = ==")
	print(" 1 - Crifra de César ")	
	print(" 2 - Código Morse ")
	print(" 3 - Chave Simetrica ")
	print("4 - Detalhes")
	print(" 5 - Sair ")
	print("= = = = = = = = = = = = = = ==")

#================
def crip_cesar (op):
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	chave = int(input(" > Insira um numero de 1 ate 26 como chave : "))
	frase = input(" > Insira sua frase : ")
	frase = frase.replace( " ", "")
	frase = frase.lower()
	cripto = ''
	para eu na frase:
		posicao_letra = alfabeto.find(i)
		se op == 1:
			posicao_letra = posicao_letra + chave
		elif op == 2:
			posicao_letra = posicao_letra - chave
		if (posicao_letra > len(alfabeto)):
			posicao_letra = posicao_letra - len(alfabeto)	
		cripto = cripto + alfabeto[posicao_letra]
	print(" > Mensagem :" , cripto)
	operação de retorno

#================

def morse():
	alfabeto_mor = ['.- ','-... ','-.-. ','-.. ','. ','..-. ','--. ','.... ','.. ','.--- ','-.- ','.-.. ','-- ','-. ','--- ','.--. ','--.- ','.-. ','... ','- ','..- ','...- ','.-- ','-..- ','-.-- ','--.. ','.---- ','..--- ','...-- ','....- ','..... ','-.... ', '--... ','---.. ','----. ','----- ',' ']
	alfabeto = 'abcdefghijklmnopqrstuvwxyz1234567890'	
	print("\n * Codigos Morse *")
	print("\n 1 - para criptografar\n 2 - para descriptografar")	
	op = input(" Selecione uma opção: ")
	se op == '1':
		posição_letra = ''
		juntatudoparaoprint = ''
		frase = input(" > Insira uma frase : ")	
		frase = frase.lower()
		para comparar na frase:
			posicao_letra = alfabeto.find(compara)			
			juntatudoparaoprint = juntatudoparaoprint + alfabeto_mor[posicao_letra]	
		print(" > Mensagem criptografada : ",juntatudoparaoprint) # imprime fora do loop o resultado da msg criptografada
	elif op == '2':
		adicionatodaletra = ''
		tamanho = int(input(" > Insira o tamanho da mensagem: ")) # solicite o tamanho da frase em uma var int			
		para ver no intervalo (tamanho):
			palavra = input(" > Insira a letra: ") # Solicita as letras da mensagem
			palavra = palavra+' '
			se palavra em alfabeto_mor:
				print(" * Letra localizada * ")
				ver_tamanho = alfabeto_mor.index(palavra)
				adicionatododaletra = adicionatodaletra + alfabeto[ver_tamanho]
				print("\n>>>>> Mensagem : ",adicionatodaletra)	 
			outro:
				print(" ** Letras incorretas")
	outro:
		print("** OP INDISPONIVEL VOLTANDO AO MENU PRINCIPAL")

		
#================

def chave_simétrica ():
	tentar:
		print(" >> Aguarde, estamos atualizando sua biblioteca de criptografia em Python <<")
		os.system("pip install rsa")
		os.system("pip install cryptocode")
		os.system("cls")
		importar criptocódigo
		print("\n * Chave simetrica *")
		print("\n 1 - para criptografar\n 2 - para descriptografar")
		ver = input("\n > Selecione a opção : ") # Solicita a opção de criptar ou descriptar
		se ver == '1' :  
			chave = input("> Insira sua chave : ")
			mensagem = input("> Insira sua mensagem: ")
			MensagemCriptografada = cryptocode.encrypt(mensagem, chave)	
	# OBS: para controle das chaves e informação o diretório no qual foi inserido o arquivo do algoritimo
	#cria um arquivo txt chamado logs que havera informacoes das chaves simetricas e msg
			arq = open("logs.txt","a")
			arq.write("\n\n> Chave: ")	
			arq.write(chave)
			arq.write("\n\n> Mensagem: ")
			arq.write(MensagemCriptografada)
			arq.close
			print("\n\n>> Mensagem criptografada: " + MensagemCriptografada)
		elif ver == '2' : # caso opção menu seja 2 é realizado a criptografia
			msg_cod = input(">> Insira sua mensagem codificada :") # Solicita a chave
			chave_cod= input(">> Insira sua chave :")# Solicita a msg cripitada
			Msg_desc = cryptocode.decrypt( msg_cod ,chave_cod )
			print ("\n\n>> Mensagem descodificada : ",Msg_desc)
			se Msg_desc == Falso:
				print(">> você inseriu a Chave ou mensagem incorreta ")
		outro :
			print(">> Opção invalida!")
	exceto Exceção como e:
		print(">> Houve um erro com sua biblioteca nativa cryptocode tente executar o algoritimo no cmd através do comando no diretório onde ele foi colocado e comando python (nome do arquivo python).py ")

#================
#MENU PRINCIPAL
# -- codificação: utf-8 --
enquanto verdadeiro:
	os.system("cls")
	introdução()
	i = input("\n > Selecione uma opção: ")
	se eu == '1':
		ex_cesar()
		os.system("cls")
		print("\n * Cifra de César *")
		print("\n 1 - para criptografar\n 2 - para descriptografar")
		op = int(input("\n > Selecione a opção : "))
		se op == 1 ou op == 2:
			crip_cesar (op)
		outro :
			print(">> Opção inválida, você será direcionado ao menu principal, tente novamente");
			
		enter = input("\n * Aperte enter para voltar ao menu principal *")
	elif i == '2':
		ex_morse()
		os.system("cls")
		morse()
		enter = input("\n * Aperte enter para voltar ao menu principal *")
	elif i == '3':
		ex_simétrica()			
		chave_simétrica()
		enter = input("\n * Aperte enter para voltar ao menu principal *")
	elif i == '4':
		consideração()	
		enter = input("\n * Aperte enter para proseguir *")
		info_cifras()
	elif i == '5':
		print("fim")
		os.system("cls")
		quebrar
	outro :	
		enter = input("\n *** OPÇÃO INVALIDA, TENTE OUTRA NOVAMENTE ***")
