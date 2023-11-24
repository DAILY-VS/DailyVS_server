# Generated by Django 4.2.4 on 2023-11-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', '남성(Man)'), ('W', '여성(Woman)')], max_length=1, null=True, verbose_name='성별')),
                ('mbti', models.CharField(choices=[('INFP', 'INFP'), ('ENFP', 'ENFP'), ('INFJ', 'INFJ'), ('ENFJ', 'ENFJ'), ('INTJ', 'INTJ'), ('ENTJ', 'ENTJ'), ('INTP', 'INTP'), ('ENTP', 'ENTP'), ('ISFP', 'ISFP'), ('ESFP', 'ESFP'), ('ISFJ', 'ISFJ'), ('ESFJ', 'ESFJ'), ('ISTP', 'ISTP'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('ESTJ', 'ESTJ')], max_length=4, null=True, verbose_name='MBTI')),
                ('age', models.CharField(choices=[('10', '10대'), ('20_1', '20대 초반'), ('20_2', '20대 후반'), ('30_1', '30대 초반'), ('30_2', '30대 후반'), ('40', '40대 이상')], max_length=4, null=True, verbose_name='나이')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('point', models.IntegerField(default=0, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
