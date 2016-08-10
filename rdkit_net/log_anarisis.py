# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        dockerlog_anarsis
# Purpose:
#
# Author:      Tetsuya Yamamoto
#
# Created:     09/08/2016
# Copyright:   (c) Tetsuya Yamamoto 2016
# Licence:     MIT
#-------------------------------------------------------------------------------

import re

def main():
    rpm_list = []
    whl_list = []

    # ログからyumインストールログを抜き出す正規表現
    rpm_rep = re.compile('^\s\s(Updating|Installing)\s+:\s+([^\s]+)\s*[0-9]+/[0-9]+\s+$')
    # ログからpipインストールログを抜き出す正規表現
    whl_rep = re.compile('^\s\sDownloading\s(.+)\s\([0-9\.]+(kB|MB)\)$')

    # ログファイルを読み込む
    # powershellでリダイレクトするとunicodeで出力されるため、
    # ログファイルは予めUTF8にエンコードしなおしておくこと
    log = open("build_log.txt", "r")

    # ログを一行ずつ精査
    for line in log.readlines():
        # yumのパッケージインストールの場合、正規表現を使ってパッケージの名前を取得
        rpm_line = rpm_rep.search(line)
        # 末尾に.rpmをつけてrpmパッケージファイルリストの末尾に追加
        if rpm_line: rpm_list.append("{}.rpm".format(rpm_line.group(2)))
        # pipインストールの場合、正規表現を使ってパッケージの名前を取得
        whl_line = whl_rep.search(line)
        # whlパッケージファイル名リストに追加
        if whl_line: whl_list.append(whl_line.group(1))
    log.close()

    print rpm_list
    print len(rpm_list)
    print whl_list


if __name__ == '__main__':
    main()
