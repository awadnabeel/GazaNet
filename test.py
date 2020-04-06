from __future__ import print_function

import sys
import time
import threading
import base64
from datetime import datetime
import hashlib
import logging
import re
from aiohttp.hdrs import (
    ACCEPT, COOKIE, PRAGMA, REFERER, CONNECTION, KEEP_ALIVE, USER_AGENT,
    CONTENT_TYPE, CACHE_CONTROL, ACCEPT_ENCODING, ACCEPT_LANGUAGE)
import requests

_LOGGER = logging.getLogger(__name__)

HTTP_HEADER_X_REQUESTED_WITH = 'X-Requested-With'
HTTP_HEADER_NO_CACHE = 'no-cache'

ip_range = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
def count_clients(ip) :
    try:
        # print(url)
        page = requests.get('http://'+ip, auth=(username,password),timeout=5)
        #print(page.text)
        parse_macs_hyphens = re.compile('xx:xx:xx:xx:[0-9A-F]{2}:[0-9A-F]{2}')
        result = parse_macs_hyphens.findall(page.text)

        for line in page.text.split('\n'):
            if line.__contains__('ssid') :
                for (i ,word)   in enumerate(line.split('</div>')) :
                    if i == 2 :
                        print (ip + ';' + str(word).split('&')[0] + ';' + str(len(result)))
    except :
        print(ip + ';;')


for host in range(1,255) :
    ip = ip_range+'.'+ str(host)
    thrd = threading.Thread(target=count_clients,args=(ip,))
    thrd.start()
# --------------------------------------
#| ip  |   ssid   | username | password |
# --------------------------------------
