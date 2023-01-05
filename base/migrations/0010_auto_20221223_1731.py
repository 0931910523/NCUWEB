# Generated by Django 3.2.7 on 2022-12-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_report_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Subject',
            field=models.IntegerField(choices=[(0, '中國文學系'), (1, '英美語文學系'), (2, '法國語文學系'), (3, '文學院學士班'), (6, '化學系'), (7, '光電科學與工程學系'), (8, '理學院學士班'), (9, '土木工程學系'), (10, '機械工程學系'), (11, '化學工程與材料工程學系'), (12, '工學院學士班'), (13, '企業管理學系'), (14, '資訊管理學系'), (15, '財務金融學系'), (16, '經濟學系'), (17, '電機工程學系'), (18, '資訊工程學系'), (19, '通訊工程學系'), (20, '資訊電機學院學士班'), (21, '大氣科學學系'), (22, '地球科學學系'), (23, '太空工程與科學學系'), (24, '地科院學士班'), (25, '客家語文暨社會科學學系'), (26, '生命科學系'), (27, '生醫工程與科學學系')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='real_first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='real_last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
