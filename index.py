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
# scores = {'network':80,'database':40,'security':70}
# total = sum(scores.values())
#
# print(total)

#タプルの利用
# scores = (70,80,55)
# print(scores)
# print(scores[0])
# print('要素数は{}'.format(len(scores)))
# print('合計は{}'.format(sum(scores)))
# menber = ('松田','山田')
# print(type(menber))

#セットの利用
# scores = {1,2,3,4}
# scores.add(4)
# print(scores)

#コレクションの相互変換
# scores = {'network':90, 'database':60,'java':70}
# members = {'松本','本田','マイケル'}
#
# print(tuple(members))#リストからタプルに変換
# print(list(scores))#キーをリストに変換
# print(set(scores.values()))#値をセットに変換

#ディクショナリーの中にディクショナリをネスト
# matuda_scores = {'network':60,'database':80,'security':70}
# tanaka_scores = {'network':40,'database':20,'security':30}
# member_scores = {
#     '松田':matuda_scores,
#     '田中':tanaka_scores
# }
#
# print(member_scores)

#コネクションのネスト
# member_hobbies = {
#     '松田':{'SNS','麻雀','ロードバイク'},
#     '田中':{'ハイキング','読書','映画鑑賞'}
#
# }
# #全ディクショナリを表情
# print(member_hobbies)
# #松田のみの一覧表示
# print('松田さんの一覧',member_hobbies['松田'])

# #二次元リストの例
# a = [1,2,3]
# b = [4,5,6]
# c = [a,b] #aを0番目、bを1番目とする2次元リストcを定義
#
# print(c)#リストc全体を参照
# print(c[0])#リストcの0番目　リストaだけを参照
# print(c[1][2])#リストcの1番目　リストbの2番目だけを参照

#セットの＆演算
# member_hobbies = {
#     '松田':{'SNS','麻雀','ロードバイク'},
#     '浅木':{'麻雀','食べ歩き','カツ丼','親子丼'}
# }
# common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
# print(common_hobbies)#2人に共通する趣味の一覧を表示する。

#4つの集合演習

# A = {1,2,3,4}
# B = {2,3,4,5}
#
# print(A | B) #和集合
# print(A & B) #積集合
# print(A - B)#差集合
# print(A ^ B)#対象差

#答えが分岐するチャットポット
# name = input('あなたの名前を教えてください>>')
# print('{}さん、こんにちは'.format(name))
#
# food = input('{}さんの好きな食べ物を教えてください>>'.format(name))
#
# if food == 'カレー':
#     print('素敵です。カレーは最高ですよね!!')
# else:
#     print('私も{}が好きですよ'.format(food))

#どんなカレーでも絶賛するチャットポット
# name = input('あなたの名前を教えてください>>')
# print('{}さん、こんにちは'.format(name))
#
# food = input('{}さんの好きな食べ物を教えてください>>'.format(name))
# if 'カレー'in food:
#     print('素敵です。カレーは最高ですよね!!')
# else:
#     print('私も{}が好きですよ'.format(food))

#100点があるかどうか調べる
# scores = [80,100,20,60]
# if 100 in scores:
#     print('100点満点の試験があたんですね。おめでとう！')
# else:
#     print('次はどれか1つでも100点満点をとろう')

#ディクショナリのキーをチェックする
# scores = {'network':60, 'database':80, 'security':50}
#
# key = input('追加する科目名を入力してください>>')
# if key in scores:
#     print('すでに登録済みです')
# else:
#     data = int(input('得点を入力してください'))
#     scores[key] = data
# print(scores)

#条件式の評価結果を確認する
# score = int(input('試験の点数を入力>>'))
# print(score >= 60)

#多分岐するif文
# score = int(input('試験の点数を入力してください>>'))
#
# if score < 0 or score > 100:
#     print('異常な得点です')
#     print('入力し直してください')
# elif score >= 60:
#     print('合格!')
#     print('よく頑張りましたね')
# else:
#     print('残念ながら不合格です')
#     print('追試を受けてください')

#晩御飯をレコメンドするチャットポット
# print('全ての質問にyまたはnで答えてください')
# okane_aruka = input('お金に余裕はありますか?>>')
# if okane_aruka == 'y':
#     onaka_suiteruka = input('お腹がすごく空いてるか?>>')
#     nomitai_kibunka = input('ビールを飲みたいですか?')
#     if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
#         print('焼肉はいかがですか')
#     elif onaka_suiteruka == 'y':
#         print('カレーはいかがですか')
#     elif nomitai_kibunka == 'y':
#         print('焼き鳥はいかがですか')
#     else:
#         print('パスタはいかがですか')
#     yashoku_iruka = input('夜食は必要ですか? >>')
#     if yashoku_iruka == 'y':
#         print('コンビニのチキンはいかがですか')
# else:
#     print('家で食べましょう')


