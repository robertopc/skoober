import unittest
from unittest.case import TestCase
from os import path
import sys

PROJECT_PATH = path.abspath(
    path.join(
        path.join(
            path.dirname(__file__),
            '..'),
        'skoob'))
sys.path.append(PROJECT_PATH)
from skoob.spiders import spider
import scrapy


class SpiderTests(TestCase):

    def setUp(self):
        self.crawler = spider.SkoobSpider({'user': 'user', 'password': 'pass'})

    def test_spider_has_username_and_password(self):
        user = 'user01'
        password = 'securepassword'

        crawler = spider.SkoobSpider({'user': user, 'password': password})
        self.assertEqual(user, crawler.user)
        self.assertEqual(password, crawler.password)

    def test_skoob_spider_inherits_from_scrapy_spider(self):
        self.assertIsInstance(self.crawler, scrapy.Spider)

    def test_raises_error_if_doesnt_have_username_and_password(self):
        with self.assertRaises(Exception):
            spider.SkoobSpider()

    def test_return_user_id_from_complete_profile_url(self):
        profile_url = "http://www.skoob.com.br/usuario/133113-guidobr"
        result = self.crawler._get_user_id(profile_url)
        expected = "133113"
        self.assertEqual(expected, result)

    def test_return_user_id_from_simplified_profile_url(self):
        profile_url = "http://www.skoob.com.br/usuario/133113"
        result = self.crawler._get_user_id(profile_url)
        expected = "133113"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()