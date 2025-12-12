from random import randint

class train:
    def __init__(self,trainNO):
        self.trainNO =trainNO

    def book(self,fro,to):
        print(f"the ticket is book in train NO{self.trainNO}")

    def getfare(self,fro,to):
        print(f"ticket fare in train no:{self.trainNO}from(fro)is {randint(222,9999)}")
    
    t=trainNO  (452020)
    t.book("bhadreak","bbsr")
    t.getfare("bhadreak","bbsr")