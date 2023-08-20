class Animal():
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec


class AnimalFactory:

    def __init__(self, animal_type, *args, **kwargs):
        self.animal_type = animal_type
        self.args = args
        self.kwargs = kwargs

    def create(self):
        if self.animal_type == 'Fishes':
            animal = Fishes(*self.args, **self.kwargs)
        elif self.animal_type == 'Birds':
            animal = Birds(*self.args, **self.kwargs)
        elif self.animal_type == 'Mammals':
            animal = Mammals(*self.args, **self.kwargs)
        else:
            raise ValueError(f'Invalid animal type: {self.animal_type}')
        return animal


factory = AnimalFactory('Fishes', 'Карась', 'Федя', 1, 15)
fish = factory.create()

print(fish.get_kind(), fish.get_name(), fish.get_age(), fish.get_specific())
