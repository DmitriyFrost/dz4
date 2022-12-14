"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


# Вариант 1

bill_sum = 0  # сумма счета... изначально равна 0
history = []  # история покупок... пока что пустой список

while True:  # выводим пункты меню и остаток на счете
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет: {bill_sum}')

    choice = input('Выберите пункт меню: ')  # выбор пункта меню
    if choice == '1':  # если выбор 1
        cost = int(input('Введите сумму пополнения: '))  # вводим сумму пополнения
        bill_sum = bill_sum + cost  # и сумма счета увеличивается на сумму пополнения
    elif choice == '2':  # если выбор 2
        cost = int(input('Введите сумму покупки: '))  # вводим сумму покупки
        if cost > bill_sum:  # но если сумма пополнения больше суммы счета
          print('Недостаточно средств на счете!')  # то выводим Недостаточно средств на счете!
        else:  # в противном случае
          bill_sum = bill_sum - cost  # сумма счета равна сумма счета минус сумма покупки
          name = input('Введите название покупки: ')  # вводим название покупки
          history.append ((name, cost))     # добавляем в историю покупок: название покупки и сумму покупки
    elif choice == '3':  # если выбор 3
        print(history)   # выводим историю покупок
    elif choice == '4':  # если выбор 4
        break            # конец
    else:                # во всех остальных случаях
        print('Неверный пункт меню!')  # выводим Неверный пункт меню!




# Вариант 2 с функцией:

bill_sum = 0  # сумма счета... изначально равна 0
history = []  # история покупок... пока что пустой список

def buy(bill_sum):
  cost = int(input('Введите сумму покупки: '))  # вводим сумму покупки
  if cost > bill_sum:  # но если сумма пополнения больше суммы счета
          print('Недостаточно средств на счете!')  # то выводим Недостаточно средств на счете!
  else:  # в противном случае
          bill_sum = bill_sum - cost  # сумма счета равна сумма счета минус сумма покупки
          name = input('Введите название покупки: ')  # вводим название покупки
          history.append ((name, cost))     # добавляем в историю покупок: название покупки и сумму покупки
  return bill_sum

while True:  # выводим пункты меню и остаток на счете
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет: {bill_sum}')

    choice = input('Выберите пункт меню: ')  # выбор пункта меню
    if choice == '1':  # если выбор 1
        cost = int(input('Введите сумму пополнения: '))  # вводим сумму пополнения
        bill_sum = bill_sum + cost  # и сумма счета увеличивается на сумму пополнения
    elif choice == '2':  # если выбор 2
        bill_sum = buy(bill_sum)
    elif choice == '3':  # если выбор 3
        print(history)   # выводим историю покупок
    elif choice == '4':  # если выбор 4
        break            # конец
    else:                # во всех остальных случаях
        print('Неверный пункт меню!')  # выводим Неверный пункт меню!