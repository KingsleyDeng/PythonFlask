# coding:utf-8

# f = open("./1.txt", "wb")
# # 2.向文件写内容
# try:
#     f.write("hello flask")
# except Exception:
#     pass
# finally:
#     # 关闭文件
#     f.close()

# with实际操作的返回的f
with open("./1.txt", "w") as f:
    f.write("Hello Flask Kingsley")

class Foo(object):
    def __enter__(self):
        """进入with语句的时候被调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit called")
        print("exc_type %s"%exc_type)
        print("exc_val %s"%exc_val)
        print("exc_tb %s"%exc_tb)

with Foo() as foo:
    print("hello Python")