import Data_Cleaning
import Messageset
import re
def get_set(PATH):
    l = Data_Cleaning.QQcleaner(PATH)
    res=[]
    for x in l:
        if x.host=="" or re.search(r'.*系统消息.*', x.host) != None:
            continue
        T = []
        T.append(x)
        flag = 0
        for y in res:
            if y.number==x.number:
                flag=1
                y.Append(x)
                break
        if flag == 0:
            res.append(Messageset.MessageSet(T))
    return res
if __name__ == "__main__":
    a = get_set('C:/Users/kjx33/Desktop/jh.txt')
    for x in a:
        print(x.host,x.number)
        if x.host=="遥梦幽兰":
            for y in x.MessageList:
                print(y.Timer)
