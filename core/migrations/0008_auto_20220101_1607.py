# Generated by Django 3.1.1 on 2022-01-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_cotacao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotacao',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]