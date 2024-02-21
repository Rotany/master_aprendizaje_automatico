palabras = "hola que tal el mundo hijo mio que te dejamos, la togu es una master del chocoflon, que tal te va todo por madrid"
palabras = palabras.replace(',', '')
palabras_dict = {
}
palabras_array = palabras.split(' ')

for palabra in palabras_array:
    if palabra in palabras_dict:
        palabras_dict[palabra]=palabras_dict[palabra]+1
    else:
        palabras_dict[palabra]=1
print(palabras_dict)