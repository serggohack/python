class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустым.")
        else:
            self.__name = new_name
            print("Имя изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "отлично"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не очень"
        else:
            m = "плохо"
        return m

    def talk(self):
        print("Меня зовут", self.name, 
              ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Большое спасибо! Было вкусно!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Ура! Спасибо что поиграл со мной!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Закрыть программу
        1 - Самочувствие зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
    
        choice = input("Ваш выбор: ")
        print()

    
        if choice == "0":
            print("Спасибо что поиграли Роман Николаевич!Хорошего дня!")

        
        elif choice == "1":
            crit.talk()
        
        
        elif choice == "2":
            crit.eat(food=int(input("Сколько дадите еды зверушке?")))
         
        
        elif choice == "3":
            crit.play(fun=int(input("Сколько будете играть со зверушкой?")))

        
        else:
            print("Извините, вы ввели не правильное число", choice)
    
main()
