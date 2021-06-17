import os
import time

while (1):
    if (time.localtime().tm_min) == 59 and time.localtime().tm_sec == 30:
        os.system(r"G:\MyProject\notifier.vbs")