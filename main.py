import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper or 's' for scissors ")
    user = user.lower()

    computer = random.choice(['r','s','p'])

    if user == computer:
        return "You and the computer chose{}, so you tied".format(computer)

    # helper function
    if  is_win(user,computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user,computer)

    return "computer has chosen {} and you have chosen {}. Computer wins!".format(user,computer)

def is_win(player, opponent):
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True
    return False

if __name__ == '__main__':
    print(play())