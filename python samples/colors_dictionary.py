colors_EN_PT_dic = {
    'azul': 'blue',
    'red': 'vermelho',
    'verde': 'green',
    'amarelo': 'yellow',
    'lilas': 'purple'
}
# recebe o nome da cor em PT
# pesquisa por get no dicionário e mostra se encontrou ou não

# all string to lower case
colorPT = input ('type a color name (in portuguese): ').lower()

colorEN = colors_EN_PT_dic.get(colorPT, 'Color not found')

print('The searched color is: ', colorEN)

