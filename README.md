本项目git仓库:https://dev.tencent.com/u/hhhhhg/p/bangumiDesktopAssistant  

该分支为dist分支,适合没有python基础的同学下载运行.  
另有[develop分支](https://dev.tencent.com/u/hhhhhg/p/bangumiDesktopAssistant/git/tree/develop),无内置python环境,无可执行exe.适合有python环境的同学clone来,用自己的python环境来运行本工具.  


### 安装
[点击此处](https://qcloud.coding.net/u/hhhhhg/p/bangumiDesktopAssistant/git/archive/dist)或页面上的下载按钮,可下载本工具压缩包.解压后双击bangumi.exe运行本工具  

### 使用
在任务栏找到图标(和项目头像是同一张图片),右键可进行追番编辑或者退出程序.  
追番编辑工具按要求填入信息,可生成一份番剧信息,保存在src/db/bangumisInfo中,如果填入得当,不发生意外,则可正常使用.  
遇到特殊情况(比如番剧停更)则需要手动改对应的json文件中的chapters部分...  

有番剧更新时,会播放音频,为src/audio/alarm.wav  
透明度,配色等配置存在src/db/config.json中,可以轻易更改

可在注册表中将bangumi.exe设为开机自启  

### 运行截图  
1080p屏幕下unfocused状态表现:  
<a href="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pUnfocused.png" target="_blank">
<img src="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pUnfocused.png" width="200px" style="float:left"/>
</a>  
1080p屏幕下focused状态(鼠标悬停在之上时)表现:  
<a href="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pFocused.png" target="_blank">
<img src="http://hhhhhg.coding.me/bangumiDesktopAssistant/src/img/readmeImg/1080pFocused.png" width="200px" style="float:left"/>
</a>  