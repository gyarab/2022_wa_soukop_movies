from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_comment_movie_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]