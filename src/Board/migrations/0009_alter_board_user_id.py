# Generated by Django 5.0.6 on 2024-05-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Board", "0008_remove_board_fb_id_remove_board_leftover_item_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="user_id",
            field=models.CharField(max_length=5),
        ),
    ]