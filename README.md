# SUPPA（Android）

## 项目目录树

```php
winter
├── app
│   ├── api
│   │   ├── common
│   │   │   ├── write_500_error.py
│   │   │   ├── get_hclc.py
│   │   │   ├── __init__.py
│   │   │   └── res.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── articles.py
│   │   │   ├── comments.py
│   │   │   ├── __init__.py
│   │   │   ├── revoked_tokens.py
│   │   │   └── users.py
│   │   ├── resources
│   │   │   ├── article
│   │   │   │   ├── add_articles.py
│   │   │   │   ├── del_article.py
│   │   │   │   ├── get_atc_collect.py
│   │   │   │   ├── get_atc_hot.py
│   │   │   │   ├── get_atc_like.py
│   │   │   │   ├── get_atc_mine.py
│   │   │   │   ├── get_atc_new.py
│   │   │   │   └── __init__.py
│   │   │   ├── atc_hclc
│   │   │   │   ├── atc_collect.py
│   │   │   │   ├── atc_comment.py
│   │   │   │   ├── atc_hit.py
│   │   │   │   ├── atc_like.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── user_change
│   │   │   │   ├── change_headimage.py
│   │   │   │   ├── change_password.py
│   │   │   │   ├── change_username.py
│   │   │   │   └── __init__.py
│   │   │   └── users
│   │   │       ├── exit.py
│   │   │       ├── get_user.py
│   │   │       ├── head_image
│   │   │       │   ├── image_file.py
│   │   │       │   └── __init__.py
│   │   │       ├── __init__.py
│   │   │       ├── login.py
│   │   │       └── register.py
│   │   └── schema
│   │       ├── add_atc_sha.py
│   │       ├── comment_sha.py
│   │       ├── login_sha.py
│   │       └── register_sha.py
│   ├── config.py
│   ├── __init__.py
│   └── manage.py
├── Dockerfile
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 4208557d303d_.py
│       ├── 8e2b0e5589ee_.py
│       └── d118e30f26ba_.py
├── README.md
├── requirements.txt
├── run.py
└── static
    └── headimages
```

## 技术栈

- Flask
- Flask_RESTful
- Flask_SQLAlchemy
- Flask_JWT_Extended
- Flask_Cors
- Flask_Migrate
- redis

## 接口文档
`https://apifox.com/apidoc/shared-22db28b4-2d98-4676-874e-4cfe46011f74`

## 已完成功能

- 用户
  - 注册
  - 登录
  - 个人主页
  - 修改信息（头像，用户名，密码）
- 文章
  - 获取文章列表
    - 最新文章
    - 热门文章（按点击量降序）
    - “我"的文章
    - “我”点赞的文章
    - “我”收藏的文章
  - 文章详页
    - 文章内容（标题，正文，添加时间，作者（头像，用户名））
    - 点赞，收藏，评论（一、二级评论）
    - 点击（同一用户两次点击间隔30s及以上有效）
  - 撰写文章（支持markdown渲染）

## 正在测试功能

- 删除文章

## 正在开发功能

- 500错误日志记录


