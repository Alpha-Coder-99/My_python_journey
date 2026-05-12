# psutil ik python  module hn
# 🟢 1. Basic import
import psutil
# 🟢 2. CPU usage
print(psutil.cpu_percent())
# 🟢 3. RAM usage
print(psutil.virtual_memory().percent)
# 🟢 4. Battery (laptop)
print(psutil.sensors_battery())
# 🟢 5. Running processes (basic idea)
for p in psutil.process_iter():
    print(p.name())
