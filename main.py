import data_collector
import dbutils
import time
db = dbutils.DB()

while True:
    ip_ranges = db.get_ip_ranges()
    # ip_ranges = [['172.16.1.0',1,254],['172.16.3.0',1,254],
    #              ['172.16.4.0',1,254],['172.16.109.0',1,254],
    #              ['172.16.110.0',1,254],['172.16.111.0',1,254]]
    system_variables = db.get_system_variable()
    # system_variables = {'timeout':10 , 'timer':1}
    print(ip_ranges)
    for range in ip_ranges :
        network_part = str(range[0]).split('.')[0]+'.'+str(range[0]).split('.')[1]+'.'+str(range[0]).split('.')[2]
        start_ip = range[1]
        end_ip = range[2]
        # print(network_part,start_ip,end_ip)
        datacollector = data_collector.DataCollector(network_part,start_ip,end_ip, 'admin', 'gn123125', int(system_variables['timeout']))
        time.sleep(3)
    time.sleep(int(system_variables['timer']) * 60 )
