""" Aula 03 - Args e Kwargs """

# * args 
# ** kwargs

# args 
def world_cup_titles(country, *args):
    print('Country:', country)
    for title in args:
        print('year:', title)

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
world_cup_titles('Espanha', '2010')

# kwargs
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0)
print(f'O preço do produto é: {final_price}')

final_price = calculate_price(100.0, discount=5.0)
print(f'O preço do produto com desconto é: {final_price}')

final_price = calculate_price(100.0, tax_percentage=7)
print(f'O preço do produto com taxa é: {final_price}')

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(f'O preço do produto com taxa e desconto é: {final_price}')