import os
import threading

threadArr = []
with os.scandir("./profilerDump/") as dirObj:
    paths =  [i.name for i in dirObj] 


paths = [ i  for i in paths  if ".pstats" in i]
    


threadArr = [threading.Thread( os.system(f"snakeviz ./profilerDump/{path}")) for path in paths]


for start in threadArr:
    start.start()


for start in threadArr:
    start.join()

print("Done with the analysis")

