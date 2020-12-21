
from Game.player import player
from Game.map import Egyptmap



class game:
    def __init__(self, map ):
        self.map=map
    ##def assign_terrs(self):


def main():

     my_map=Egyptmap()
     new_game = game(my_map)
  #   new_game.assign_terrs() here delete !!!!
     player1= player("Moh",new_game.map.p1_terrs,"Human")
     player2= player("Hima",new_game.map.p2_terrs,"DES")
     for i in range(len(player1.my_terrs)):
        print("p1 list is : " + str(player1.my_terrs[i].terr_id))
     print("")

     for i in range(len(player2.my_terrs)):
         print("p2 list is : " + str(player2.my_terrs[i].terr_id))

     removed=player1.remove_terr(1)
     if not removed :
         print("******[not found]*****")
     else:
         player2.add_terr(removed)

     print("\n")
     for i in range(len(player1.my_terrs)):
        print("p1 list is : " + str(player1.my_terrs[i].terr_id))
     print("")

     for i in range(len(player2.my_terrs)):
         print("p2 list is : " + str(player2.my_terrs[i].terr_id))



if __name__ == "__main__":
    main()