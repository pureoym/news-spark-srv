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
# 动态加载pyspark
import os
import sys

import web

os.environ['SPARK_HOME'] = "/application/search/spark-2.1.0-hadoop2.7"
sys.path.append("/application/search/spark-2.1.0-hadoop2.7/python")
sys.path.append("/application/search/spark-2.1.0-hadoop2.7/python/lib/py4j-0.10.4-src.zip:/usr/local/python")
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print ("import spark success")
except ImportError as e:
    print ("error importing spark modules", e)
    sys.exit(1)

# 配置接口URL
urls = (
    '/test', 'test',
)
app = web.application(urls, globals())

TEST_INPUT = 'hdfs://10.10.160.150:9000/test/test.txt'


class test:
    def GET(self):
        sc = None
        try:
            conf = (SparkConf()
                    .setMaster("spark://10.10.160.151:7077")
                    .setAppName("news test")
                    .set("spark.executor.memory", "1g"))
            sc = SparkContext(conf=conf)
            test_rdd = sc.textFile(TEST_INPUT)
            test_result = 'test: ' + str(test_rdd.take(1))
        finally:
            sc.stop()
        return test_result


if __name__ == "__main__":
    # pdb.set_trace()
    reload(sys)
    sys.setdefaultencoding('utf8')

    # smysql = SMysql()
    # smysql.connect()

    web.internalerror = web.debugerror
    app.run()
