lista1 = ['manzana', 'banana', 'cereza']
diccionario = {'fruta1': 'pera', 'fruta2': ["Hola", ['cucurella','50']], 'fruta3': 'kiwi'}

lista1.extend(diccionario.keys())
print(diccionario['fruta2'][1][1])
print(diccionario.get('fruta2')[1][0])
