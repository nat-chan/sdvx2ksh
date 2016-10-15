#sdvx2ksh
![splash](https://github.com/nat-chan/sdvx2ksh/wiki/splash.png)

サイトsdvx.inからのkshootmaniaの譜面を作成を支援するツールです.
##使い方
1. ここ<https://www.dropbox.com/s/hugwby16y7yg1zw/gui.zip?dl=0>からzipで落としてください
2. 展開してgui.exeを実行してください
3. 譜面サイトのurlを入力してrunボタンをクリック
##現状(ver1.1β)
曲名、アーティスト名、bpm(ソフラン曲は無理)等が自動で入る。
fxとnofx音源を切り替えるのでエフェクトの種類などを一々記入しないで済む。
fx,nofx音源のズレをframe単位で修正する機能を追加。
譜面生成が終わったら自動でeditorを開いてくれるようになった。
VOLは精度がアレなのでBTFXのみ。あと何故かFXが頭しか入らなくなった。そのうち改善します。

#以降プログラマ向け
##importしてるの
1. Python2.7
2. Selenium
3. PhandomJS <https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip>
4. numpy scipy cv2
5. PIL
6. urllib2
7. cStringIO
8. pafy
9. lxml

##インタプリタでこんな風に叩く
```python
from sdvx2ksh import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
head = onikyokan.getHeader() #詳細な譜面情報を取得(重い)
body = parseScore(onikyokan) #こっちが譜面本体
with open('onikyokan.ksh','w') as f: #これでkshoot editerから開けるようになる
	f.write((head + body).encode('sjis','replace')) #winなのでsjisの必要あり
```

```python
from sdvx2ksh import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
onikyokan.getImage('data').show() #譜面が表示
show(onikyokan[15]) #16小節目を表示
color_picker(onikyokan[15]) #16小節目に含まれる色を降順で表示
for measure in onikyokan:
	show(measure) #イテレーションも可能
```

