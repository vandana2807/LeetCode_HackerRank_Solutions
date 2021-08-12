

import fileinput
class TradeRec:
    def __init__(self):
        self.l1=[]
    def process(self,lin:str)->str:
        s=lin.split(",")
        #print(s)
        if lin[0]!='R':
            self.l1.append(s)
            #print(",,",self.l1)
            return s[2]
            
        else:
            a=[]
            b=[]
            #print(self.l1)
            for i in self.l1:
                #print(i)
                #print(i[0],s[1])
                if i[0]==s[1].strip():
                    a.append(i)
                    #print(a)
                else:
                    b.append(i)
            if (len(a)>0 and len(b)==0) or (len(a)==0 and len(b)>0):
                #print(len(a))
                return len(a)
            else:
                c=0
                for i in a:
                    for j in b:
                        if i[1]==j[1] and i[2]==j[2] and i[3]==j[3]:
                            c+=1
                #print(len(a)-c)
                return len(a)-c
            
if __name__=="__main__":
    rec=TradeRec()
    for line in l:
        cleaned_line=line.replace("\n", "")
        print(cleaned_line)
        print(rec.process(cleaned_line))
