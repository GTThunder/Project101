import random

class Question:
    def __init__(self, q, a1, a2, a3):
        self.__q = q
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3

    def get_q(self):
        return self.__q

    def set_q(self, q):
        self.__q = q

    def get_a1(self):
        return self.__a1

    def set_a1(self, a1):
        self.__a1 = a1

    def get_a2(self):
        return self.__a2

    def set_a2(self, a2):
        self.__a2 = a2

    def get_a3(self):
        return self.__a3

    def set_a3(self, a3):
        self.__a3 = a3


q1 = Question('Actions:', 'Give Seat to Elderly.', 'Pretend nothing is going on.', 'Call friend to give up seat.')
q2_1 = Question("Actions:", "Investigator", "","")
q2_2 = Question("Actions:", "Investigator", "","")
q2_3 = Question("Actions:", "Investigator", "","")

list1 = [q1.get_q(), q2_1.get_q(), q2_2.get_q(), q2_3.get_q(), ]
list2 = [q1.get_a1(), q1.get_a2(), q1.get_a3()]
list3 = [q1.get_a1(), q2_1.get_a1(), q2_2.get_a1(), q2_3.get_a1()]
Game = 1
for x in range(Game):
    print("Welcome to MrtGuide!")
    print("This is a game where every action will lead to different situations")
    name = input("Enter your name to start: ")
    print(name, "and his friend was in the mrt waiting for his friend to come")
    print("Upon arriving at Yio Chu Kang MRT, an elderly boarded the MRT however, there was no seats avaliable.")
    print(list1[0])
    print('1.{} 2.{} 3.{}'.format(list2[0], list2[1], list2[2]))
    while True:
        choice1 = input("Choice(1-3): ")
        if choice1 == 1:
            break
        elif choice1 == 2:
            break
        elif choice1 == 3:
            break
        else:
            print('Invalid Choice please try again:')



'''
i=0
s=0
while i<3:
    i+=1
    num = random.randint(0, 4)
    q = Quiz.questions[num]
    print(q.get_q())
    Answer = input("Answer: ")
    if Answer.upper() == q.get_a():
        s+=1
        print("Congratulations you are correct! Score: ", s)
    else:
        print("Orh oh Wrong Answer. Score: ", s)

print("Thanks for playing!")
'''