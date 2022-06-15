# Prometheus Adapter

Read remote from Aliyun SLS

## Getting started

### 安装
```commandline
pip install -r requirements.txt
```

```commandline
flask run -h 0.0.0.0 --reload
```

### 配置参考

```commandline
remote_read:
  - url: 'http://172.26.132.63:5000/read'
    read_recent: true
    basic_auth:
      username: 'user'
      password: 'pass'
```
