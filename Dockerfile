FROM ubuntu:latest
LABEL authors="sanchezrick"

ENTRYPOINT ["top", "-b"]

# 基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到容器中
COPY requirements .

# 安装依赖
RUN pip install --no-cache-dir -r requirements

# 复制项目代码到工作目录
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 运行迁移命令
RUN python manage.py migrate

# 暴露端口
EXPOSE 8000

# 运行命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
