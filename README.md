# Djangoデモ

## 目的
Djangoを使用して機械学習をweb化する

## 動作確認方法
```
> cd src  # manage.pyがあるディレクトリに移動する
> python manage.py migrate  # demoアプリ用のDB更新スクリプトを実行し、DBを作成
> python manage.py runserver  # サーバーを起動する
```

※ 初回起動時は下記を行い、ユーザーを登録する
1. DBの作成
```
> cd src  # manage.pyがあるディレクトリに移動する
> python manage.py makemigrations demo  # demoアプリ用のDB更新スクリプトを生成
> python manage.py migrate  # demoアプリ用のDB更新スクリプトを実行し、DBを作成
```

1. ユーザー登録
```
> sqlite3 db.sqlite3  # 使用しているsqliteというDBに入る
sqlite> insert into demo_user (username, password, regist_date) values ('demo',
sqlite> select * from demo_user;  -- `1|demo|demo|2019-10-01 01:02:03` のような
sqlite> .exit  -- sqlite DBから抜ける
```


## 画面モック
[mock_html.zip](doc/mock_html.zip)をダウンロードしてお試しください

## 構成
- 検討中


## 注意
Pycharmが作成する設定ファイル等（.idea、venv等）はgitにupしないで下さい。


## 参考
[PyCharm](https://pleiades.io/help/pycharm/basic-tutorials.html)

[はじめての Django アプリ作成](https://docs.djangoproject.com/ja/2.2/intro/)

[Dive Into Python 3Dive Into Python 3](http://diveintopython3-ja.rdy.jp/special-method-names.html)
