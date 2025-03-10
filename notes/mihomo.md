VPN在linux 命令行端使用方式 （本质上用的还是你的VPN，只是在外面套了一层，让VPN在linux上也能使用）
1. 下载 mihomo （https://github.com/MetaCubeX/mihomo/releases/tag/v1.18.8）
  1. 阿里云端可以选择下载mihomo-linux-amd64-compatible-v1.18.8.gz，其它看系统配置
  2. 如何下载到linux上？
    1. 可以先下载到本机
    2. 然后上传到huggingface自己的一个目录里
    3. 上传好后点击这个文件会有下载链接
      1. [This file is stored with Git LFS . It is too big to display, but you can still download it.]
      2. 从download里可以复制出来下载链接
    4. 将下载链接中的https://huggingface.co/替换为https://hf-mirror.com/，随后export huggingface的镜像链接
export HF_ENDPOINT=https://hf-mirror.com
    5. 使用wget进行下载
2. 对文件进行处理
mv [原文件名] mihomo.gz
gunzip mihomo.gz
sudo chmod +x mihomo
sudo cp mihomo /usr/local/bin
sudo mkdir /etc/mihomo -p
3. 获取config.yaml文件
  此文件来源于自己使用的VPN，VPN在clash 配置中运行时一般会创建这样一个文件，可以直接把里面的内容拿出来
  一些可供参考的clash，复制VPN的订阅地址到里面即可使用：
    1. MAC：
    arm(M系列芯片)
    x86(intel系列)
    2. Windows：
    64位 
    32位
  这里以 魔戒 为例进行说明，其它 VPN 也可从本地相应的文件中获取配置信息
  1. 在网址可以找到相应的订阅地址
[图片]
  2. 在clash安装好运行以后，首先配置订阅地址，随后点应用目录会跳转到文件存放目录
[图片]
[图片]
  3. 这里打开clash-verge.yaml，里面即存放了要获取的内容
[图片]
4. 将config.yaml文件放到服务器中
sudo vi /etc/mihomo/config.yaml # 里面写入之前复制的内容
5. 启动VPN
  1. 直接启动
    1. 可以放在bash脚本里nohup挂起，或者放到screen里
sudo /usr/local/bin/mihomo -d /etc/mihomo
    2. 配置本地端口 （这里为config.yaml文件中的端口）
export http_proxy="http://127.0.0.1:8888"
export https_proxy="https://127.0.0.1:8888"
    3. 取消本地端口的配置
unset http_proxy
unset https_proxy
  2. 使用 systemctl 启动 （阿里云不支持）
    1. 创建 mihomo 服务
sudo vi /etc/systemd/system/mihomo.service
    2. 粘贴以下内容
[Unit]
Description=mihomo Daemon, Another Clash Kernel.
After=network.target NetworkManager.service systemd-networkd.service iwd.service

[Service]
Type=simple
LimitNPROC=500
LimitNOFILE=1000000
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH
Restart=always
ExecStartPre=/usr/bin/sleep 1s
ExecStart=/usr/local/bin/mihomo -d /etc/mihomo
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
    3. 重载 systemd
systemctl daemon-reload
    4. 启用 mihomo 服务（开机、重启系统后自动启动）
systemctl enable mihomo
    5. 立即启动 mihomo 服务
systemctl start mihomo
    6. 检查 mihomo 服务状态
systemctl status mihomo
