
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mudur', '0006_textboxquestions'),
        ('training', '0008_auto_20160629_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='textboxquestion',
            field=models.ManyToManyField(to='mudur.TextBoxQuestions', verbose_name='Klasik Sorular', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='question',
            field=models.ManyToManyField(to='mudur.Question', verbose_name='\xc3\x87oktan Se\xc3\xa7meli Sorular', blank=True),
        ),
    ]
