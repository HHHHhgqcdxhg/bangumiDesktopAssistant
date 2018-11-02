if __name__ == '__main__':
    try:
        from __init__ import bangumi
        bangumi()
    except Exception as e:
        print(str(e))
        a = input("输入任意值后回车关闭 : ")
