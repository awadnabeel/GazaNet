from ping3 import ping, verbose_ping
time = ping('172.16.111.110')  # Returns delay in seconds.
print(time)