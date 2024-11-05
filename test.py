import abc


class Cars(abc.ABC):
    def __init__(self, body, wheels):
        self.body = body
        self.wheels = wheels

    def color(self, color: str = 'черный'):
        return f'Самый практичный цвет машины: {color}.'

    def fuel(self, fuel: str = 'бензин'):
        return f'Самое популярное топливо машины: {fuel}.'

    @abc.abstractmethod
    def body_type(self):
        pass

    @abc.abstractmethod
    def num_wheels(self):
        pass


class Toyota(Cars):
    def body_type(self):
        return f'Самый популярный тип кузова у Toyota: {self.body}.'

    def num_wheels(self):
        return f'Самый популярный размер шин у Toyota: {self.wheels} дюймов.'

    def from_county(self, country: str = 'Япония'):
        return f'Toyota произведена в стране: {country}.'


class Renault(Cars):
    def body_type(self):
        return f'Самый популярный тип кузова у Renault: {self.body}.'

    def num_wheels(self):
        return f'Самый популярный размер шин у Renault: {self.wheels} дюймов.'

    def engine(self, engine: str = 'K4M'):
        return f'Один из популярных двигателей Renault: {engine}.'


class Plain(abc.ABC):
    def __init__(self, country):
        self.country = country

    def color(self, color: str = 'белый'):
        return f'Самый частый цвет самолета: {color}.'

    def fuel(self, fuel: str = 'керосин'):
        return f'Самое популярное топливо самолета: {fuel}.'

    @abc.abstractmethod
    def from_county(self):
        pass


class Tupolev(Plain):
    def from_county(self):
        return f'Туполев произведен в стране: {self.country}.'

    def engine(self, engine: str = 'ПС-90А'):
        return f'Самолёт Туполев-204 оснащён российскими двигателями {engine}.'


class Boeing(Plain):
    def from_county(self):
        return f'Boeing произведен в стране: {self.country}.'

    def speed(self, speed: str = '852'):
        return f'Крейсерская скорость самолета Boeing 737-800 равна {speed} км/ч.'



tupolev = Tupolev('Россия')
print(tupolev.from_county())

boeing = Boeing('США')
print(boeing.speed(), boeing.color())

toyota = Toyota('седан', '15')
print(toyota.color(), toyota.num_wheels())

renault = Renault('универсал', '17')
print(renault.engine(), renault.num_wheels(), renault.color())

null_list = []
technique = [tupolev, boeing, toyota, renault]
for te in technique:
    null_list.append(te.fuel())
print(null_list)