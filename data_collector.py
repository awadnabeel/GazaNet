from __future__ import print_function
from ping3 import ping, verbose_ping
import threading
import dbutils
import logging
import re
import requests

_LOGGER = logging.getLogger(__name__)

HTTP_HEADER_X_REQUESTED_WITH = 'X-Requested-With'
HTTP_HEADER_NO_CACHE = 'no-cache'

class DataCollector() :
    result = ''
    def __init__(self,ip_range,start_ip,end_ip,username,password,timeout) :
        for host in range(start_ip,end_ip+1) :
            ip = ip_range+'.'+ str(host)
            thrd = threading.Thread(target=self.count_clients,args=(ip,username,password,timeout))
            thrd.start()
    def count_clients(self,ip,username,password,timeout) :
        result = []
        try:
            ping_time  =  ping(ip) * 1000
            if (ping_time is not None ):
                # TO DO  store ping time
                page = requests.get('http://'+ip, auth=(username,password),timeout=int(timeout))
                # print(page.text)
                parse_macs_hyphens = re.compile('xx:xx:xx:xx:[0-9A-F]{2}:[0-9A-F]{2}')
                result = parse_macs_hyphens.findall(page.text)
                ssid = ''
                for line in page.text.split('\n'):
                    if line.__contains__('ssid') :
                        for (i ,word)   in enumerate(line.split('</div>')) :
                            if i == 2 :
                                ssid = str(word).split('&')[0]
                                # print (time+';'+ip + ';' + str(word).split('&')[0] + ';' + str(len(result)))
                                client_count = len(result)
                page2 = requests.get('http://'+ip+'/Status_Router.asp', auth=(username,password),timeout=int(timeout))
                for line in page2.text.split('\n'):
                    if line.__contains__('<span id="uptime">'):
                        uptime = line.split('<span id="uptime">')[1].split('up ')[1].split(',  load')[0]
                        uptime_days = uptime.split(',')[0].split('days')[0].strip()
                        uptime_hr = uptime.split(',')[1].split(':')[0].strip()
                        uptime_min = uptime.split(',')[1].split(':')[1].strip()
                        print(uptime_days+' d '+uptime_hr+':'+uptime_min)
                        uptime = uptime_days+' d '+uptime_hr+':'+uptime_min
                        try:
                            uptime_hours = int(uptime_days)*24 + int(uptime_hr)
                            print(uptime_hours)
                        except:
                            uptime_hours = int(uptime_hr)
                            print(uptime_hours)


                print(ip,ping_time, ssid, client_count,uptime)
                dbutils.DB.insert(ip,ping_time,ssid, client_count,uptime,uptime_hours)
            else:
                dbutils.DB.insert(ip,ping_time,None, 0,None,0)
                print(ip ,'is not reachable')
        except :
                result += ip + ';;'
                print(ip + ';;')

    # --------------------------------------
    #| ip  |   ssid   | username | password |
    # --------------------------------------
