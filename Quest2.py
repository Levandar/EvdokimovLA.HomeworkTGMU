bagpackpermit = False
clothespermit = False
def clothes(bagpackpermit):
    if bagpackpermit:
        print("Теперь можно бежать на остановку.")
        return True

    else:
        print("Сначала лучше собрать сумку.")
        return False

def facewash():
    print("""Ты смотришь на себя в зеркало и думаешь: зачем это всё?
                Умываешься и становится немного легче. Появляются силы действовать дальше.""")

def food():
    print("Какая еда?! Тебе ещё два часа на автобусе ехать, надо выходить, а то опоздаешь.")

def backpack():
    print('Теперь осталось одеться и можно выходить.')
    return True

print("Звонит будильник.Встать с кровати или спать дальше?")
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
                clothespermit = clothes(bagpackpermit)
                if clothespermit:
                    break
            elif choose == 4:
                bagpackpermit = backpack()
        except:
            print("""К сожалению, ты заперт в клетке остоятельств. 
            Нужно выбрать один из доступных вариантов.""")

else:
    print("""Твоя воля оказалась слаба.
     Тебя отчислили из универа,зато зато теперь ты довольный жизнью работник завода!""")