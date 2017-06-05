# raspberry_ip2qq
树莓派获取家用路由器动态IP并且发送给QQ邮箱
python2.7版本
在树莓派中搭建mysql数据库，创建名为ip的库，在库中创建ip_list表，表中创建ip_id和ip_name两个字段，ip_id为主键
用户只需修改脚本运行时间，QQ邮箱名称和qq邮箱SMTP授权码
需要用户配置树莓派系统中的/etc/rc.local文件，达到开机运行脚本的功能。命令：sudo vim /etc/rc.local，在注释后面添加命令，但是要保证exit 0这行代码在最后，然后保存文件退出。
命令：Python /home/pi/raspberry_ip2qq.py &
