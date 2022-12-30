def alphabet():
    for ascii in range(ord('A'), ord('Z') + 1):
        print(chr(ascii), end=' ')

if __name__ == "__main__":
    alphabet()