class PartyAnimal:
    x = 0
    name = ''
    def __init__(self,name,x):
        self.x = self.x + x
        self.name = name

    def party(self,x):
        self.x = self.x+x
        print('as of now',self.x)

#    def __del__(self):
    #    print("am done")


class cricketer(PartyAnimal):

    runs = 0
    #def __init__(self,runs):
    #    self.runs = self.runs + runs

    def score(self):
        print('runs scored',self.runs)
        print('x = ',self.x)   # here x gets 0 cause this is another copy of x for cricketer class so x will be 0
        print('name',self.name) #here also same x will be 0
ob = PartyAnimal('me1',22)
ob.party(10)
ob.party(10)
ob = 5
#ob.party(20)#error here

nn = cricketer('ohh',40)           #see if u dont have ur own constructor then ur parent constructor will be called
nn.score()
print(dir(nn))
