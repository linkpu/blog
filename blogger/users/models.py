from django.db import models


class Pictures(models.Model):
    p_address = models.CharField(max_length=200)
    p_lastTime = models.DateField(auto_now_add=True)
    p_createTime = models.DateField(auto_now_add=True)
    p_isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'pictures'

class ArticlesManager(models.Manager):
    def get_queryset(self):
        return super(ArticlesManager,self).get_queryset().filter(a_isDelete=False)
    def createArticle(self, a_author, a_title, a_address,
                      a_keyWord, a_describe, a_column,
                      a_label, a_lastTime, a_createTime,
                      a_state, a_isDelete,):
        article = self.model()
        article.a_author = a_author
        article.a_title = a_title
        article.a_address = a_address
        article.a_keyWord = a_keyWord
        article.a_describe = a_describe
        article.a_column = a_column
        article.a_label = a_label
        article.a_lastTime = a_lastTime
        article.a_createTime = a_createTime
        article.a_state = a_state
        article.a_isDelete = a_isDelete
        return article


class Articles(models.Model):
    #自定义模型管理器
    #自定义模型管理器后, 默认模型管理器objects就会失效
    artObj = ArticlesManager()

    a_author = models.CharField(max_length=30)
    a_title = models.CharField(max_length=50)
    a_keyWord = models.CharField(max_length=100)
    a_describe = models.CharField(max_length=500)
    a_column = models.IntegerField(default=1)
    a_label = models.CharField(max_length=20)
    a_lastTime = models.DateField(auto_now=True)
    a_createTime = models.DateField(auto_now_add=True)
    a_state = models.BooleanField(default=True)
    a_isDelete = models.BooleanField(default=False)
    a_picture = models.ImageField(upload_to='static/mdeia/img', null=True)

    class Meta:
        db_table = 'articles'