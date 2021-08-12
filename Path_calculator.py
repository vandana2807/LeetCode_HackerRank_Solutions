ip=["CHI:NYC:719",
"NYC:LA:2414",
"NYC:SEATTLE:2448",
"NYC:HAWAII:4924"]

class PathCalculator:
    def __init__(self):
        self.di = dict()
    def process(self,s):
        t = s.split(":")
        #print(t)
        #y=0
        #self.di[(t[0], t[1])] = int(t[2])
        if len(self.di) == 0:
            self.di[(t[0], t[1])] = int(t[2])
            return None
        else:
            #y=0
            for i, j in self.di.items():
                ma = 0
                if t[0] in i:
                    if t[0]==i[0]:
                        y = i[1]
                    else:
                        y = i[0]
                    #print(ma, ma + j + int(t[2]))
                    ma = max(ma, ma + j + int(t[2]))
                    
                if t[1] in i:
                   
                    if t[1] == i[0]:
                        y = i[0]
                    else:
                        y = i[1]
                    
                    ma = max(ma, ma + j + int(t[2]))
                    #print(ma)
        #print(ma)

        
        self.di[(t[0], t[1])] = int(t[2])
        A, B = sorted([y, t[1]])
        #print(":".join([str(ma),A,t[0],B]))
        return ":".join([str(ma),A,t[0],B])

if __name__=="__main__":
    rec=PathCalculator()
    for line in ip:
        print(rec.process(line))
