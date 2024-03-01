if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('程序被另一模块引用')

def log( par ):
    print ("logFun : ", par)
    return

def log1( par ):
    print ("log1Fun : ", par)
    return