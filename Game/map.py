import copy

from Game.territory import terr
import random
total = 6


class Egyptmap:
    def __init__(self ):
        self.p1_terrs=[]
        self.p2_terrs=[]
        self.map_terrs= self.generate_map() ## All terr list
        self.random_map()

    def print_map ( self,list_of_terrs):
        # Printing shuffled list
        for i in range(len(list_of_terrs) ):
            print("The shuffled list is : " + str(list_of_terrs[i].terr_id))
    #list of terr objects

    def generate_map(self):
        terr1 = terr(1, None)
        terr3 = terr(2, None)
        terr2 = terr(3, None)
        terr4 = terr(4, None)
        terr5 = terr(5, None)
        terr6 = terr(6, None)

        terr1.add_neighbours([terr3, terr6])
        terr2.add_neighbours([terr4, terr6])
        terr3.add_neighbours([terr1, terr4])
        terr4.add_neighbours([terr3, terr2, terr6])
        terr5.add_neighbours([terr6])
        terr6.add_neighbours([terr1, terr2, terr4, terr5])
        list_of_terrs = [terr1, terr2, terr3, terr4, terr5, terr6]
        return list_of_terrs

    def random_map(self):
        ##generate random number of terr to player 1
        ## form [ 2-5]
        player1_terr_count= random.randint(2,4)
        player2_terr_count=total - player1_terr_count

#   shuffling the list in order to distribute the terrs among the players
        for i in range(len(self.map_terrs) - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i)
            # Swap arr[i] with the element at random index
            self.map_terrs[i], self.map_terrs[j] = self.map_terrs[j], self.map_terrs[i]
        #Distribute the terrs among player1 and player2
        #loop ( 0 to player1_terr_count - 1)
        for p1 in range(player1_terr_count):
            self.p1_terrs.append(copy.deepcopy(self.map_terrs[p1]))
    # loop ( player1_terr_count to end)
        for p2 in range(player1_terr_count,len(self.map_terrs),1):
            self.p2_terrs.append(self.map_terrs[p2])





