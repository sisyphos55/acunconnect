# Generated by Django 5.0 on 2023-12-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AcunConUser", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="profile_pics"),
        ),
    ]
