#-*- coding:utf-8 -*- 
#-- db config --
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWD = "123456"
DB_NAME = "thepast"

#-- redis config --
REDIS_HOST = "localhost"
REDIS_PORT = 6379


#-- app config --
DEBUG = True
SECRET_KEY = "dev_key_of_thepast"
SESSION_COOKIE_NAME = "pastme"

SITE_COOKIE = "pastck"

#-- openid type config --
OPENID_DOUBAN = 'douban'
OPENID_SINA = 'sina'
OPENID_WORDPRESS = 'wordpress'
OPENID_QQ = 'qq'
OPENID_GOOGLE = 'google'
OPENID_FACEBOOK = 'facebook'
OPENID_TWITTER = 'twitter'

OPENID_TYPE_DICT = {
    OPENID_DOUBAN : "D",
    OPENID_SINA : "S",
    OPENID_WORDPRESS : "W",
    OPENID_QQ : "Q",
    OPENID_GOOGLE : "G",
    OPENID_FACEBOOK : "F",
    OPENID_TWITTER : "T",
}

#-- oauth key & secret config --
APIKEY_DICT = {
    OPENID_DOUBAN : {
        "key" : "047e255f2309478c0d7a701d691bd6a4",
        "secret" : "0253348fa4d10541",
        "redirect_uri" : "http://127.0.0.1:5000/connect/douban/callback",
    },
    OPENID_SINA : {
        "key" : "4028327410",
        "secret" : "cb59a6ea5c8e0220f452d2bc4a9145c1",
        "redirect_uri" : "http://127.0.0.1:5000/connect/sina/callback",
    },
}

#-- category of status --
CATE_DOUBAN_STATUS = 100
CATE_DOUBAN_NOTE = 101
CATE_DOUBAN_MINIBLOG = 102
CATE_DOUBAN_PHOTO = 103
CATE_SINA_STATUS = 200
CATE_WORDPRESS_POST = 300
CATE_TWITTER_STATUS = 400

CATE_LIST = (
    CATE_DOUBAN_STATUS,
    CATE_DOUBAN_NOTE,
    CATE_DOUBAN_MINIBLOG,
    CATE_DOUBAN_PHOTO,
    CATE_SINA_STATUS,
    CATE_WORDPRESS_POST,
    CATE_TWITTER_STATUS,
)

from local_config import *
