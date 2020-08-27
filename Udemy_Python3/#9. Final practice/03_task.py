# Разработать функцию sweetest_icecream,
# которая принимается список инстанций класса IceCream
# и возвращает "уровень сладости" самого сладкого мороженого.
# "Уровень сладости" складывается из ароматизатора и количества посыпок.
# Сладость одной посыпки = 1, а сладость ароматизаторов считается по таблице:
#   Plain = 0
#   Vanilla = 5
#   ChocolateChip = 5
#   Strawberry = 10
#   Chocolate = 10
# В функцию будут передаваться два аргумента: ароматизатор (как строка) и кол-во посыпок.
flavors = {
    'Plain': 0,
    'Vanilla': 5,
    'ChocolateChip': 5,
    'Strawberry': 10,
    'Chocolate': 10
}


class IceCream:

    def __init__(self, flavor: str, sprinkles: int):
        self.flavor = flavor
        self.sprinkles = sprinkles

    def sweetest(self):
        return flavors[self.flavor] + self.sprinkles


def sweetest_icecream(lst):
    # result = []
    # for _ in lst:
    #     result.append(_.sweetest())
    # return max(result)
    return max([_.sweetest() for _ in lst])

def sweetest_icecream_test():
    print(f'Te test of the function sweetest_icecream begin...')
    print('#Test 1 was successful.' if sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) == 23 else '#Test 1 failed.')
    print('#Test 2 was successful.' if sweetest_icecream([ice3, ice1]) == 23 else '#Test 2 failed.')
    print('#Test 3 was successful.' if sweetest_icecream([ice3, ice5]) == 17 else '#Test 3 failed.')
    print('#Test 4 was successful.' if sweetest_icecream([ice2, ice3, ice4, ice5]) == 18 else '#Test 4 failed.')


ice1 = IceCream('Chocolate', 13)
ice2 = IceCream('Vanilla', 0)
ice3 = IceCream('Strawberry', 7)
ice4 = IceCream('Plain', 18)
ice5 = IceCream('ChocolateChip', 3)

if __name__ == '__main__':
    sweetest_icecream_test()
