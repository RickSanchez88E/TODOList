# MusicPlayer

---

## 目录

- [安装](#安装)
- [使用方法](#使用方法)
- [许可证](#许可证)



## 安装:

1.  安装包
### 导入node库
```bash
winget install Schniz.fnm
fnm use --install-if-missing 20
npm i
```
### 导入python库
```bash
pip3 install -r requirements
```
---
### 制作json文件

```bash
nano top-script-417701-71a594897872.json
```

#### 将下列内容粘贴到其中
> {
  "type": "service_account",
  "project_id": "top-script-417701",
  "private_key_id": "71a594897872e999986b3f1b24e5f1b1405eed81",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQD3HwzGwIIUvjH5\n90Nzq6XsKxnw4m21Ehjbg990BzqhYOz+MYZJ1DKQxy5ZnBDKpcE81wuV3P5wvMZm\nRrh0wvOVFw7TMKPpzQqfNZ0KPizq/2AnCn0nQs8PxuhcPkHCAK8/rdgCVUgnpiA5\n6c7NCMoOyS6Afbj2lrE0THM4aUQKF6Nl+q0Ql/VxzcCbyadmu+KoTwNBi5tClzOf\nJpbm/XFlqGZ7ZbEutpG94Zy4EkJ6AQFqhn+ni4ESh0Osy6eK/bV8dMtGvv7SpVQB\na8tYi+y1qfFV/jZHChK+EVA5wT0HDn2DTJf67uoHxdLZHcPcdEWB59JN1TGmwZAJ\nX9jVZTHZAgMBAAECggEAdkztc1omC6MPTrAxoLabvCbYCMqEpWmP78o+Fw/839OE\nMJ3pwP8t48QOasR8/14BV0xFFg2Q2sxsF/skA3VuYUGEDdLbrSnEu3nRf11LaIYv\ndBEf38MqV82rX7lIBoUIYC4rWdaUr7Jl/ANzRhE+lXx23/kPqjByjWxJvkgaU8+T\nSlPtejbePDpU+SDDqrOBJPSKAGNLk5ndw9+Gp3wMyC3vbduUXA3nJU6BqE7iruin\nTkv6PxgQPRhLsHTtaxFfiqTwU50lcopm2Kz78FR/HF1k/+6Hu5wDNXrznHr3zVk3\nK3x+JJXpbBCex9s1ohQBGZ+jBgODP+QuT8zO7uIDhwKBgQD+e7PGZ8kBROTKmXdX\nI2T0oCEdSGVM+bdfx76540yorLH07vV27WKNWxnaFl7Wvq7qYH6D2PQDbsVPL9Mj\nLE8Lygr+3/iF02V/T7/hHvK+9YCFXMMBNLCrSCJGutDfqlM5PKl4IOHLba0WVRI2\nD6A58eZpG3t4xxyvMcW04FUOUwKBgQD4mB1YUMDysIfEvaWpuhMm7y85gmHLdc+A\nPR1aMnoXVfVoCCw9HTT3t1SW+XJIFme9emetQKJO0mHWx9Ctl8xUslcKFrloi6So\nYcGdaBGUltD4ndE8OgUbctTrynPkvf/sNte5p4BKUWjBmoVwt2ZQwImsa2lNEmLT\n2AeOh75BowKBgQC36qbuiStX43aGhYseStI3iVLlWuD7VK4WZsGMjp1kegrSvbBh\nFwbWqjRwzSIViRHZCYvltfIEWRX4ONQa43btSkPQGAYAkdsUu4otJLTDFaKgv32f\nbXkRELzU6UbznqEvCIxh6UHGR6mELk9PCtP9jLm81MPTcfNlGk+MfWR7SQKBgQCP\n1nQkRZVe1wW3sIPKUQAD5yFMBUTQlLobWUFCjzJVjkcQiqoOMngTXOB0+qBFVbFw\n0QJsHJnNQa2auMLlro9r8kSqcbuV4jbDtsxwZ2bEsv7221nVnzyVRTwtslacY9NQ\nuerYYTK5zaDvZJkRPwzUbJM8UGn9TkYgjT7SGXjcQQKBgEaWKfklwAZZa5BlWQNZ\nYARf2mebAWA0mUXQS5Y066ycnpDe/cYPrPBXdL4TOfP+LAHiWAklWT0dGYSKcpBi\nvxJF1vtIVjUtKhHYBetpOJ4r/ekEM/VXDREdoa9H8ZVPo1/q3tDnsznNyq1byWu9\nTWKKe6ajAVSaM+/YLKDErFxY\n-----END PRIVATE KEY-----\n",
  "client_email": "1084950800355-compute@developer.gserviceaccount.com",
  "client_id": "106566242488063616565",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/1084950800355-compute%40developer.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

#### 接着ctrl+o 回车 ctrl+x



---
## 或者也可以使用Docker来部署本地环境
```bash
docker build -t my-app .
```
```bash
docker scout quickview
```
---

### For Linux (Ubuntu):
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
