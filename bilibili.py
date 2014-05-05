#! /usr/bin/env python
# encoding: UTF-8

# Copyright 2014 Chen Ruichao <linuxer.sheep.0x@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib import urlopen  # 网络传输
import zlib                 # 压缩/解压
import json                 # JSON
from datetime import date   # 时间与日期

# 从Bilibili获取信息
infourl = 'http://bilibili.kankanews.com/index/bangumi.json'
compressed_json = urlopen(infourl).read()

# 解压
gunzip = zlib.decompressobj(31)
info = gunzip.decompress(compressed_json)

# 读取JSON字符串，转换成Python的数据结构
# 换句话说，把"[1,2,3]"转换成[1,2,3]
info = json.loads(info)

# 今天是周几？
# isoweekday()返回1~7，而我们需要0~6，所以模一下
weekday = date.today().isoweekday() % 7

# 抓出今天更新的番剧
print '今天更新的番剧:'
for bgm in info:
    if bgm['weekday'] == weekday:
        print '    ' + bgm['title']
