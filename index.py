# #変数を定義する
a = 1 #数値
b = 'AAA' #文字列
c = [1,2,3] #リスト
d = {'apple': 200,'orange': 100, 'banana':150} #辞書

# #定義した変数の内容を出力してみる
print(a)
print(b)
print(c)
print(d)
x,y,z = 1,2,3
a,b,c = x,y,z

print(a)
print(b)
print(c)
bin_val = 0b0101
print(bin_val)

x = 0.0012
print(x)
print('1' + '1')
print('hoge' * 5)
print('闇夜' + 'の世界')

print('はじめまして山田です趣味はスポーツ観戦です')
print('初めまして\n山田です\n趣味はスポーツ観戦です')

name = '山田'
age = 22

print(name)
print(age)

print('半径が3cmの円の直径は')

diameter = 3 * 2

print(diameter)

print('円周の長さは')
print(diameter * 3.14)

age += 3

print(age)

name = input('あなたの名前を入力してください')

print('おお' + name + 'よ、そなたを待っておったぞ')

name = '山田太郎'
age = 23
height = 175.6
#
# print('私の名前は' + name + 'です。年齢は' + str(age) + '歳です。身長は' + str(height) + 'です')

print('私の名前は {} です。年齢は{}歳です。身長は{}CMです。'.format(name,age,height))

price = int(input('料金を入力'))
number = int(input('人数を入力'))

payment = int(price/number)
print('お支払いは{}円です'.format(payment))

print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです')

menu = ['カツ丼','親子丼','他人丼']
print(menu[0])

# リストの合計の求め方
scores = [80,90,50]

total = scores[0] + scores[1] + scores[2]

print('合計{}点'.format(total))

別コード
リストの合計の求め方
scores = [80,90,50]

total = sum(scores)

print('合計{}点'.format(total))

#リストの合計値と平均値を求める方法
scores = [80,90,50]
total = sum(scores)
avg = total / len(scores)

print('合計{}点、平均点{}点'.format(total,avg))

#リストに要素を追加する方法
members = ['工藤','松本','浅田']
members.append('中山')
print(members)

#リストから要素を削除する方法
members = ['工藤','松本','浅田']
members.remove('工藤')
print(members)

#ディクショナリの作成
scores = {'network':80,'database':90,'security':70}
print(scores)

#ディクショナリ要素の参照
scores = {'network':80,'database':90,'security':70}
print(scores['network'])

#ディクショナリの要素の追加と変更
scores = {'network':80,'database':90,'security':70}
scores['programming'] = 65
scores['security'] = 50

print(scores)

#ディクショナリの要素の削除
scores = {'network':80,'database':40,'security':70}
del scores['security']

print(scores)

#ディクショナリの合計を求める方法
scores = {'network':80,'database':40,'security':70}
total = sum(scores.values())

print(total)

#タプルの利用
scores = (70,80,55)
print(scores)
print(scores[0])
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))
menber = ('松田','山田')
print(type(menber))

#セットの利用
scores = {1,2,3,4}
scores.add(4)
print(scores)

#コレクションの相互変換
scores = {'network':90, 'database':60,'java':70}
members = {'松本','本田','マイケル'}

print(tuple(members))#リストからタプルに変換
print(list(scores))#キーをリストに変換
print(set(scores.values()))#値をセットに変換

#ディクショナリーの中にディクショナリをネスト
matuda_scores = {'network':60,'database':80,'security':70}
tanaka_scores = {'network':40,'database':20,'security':30}
member_scores = {
    '松田':matuda_scores,
    '田中':tanaka_scores
}

print(member_scores)

#コネクションのネスト
member_hobbies = {
    '松田':{'SNS','麻雀','ロードバイク'},
    '田中':{'ハイキング','読書','映画鑑賞'}

}
#全ディクショナリを表情
print(member_hobbies)
#松田のみの一覧表示
print('松田さんの一覧',member_hobbies['松田'])

# #二次元リストの例
a = [1,2,3]
b = [4,5,6]
c = [a,b] #aを0番目、bを1番目とする2次元リストcを定義

print(c)#リストc全体を参照
print(c[0])#リストcの0番目　リストaだけを参照
print(c[1][2])#リストcの1番目　リストbの2番目だけを参照

#セットの＆演算
member_hobbies = {
    '松田':{'SNS','麻雀','ロードバイク'},
    '浅木':{'麻雀','食べ歩き','カツ丼','親子丼'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)#2人に共通する趣味の一覧を表示する。

#4つの集合演習

A = {1,2,3,4}
B = {2,3,4,5}

print(A | B) #和集合
print(A & B) #積集合
print(A - B)#差集合
print(A ^ B)#対象差

#答えが分岐するチャットポット
name = input('あなたの名前を教えてください>>')
print('{}さん、こんにちは'.format(name))

food = input('{}さんの好きな食べ物を教えてください>>'.format(name))

if food == 'カレー':
    print('素敵です。カレーは最高ですよね!!')
else:
    print('私も{}が好きですよ'.format(food))

#どんなカレーでも絶賛するチャットポット
name = input('あなたの名前を教えてください>>')
print('{}さん、こんにちは'.format(name))

food = input('{}さんの好きな食べ物を教えてください>>'.format(name))
if 'カレー'in food:
    print('素敵です。カレーは最高ですよね!!')
else:
    print('私も{}が好きですよ'.format(food))

#100点があるかどうか調べる
scores = [80,100,20,60]
if 100 in scores:
    print('100点満点の試験があたんですね。おめでとう！')
else:
    print('次はどれか1つでも100点満点をとろう')

#ディクショナリのキーをチェックする
scores = {'network':60, 'database':80, 'security':50}

key = input('追加する科目名を入力してください>>')
if key in scores:
    print('すでに登録済みです')
else:
    data = int(input('得点を入力してください'))
    scores[key] = data
print(scores)

#条件式の評価結果を確認する
score = int(input('試験の点数を入力>>'))
print(score >= 60)

#多分岐するif文
score = int(input('試験の点数を入力してください>>'))

if score < 0 or score > 100:
    print('異常な得点です')
    print('入力し直してください')
elif score >= 60:
    print('合格!')
    print('よく頑張りましたね')
else:
    print('残念ながら不合格です')
    print('追試を受けてください')

#晩御飯をレコメンドするチャットポット
print('全ての質問にyまたはnで答えてください')
okane_aruka = input('お金に余裕はありますか?>>')
if okane_aruka == 'y':
    onaka_suiteruka = input('お腹がすごく空いてるか?>>')
    nomitai_kibunka = input('ビールを飲みたいですか?')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかがですか')
    elif onaka_suiteruka == 'y':
        print('カレーはいかがですか')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかがですか')
    else:
        print('パスタはいかがですか')
    yashoku_iruka = input('夜食は必要ですか? >>')
    if yashoku_iruka == 'y':
        print('コンビニのチキンはいかがですか')
else:
    print('家で食べましょう')

#while文
#羊を数えるのを3回繰り返す
count = 0
while count < 3:
    count += 1
    print('羊が{}匹'.format(count))
print('おやすみなさい')

#羊を数えるのを眠るまで繰り返す
is_awake = True
count = 0

while is_awake == True:
    count += 1
    print('羊が{}匹・・・'.format(count))
    key = input('もう眠りそうですか？(y/n)>>')
    if key == 'y':
        is_awake = False
print('おやすみなさい')

#繰り返しを使って得点リストを作成する
count = 0 #カウンタ変数
student_num = int(input('学生の数を入力'))#学生の数
score_list = list()#得点リスト

while count < student_num:
    count += 1
    score = int(input('{}人目の試験の得点を入力>>'.format(count)))
    score_list.append(score)

print(score_list)
total = sum(score_list)
print('平均点は{}点です'.format(total / student_num))

#リストの全要素を繰り返し参照する
scores = [80,20,75,60]
count = 0

while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1

#for分で決まった回数を繰り返す
for num in range(3):
    print('ホゲホゲ')

#データのまとまりからサンプルを抽出
ages = [28,50,8,20,78,25,22,10,27,33] #対照データ
num = 5
samples = list()

for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)

#目的数に達したら繰り返しを終了する
ages = [28,50,8,20,78,25,22,10,27,33]#対象データ
num = 5#目標の抽出数
samples = list()#サンプルデータを格納するリスト

for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)

#不要なかいのループをスキップする
ages = [28,50,'秘密',20,78,25,22,10,'無回答',33]
samples = list()
for data in ages:
    if not isinstance(data,int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)

#hello関数の定義
def hello():
    print('こんにちは')

hello()

#引数を受け取りhello関数を呼び出す
def hello(name):
    print('こんにちは。{}です。'.format(name))

hello('ホゲホゲ')

#複数の引数を引き受けるprofile関数
def profile(name,age,hobby):
    print('私の名前は{}です。'.format(name))
    print('年齢は{}歳です。'.format(age))
    print('趣味は{}です。'.format(hobby))

profile('浅木',23,'カフェ巡り')

#足し算の結果を返す
def plus(x,y):
    answer = x + y
    return answer

resurt = plus(100,50)
print('足し算の答えは{}です'.format(resurt))


#さまざまな機能を担当する関数の定義
def input_scores(name):#得点入力を担当する関数
    print('{}さんの試験結果を入力してください'.format(name))
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))

    scores = [network,database,security]

    return scores

def calc_average(scores):#平均の計算を担当する関数
    avg = sum(scores) / len(scores)

    return avg

def output_result(name,avg):#平均点の出力を担当する関数
    print('{}さんの平均点は{}です'.format(name,avg))

#得点入力
hitorime_scores = input_scores('生徒A')
hutarime_scores = input_scores('生徒B')

#平均点を計算
hitorime_avg = calc_average(hitorime_scores)
hutarime_avg = calc_average(hutarime_scores)

#結果を出力
output_result('生徒A',hitorime_avg)
output_result('生徒B',hutarime_avg)

#２つの戻り値を返すし、戻り値のタプルをアンバック代入
def plus_and_minus(a,b):

    return a + b,a - b

(next,prev) = plus_and_minus(1978,1)

print((next,prev))

#eat関数(デフォルト値を利用)
def eat(breakfast, lunch, dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))

print('本日の食事は下記の通りです')

eat('パン','焼きそば')

#可変長引数を利用した関数定義
def eat(breakfast,lunch,dinner='カレー', *desserts):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))

    for d in desserts:
        print('おやつに{}を食べました'.format(d))

eat('トースト','パスタ','カレー','アイス','チーズケーキ','プリン')

#ディクショナリを用いた可変長引数
def eat(**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key,kwargs[key]))

eat(朝食='納豆')

#global文を用いてグローバル変数を代入する
name = 'ホゲホゲ'

def change_name():
    global name
    name = 'ゲホゲホ'


def hello():
    print('こんにちは' + name + 'さん')

change_name()

hello()

#RPGの勇者を表すクラスの定義と利用
class Hero:
    name = '松本'
    hp = 100
    def sleep(self,hours):
        print('{}は{}時間寝た!'.format(self.name,hours))
        self.hp += hours

print('ファイナルファンタジー')

h = Hero()
h.sleep(3)

print('{}のHPは現在{}です'.format(h.name,h.hp))

#オブジェクトのidentity

scores1 = [80,40,50]
scores2 = [80,40,50]

print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))

if scores1 == scores2:
    print('scores1とscores2は同じ内容です。')
else:
    print('scores1とscores2は違う内容です。')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ存在です。')
else:
    print('scores1とscores2は違う存在です。')

#リストオブジェクトのコピーの動作
scores1 = [20,30,40]
scores2 = [20,30,40]

print('scores1の先頭要素は{}'.format(scores1[0]))
print('scores2の先頭要素は{}'.format(scores2[0]))

print('変数scores2の中身を変数scores1に代入')
scores1 = scores2

print('scores1の先頭要素を90に書き換え')
scores1[0] = 90

print('90を代入したscores1の先頭要素は{}'.format(scores1[0]))
print('90を代入していないscores2の先頭要素は{}'.format(scores2[0]))





