shopping_dict = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb', 'pączek', 'bułki']}
k=0
print('Lista zakupów')
for r in shopping_dict :
    k = k + len(shopping_dict[r])
    print(f'Idę do {str.capitalize(r)} kupić {shopping_dict[r]}')
print(f'Kupiono {k} produktów')   
print('Nie kupiono sera i jabłek')
for i in range(15):
    i=i+i
    print(i)

