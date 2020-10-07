# yuki-emby-crack

Windows简单白嫖Emby会员

原理出自这篇博客：[白嫖一下Emby](https://imrbq.cn/exp/emby_hack.html) ，有兴趣可以去看看

代码实现基于tornado+pyinstaller

## 使用效果

> Emby Server

![i-demo-1](/images/i-demo-1.png)

> Emby Theater

![i-demo-2](/images/i-demo-2.png)

## 使用方法：

### 解压缩文件

从Release页面下载`dist.zip`，解压缩至`C:\Users\<UserName>\Documents\dist`(即文档文件夹)

![i-dist.png](images/i-unzip.png)

此时在文档中应存在如下文件结构：

![i-dist.png](images/i-dirlist.png)

双击`main.exe`运行程序，在Windows上可能会弹出防火墙设定，两个全勾选允许通过即可

> 注意：此处的程序解压缩路径可以随意修改，不过只能放在C盘个人文件夹或除C盘以外的其他磁盘分区，否则可能会因为权限不足而无法启动

### 设置开机自启动

右键`main.exe`，选择`创建快捷方式`，将得到的`main.exe - 快捷方式`复制到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`目录

![i-autostart.png](images/i-autostart-1.png)

![i-autostart.png](images/i-autostart-2.png)

### 修改Host文件

进入`C:\Windows\System32\drivers\etc`目录，修改hosts文件，**在文件末尾增加**如下内容：

```
127.0.0.1 mb3admin.com

```

> 注意此处`127.0.0.1 mb3admin.com`后面需要加一个空行，不然有可能会出现修改不生效的神奇问题

### 安装证书

在[`release`](https://github.com/MitsuhaYuki/yuki-emby-crack/releases) 页面下载和`dist.zip`一同发布的`guomi.cer`证书文件，双击证书文件并选择`安装证书`，在弹出的窗口中依次选择`当前用户`-`将所有证书都放入下列存储`，单击`浏览`并选择到`受信任的根证书颁发机构(如下图)`，然后依次单击`确定`-`下一步`-`完成`来完成证书的安装

![i-installcert](images/i-installcert.png)

至此重新启动位于本机的EmbyServer你会发现小金标应该已经有了，如果没有出现的话可以到Emby控制台中的Emby Premiere里面随便输入任意字符点击验证即可

## 常见问题

### 激活失败

#### STEP1：检查程序是否正常启动

打开任务管理器，往下找，如果程序正常启动的话你应当能看到标有main.exe`字样的进程

![i-step1](/images/i-step1.png)

如果没有的话代表你设置自启动的那一步存在问题，或者如果你想要手动启动的话请手动双击`main.exe`来启动程序

#### STEP2：检查host是否正确设定

按下`win`+`r`键输入`cmd`并回车来打开cmd窗口，输入`ping mb3admin.com`，应当能得到如下结果

![i-step2](/images/i-step2.png)

如果结果不是`来自 127.0.0.1 的回复`字样则代表你的hosts文件设置存在问题，请按照教程重新设定host文件

#### STEP3：检查是否存在代理问题

如果以上检查都没有问题，则打开浏览器访问[`https://mb3admin.com/`](https://mb3admin.com/) ，如果出现错误点击`高级`-`继续访问`，此时应该出现如下内容

![i-step3-1](/images/i-step3-1.png)

如果没有出现对应内容且STEP1和2都没有出现问题，请检查你是不是使用了某些代理插件，关闭它们之后重启浏览器再试一次。如果依旧存在问题可以手动进入`Windows设置`-`网络和Internet-代理`，将`使用代理服务器`设为关闭，之后重启浏览器再试一次

![i-step3-2](/images/i-step3-2.png)

#### STEP4：还有问题？

那我就没法解决了，毕竟我也没遇到过#笑，请自行解决~

## 附加信息

### 关于本项目？

项目基于Python tornado框架，寥寥几行无需多讲，无非是加载证书创建web服务器返回一个已激活的信息而已。搞这个东西的初衷也只是为了在windows上的激活更简单一些，经测试可以激活安装在windows上的Emby Server/Emby Theater，原理基于[白嫖一下Emby](https://imrbq.cn/exp/emby_hack.html) 。如非必要本项目一般不会再次更新，以及**不会**提供技术支持

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

### 关于常见问题-STEP3

我也是偶然发现这个问题，实际上并不是说不能同时使用代理，翻找一下你使用的插件，只需要让你的插件不再代理`mb3admin.com`这个网址即可，例如我使用的Clash for Windows中在Settings里面就有设置系统代理bypass选项，只需要加一行`  - mb3admin.com`即可，如果你没在浏览器页面中看到小金标，看看是不是用了SwitchyOmega或者其他类似插件，如果有的话将`mb3admin.com`加入`不代理的地址列表`，然后刷新页面就能看到小金标啦

