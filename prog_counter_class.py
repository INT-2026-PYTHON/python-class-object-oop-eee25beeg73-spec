class counter:
    total=0
    def __init__(self,name):
        self.name=name
        self.count=0
    def increment(self,step=1):
        self.count +=step
        counter.total +=step
    def reset(self):
        self.count=0
    def __str__(self):
        return (f"{self.name}:count={self.count}")
    def show_total():
        return counter.total
c1=counter('counter')
c2=counter('views')
c3=counter('downloads')
for i in range(3):
    c1.increment()
for i in range(5):
    c2.increment()
c3.increment(10)
c1.reset()
print(c1)
print(c2)
print(c3)
