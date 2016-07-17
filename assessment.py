"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

The three main design advantages that object orientation provides are:
1) Encapsulation:
    This allows data to live closer to its functionality.  Another way to
    explain that would be to say the data and the functions that manipulate
    the data are kept safe from outside interference.  This allows the 
    values or state of a structured data object inside a class to be hidden.

2) Abstraction:
    In abstraction a method can be utilized without knowing the information
    that method uses internally.  This allows the programmer to hide all but
    the relevant data about an object so complexity is reduced and efficiency
    is increased.

3) Inheritance:
    This allows for different and interchangeable types.  The benefit of
    inheritance is specifiying implementation of same behavior and allows
    for code reuse.  Inheritance can also be used in a single or multiple
    fashion allowing for hierarchical and hybrid inhertance types.

2. What is a class?
    A class is a type of thing.  This is a broad definition for the methods 
    and variables that are particular to a kind of object.  The object is
    a specific instance of a class; meaning the class contains real values
    instead of variables.

3. What is an instance attribute?
    An instance attribute is a specific instance of a class 
    containing real values.

4. What is a method?
    A method is a function (a set of instructions, procedure) defined 
    on a class.

5. What is an instance in object orientation?
    An instance is an individual instance of a class.  This means that
    there is creation of a realized instance (instantiation).  The
    instance attributes are realized upon instantiation.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is inherent to that class and does not change upon
   instantiation unless otherwise specified.  An instance attribute is
   an attribute that is given upon instantiation of the object.

   A class attribute would be utilized for a shared trait all potential
   child classes may utilize or an attribute that would be static for all 
   instantiations of that class.


"""

#PART 2:
#1:

# class Student(object):
#     def __init__(self, first_name, last_name, address):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address


#2:

# class Question(object):
#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer



#3:

# class Exam(object):
#     def __init__(self, name):
#         self.name = name
#         self.question = []


#PART 3:

#1:

# class Exam(Question):
#     def __init__(self, name):
#         self.name = name
#         self.question = []

#     def add_question(self, new_question, correct_answer):
#         self.new_question = new_question
#         self.correct_answer = correct_answer
#         self.question.append(new_question)


#2:
class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print_question(self):
        print self.question
        ask_and_evaluate = raw_input('>>>')
        if ask_and_evaluate == self.answer:
            return True
        else:
            return False


#3:

class Exam(Question):
    def __init__(self, name):
        self.name = name
        self.question = []

    def add_question(self, new_question, answer):
        self.new_question = new_question
        self.answer = answer
        self.question.append(new_question)
        

    def administer(self):
        self.score = 0
        correct_answer = self.print_question()
        if correct_answer == True:
            self.score += 1
        else:
            self.score -= 1

        return self.score


#PART 4:

#1:
def take_test(exam, student):
    exam = Exam(student)
    exam.add_question("What color is the sky?", "Blue")
    score = exam.administer()
    print score

#2:
def example(exam, student):
    exam = Exam(student)
    exam.add_question("What color is the sky?", "Blue")
    exam.add_question("What is 3 + 4", "7")
    exam.add_question("""What is the average air speed velocity of a laden swallow?""", "24mph")
    exam.administer()


#PART 5:






