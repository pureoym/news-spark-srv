# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/11/20 15:07
# Copyright 2017 pureoym. All Rights Reserved.
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
# ==============================================================================
import web
import sys
from pyspark.sql import SparkSession

# 配置接口URL
urls = (
    '/test','test',
)
app = web.application(urls, globals())

TEST_INPUT = 'hdfs://10.10.160.150:9000/test/test.txt'

class test:
    '''w2v'''
    def GET(self):
        spark = SparkSession.builder().appName("test").master("yarn").getOrCreate()
        test_rdd = spark.read.text(TEST_INPUT).cache()
        return "test!" + str(len(test_rdd))

if __name__ == "__main__":
    #pdb.set_trace()
    reload(sys)
    sys.setdefaultencoding('utf8')

    #smysql = SMysql()
    #smysql.connect()

    web.internalerror = web.debugerror
    app.run()