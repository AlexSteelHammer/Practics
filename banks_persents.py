per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите ссума вклада: '))
val_per = list(per_cent.values())
t,s,v,sb = val_per[0], val_per[1], val_per[2], val_per[3]
TKB = int(t * money/100)
CKB = int(s * money/100)
VTB = int(v * money/100)
SBER = int(sb * money/100)
deposit = [TKB, CKB, VTB, SBER]
print(deposit)
print('Максимальная сумма, которую Вы сможете заработать: ', max(deposit))