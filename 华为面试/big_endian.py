import sys

def transfrom_char(temp_line):
    i=0
    s=''
    while i < len(temp_line):
        s = s+temp_line[8-1-i]
        # print(temp_line[8-1-i])
        i +=1
    return s+" "



if __name__ == '__main__':
    # 读取第一行的n,即有几个编码串
    n = int(sys.stdin.readline().strip())

    # 读取字符串
    lines = sys.stdin.readline().strip()
    # 求取字符串长度
    length=len(lines)

    output_lines=''

    # string_char=list(lines)

    for i in range(n):
        if lines[i*8+i]=='0':
            output_lines =output_lines+transfrom_char(lines[i*8+i+1:(i+1)*8+i+1])
        elif lines[i*8+i]=='1':
            output_lines= output_lines + lines[i*8+i+1:(i+1)*8+i+1]+" "

    print(output_lines)
