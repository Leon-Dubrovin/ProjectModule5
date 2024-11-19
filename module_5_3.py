class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей:  {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors != other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors >= other
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        return self + value
    def __iadd__(self, value):
        return self + value
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for n_floor in range(1, new_floor + 1):
                print(n_floor)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print('h1 == h2', h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print('h1 == h2', h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print('h1 > h2', h1 > h2) # __gt__
print('h1 > 20', h1 > 20)
print('h1 >= h2', h1 >= h2) # __ge__
print('h1 >= 30', h1 >= 30)
print('h1 < h2', h1 < h2) # __lt__
print('10 < h2', 10 < h2)
print('h1 <= h2', h1 <= h2) # __le__
print('30.1 <= h2', 30.1 <= h2)
print('h1 != h2', h1 != h2) # __ne__
print('h1 != 21.5', h1 != 21.5)