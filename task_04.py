# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
print('Сколько ребята сделали журавликов?')
crane = int(input())
if crane % 6 == 0:
    ferstNumber = int(crane/6)
    secondNumber = int(crane - crane/3)
    print("Петя сделал " + str(ferstNumber) + " журавликов")
    print('Катя сделала ' + str(secondNumber) + ' журавликов')
    print('Серёжа сделал ' + str(ferstNumber) + ' журавликов')
else:
    print('Не подходящее число')