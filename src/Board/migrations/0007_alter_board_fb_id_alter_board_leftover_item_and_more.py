# Generated by Django 5.0.6 on 2024-05-28 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Board", "0006_alter_board_user_id"),
        ("Organization", "0002_welfareorganization_delete_welfare_organization"),
        ("Users", "0007_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="fb_id",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Organization.food_bank",
                verbose_name="食物銀行",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="leftover_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Users.leftover",
                verbose_name="剩食編號",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="waste_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Users.waste",
                verbose_name="二手物品編號",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="wo_id",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Organization.welfareorganization",
                verbose_name="社福機構",
            ),
        ),
    ]
