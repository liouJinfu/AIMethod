# --*-- coding:utf-8 --*--
'''我的目标是：在WEB页面，实现语音输入时，根据语音的输出结果进行各种自己的日常操作，目前可以支持查看LIB 的日志记录，
支持发送WLAN的lib'''
import aiml,os
from pip._vendor.distlib.compat import raw_input

os.chdir('./alice') # 将工作区目录切换到刚才复制的alice文件夹
alice = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    alice.bootstrap(brainFile="bot_brain.brn")
else:
    alice.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    alice.saveBrain("bot_brain.brn")

if __name__ == '__main__':
    while True:
        message = raw_input("Enter your message to bot:")
        if message == "quit":
            exit()
        elif message == "save":
            alice.saveBrain("bot_brain.brn")
        else:
            print(alice.respond(message))