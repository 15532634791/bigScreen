# Generated by Django 3.2.13 on 2024-01-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigScreen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigscreen',
            name='comprehensive_score',
            field=models.IntegerField(blank=True, help_text='综合得分', max_length=150, null=True),
        ),
    ]
