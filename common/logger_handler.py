"""
封装log模块，继承
小技巧：在定义的模块当中初始化

"""
import logging
class LoggerHandler(logging.Logger):
    def __init__(self,
                 name='root',
                 level="DEBUG",
                 file='',
                 fmt='%(asctime)s--%(filename)s--%(name)s--%(lineno)s--%(levelname)s--%(message)s',
                 ):
        super().__init__(name)  # 直接用父类的构造方法，产生一个logger
        # super.__init__(name)  # 这里没有括号，变成调用父类的属性

        # logger = logging.getLogger(name)

        # logger.setLevel(level)
        self.setLevel(level)  # 直接用父类的setLevel方法

        if file:
            handler = logging.FileHandler(file)
        else:
            handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(fmt))
        # logger.addHandler(stream_handler)
        self.addHandler(handler)

        # self.logger = logger

    def info(self, msg):
        super().info(msg)
        print("我正在使用。。。")


# 一个项目中初始化1个log对象就够了，其他logger_handler_user.py使用时，可以存在同一个log文件里
logger = LoggerHandler("python25", file="python25.txt")


# if __name__ == '__main__':
#     logger = LoggerHandler()
#     # logger = LoggerHandler(file=" r.txt")  # 这里即使输入了file名，还是有指定输出file.txt
#     logger.debug("hello world")  # 能正确显示调用的行号



