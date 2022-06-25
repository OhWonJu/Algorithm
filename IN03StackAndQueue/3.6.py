## 동물 보호소 ##

from Queue import *


def Solution1():
    class AnimalShelter:
        def __init__(self):
            self.cats = Queue()
            self.dogs = Queue()
            self.timeStemp = 0

        def enqueue(self, types):
            if(types != "dog" and types != "cat"):
                return
            if(types == "dog"):
                self.dogs.add(self.timeStemp)
            elif(types == "cat"):
                self.cats.add(self.timeStemp)
            self.timeStemp += 1

        def dequeueAny(self):
            dog = self.dogs.peek()
            cat = self.cats.peek()
            return self.dogs.remove() if dog.data < cat.data else self.cats.remove()

        def dequeueDog(self):
            return self.dogs.remove()

        def dequeueCat(self):
            return self.cats.remove()

        def printAll(self):
            print("dogs shelter___")
            self.dogs.printQueue()
            print("cats shelter___")
            self.cats.printQueue()

    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.printAll()
    print("+++++++++++++++++++++++")

    shelter.dequeueAny()
    shelter.printAll()
    shelter.dequeueAny()
    shelter.printAll()
    shelter.dequeueAny()
    shelter.printAll()
    shelter.dequeueAny()
    shelter.printAll()
  

if __name__ == "__main__":
    Solution1()
