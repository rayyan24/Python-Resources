class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.seats=seats
        self.fare=fare
    def getInfo(self):
        print(f"The name of train is {self.name}")
        print(f"The fare of train is {self.fare}")
    def getSeatInfo(self):
        print(f"Number of seats are {self.seats}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"your seat has been booked your seat no is {self.seats}")
            self.seats=self.seats-1
        else:
            print("The train is full")
ExpressTrain=Train("Rajdhani",500,10)
ExpressTrain.getInfo()
ExpressTrain.getSeatInfo()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()
ExpressTrain.bookTicket()

