# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
import stdimage.utils
import dynamic_filenames


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                (
                    "image",
                    stdimage.models.StdImageField(
                        blank=True,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="{model_name}/{instance.title:slug}{ext}"
                        ),
                    ),
                ),
                ("description", models.TextField()),
                (
                    "date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("categories", models.ManyToManyField(to="blog.Category")),
            ],
            options={"ordering": ("date",)},
        ),
    ]
