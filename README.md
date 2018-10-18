本项目git仓库:https://dev.tencent.com/u/hhhhhg/p/bangumiDesktopAssistant  
尝试了打包成exe却做不到XD  
python版本:3.6.4  
使用:

```
git clone https://git.dev.tencent.com/hhhhhg/bangumiDesktopAssistant.git
cd bangumiDesktopAssistant
pip install -r requirements.txt
pythonw __main__.py
```
在任务栏找到图标(图表和项目头像一张图片),右键可进入追番编辑或者退出程序.  
追番编辑工具按要求填入信息,可生成一份番剧信息,在db/bangumisInfo中,如果填入得当,不发生意外,则可正常使用.遇到特殊情况(比如停更)则需要手动改对应的json文件...

到番剧更新时间时,会播放音频,为src/audio/alarm.wav,可替换为其他wav文件  
透明度,配色等配置存在src/db/config.json中,可以轻易更改  
截图:  
unfocused状态:
![1080p unfocused](http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pdisactive.png)  
focused状态:(鼠标悬停在之上)
![1080p focused](http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pactive.png)