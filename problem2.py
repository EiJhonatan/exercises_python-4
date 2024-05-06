Km = int(input('Quantos KM foram Percorrido? '))
dias = int(input('Quanto dia Foram percorridos? '))

preco = 60 * dias + 0.15 + Km
print(f'km rodados{Km}, Dias percorridos {dias}.')
print(f'valor a ser pago foi de {preco}.')