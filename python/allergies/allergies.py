class Allergies:
    # 1   1  1  1   1  1  1  1
    # 128 64 32 16  8  4  2  1
    ITEMS={"eggs":1,"peanuts":2,"shellfish":4,"strawberries":8,"tomatoes":16,"chocolate":32,"pollen":64,"cats":128}
    def __init__(self, score):
        self.score=score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return [key_ for key_,value_ in Allergies.ITEMS.items() if self.score & value_]

