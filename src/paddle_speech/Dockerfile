# 基础镜像：Ubuntu 22.04，自带 GCC 11+ 和新 libstdc++
FROM ubuntu:22.04

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

# # 替换为清华大学镜像源以加速下载
# RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list && \
#     sed -i 's@//.*security.ubuntu.com@//mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 python3.10-distutils python3.10-dev python3-pip \
    build-essential gcc g++ cmake \
    git curl wget ca-certificates \
    libsndfile1 libsndfile1-dev \
    ffmpeg \
    cython3 \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /paddle/speech
RUN mkdir -p /paddle/speech/logs
COPY /speech /paddle/speech

# list all files and folders in /paddle/speech
RUN ls -l /paddle/speech

EXPOSE 8090
EXPOSE 8092

# 设置工作目录
WORKDIR /paddle

# 设置 pip 统一源
# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装编译依赖和基础包
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy cython
RUN pip install supervisor
# 安装 PaddlePaddle CPU 版本
RUN pip install paddlepaddle
RUN pip install paddlespeech
#Fix cannot import name 'download' from 'aistudio_sdk.hub'
RUN pip uninstall -y aistudio_sdk
RUN pip install "aistudio_sdk<0.3.0"

CMD ["supervisord", "-c", "/paddle/speech/supervisord.conf"]