# Generated by Django 3.2.6 on 2021-09-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0343_alter_useractivityinterval_index_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realmuserdefault",
            name="emojiset",
            field=models.CharField(
                choices=[
                    ("google", "Google modern"),
                    ("google-blob", "Google classic"),
                    ("twitter", "Twitter"),
                    ("text", "Plain text"),
                ],
                default="google",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="emojiset",
            field=models.CharField(
                choices=[
                    ("google", "Google modern"),
                    ("google-blob", "Google classic"),
                    ("twitter", "Twitter"),
                    ("text", "Plain text"),
                ],
                default="google",
                max_length=20,
            ),
        ),
    ]
