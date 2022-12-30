
def count_tics(tic:str, discours:list):
    c = 0
    for mot in discours:
        if mot == tic:
            c += 1
    return c

if __name__ == "__main__":
    tic = str(input())
    discours = list(map(str, input().lower().split()))
    print(count_tics(tic, discours))