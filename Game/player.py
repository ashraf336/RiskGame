class player:
    def __init__(self, name, my_terrs,type):
        self.name = name
        self.my_terrs = my_terrs
        self.type = type

    def add_terr(self, terr):
        self.my_terrs.append(terr)


    def remove_terr(self,id):
        removed_terr = None
        for i in range (len(self.my_terrs)):
            if self.my_terrs[i].terr_id == id:
                removed_terr=self.my_terrs.pop(i)
                return removed_terr

        return removed_terr

# def get_terr(self,id):
    #    for i in range (len(self.my_terrs)):