def alphabet():
    for ascii in range(ord('A'), ord('Z') + 1):
        if chr(ascii) not in 'AEIOUY':
            print(chr(ascii), end=' ')

if __name__ == "__main__":
    alphabet()