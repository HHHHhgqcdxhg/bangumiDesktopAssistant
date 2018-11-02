本项目git仓库:https://dev.tencent.com/u/hhhhhg/p/bangumiDesktopAssistant  

该分支为[develop](#)分支,无内置python环境,无可执行exe.适合有python环境的同学clone来,用自己的python环境来运行本工具.
另有[dist](#)分支,适合没有python基础的同学下载运行.

python版本是3.6.4(因为用到了[f前缀字符串](https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals),所以大概需要至少3.6版本),操作系统只试了windows.  

使用:
```
git clone https://git.dev.tencent.com/hhhhhg/bangumiDesktopAssistant.git
cd bangumiDesktopAssistant
pip install -r requirements.txt
python __main__.py
```
在任务栏找到图标(和项目头像是同一张图片),右键可进行追番编辑或者退出程序.  
追番编辑工具按要求填入信息,可生成一份番剧信息,保存在src/db/bangumisInfo中,如果填入得当,不发生意外,则可正常使用.  
遇到特殊情况(比如番剧停更)则需要手动改对应的json文件中的chapters部分...  

有番剧更新时,会播放音频,为src/audio/alarm.wav  
透明度,配色等配置存在src/db/config.json中,可以轻易更改

配置好环境后,之后可以运行bangumi.bat来运行本工具,也可在注册表中将bangumi.bat设为开机自启  
运行截图:  
1080p屏幕下unfocused状态表现:  
<a href="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pUnfocused.png" target="_blank">
<img src="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pUnfocused.png" width="200px" style="float:left"/>
</a>  
1080p屏幕下focused状态(鼠标悬停在之上时)表现:  
<a href="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pFocused.png" target="_blank">
<img src="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pFocused.png" width="200px" style="float:left"/>
</a>  
<!--4k屏幕下unfocused状态表现:-->
<!--![4kUnfocused.png](http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/4kUnfocused.png)  -->
<!--4k屏幕下focused状态(鼠标悬停在之上)表现:-->
<!--![4kFocused.png](http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/4kFocused.png)  -->
之前用tkinter写了两天了,察觉有点不好用,又换成了PyQt5.  
耗资源方面,平常在后台运行就占用十几二十M内存    