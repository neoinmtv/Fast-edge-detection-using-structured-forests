import os
import sys
import subprocess
from subprocess import Popen
import re
import time

IN_DIR=sys.argv[1]
OUT_DIR=sys.argv[2]

cnt=0
for f in os.listdir(IN_DIR):
  outf = os.path.join(OUT_DIR, f)
  if os.path.exists(f):
    continue
  start_time = time.time()
  print('DIR={}, CNT={}'.format(IN_DIR, cnt))
  subprocess.call([ 'time', 'python3', '/home/neoinmtv/dev/memesearch/Fast-edge-detection-using-structured-forests/Edge_detection/Edge_detection.py', IN_DIR, f, outf])
  et = time.time() - start_time
  print('{:2d}min {:.2f}s'.format(int(et//60), round(et,2)))
  cnt+=1
  #if cnt>=2: 
  #  break


