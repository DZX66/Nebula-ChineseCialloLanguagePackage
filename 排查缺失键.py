import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PATH_SCHINESE = r"ChineseCiallo/Language/SChinese.dat"
PATH_ENGLISH = r"origin/English.dat"
# 日语文件取自【游戏根目录\BepInEx\nebula\Nebula.dll\.text\DefaultLanguage\Language\Japanese.dat】
PATH_JAPANESE = r"origin/Japanese.dat"

def dat_to_dict(path)->dict:
    res = {}
    with open(path,"r",encoding="utf-8") as f:
        a = "pass"
        while a!="":
            a = f.readline()
            b = a.split('" : "')
            if len(b) == 2:
                res[b[0][1:]] = b[1][:-2]
    return res
def compare(target:str,sample:str)->dict:
    '''返回target相对于sample缺失的键'''
    target_dict = dat_to_dict(target)
    sample_dict = dat_to_dict(sample)
    missing = {}
    for i in sample_dict:
        if i not in target_dict:
            missing[i] = sample_dict[i]
    return missing
def print_dict(dict:dict):
    for i in dict:        
        print(f'"{i}" : "{dict[i]}"')
print("输入值应为C（中文），E（英文）或J（日文）")
target = input("目标（默认C）：")
if target=="" or target=="C":
    target = PATH_SCHINESE
elif target=="E":
    target = PATH_ENGLISH
elif target=="J":
    target = PATH_JAPANESE
else:
    raise TypeError("不正确的输入，输入值应为C（中文），E（英文）或J（日文）。")
sample = input("目标：")
if sample=="C":
    sample = PATH_SCHINESE
elif sample=="E":
    sample = PATH_ENGLISH
elif sample=="J":
    sample = PATH_JAPANESE
else:
    raise TypeError("不正确的输入，输入值应为C（中文），E（英文）或J（日文）。")
print_dict(compare(target,sample))