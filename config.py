# coding=utf-8
__author__ = 'Shan'
import os
# basedir = os.path.join(os.path.dirname(__file__))
basedir = os.getcwd()

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# 分页
POSTS_PER_PAGE = 3

# 内容索引 :使用了flask-whooshalchemy 扩展
WHOOSH_BASE = os.path.join(basedir, 'search.db')
# 最大的搜索结果返回数
MAX_SEARCH_RESULTS = 50

# 邮件服务设置
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# 管理员列表
ADMINS = ['test@test.com']

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'VeriSign', 'url': 'https://pip.verisignlabs.com' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]