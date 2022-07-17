# №1
def credit_card(card):
    return "************" + card[12:]


print(credit_card("1234567812345678"))


#№2

def palidrom(a):
    a = a.lower()
    # if len(a) <= 1:
    #     return True
    # if a[0] != a[-1]:
    #     return False
    # else:
    #     return palidrom(a[1:-1])

    sizeA = len(a) - 1
    for i in range(len(a)):
        if i >= sizeA - i:
            break
        if a[i] != a[sizeA - i]:
            return False

    return True

print(palidrom("шалаш"))
print(palidrom("Test"))


# №3
class Tomato:
    states = (1, 2, 3)
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grown(self):
        self._state += 1

    def is_ripe(self):
        return self._state >= Tomato.states[2]

class TomatoBush:
    def __init__(self, num: int):
        self.__tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for i in self.__tomatoes:
            i.grown()

    def all_are_ripe(self):
        for i in self.__tomatoes:
            if not i.is_ripe():
                return False
        else:
            return True

    def give_away_all(self):
        self.__tomatoes.clear()


class Gardener:
    def __init__(self, name, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("сбор урожая")
        else:
            print("Помидоры еще не созрели")

    @staticmethod
    def knowledge_base():
        print("посадите помидор, закрепите за ним садовника, заставляйте его работать пока помидор не созреет")


Gardener.knowledge_base()
gardener = Gardener("Nata", TomatoBush(5))
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
