import sys
import random
import copy
from termcolor import colored
f_texto = open("lista.txt", "r")
lista_jogadores = [item.replace("\n", "") for item in f_texto.readlines()]
qtd_de_jogadores = len(lista_jogadores)
num_de_jogador_time = int(sys.argv[1])
qtd_de_times = qtd_de_jogadores/num_de_jogador_time

print "\n################################################################\n"
print colored("Quantidade de times: "+str(qtd_de_times),'blue')
print colored("Quantidade de Jodadores: "+str(qtd_de_jogadores),'green')
print colored("Quantidade de Jogador por Time: "+str(num_de_jogador_time),'red')
print "\n################################################################\n"
for i in range(0,qtd_de_times):
	for j in range(0,100):
		random.shuffle(lista_jogadores)
	print colored("\ntime "+str(i+1)+":\n",'red')
	time = random.sample(lista_jogadores,num_de_jogador_time)
	print colored(time,'green')
	new_lista = []
	for item in lista_jogadores:
		if item not in time:
			new_lista.append(item)	
	lista_jogadores = copy.copy(new_lista)
	if i+1 == qtd_de_times:
		print "\n################################################################\n"
		print colored("Jogadores de Proximos:\n",'blue')
		print lista_jogadores

print "\n################################################################\n"

