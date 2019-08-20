import os
myCmd = "adduser celeryTaks && su celeryTaks && ./wait-for-it.sh www.google.com:80 -- echo 'google is up' "
os.system(myCmd)
