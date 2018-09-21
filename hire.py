class Name:
    def __init__(self, name, color, price, time):
        self.name = name
        self.color = color
        self.price = price
        self.time = time

    def __str__(self):
        return f'марка машины: {self.name}, {self.color} ({self.price}) - {self.time}.'
        #     in self.dimension:
        #         return f'пицца: {self.name}. {self.ingredients} ({self.size}) {self.price}.'
        #     else:

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            #_item = Student(**item_dict)
            #_item = Teacher(**item_dict)
            items.append(_item)
        return items


class Driver(Name):

    def __init__(self, name, patronymic, experience, *args, **kwargs):
        self.name = name
        self.patronymic = patronymic
        self.experience = experience

    def __str__(self):
        if self.experience:
            return f'водитель: {self.name}, {self.patronymic} {self.experience}.'
        else:
            return f'водитель: {self.name}. {self.patronymic} ({self.experience}).'





