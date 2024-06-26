# Generated by Django 5.0.6 on 2024-05-29 22:56

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_content_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='content2',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article'),
        ),
    ]
