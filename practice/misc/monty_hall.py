import random


class Monty:

    def simulate(self, switch:bool) -> int:

        sample_space = [0,1,2]
        room = ["goat","goat","goat"]

        # place the goat at random
        car_door = random.randint(0,2)
        room[car_door] = "car"

        # contenstant picks door
        contestant_door = random.randint(0,2)

        # host shows 1 door that has goat but not the same door as contestant 
        # [g, g, c] -> 2, host will only show 1,2
        # [g,g,c] -> 1, host will show only [0]

        host_door = [x for x in sample_space if x not in [car_door, contestant_door]][0]       

        # ask to switch
        if switch:
            contestant_door = [x for x in sample_space if x not in [host_door, contestant_door]][0]
        
        ans = 0
        if room[contestant_door]=="car":
            ans = 1
        
        return ans

N = 100000
count1 = count2 = 0
monty = Monty()
for _ in range(N):
    count1 += monty.simulate(switch = True)
    count2 += monty.simulate(switch = False)

print(count1/N, count2/N)