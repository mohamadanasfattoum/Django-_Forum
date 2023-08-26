# Generated by Django 4.2 on 2023-08-26 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Quetion_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_question', to='question.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quetion_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]