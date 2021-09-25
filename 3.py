class TV:

    def num(self):
        print("Вы включили телевизор")

    def v1(self):
        x = int(input('Выставте громкость: '))
        if x > 100:
            print('Громкость поставлена на максимум')
            x1 = 100
        elif x <= 100 and x >= 0:
            print('Громкость изменена')
            x1 = 0
            x1 = x
        elif x < 0:
            print('Громкость поставлена на минимум')
            x1 = 0
        print('Cейчас стоит', x1, 'уровень громкости')
    def v2(self):
        x2 = int(input('Изменит канал: '))
        if x2 > 32:
            print('Выше 84 канолов больше нет')
        elif x2 <=32 and x2 > 0:
            print('Канал изменён')
            x3 = x2
        elif x2<=0:
            print('Ниже 1 канала нет ')
        print('Щас включен', x3, 'канал')
 

def main():
    crit = TV()

    choice = None  
    while choice != "0":
        print \
        ("""
        Мой Телевизор
    
        0 - Выключить и выйти
        1 - Включить телевизор
        2 - Изменить звук
        3 - Изменить канал
        """)
    
        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("Спасибо за просмотр! Хорошего дня!")

        elif choice == "1":
            crit.num()
        
        elif choice == "2":
            crit.v1()
         
        elif choice == "3":
            crit.v2()

        else:
            print("Извините, в меню нет пункта", choice)
    
main()
