from django.forms import ModelForm
from .models import Article, Comment
from tinymce.widgets import TinyMCE
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ["author"]
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {'comment_content': TinyMCE(attrs={'cols': 80, 'rows': 30})}