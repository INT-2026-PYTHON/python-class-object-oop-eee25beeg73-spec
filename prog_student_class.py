class student:
    def __init__(self,name,roll,mark=None):
        self.name=name
        self.roll=roll
        if mark is None :
            self.mark=[]
    def add_mark(self,mark):
        if mark<0 or mark>100:
            print("mark can't be greater then 100 or negative")
        else:
            self.mark.append(mark)
    def total(self):
        sum=0
        for i in self.mark:
            sum += i
        return sum
    def average(self):
        total=0
        if not self.mark:
           return 0
        else:
           count=0
           for i in self.mark:
               total=total+i
               count+=1
        average=total/count
        return average
    def grade(self):
        a=self.average()
        if a>=90:
            g= "A"
        elif a>=75 and a<90:
            g= "B"
        elif a>50 and a<75:
            g= "C"
        else:
            g= "F"
        return g
    def report(self):
        return (f"{self.name},{self.roll},{self.total()},{self.average()},{self.grade()}")
s1=student("Alice",101)
for m in [90,85,95]:
    s1.add_mark(m)
s2 =student("Bob", 102)
for m in [40, 55, 60]:
    s2.add_mark(m)
print(s1.report())
print(s2.report()) 
