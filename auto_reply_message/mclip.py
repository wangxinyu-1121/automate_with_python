#! python3
# mclip.py - A multi-clipboard program.
# 　一个多剪切板程序

TEXT = {
    'agree': '是的，我同意。听起来挺不错',
    'busy': '对不起！你所呼叫的用户暂时无法接听，请稍后再拨',
    'upsell': '要充Q币吗？',
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('功能:用python的mclip.py模块,根据[关键字]复制对应文本')
    sys.exit()

keyphrase = sys.argv[1]  # 第一个命令行参数是关键字（改成手动输入的也行）

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('文本"{}"已复制到剪切板'.format(keyphrase))
else:
    print('没有该关键字"{}"的相关文本'.format(keyphrase))


