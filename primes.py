def isPrime():
    for primer in range(2,1000):
        for divider in range(2,primer):
            if(primer%divider == 0):
                break
        else:
            print(primer)

if __name__ == "__main__":
    isPrime()
