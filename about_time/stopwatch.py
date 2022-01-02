#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :stopwatch.py
# @Time      :2022/1/2 15:52
# @Author    :wangxinyu
# description：
import sys, time


def func():
    print("回车开始，回车计时，ctrl+c退出")
    input()
    print("开始计时")
    start_time = time.time()
    end_time = start_time
    lap_num = 1
    try:
        while True:
            input()
            lap_time = round(time.time() - end_time, 3)
            total_time = round(time.time() - start_time, 3)
            print(f"圈数：{lap_num}\n单圈时间：{lap_time}\n整体时间：{total_time}")
            lap_num += 1
            end_time = time.time()
    except Exception as e:
        print(e)
        print("退出")


def func1():
    """超级秒表"""
    start_time = 0
    end_time = 0
    while True:
        print("输入s开始，输入e并按回车退出")
        line = sys.stdin.readline().strip().lower()
        if line == "s":
            print("开始计时")
            time1 = round(time.time(), 3)
            while True:
                print("按回车计时，输入e并按回车结束")
                line = sys.stdin.readline().strip().lower()
                if line == "e":
                    print("结束计时")
                    break
                elif line:
                    print("应该按回车或者输入e结束")
                else:
                    time2 = round(time.time(), 3)
                    time_diff = time2 - time1
                    end_time = start_time + time_diff
                    print(f"上一时间；{start_time}\n当前时间:{end_time}\n时间差={time_diff}")
                    time1 = time2
                    start_time = end_time
        elif line == "e":
            print("退出程序")
            break
        else:
            print("你应该输入s开始，或者输入e退出")


def unit_test():
    func()


if __name__ == "__main__":
    print('*' * 10 + 'start' + '*' * 10)
    unit_test()
    print('*' * 10 + 'end' + '*' * 10)
