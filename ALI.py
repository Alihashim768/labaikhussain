import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from ALI import alibuy
    alibuy()
elif bit == '32bit':
    from ALI32 import alibuy
    alibuy()
