# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите длину шоколадки')
lenght = int(input())
print('Введите ширину шоколадки')
width = int(input())
print('Сколько долек хотите отломить')
sliceChocolote = int(input())
if sliceChocolote % lenght == 0 or sliceChocolote % width == 0:
    if lenght*width == sliceChocolote:
        print('Это целая шоколадка')
    else:
        print('Можно взять ' + str(sliceChocolote) + ' долек, отломив один раз')
else:
    print('Не получиться взять ' + str(sliceChocolote) + ' долек, отломив один раз')