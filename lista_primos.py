def listar_primos(inicio, fim):
	cont = 0
	col = 10
	valor = 2
	
	if inicio < 2:
		return
	
	if inicio == 2:
		cont += 1
		print(f'{valor:4d}', end='')
	
	if inicio % 2 == 0:
		inicio += 1
	
	for i in range(inicio, fim,2):
		if eh_primo(i) == True:
			cont += 1
			elemento = cont%col
			
			if elemento == 0:
				print(f', {i:4d}')
			elif elemento == 1:
				print(f'{i:4d}', end='')
			else:
				print(f', {i:4d}', end='')

	if cont%col!=0:
		print()
	

def eh_primo(num):
	resultado = False
	
	if num%2 == 0:
		return resultado
		
	for i in range(3,num,2):
		if num%i == 0:
			return resultado
			
	resultado = True
	return resultado
	
def main():
	listar_primos()
	#print(eh_primo(5))

if __name__ == "__main__":
	main()