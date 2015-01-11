class Student(object):

    def __init__(self, firstName, lastName, year, gpa):
        self.firstName = firstName
        self.lastName = lastName
        self.year = year
        self.hw_scores = []
        self.test_scores = []
        self.gpa = gpa

    def add_hw_score(self, hw_score):
        self.hw_scores.append(hw_score)

    def add_test_score(self, test_score):
        self.test_scores.append(test_score)

    def compute_hw_avg(self, hw_scores):
        hw_avg = sum(hw_scores)/len(hw_scores)
        return hw_avg
    
    def compute_test_avg(self, test_scores):
        test_avg = sum(test_scores)/len(test_scores)
        return test_avg

    #TODO
    #def compute_gpa()

class Course(object):

    def __init__(self, name, instructor, credits):
        self.name = name
        self.instructor = instructor
        self.credits = credits

    def change_instructor(self, new_instructor):
        self.instructor = new_instructor
        return new_instructor


if __name__ == "__main__":
    sean = Student('Sean', 'Perkins', 'Senior', 0.0)
    sean.add_hw_score(90)
    sean.add_hw_score(80)
    print sean.compute_hw_avg(sean.hw_scores)
    history = Course('History', 'Professor X', 3.0)
    print sean.firstName
    print history.instructor
       

