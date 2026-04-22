class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            grade = "A"
        elif body >= 80 and body < 90:
            grade = "B"
        elif body >= 70 and body < 80:
            grade = "C"
        elif body >= 60 and body < 70:
            grade = "D"
        elif body >= 50 and body < 60:
            grade = "E"
        elif body < 50:
            grade = "F"
        return grade

    def find(self, body):
        najdene_indexy = []
        for j, i in enumerate(self.scores):
            if i == body:
                najdene_indexy.append(j)
        return najdene_indexy

    def get_sorted(self):
        scores = list(self.scores)
        for j in range(len(scores)):
            for i in range(len(scores) - j - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
        return scores



# results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
# print(results.get_grade(2))  # A (91 bodů)
# print(results.get_grade(6))  # A (100 bodů)
# print(results.get_grade(7))  # F (38 bodů)
# print(results.find(100))  # [6]
# print(results.find(50))   # [4]
# print(results.find(77))   # []
# print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
# print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"pocet student: {results.count()}")
    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")
    print(f"Student {results.find(100)} mel plny pocet")
    print(f"serazene vysledky: {results.get_sorted()}")




main()
