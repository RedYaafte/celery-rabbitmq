# import os
# myCmd = "docker exec -it dcr bash"
# myCelery = "celery -A tasks worker --loglevel=info"
# os.system(myCmd, myCelery)


import subprocess
MyOut = subprocess.Popen(['ls', '-l', '.'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
stdout, stderr = MyOut.communicate()
print(stdout)
print(stderr)
