class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def next(self):
        ret=self.i
        self.i +=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret
for i in myrange(5):
    print(i)
    