import os

pid = os.fork()
if pid == 0:
    MAX_INT = 100000000000
    acum = 0
    for i in range(MAX_INT):
        acum += 1
else:
    print("Waiting for child")
    os.wait()
    