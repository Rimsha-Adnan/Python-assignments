import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You Won!"
    
    return 'You Lost!'
    
def is_win(player, oppenent):
    # return true if player win
    # r > s, s > p, p > r
    if (player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') \
        or (player == 'p' and oppenent == 'r'):
        return True
    
print(play())