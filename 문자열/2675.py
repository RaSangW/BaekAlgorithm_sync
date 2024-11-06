total = int(input())
for _ in range(total):
    num, ss = input().split()
    for i in ss:
        print(int(num)*i,end="")
    print()