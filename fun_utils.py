import os 

command = "df -h"
command = "uptime"
command = "date" 

def check_cpu(command):
     print(os.system(command))

check_cpu("df -h")

def check_date(command):
    print(os.system(command))

check_date("date")

def check_uptime(command):
    print(os.system(command))

check_uptime("uptime")

def check_ram(command):
    print(os.system(command))

check_ram("df -h")

