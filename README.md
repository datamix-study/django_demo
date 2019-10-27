# Djangoデモ

## 目的
Djangoを使用して機械学習をweb化する

## 動作確認方法
1. [wikiのgit-連携](https://github.com/snufkin92/django_demo/wiki/Pycharm#git-連携) を参考にリポジトリをクローンする
1. [wikiのDjangoコマンド実行](https://github.com/snufkin92/django_demo/wiki/Pycharm#djangoコマンド実行)を参考にプロジェクトを起動する。  
   直接コマンドを入力する場合はターミナルから下記を実行する
    ```
    > cd src  # manage.pyがあるディレクトリに移動する
    > python manage.py migrate  # demoアプリ用のDB更新スクリプトを実行し、DBを作成
    > python manage.py runserver  # サーバーを起動する
    ```
1. http://127.0.0.1:8000/demo/ にアクセスする

※ 初回起動時は下記コマンドを実行し、ユーザーを登録する(ユーザー名 = demo、 パスワード = demoのユーザー)
1. DBの作成
```
> cd src  # manage.pyがあるディレクトリに移動する
> python manage.py makemigrations demo  # demoアプリ用のDB更新スクリプトを生成
> python manage.py migrate  # demoアプリ用のDB更新スクリプトを実行し、DBを作成
```

2. ユーザー登録
```
> sqlite3 db.sqlite3  # 使用しているsqliteというDBに入る
sqlite> insert into demo_user (username, password, regist_date) values ('demo', 'demo', current_timestamp);
sqlite> select * from demo_user;  -- `1|demo|demo|2019-10-01 01:02:03` のようなレコードが表示されることを確認
sqlite> .exit  -- sqlite DBから抜ける
```


## 画面モック
[mock_html.zip](doc/mock_html.zip)をダウンロードしてお試しください

- [ログイン]（http://htmlpreview.github.io/?https://github.com/datamix-study/django_demo/blob/master/doc/mock_html/login.html）
- [一覧]（https://htmlpreview.github.io/?https://github.com/datamix-study/django_demo/blob/master/doc/mock_html/list.html）

## 構成
- 検討中


## 注意
Pycharmが作成する設定ファイル等（.idea、venv等）はgitにupしないで下さい。


## 参考
[PyCharm](https://pleiades.io/help/pycharm/basic-tutorials.html)

[はじめての Django アプリ作成](https://docs.djangoproject.com/ja/2.2/intro/)

[Dive Into Python 3Dive Into Python 3](http://diveintopython3-ja.rdy.jp/special-method-names.html)
