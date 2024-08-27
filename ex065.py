resp = 'S'
soma = quant = média = maior = menor =0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            meior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
