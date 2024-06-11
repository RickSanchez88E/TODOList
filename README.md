# MusicPlayer

---

## 目录

- [安装](#安装)
- [使用方法](#使用方法)
- [许可证](#许可证)



## 安装:

1.  安装包
```bash
pip3 install -r requirements
```
---

2. 或者也可以使用Docker来部署本地环境
```bash
docker build -t my-app .
```
```bash
docker scout quickview
```
---

### For Linux (ubuntu):
#### 安装Docker请前往: [Docker官网](https://docs.docker.com/engine/install/ubuntu/)

```bash
sudo apt update
```
```bash
sudo apt install python3-pip
```
---

## 使用方法:

### Activate Virtual Environment
```bash
virtualenv venv
```

```bash
source venv/bin/activate
```
---
### Run Django Server:
```bash
python3 manage.py runserver
```
---
### Migrate Database :
```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```
---
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)


## 贡献:

欢迎贡献代码！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细流程。


## 许可证:

本项目基于 MIT 许可证，详细信息请参见 [LICENSE](LICENSE) 文件。
