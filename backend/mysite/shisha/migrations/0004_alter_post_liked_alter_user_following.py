# Generated by Django 5.0.4 on 2024-12-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shisha", "0003_shop_remove_post_user_name_post_liked_post_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="liked",
            field=models.ManyToManyField(
                blank=True, related_name="like", to="shisha.user"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="followed_by", to="shisha.user"
            ),
        ),
    ]
