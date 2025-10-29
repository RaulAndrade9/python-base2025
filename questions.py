names = ['joao', 'bruno', 'jose', 'bernardo']


#TODO:usar lambdas

def starts_with_b(text):
    return text[0].lower() == 'b'
    

lista = list(filter(starts_with_b, names))

print(lista)