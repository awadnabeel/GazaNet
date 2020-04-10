import mysql.connector

hostname = 'localhost'
username = 'root'#'data_collector'
password = 'P@lestine' #'dc_password'
database = 'gnet'

# Simple routine to run a query on a database and print the results:
class DB:

    def get_ip_ranges(self) :
        myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
        cur = myConnection.cursor()
        cur.execute( "SELECT network_ip , start_ip , end_ip FROM ch_ip_ranges" )
        ranges = []
        for network_ip , start_ip , end_ip  in cur.fetchall() :
            ranges.append([network_ip , start_ip , end_ip])
            # print( network_ip , start_ip , end_ip  )
        return ranges

    # def __init__(self):
    #     try :
    #         self.myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
    #     # doQuery( myConnection )
    #     # myConnection.close()
    #         print ("connection started…")
    #     except :
    #         print("connection failed…")

    @staticmethod
    def insert(ip,ssid,count,uptime,uptime_hours) :
        myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
        cur = myConnection.cursor()

        sql = "INSERT INTO ch_outputs (ip ,ssid, client_count,uptime,uptime_hours) VALUES" \
              " ('"+ip+"','"+ssid+"',"+str(count)+",'"+uptime+"'"+","+str(uptime_hours)+")"
        cur.execute(sql)
        myConnection.commit()
