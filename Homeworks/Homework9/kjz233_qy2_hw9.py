
import random
class Die:
    def __init__(self,face=6):
        self.number_of_faces = face
        self.curr_face_value = random.randint(1,6)
    def __repr__(self):
        return self.curr_face_value
    def roll(self):
        self.curr_face_value = random.randint(1,6)
        return (self.curr_face_value)

class PigGamePlayer:
    def __init__(self,name):
        self.name = name
        self.die = Die()
        self.score = 0
    def play_turn(self):
        self.die.roll()
        roll = self.die.roll()
        print("You rolled",roll)
        return roll

class PigGame:
    def __init__(self,player1_name,player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
    def play(self):
        pigPlay1 = PigGamePlayer(self.player1_name)
        pigPlay2 = PigGamePlayer(self.player2_name)
        turnScore1 = 0
        totalScore1 = 0
        turnScore2 = 0
        totalScore2 = 0
        while totalScore1 <= 100 and totalScore2 <= 100:
            print()
            print(self.player1_name+"'s turn:")
            roll1 = (pigPlay1.play_turn())
            turnScore1 += roll1
            if roll1 == 1:
                turnScore1 = 0
                print("You scored", turnScore1, "points this turn. Your total score is", totalScore1)
            else:
                print("Your score for this turn is:", turnScore1)
                choice = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                while choice == "r" and totalScore1 <= 100 and totalScore2 <= 100 and roll1 != 1:
                    roll1 = pigPlay1.play_turn()
                    turnScore1 += roll1
                    if roll1 == 1:
                        turnScore1 = 0
                        break
                    print("Your score for this turn is:", turnScore1)
                    choice = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                totalScore1 += turnScore1
                print("You scored",turnScore1,"points this turn. Your total score is",totalScore1)
                if totalScore1 >= 100:
                    print(self.player1_name,"won!")
                    return
                turnScore1 = 0
                #print(totalScore1)
            print()
            print(self.player2_name+"'s turn:")
            roll2 = pigPlay2.play_turn()
            turnScore2 += roll2
            if roll2 == 1:
                turnScore2 = 0
                print("You scored", turnScore2, "points this turn. Your total score is", totalScore2)
            else:
                print("Your score for this turn is:", turnScore2)
                choice = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                while choice == "r" and totalScore1 <= 100 and totalScore2 <= 100 and roll2 != 1:
                    roll2 = pigPlay2.play_turn()
                    turnScore2 += roll2
                    if roll2 == 1:
                        turnScore2 = 0
                        break
                    print("Your score for this turn is:", turnScore2)
                    choice = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                totalScore2 += turnScore2
                print("You scored", turnScore2, "points this turn. Your total score is", totalScore2)
                turnScore2 = 0
                if totalScore2 >= 100:
                    print()
                    print(self.player2_name,"won!")
                #print(totalScore2)
def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1,name2)
    game1.play()

main()