import os

def main():
    if len(sys.argv) <= 1:
        print(f"usage: {sys.argv[0]} #NUMCHILDS")
        sys.exit(0)

    MAX_INT = 10000000000

    num_childs = int(sys.argv[1])
    if num_childs <= 0:
        print(f"usage: {sys.argv[0]} #NUMCHILDS")
        print("          #NUMCHILDS must be greater than 0")
        sys.exit(0)
    print(f"launching {num_childs} childs loops")

    for i in range(num_childs):
        pid = os.fork()
        if 0 == pid:
            print(f"  Starting child {i}")
            acum = 0
            for i in range(MAX_INT):
                acum += 1
            time.sleep(i)
            print(f"  End of child {i}")
            sys.exit(0)
        else:
            print(f"Started child {pid}")
    time.sleep(1)
    if 1 == num_childs:
        print("Waiting for child")
    else:
        print("Waiting for children")
    for wcont in range(num_childs):
        chpid, wstatus = os.wait()
        print(f"Child {chpid} exited")
    sys.exit(0)

if __name__ == "__main__":
    main()
