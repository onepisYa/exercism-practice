import numpy as np
import pandas as pd


class Garden:
    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]
    FLOWERS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=STUDENTS):
        diagram = diagram.split()
        a = diagram[0]
        b = diagram[1]

        # method 1
        # flowers = zip(*[iter(a)] * 2 + [iter(b)] * 2)
        # self.cups = dict(zip(sorted(students), flowers))

        # method 2
        dd = np.array(list(a))
        ee = np.array(list(b))
        ddd = dd.reshape(dd.size // 2, 2)
        eee = ee.reshape(ee.size // 2, 2)
        flowers = np.hstack((ddd, eee))
        self.cups = dict(zip(sorted(students), flowers))

    def plants(self, who):
        # method 1
        df = pd.DataFrame(self.FLOWERS, index=["flowers"])
        return list(df.loc["flowers", list(self.cups[who])])
        # method 2
        return list(map(self.FLOWERS.get, self.cups[who]))
