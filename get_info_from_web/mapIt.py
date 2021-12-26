#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :mapIt.py
# @Time      :2021/12/19 11:57
# @Author    :wangxinyu
# description：从web上获取信息
import webbrowser, sys, pyperclip, requests
from selenium import webdriver
# browser = webdriver.Edge()


def map_it(address=None):
    """
    从web中获取信息
    :return:
    """
    if address:
        a = address
    elif len(sys.argv) > 1:
        a = ''.join(sys.argv[1:])
    elif pyperclip.paste():
        a = pyperclip.paste()
    else:
        a = "https://docs.python.org/zh-cn/3/library/index.html"
    res = requests.get(a)

    try:
        res.raise_for_status()
    except Exception as exc:
        print('异常原因：{}'.format(exc))
    if res.status_code == requests.codes.ok:
        # print(res.text)
        with open("E:\\临时文件\\pytest\\mapit.txt", "wb+") as f:
            for text in res.iter_content():
                f.write(text)

    # webbrowser.open(a)


def unit_test():
    map_it()


if __name__ == "__main__":
    print('*' * 10 + 'start' + '*' * 10)
    unit_test()
    print('*' * 10 + 'end' + '*' * 10)
