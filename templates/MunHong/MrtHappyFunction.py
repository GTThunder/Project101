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

q1 = Question('Actions:', 'Give Seat to Elderly.', 'Pretend that you saw nothing.', '')
q2 = Question("Actions:", "Post on facebook", "Move in and notify others there are more space inside.", "Do nothing.")
q3 = Question("Actions:", "", "", "Get friend to check if elderly woman is ok.")
q4 = Question("Actions:", "Investigator", "","")

questionList = [q1.get_q(), q2.get_q(), q3.get_q(), q4.get_q()]
choice1List = [q1.get_a1(), q1.get_a2(), q1.get_a3()]
choice2List = [q2.get_a1(), q2.get_a2(), q2.get_a3()]
choice3List = [q3.get_a1(), q3.get_a2(), q3.get_a3()]
choice4List = [q4.get_a1(), q4.get_a2(), q4.get_a3()]
Game = 1
Score = 0
for x in range(Game):
    print("Welcome to MrtGuide!")
    print("This is a game to educate on what we should do in the MRT")
    name = input("Enter your name to start: ")
    print("Q1) You and your friend was in the mrt waiting for his friend to come")
    print("Upon arriving at Yio Chu Kang MRT, an elderly woman boarded the MRT however, there was no seats avaliable.")
    print("But by chance, you have a seat avaliable. What should you do?")
    print(questionList[0])
    print('1.{} 2.{} 3.{}'.format(choice1List[0], choice1List[1], choice1List[2]))
    choice1 = int(input("Choice(1-3): "))
    if choice1 == 1:
        Score+=1
        print("Congratulations that is a right move to make.")
        print("Score: ", Score)
        print("By allowing the eldery to have a seat it minimises the chance of them")
        print("injuring themselves, example if the Mrt suddenly stops they may fall and")
        print("take a long while to recover.")
    elif choice1 == 2:
        print("Orh Oh Wrong Answer.")
        print("Score: ", Score)
        print("By allowing the eldery to have a seat it minimises the chance of them")
        print("injuring themselves, example if the Mrt suddenly stops they may fall and")
        print("take a long while to recover.")
    elif choice1 == 3:
        print("Orh Oh Wrong Answer.")
        print("Score: ", Score)
        print("By allowing the eldery to have a seat it minimises the chance of them")
        print("injuring themselves, example if the Mrt suddenly stops they may fall and")
        print("take a long while to recover.")
    print("Q2) You are in the MRT during Peak hours but on the stop Serangoon people come in and not everyone could fit")
    print("But behind there are still many spaces behind you. What should you do?")
    print(questionList[1])
    print('1.{} 2.{} 3.{}'.format(choice2List[0], choice2List[1], choice2List[2]))
    choice2 = int(input("Choice(1-3): "))
    if choice2 == 1:
        Score+=1
        print("Orh Oh Wrong Answer.")
        print("Score: ", Score)
        print("If you had stepped in and help everyone would have been able to fit into the MRT.")
        print("It is important to put yourself into others shoes to consider about their feelings.")
    elif choice2 == 2:
        Score += 1
        print("Congratulations that is a right move to make.")
        print("Score: ", Score)
        print("By doins so everyone was able to fit into the MRT and reach their destinations in time")
    elif choice2 == 3:
        print("Orh Oh Wrong Answer.")
        print("Score: ", Score)
        print("If you had stepped in and help everyone would have been able to fit into the MRT.")
        print("It is important to put yourself into others shoes to consider about their feelings.")
    print("Q3) You are in a crowded Mrt your bad is very big and keeps touching others.")
    print("What should you do?")
    print(questionList[2])
    print('1.{} 2.{} 3.{}'.format(choice2List[0], choice2List[1], choice2List[2]))
