"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

#Год рождения Пушкина 1799.06.06

rightYear = '1799'
rightDate = '06.06'
questionYear = "Введите год рождения Пушкина: "
questionDate = "Введите день рождения Пушкина в формате MM.DD: "

def CheckAnswer(question, answer):
    while input(question) != answer:
        print("Неверно, пропробуйте ещё раз")

CheckAnswer(questionYear, rightYear)
CheckAnswer(questionDate, rightDate)

print("Верно!")


