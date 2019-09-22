# 还原单词列表
correct_words = ["undefined", "function", "object", "global", "window", "self", "Object", "Number", "String", "Date", "SyntaxError", "TypeError", "Math", "JSON", "bug-string-char-index", "a", "json", "json-stringify", "json-parse", "{\"a\":[1,true,false,null,\"\\u0000\\b\\n\\f\\r\\t\"]}", "0", "\"\"", "1", "[1]", "[null]", "null", "[null,null,null]", "\x00\x08\x0A\x0C\x0D\x09", "[\x0A 1,\x0A 2\x0A]", "\"-271821-04-20T00:00:00.000Z\"", "\"+275760-09-13T00:00:00.000Z\"", "\"-000001-01-01T00:00:00.000Z\"", "\"1969-12-31T23:59:59.999Z\"", "\"\x09\"", "01", "1.", "[object Function]", "[object Date]", "[object Number]", "[object String]", "[object Array]", "[object Boolean]", "valueOf", "toString", "toLocaleString", "propertyIsEnumerable", "isPrototypeOf", "hasOwnProperty", "constructor", "prototype", "\\\\", "\\\"", "\\b", "\\f", "\\n", "\\r", "\\t", "000000", "\\u00", "\"", "", "toJSON", "-", "+", "T", ":", ".", "Z", "[\x0A", ",\x0A", "\x0A", "]", "[", ",", "[]", " ", "{\x0A", "}", "{", "{}", "\\", "/", "\x08", "\x09", "\x0C", "\x0D", "@", "0x", "true", "false", "$", "string", "runInContext", "JSON3", "use strict", "./isArguments", "Object.keys called on a non-object", "[object Arguments]", "number", "./zlib/deflate", "./utils/common", "./utils/strings", "./zlib/messages", "./zlib/zstream", "[object ArrayBuffer]", "must be non-object", "./common", "../utils/common", "./trees", "./adler32", "./crc32", "./messages", "pako deflate (from Nodeca project)", "need dictionary", "stream end", "file error", "stream error", "data error", "insufficient memory", "buffer error", "incompatible version", "&", "=", "%20", "boolean", "./decode", "./encode", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", "pako/lib/deflate", "./btoa", "querystring", "./webdriver", "object-keys", "Function.prototype.bind - what is trying to be bound is not callable", "json3", "ps", "token", "_token", "1.0.6", "srcElement", "on", "mousemove", "keydown", "click", "ontouchmove", "touchmove", "?", "hasAttribute", "webdriver", "__driver_evaluate", "__webdriver_evaluate", "__selenium_evaluate", "__fxdriver_evaluate", "__driver_unwrapped", "__webdriver_unwrapped", "__selenium_unwrapped", "__fxdriver_unwrapped", "__webdriverFunc", "_Selenium_IDE_Recorder", "_selenium", "calledSelenium", "domAutomation", "domAutomationController", "__lastWatirAlert", "__lastWatirConfirm", "__lastWatirPrompt", "dw", "de", "di", "wf", "wwt", "ww", "gw", "__webdriver_script_fn", "ChromeDriverwjers908fljsdf37459fsdfgdfwru=", "$cdc_asdjflasutopfhvcZLmcfl_", "$chrome_asyncScriptInfo", "_WEBDRIVER_ELEM_CACHE", "__$webdriverAsyncExecutor", "cd_frame_id_", "iframe", "frame", "driver-evaluate", "webdriver-evaluate", "selenium-evaluate", "webdriverCommand", "webdriver-evaluate-response", "lwe", "f", "v", "p", "h", "l", "S", "lwc", "Cannot find module \'", "\'", "MODULE_NOT_FOUND"]
# 目标还原js文件
file = '混淆文件.js'
with open(file,'r',encoding='utf8') as f:
    text = f.read()

for i in range(len(correct_words)):
    correct_word= correct_words[i]
    wrong_word = f'_$_543c[{i}]'
    print(wrong_word)
    # text = text.replace(wrong_word,"'%s'"%(correct_word))
    text = text.replace(wrong_word,"%s"%(correct_word))

with open('done_'+file,'w',encoding='utf8') as f:
    f.write(text)

