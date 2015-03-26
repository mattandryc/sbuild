# 快速地编写符合原生安卓格式的字符串
* 保证string name符合原生安卓的命名标准
* 输入的每条string会被自动地拷贝到values-zh-rCN相关的文件
* tools/下的string_names是安卓5.0所用的原生的string name
* 以后打算应用百度或谷歌的翻译API
* 如果有任何反馈意见随时联系哦～

# Usage:
`$python sbuild.py path/to/values/strings.xml`

如果想建新的strings.xml文件的话就用$python sbuild.py target/path/to/values/
描述写地更系有助于第三方翻译

