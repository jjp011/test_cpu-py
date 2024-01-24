import signal

def display_message(s, numTicks=[0]):
    numTicks[0] += 1
    print(f"TIC {numTicks[0]}")
    signal.alarm(1)

def main():
    signal.signal(signal.SIGALRM, display_message)
    signal.alarm(1)

    MAXCOUNT = 1000000000000
    cont = 0
    for i in range(MAXCOUNT):
        cont += 1
        if i % 1000000000 == 0:
            print(f"{cont:10d}")
    return 0

if __name__ == "__main__":
    main()
