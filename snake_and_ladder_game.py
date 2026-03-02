# Snake and ladder game
import random
p1_current_score = 0
p2_current_score = 0
dice_roll = 0
snakes = {25:3, 42:1, 56:48, 61:43, 92:67, 95:12, 98:80}
ladders = {7:30, 16:33, 20:38, 36:83, 50:68, 63:81, 71:89, 86:97}
while p1_current_score < 100 and p2_current_score < 100: 
    dice_roll = random.choice(range(1,6))
    if p1_current_score in list(snakes.keys()):
        p1_current_score = snakes[p1_current_score]
    elif p1_current_score in list(ladders.keys()):
        p1_current_score = ladders[p1_current_score]
    else:
        p1_current_score = p1_current_score + dice_roll
    dice_roll = random.choice(range(1,6))
    if p2_current_score in list(snakes.keys()):
        p2_current_score = snakes[p2_current_score]
    elif p2_current_score in list(ladders.keys()):
        p2_current_score = ladders[p2_current_score]
    else:
        p2_current_score = p2_current_score + dice_roll            
    print("P1 current score: ", p1_current_score)
    print("P2 current score: ", p2_current_score)
if p1_current_score >= 100:
    print("P1 wins")
else:
    print("P2 wins")