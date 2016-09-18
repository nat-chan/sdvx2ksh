#現在BTとFXのみ

```python:
from sdvx2py import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
ksh = parseScore(onikyokan, 32) #1小節で刻むビート
print ksh #譜面を表示
with open('onikyokan.ksh','w') as f:
	f.write(ksh)
#これでkshoot editerから開けるようになる
```

```python:
from sdvx2py import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
onikyokan.getImg('data').show() #譜面がみれる
show(onikyokan[15]) #16小節目を表示
color_picker(onikyokan[15]) #16小節目に含まれる色を降順で表示
for measure in onikyokan:
	show(measure) #イテレーションも可能
```

```python:
from sdvx2py import *
onikyokan = Score('http://sdvx.in/03/03044/03044e.htm')
onikyokan.getDetail() #詳細な譜面情報を取得(重い)
#次の情報がsetされる
self.title
self.artist
self.level
self.bpm
self.chain

self.url['fx']   #youtubeの音源url
self.url['nofx']

self.effect
self.illustrator
```