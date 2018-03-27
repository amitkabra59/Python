class Person:
    nop=0
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
        Person.nop=+1

    def info(self):
        print "Name is %s and Number is %d"%(self.name,self.phno)

    def count(self):
        print Person.nop
obj1=Person("amit",99999)
obj2=Person("kabra",123456)
obj1.info()
obj2.info()

obj2.count()
#print getattr(obj1,'name')
