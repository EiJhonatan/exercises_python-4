preco = float(input('qual valor do produto:'))
percentual = float(input('Qual o desconto a ser aplicado(0-100%):'))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'o preco do produto de {preco} Reais.')
print(f'Com desconto de {desconto}% ficara {final}Reais')