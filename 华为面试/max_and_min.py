import sys

if __name__ == '__main__':
    # 读取正整数
    N = int(sys.stdin.readline().strip())

    if 0<N and N<=10 or N==100 or N==1000:
        print(0)
    elif N>10 and N<=99:
        two = N//10
        one = N%10
        if one==0:
            print(0)
        elif one>two:
            print((one*10+two)-N)
        else:
            print(N-(one*10+two))

    elif N>100 and N<=999:
        three = N//100
        two = N // 10%10
        one = N % 10
        if two ==0 and one==0:
            print(0)
        elif two==0:
            if one>=three:
                print(one*100+three*10-three*100-one)
            else:
                print(three*100+one*10-one*100+three)
        elif one ==0:
            if two>=three:
                print(two*100+three*10-three*100-two)
            else:
                print(three*100+two*10-two*100-three)
        else:
            if three>=one and three>=two:
                if two>=one:
                    print(three*100+two*10+one-one*100-two*10-three)
                else:
                    print(three*100+one*10+two-two*100-one*10-three)
            elif two >=one and two>=three:
                if one >=three:
                    print(two * 100 + one * 10 + three - three* 100 - one * 10 - two)
                else:
                    print(two * 100 + three * 10 + one - one * 100 - three * 10 - two)

            elif one >= two and one >= three:
                if two >= three:
                    print(one * 100 + two * 10 + three - three * 100 - two * 10 - one)
                else:
                    print(one * 100 + three * 10 + two - two * 100 - three * 10 - one)
    else:
        four = N //1000
        three = N // 100%10
        two = N // 10 % 10
        one = N % 10

        l1=[]
        l1.append(four)
        l1.append(three)
        l1.append(two)
        l1.append(one)
        l1.sort()

        if l1[0]!=0:
            print(l1[3]*100+l1[2]*10)







