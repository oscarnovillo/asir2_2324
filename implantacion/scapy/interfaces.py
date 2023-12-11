import psutil,os

print("NIC info:")
print(psutil.net_if_stats())
for iface in psutil.net_if_stats():
    print(iface)

# os.system("ipconfig")
import subprocess
output = subprocess.check_output("ipconfig", shell=True)
for line in output.splitlines():
    if ("IPv4" in str(line)):
        print(str(line).split(":")[1].strip().split("'")[0])
