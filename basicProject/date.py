#日付について

import datetime # とりあえずこれ必要

# 現在の日時
print(datetime.date.today())             # 2019-04-14
print(datetime.datetime.today())         # 2019-04-14 21:34:24.382658

now = datetime.datetime.today()
print(now.hour)                          # 21 （このように、"時"だけ出力することもできる）
print(now.time())                        # 21:38:05.691003

comp1 = datetime.datetime(2018, 11, 22, 9, 55, 28)
comp2 = datetime.datetime.today()
print("日付の大きさチェック：")
print((comp1 < comp2))                   # true
print("\n")



# 日付変換（文字列から日付）
# 「datetime.datetime.strptime」を使用
date_str = "2018/08/09"
date_formatted = datetime.datetime.strptime(date_str, "%Y/%m/%d")
print(date_formatted)                   # 2018-08-09 00:00:00

date_str = "20180809"
date_formatted = datetime.datetime.strptime(date_str, "%Y%m%d")
print(date_formatted)                   # 2018-08-09 00:00:00
print(type(date_formatted))             #datetime.datetime型
print("\n")


# 日付変換（日付から文字列）
today = datetime.date.today()           # 2019-04-14
today_str = today.strftime("%Y%m%d")    # 20190414
print(today_str)
print(type(today_str))                  #str型
print("\n")


