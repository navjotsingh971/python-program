#!/usr/bin/python
#### loadbalancer by iptables for n number of apache server  #######
import requests
import time
import commands
number=int(raw_input("enter the no of server"))
p = list()
for x in range(number) :
     p.append(raw_input("enter the server's ip"))
#print len(p)
for i in range(len(p)):   
       r=requests.get("http://{0}".format(p[i]))
       code=r.status_code
       if (code==200):
              commands.getoutput("""iptables -t nat -A PREROUTING -p tcp -i virbr0 --dport 80 -m state --state NEW -m statistic --mode nth --every {0} --packet {1} -j DNAT --to-destination {2}:80""".format(number,i,p[i]))
       else :
          commands.getoutput("""iptables -t nat -D -A PREROUTING -p tcp -i virbr0 --dport 80 -m state --state NEW -m statistic --mode nth --every {0} --packet {1} -j DNAT --to-destination {2}:80""".format(number,i,p[i]))
       time.sleep(5)
       commands.getoutput("iptables -t nat -A POSTROUTING -j MASQUERADE")
