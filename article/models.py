from django.db import models
from tinymce import models as tinymce_models



# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")  # 50 stringlik boş bi karakter alanı tutuyo
    content = tinymce_models.HTMLField(verbose_name="İçerik")
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye fotoğraf ekleyin.")
    created_date = models.DateTimeField(auto_now_add=True)  # autonow add oluşturulma tarihini güncel tarih yapıyor


    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="isim")
    comment_content = tinymce_models.HTMLField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

# from django.contrib.auth.models import User\n",
#     "from article.models import Article\n",
#     "newUser = User(username=\"denemekullanici\",password=\"123\")\n",
#     "newUser\n",