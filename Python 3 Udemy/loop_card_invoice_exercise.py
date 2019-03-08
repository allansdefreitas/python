#Credit card invoice
#Enquanto True
    # se resposta for 's'
       # Recebe o nome e preço do produto
        #adiciona à fatura
    # se resposta for 'n'
        #sai do laço

#imprime a fatura:
    # nome e preço
    #total da fatura

answer = 'y'
# invoice_items = []
#dictionary é melhor
invoice_items_dictionary = {}
product_name = ''
product_price = 0.0
invoice_total_price = 0.0
# validação
valid_price = False

while answer == 'y':
    product_name = input('Product name: ')

    #product_price = float (input('Product price: '))    

    while valid_price == False:

        product_price = input('Product price: ')
        
        try:
            # try convert to float
            product_price = float(product_price)
            valid_price = True
        except:
            print("invalid format for price. Use '.' instead of ',' to cents ")

    # Adiciona ao dictionary
    invoice_items_dictionary.update({product_name: product_price})
    # invoice_items.append([product_name, product_price])
    
    # Somatório dos preços
    invoice_total_price += product_price

    answer = input('Do you want add more products (Y, N)? ').lower()


# Impressão da fatura

print('_______________________________')
print('INVOICE DETAILS')
print('_______________________________')

for i in invoice_items_dictionary:
    #Name ..........................price
    print(i, '....................',invoice_items_dictionary.get(i))
    # com list (SOLUÇÃO NÃO IDEAL)
    # print( i[0], '-------' ,i[1] )

print('_______________________________')
print('TOTAL PRICE ($):' , invoice_total_price)

# print(invoice_items)
