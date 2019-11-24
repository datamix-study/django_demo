from django.db import models

class User(models.Model):
    """
    ログインユーザ
    """
    # ユーザ名
    username = models.CharField(max_length=20)

    # パスワード
    password = models.CharField(max_length=20)

    # 登録日付
    regist_date = models.DateTimeField('date published')

    def __str__(self):
        return self.username;


class Item(models.Model):
    """
    商品
    """
    # 商品名
    name = models.CharField(max_length=255)

    # 商品画像ファイルパス
    image_path = models.CharField(max_length=20)

    # 商品説明
    descrition = models.CharField(max_length=3000)

    # 価格
    price = models.PositiveSmallIntegerField()

    # 在庫数
    stock_quantity = models.PositiveSmallIntegerField()


# class Cart(models.Model):
#     """
#     カート情報
#     """
