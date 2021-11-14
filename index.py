# #変数を定義する
# a = 1 #数値
# b = 'AAA' #文字列
# c = [1,2,3] #リスト
# d = {'apple': 200,'orange': 100, 'banana':150} #辞書
#
# #定義した変数の内容を出力してみる
# print(a)
# print(b)
# print(c)
# print(d)
# x,y,z = 1,2,3
# a,b,c = x,y,z
#
# print(a)
# print(b)
# print(c)
# bin_val = 0b0101
# print(bin_val)

# x = 0.0012
# print(x)
# print('1' + '1')
# print('hoge' * 5)
# print('闇夜' + 'の世界')

# print('はじめまして山田です趣味はスポーツ観戦です')
# print('初めまして\n山田です\n趣味はスポーツ観戦です')

# name = '山田'
# age = 22
#
# print(name)
# print(age)
#
# print('半径が3cmの円の直径は')
#
# diameter = 3 * 2
#
# print(diameter)
#
# print('円周の長さは')
# print(diameter * 3.14)
#
# age += 3
#
# print(age)

# name = input('あなたの名前を入力してください')
#
# print('おお' + name + 'よ、そなたを待っておったぞ')

# name = '山田太郎'
# age = 23
# height = 175.6
# #
# # print('私の名前は' + name + 'です。年齢は' + str(age) + '歳です。身長は' + str(height) + 'です')
#
# print('私の名前は {} です。年齢は{}歳です。身長は{}CMです。'.format(name,age,height))

# price = int(input('料金を入力'))
# number = int(input('人数を入力'))
#
# payment = int(price/number)
# print('お支払いは{}円です'.format(payment))

# print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです')

# menu = ['カツ丼','親子丼','他人丼']
# print(menu[0])

# リストの合計の求め方
# scores = [80,90,50]
#
# total = scores[0] + scores[1] + scores[2]
#
# print('合計{}点'.format(total))

# 別コード
# リストの合計の求め方
# scores = [80,90,50]
#
# total = sum(scores)
#
# print('合計{}点'.format(total))

#リストの合計値と平均値を求める方法
# scores = [80,90,50]
# total = sum(scores)
# avg = total / len(scores)
#
# print('合計{}点、平均点{}点'.format(total,avg))

#リストに要素を追加する方法
# members = ['工藤','松本','浅田']
# members.append('中山')
# print(members)

#リストから要素を削除する方法
# members = ['工藤','松本','浅田']
# members.remove('工藤')
# print(members)

#ディクショナリの作成
# scores = {'network':80,'database':90,'security':70}
# print(scores)

#ディクショナリ要素の参照
# scores = {'network':80,'database':90,'security':70}
# print(scores['network'])

#ディクショナリの要素の追加と変更
# scores = {'network':80,'database':90,'security':70}
# scores['programming'] = 65
# scores['security'] = 50
#
# print(scores)

#ディクショナリの要素の削除
# scores = {'network':80,'database':40,'security':70}
# del scores['security']
#
# print(scores)

#ディクショナリの合計を求める方法
scores = {'network':80,'database':40,'security':70}
total = sum(scores.values())

print(total)
