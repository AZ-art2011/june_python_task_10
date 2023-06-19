# Задача 10

n = int(input('Укажите число монет '))
coin_o = coin_r = 0
for i in range(n):
    side_of_coin = int(input('Орел-1, решка-0 '))
    if side_of_coin == 1:
        coin_o += 1
    else:
        coin_r += 1
if coin_o < coin_r:
    print(f'Наименьшее количество монет орлами вверх - {coin_o} шт. Их необходимо перевернуть.')
elif coin_o == coin_r:
    print(f'Орлов и решек поровну - {coin_o} шт.')
else:
    print(f'Наименьшее количество монет решками вверх - {coin_r} шт. Их необходимо перевернуть.')