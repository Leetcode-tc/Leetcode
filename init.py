#-*- coding:utf-8 -*-

import os

if __name__ == '__main__':
    cwd = "./"
    folders = {"cpp":"cpp", "python":"py", "java":"java", "js":"js"}
    for folder in folders.keys():
        path = cwd+folder+"/"
        for root, dirs, files in os.walk(path):
            for f in files:
                sourceFile = path+f
                num, name = f.split('_')[0], '_'.join(f.split('_')[1:])
                num = path+num
                name = name+"."+folders[folder]
                cmd = "mv " + sourceFile + " " + num+"/"+name
                if not os.path.exists(num):
                    os.mkdir(num)
                os.popen(cmd)