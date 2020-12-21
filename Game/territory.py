
class terr:
    def __init__(self, terr_id, neighbours):
        self.terr_id = terr_id
        self.neighbours = neighbours#list
        self.army = 0
    def add_neighbours(self,neighbours_list):
        self.neighbours=neighbours_list
