# Generated by Django 3.2.13 on 2024-01-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigScreen', '0002_bigscreen_comprehensive_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigscreen',
            name='comprehensive_score',
            field=models.IntegerField(blank=True, help_text='综合得分', null=True),
        ),
    ]
