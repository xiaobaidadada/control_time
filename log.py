
import time

def write_log(tuple):
    #按行输入一个记录，每个记录有多个长度
    f=open(file="log.txt",mode="a")
    f.write("\n\n\n")
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    for value in tuple:
        f.write(value)
        f.write("\000\000\000")

    f.close()

if __name__ == "__main__":
    write_log(("名字","性别"))
