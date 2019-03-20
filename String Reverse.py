class ster:
    def __init__(self,strin):
        self.strin = strin
    def strrev(self,strin):
        n = len(strin)
        strre = ''
        for i in range(n-1,-1,-1):
            strre = strre + strin[i]
        return strre
    def strcpy(self,strin):
        dummy = strin
        dummy = dummy + ' it is copied element.'
        print dummy

strin = raw_input()
s = ster(strin)
print (s.strrev(strin))
s.strcpy(strin)
