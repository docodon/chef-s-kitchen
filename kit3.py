
from lxml import html
import time

def get_list_contest() :

    url='http://www.codechef.com/contests'   
    b=html.parse(url)

    cnt_name=b.xpath(".//*[@id='statusdiv']/table//tr/td/a/text()")  
    data=b.xpath(".//*[@id='statusdiv']/table//tr/td/text()")

    fcnt=[]   #future contest
    pcnt=[]   #present contest

    crnt_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


    for i in range(0,len(data),3) :
        lst=[]
        lst.append(data[i])
        lst.append(cnt_name[int(i/3)])
        lst.append(time.strptime(data[i+1],'%Y-%m-%d %H:%M:%S'))  
        lst.append(time.strptime(data[i+2],'%Y-%m-%d %H:%M:%S'))
    
        if data[i+1]<=crnt_time and data[i+2]>crnt_time :
            pcnt.append(lst)
        elif data[i+1]>crnt_time :
            fcnt.append(lst)
        elif data[i+2]<crnt_time :
            break
     
    return fcnt,pcnt 
    #for i in fcnt :
     #  print(i[0],' ',i[1],' ',time.strftime('%Y-%m-%d %H:%M:%S',i[2]),' ',time.strftime('%Y-%m-%d %H:%M:%S',i[3]))

    #for i in pcnt :
     #   print(i[0],' ',i[1],' ',time.strftime('%Y-%m-%d %H:%M:%S',i[2]),' ',time.strftime('%Y-%m-%d %H:%M:%S',i[3]))


