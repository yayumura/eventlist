from django.db import models

CATEGORY = (('game', 'ゲーム'), ('anime', 'アニメ'), ('eat', '食事'), ('other', 'その他'))

class Event(models.Model):
    date = models.DateField("開催日") # 複数開催日を考慮できていない
    title = models.CharField("イベント名", max_length=128)
    link = models.URLField("リンク")
    category = models.CharField(max_length=128, choices=CATEGORY)

    # admin管理画面でDB上の各レコードをtitle名で表示する
    def __str__(self):
        return self.title
