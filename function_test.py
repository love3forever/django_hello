#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 13:45:41
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from selenium import webdriver
import unittest


class FirstPageTest(unittest.TestCase):
    """测试初始页面"""

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_fp_function(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main()
