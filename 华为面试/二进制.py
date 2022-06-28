import sys

if __name__ == '__main__':
    # 读取正整数
    N = int(sys.stdin.readline().strip())

    for i in range(N):
        length=int(sys.stdin.readline().strip())
        lines=str(sys.stdin.readline().strip())
        i=0
        s=''
        while i+1<length:
            if lines[i]=='0' and lines[i+1]=='0':
                s=s+'1'
                i = i + 1
            else:
                s=s+lines[i]
                i=i+1

        s = s+ lines[i]

        print(s)
