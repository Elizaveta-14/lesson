# Generated by Django 5.2.3 on 2025-06-11 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название курса (до 160 символов).",
                        max_length=160,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview_img",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение для превью курса (необязательно).",
                        null=True,
                        upload_to="course_previews/",
                        verbose_name="Превью курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите подробное описание курса.",
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название урока (до 160 символов).",
                        max_length=160,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите подробное описание урока.",
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview_img",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение для превью урока (необязательно).",
                        null=True,
                        upload_to="lesson_previews/",
                        verbose_name="Превью урока",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True,
                        help_text="Введите URL-адрес видео для урока (необязательно).",
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="Выберите курс, к которому относится данный урок.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="study.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
    ]
