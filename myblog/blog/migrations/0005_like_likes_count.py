# Generated by Django 5.0.4 on 2024-05-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_author_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]