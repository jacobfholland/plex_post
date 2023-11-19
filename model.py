from .printable import Printable


class Model(Printable):
    def __init__(self, data) -> None:
        for k, v in data.items():
            setattr(self, k, v)


class Metadata(Model):
    def __init__(self, data) -> None:
        key_class_mapping = {
            "Genre": Genre, "Country": Country, "Guid": Guid,
            "Rating": Rating, "Director": Director, "Writer": Writer,
            "Role": Role, "Producer": Producer, "Field": Field,
            "Mood": Mood, "Collection": Collection
        }
        for key, cls in key_class_mapping.items():
            if key in data:
                processed_data = self.get_objs(data, key, cls)
                data[key.lower()] = processed_data
                del data[key]
        super().__init__(data)

    def get_objs(self, data, key, cls):
        objs = [cls(item) for item in data.get(key, [])]
        return objs


class Account(Model):
    pass


class Collection(Model):
    pass


class Server(Model):
    pass


class Player(Model):
    pass


class Guid(Model):
    pass


class Genre(Model):
    pass


class Country(Model):
    pass


class Guid(Model):
    pass


class Rating(Model):
    pass


class Director(Model):
    pass


class Writer(Model):
    pass


class Role(Model):
    pass


class Producer(Model):
    pass


class Field(Model):
    pass


class Mood(Model):
    pass
