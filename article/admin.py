from django.contrib import admin

# Register your models here.
from .models import Article,Comment

# admin.site.register(Article)
#


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["author__username"]
    list_filter = ["title"]

    class Meta:
        model = Article




admin.site.register(Comment)

# django admin site documentation