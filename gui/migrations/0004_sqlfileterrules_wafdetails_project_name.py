# Generated by Django 4.0.2 on 2022-04-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0003_wafdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='SQlFileterRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('SQLFilterStr', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='wafdetails',
            name='project_name',
            field=models.CharField(default='sgn', max_length=200),
            preserve_default=False,
        ),
    ]
