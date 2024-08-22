# omc_autotest

## How to setup your development environment?
1. Prepare your python3 env
```
sudo apt install python3-pip
pip3 install ddddocr
pip3 install robotframework-seleniumlibrary==4.3.0 指定版本安装
pip3 install robotframework-seleniumlibrary
pip3 install webdriver-helper
pip3 install XTestRunner
#用于删除登录验证码失败的redis key
pip3 install redis

示例(设置了超时时间，-i临时指定源地址)：
pip3 --default-timeout=1000 install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

2. download chromedriver
```
https://registry.npmmirror.com/binary.html?path=chromedriver/    对应浏览器版本
```

3. run
```
python3 runner.py

开发时自测可使用（错误输出到终端，不生成测试报告）
python3 -m unittest testcase/func_test.py
```

## 测试报告
```
 /reports/5gc_test_*.html
```

## 测试用例
```
在testcase目录的test开始的的函数会自动运行
```

## todo
```
当验证码错误时，自动删除测试ip的redis的key
```