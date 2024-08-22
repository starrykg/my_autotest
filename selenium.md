一.环境搭建

#免费的OCR文字识别库
pip install ddddocr
二.八大元素定位
面试题：如果元素定位不到，怎么去分析
2.Frame中
3.元素不可用，不可读，不可见
4.动态属性。动态的DIV层

前提：需要定位的元素或它的属性必须是唯一的

id,name,class_name,css,tag_name,link_text,partail_link_text
xpath定位：
    绝对路径
    相对路径：
        input
        1.相对路径 + 索引定位
        2.相对路径 + 属性定位
        2.相对路径 + 通配符（复制xpath经常会出错）
        4.相对路径 + 部分属性定位
        4.相对路径 + 文本定位
定位方式有种(不建议使用)：
contains(属性名，字符串)：使用文本匹配，功能很强大
starts-with(属性名，字符串）：根据开头进行模糊匹配
ends-with(属性名，字符串）：根据结尾内容进行匹配
matchs(属性名，字符串）：根据正则进行匹配

css定位：
    1.绝对路径：不用
    2.通过id和class定位
    3.通过属性定位
    4.通过部分属性定位
    5.查询子元素定位
    6.查询兄弟节点定位

unittest使用
1.新建一个累心继承unittest.TestCase
2.导入unittest
3.写一个test开头的方法

unittest运行测试用力的大坑：
1.命令行方式
    python3 -m unittest  threeweb/unitest.py
2.main方式
    必须要配置环境，我个人不用

unittest原理，selenium原理， ddt原理

frameset:框架集（忽略）
frame（框架）
iframe（子框架）
driver.switch_to.frame("menu-frame")