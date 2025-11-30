from StudentQuest import Student

stud = Student(False, False,False)

if __name__ == '__main__':

    def clothes():
        if stud.bagpack == True:
            print("Теперь можно бежать на остановку.")
            stud.clothes = True
        else:
            print("Сначала лучше собрать сумку.")

    def facewash():
        if stud.facewash:
            print('Ты уже умылся')
        else:
            print("""Ты смотришь на себя в зеркало и думаешь: зачем это всё?
                        Умываешься и становится немного легче. Появляются силы действовать дальше.""")
            stud.facewash = True

    def food():
        print("Какая еда?! Тебе ещё два часа на автобусе ехать, надо выходить, а то опоздаешь.")

    def backpack():
        if stud.bagpack:
            print('Рюкзак уже собран')
        else:
            print('Теперь осталось одеться и можно выходить.')
            stud.bagpack = True

    print("Звонит будильник. На часах 6 утра. Встать с кровати или спать дальше?")
    enter = input("Встать/Спать")

    if 'Встать' == enter:
        print("Было тяжело, но ты справился!")

        while True:
            try:
                choose = int(input("Что делать: умыться (1), поесть (2), одеться (3), собрать сумку (4)"))
                if choose == 1:
                    facewash()
                elif choose == 2:
                    food()
                elif choose == 3:
                    clothes()
                    if stud.clothes:
                        break
                elif choose == 4:
                    backpack()
                else:
                    print("""К сожалению, ты заперт в клетке остоятельств. 
                                Нужно выбрать один из доступных вариантов.""")
            except:
                print('Выбор можно сделать только вписав номер варианта 1,2,3,4.')

        print ("""Ты выходишь из дома на темную улицу, вдыхаешь холодный воздух и думаешь,
        что когда-нибудь это все закончится, и ты будешь счастлив.""")

    else:
        print("""Твоя воля оказалась слаба.
         Тебя отчислили из универа,зато зато теперь ты довольный жизнью работник завода!""")