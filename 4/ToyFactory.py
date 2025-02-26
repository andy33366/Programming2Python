#ToyFactory class
from Toy import Toy

class ToyFactory:

    def __init__(self):
        #100 heads
        self.heads = 100
        #100 bodies
        self.bodies = 100
        #200 arms
        self.arms = 200
        #200 legs
        self.legs = 200
        #5 workers
        self.workers = 5
        #status message - blank
        self.message = ""

    def makeToy(self, name):
        #grabParts() --> if false print message
        #assemble() --> if false print message
        # if (grabParts() && assemble()):
        #   return Toy(name)
        #else:
        #   print message
        if (self.grabParts() and self.assemble()):
            return Toy(name)

    def grabParts(self):
        self.heads = self.heads - 1
        self.bodies = self.bodies - 1
        self.arms = self.arms - 2
        self.legs = self.legs - 2
        #-1 head
        #-1 body
        #-2 arms
        #-2 legs
        #return OOSCheck()
        return self.OOSCheck()
    

    def assemble(self):
        #-1 worker
        self.workers = self.workers - 1
        #return laborCheck()
        return self.laborCheck()

    def laborCheck(self):
        #if workers == 0 then set labor message && return false
        if self.workers == 0:
            self.message = "Not enough workers to make toy."
            return False
        else:
            return True

    def OOSCheck(self):
        #the factory is out of stock
        #if head or body of arms or legs == 0, then set message OOS, return false
        if (self.heads == 0 or self.bodies == 0 or self.arms ==0 or self.legs ==0):
            
            self.message = "Parts are out of stock."
            return False
        else:
            return True

    def getMessage(self):
        return self.message



