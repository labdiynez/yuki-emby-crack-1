# yuki-emby-crack

Windows简单白嫖Emby会员

原理出自这篇博客：[白嫖一下Emby](https://imrbq.cn/exp/emby_hack.html)，有兴趣可以去看看

代码实现基于tornado+pyinstaller

## 使用效果

![AfterUsing](/images/i-afterusing.png)

## 使用方法：

### 解压缩文件

从Release页面下载`dist.zip`，解压缩至`C:\Users\<UserName>\Documents\dist`(即文档文件夹)

此时在文档中应存在如下文件结构：

```
dist
|---cert
|	|---server.crt
|	|---server.key
|---main.exe
```

双击`main.exe`运行程序，在Windows上可能会弹出防火墙设定，两个全勾选允许通过即可

> 注意：此处的程序解压缩路径可以随意修改，不过只能放在C盘个人文件夹或除C盘以外的其他磁盘分区，否则可能会因为权限不足而无法启动

### 设置开机自启动

右键`main.exe`，选择`创建快捷方式`，将得到的`main.exe - 快捷方式`复制到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`目录

### 修改Host文件

进入`C:\Windows\System32\drivers\etc`目录，修改hosts文件，在文件末尾增加如下内容：

```
127.0.0.1 mb3admin.com
```

至此重新启动位于本机的EmbyServer你会发现小金标应该已经有了，如果没有出现的话可以到Emby控制台中的Emby Premiere里面随便输入任意字符点击验证即可

## 常见问题

### 无法激活？

首先检查是不是严格按照步骤成功启动了，直接打开浏览器访问[`https://127.0.0.1/`](https://127.0.0.1/)，如果出现错误点击`高级`-`继续访问`，出现下图内容则代表激活程序成功启动：

![After Using](/images/i-checkstatus.png)

如果上图信息成功显示，则可能是未安装证书的问题，Windows请下载同release一同发布的`guomi.cer`证书文件，双击证书文件并选择`安装证书`，在弹出的窗口中依次选择`当前用户`-`将所有证书都放入下列存储`，单击`浏览`并选择到`受信任的根证书颁发机构(如下图)`，然后依次单击`确定`-`下一步`-`完成`来完成证书的安装
![InstallCert](images/i-installcert.png)

## 附加信息

### 关于本项目？

项目基于Python tornado框架，寥寥几行无需多讲，无非是加载证书返回一个已激活的信息而已，搞这个东西的初衷也只是为了在windows上的激活更简单一些，经测试可以激活安装在windows上的Emby Server/Emby Electron

### 自行编译？

当然可以，使用pycharm加载该项目，在`terminal`执行

```shell
pip install -r requirements.txt
```

然后运行执行命令

```shell
pyinstaller -F -w main.py
```

然后你就能在`dist`目录找到编译好的exe文件了，但是还是要配合证书使用

### 关于证书？

证书偷懒了，直接使用了来自于 [embyonekey](https://github.com/s1oz/embyonekey) 项目的证书，如果担心证书存在安全问题，可以依据开头引用的博客中的指引自行申请证书

