"""
Mason Blanford
Sept. 25, 2022
Imports statistics module to calculate mean, median, mode of student grades
"""

import statistics

class Student:                                      # pylint: disable = too-few-public-methods
    """Initializes student names and grades"""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        """Accesses private member grade"""
        return self._grade

def basic_stats(grades):
    """Calculates the mean, median, and mode of students' grades"""
    stats = []
    for score in grades:
        score = score.get_grade()
        stats.append(score)
    mean = statistics.mean(stats)
    median = statistics.median(stats)
    mode = statistics.mode(stats)
    return (mean, median, mode)

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))
