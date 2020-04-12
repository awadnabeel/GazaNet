import data_collector
import dbutils
import time
db = dbutils.DB()

while True:
    ip_ranges = db.get_ip_ranges()
    system_variables = db.get_system_variable()
    print(ip_ranges)
    for range in ip_ranges :
        network_part = str(range[0]).split('.')[0]+'.'+str(range[0]).split('.')[1]+'.'+str(range[0]).split('.')[2]
        start_ip = range[1]
        end_ip = range[2]
        # print(network_part,start_ip,end_ip)
        datacollector = data_collector.DataCollector(network_part,start_ip,end_ip, 'admin', 'gn123125', system_variables['timeout'])
        time.sleep(3)
    time.sleep(system_variables['timer'])
