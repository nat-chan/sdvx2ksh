#*sdvx2ksh*
![splash](https://github.com/nat-chan/sdvx2ksh/wiki/splash.png)

サイトsdvx.inからのkshootmaniaの譜面を作成を支援するツールです.

##Requirements
1. Python2.7
2. Selenium
3. PhandomJS <https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip>
4. Numpy
5. PIL
6. urllib2
7. cStringIO

#How to use
```python
from sdvx2ksh import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
ksh = parseScore(onikyokan, 32) #1小節で刻むビート
print ksh #譜面を表示
with open('onikyokan.ksh','w') as f:
	f.write(ksh) #これでkshoot editerから開けるようになる
```

```python
from sdvx2ksh import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
onikyokan.getImg('data').show() #譜面が表示
show(onikyokan[15]) #16小節目を表示
color_picker(onikyokan[15]) #16小節目に含まれる色を降順で表示
for measure in onikyokan:
	show(measure) #イテレーションも可能
```

```python
from sdvx2ksh import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
onikyokan.setDetail() #詳細な譜面情報を取得(重い)
#次の情報がsetされる
onikyokan.title
onikyokan.artist
onikyokan.level
onikyokan.bpm
onikyokan.chain
onikyokan.url['fx']   #youtubeの音源url
onikyokan.url['nofx']
onikyokan.effect
onikyokan.illustrator
```
