# 基础镜像：Ubuntu 22.04，自带 GCC 11+ 和新 libstdc++
FROM ubuntu:22.04

ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

# # 替换为清华大学镜像源以加速下载
# RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list && \
#     sed -i 's@//.*security.ubuntu.com@//mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list

# 设置 pip 统一源
# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装 PaddleOCR 必需的系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 python3.10-distutils python3-pip \
    wget ca-certificates \
    libgl1-mesa-glx libglib2.0-0 libgomp1 \
    && rm -rf /var/lib/apt/lists/*

#将本地ocr目录同步到镜像的/paddle/ocr目录下
RUN mkdir -p /paddle/ocr
COPY ocr/ /paddle/ocr/

#检查uploads目录是否存在
RUN mkdir -p /paddle/uploads

#安装python依赖环境
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install python-multipart

#安装PaddleOCR依赖
RUN pip install paddleocr

EXPOSE 8093

#运行PaddleOCR的主程序
CMD ["python", "/paddle/ocr/main_ocr.py"]