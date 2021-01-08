import Data_Standardization
import time
import re

def T(m):
    date=re.match(r'(.*)-(.*)-(.*) (.*):(.*):(.*)',m.Time)
    return (date)



def begin(Name):
    bq=0#表情
    qd=0#签到
    tp=0#图片
    daily=0#每天发言数
    a = Data_Standardization.get_set('C:/Users/kjx33/Desktop/22.txt')
    M=[]
    for x in a:
        if x.number==Name:
            print("亲爱的静海舰员",x.host,",以下是您的2020静海年度报告，请您查收。")
            M=x.MessageList
            break
    last=-1
    early=12*60*60
    for x in M:
        t=int(T(x).group(4))*60*60+int(T(x).group(5))*60+int(T(x).group(6))
        if t <6*60*60 and t>last:
            last=t
            last_t=x.Time
        if t>6*60*60 and t<early:
            early=t
            early_t = x.Time
        #print(x.text,x.Time,)
        T(x)
        if x.text=="[表情]":
            bq=bq+1
        if x.text=="[群签到]请使用新版QQ进行查看。":
            qd=qd+1
        if x.text=="[图片]":
            tp=tp+1
    daily=len(M)/365
    #print(last,early)
    #print(len(M),daily,bq,qd,tp,last_t,early_t)
    print("2020是非凡的一年，我们经历了一次百年未有之大变局。但还好，至少在静海，这里的温馨帮助我们度过了凛冽寒冬和炎炎夏日。")
    if daily>=1:
        print("今年，您在静海共计发布了",len(M),"条消息，平均每天发送了",daily,"条消息。感谢你的存在，让我们的大家庭热闹了起来。")
    else:
        print("今年，您在静海共计发布了", len(M), "条消息。在新的一年，也要继续加油水群呦！")
    if bq >20:
        print("在2020年，您共计发出表情",bq,"次，表情包达人就是你吧！")
    else:
        print("在2020年，您共计发出表情", bq, "次，发的表情有点少呢，果然是冷酷的高手嘛！")
    if qd >20:
        print("在2020年，您共计签到",qd,"次。看来您已经习惯了每日签到占卜吉凶！看到喜欢的结果不妨高兴高兴，如果看到不喜欢的结果，那就不要当真呦~")
    else:
        print("在2020年，您共计签到", qd, "次，可以再多试试每日签到呀！看到喜欢的结果不妨高兴高兴，如果看到不喜欢的结果，那就不要当真呦~！")
    if tp >20:
        print("在2020年，您共计发出图片或动图",tp,"次，在下擅自封您为斗图达人！！")
    else:
        print("在2020年，您共计发出图片或动图", tp, "次，不斗图装高冷，哼！~")
    if last!=-1:
        print("在",last_t,",您还在群里发消息。这么晚了还不睡觉，在聊什么呢呀？以后要少熬夜哦~")
    if early!=12*60*60:
        print("在",early_t,",您早早地就在群里发消息了。早起是自律的体现，在2021大家都要再继续加油！")
    print("以上就是您的2020静海年度报告啦！希望您在新的一年也能在这里和小伙伴们愉快玩耍。永远保持激情，永远追求进步空间，这是静海数十年以来的共识。虽然人员更换、新老交替，但是这个美好的初衷却深深地烙印在了每一个社员的心中。聚似一团火，散若满天星，擎着这份信念，坚持不懈，奋勇向前。静海动漫社，因热爱相聚。祝大家2021新年快乐！")
if __name__ == "__main__":
    begin("2241464644")


