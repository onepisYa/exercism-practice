from operator import itemgetter


class School:
    def __init__(self):
        self.db = []

    def add_student(self, name, grade):
        self.db.append({"name": name, "grade": grade})

    def sort_db(functi):
        def funcin(self, *args):
            self.db = sorted(self.db,
                             key=itemgetter("grade", "name"),
                             reverse=False)
            return functi(self, *args)

        return funcin

    @sort_db
    def roster(self):
        return [i['name'] for i in self.db]

    @sort_db
    def grade(self, grade_number):
        return [
            i['name']
            for i in filter(lambda x: x['grade'] == grade_number, self.db)
        ]
