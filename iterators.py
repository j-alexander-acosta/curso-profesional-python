import time

class FiboIter():

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if self.counter <= self.max:
                self.counter += 1
                self.n3 = self.n1 + self.n2
                self.n1 = self.n2
                self.n2 = self.n3
                return self.n3
            else:
                raise StopIteration

if __name__ == "__main__":
    fibo = FiboIter(10)
    for i in fibo:
        print(i)
        time.sleep(0.5)
    print("Done")