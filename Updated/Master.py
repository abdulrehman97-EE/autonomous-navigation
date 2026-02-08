import subprocess

p = subprocess.Popen(['roslaunch','p3dx_navigation','Run.launch'])
try:
    p.wait()
except KeyboardInterrupt:
    try:
       p.terminate()
    except OSError:
       pass
    p.wait()

