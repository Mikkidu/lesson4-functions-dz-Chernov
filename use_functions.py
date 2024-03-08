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

moneyAmount = 0.
history = []
hKey = 'expenseItem'
hValue = 'price'

def ChangeBalance(value):
    global moneyAmount
    moneyAmount += value
    print(f"Сумма на счету: {moneyAmount : .02f}")

def CheckBalance(requaredAmount):
    global moneyAmount
    if requaredAmount <= moneyAmount:
        return True
    else:
        return False

def AddHistory(purpose, amount):
    global hKey, hValue
    historyItem = { hKey : purpose, hValue : amount}
    history.append(historyItem)

def PrintHistoryItem(item):
    global  hKey, hValue
    print(f"Purpose {item[hKey]} --> {item[hValue]}")

def DepositMenu():
    global moneyAmount
    value = float(input("Сколько хотите внести?: "))
    if value > 0:
        ChangeBalance(value)
    else:
        print("Ошибка, сумма должна быть положительным числом!")

def PurchaseMenu():
    value = float(input("Введите стоимость покупки?: "))
    if CheckBalance(value):
        key = input("Ведите статью расхода: ")
        ChangeBalance(-value)
        AddHistory(key, -value)
    else:
        print('Недостаточно средств')

def HistoryMenu():
    global history
    print("История покупок:")
    for item in history:
        PrintHistoryItem(item)




while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        DepositMenu()
    elif choice == '2':
        PurchaseMenu()
    elif choice == '3':
        HistoryMenu()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
print("До встречи, будем вас ждать!")