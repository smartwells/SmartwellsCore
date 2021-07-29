from django.db import models

from django.conf import settings

class Profile(models.Model):				# класс, описывающий модель профиля
    user = models.OneToOneField(			# связь с пользователем Django (связь один-к-одному)
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)		# опциональный URL, по которому можно узнать больше о пользователе
    bio = models.CharField(max_length=240, blank=True)	# о себе

    def __str__(self):					# для удобного отображения профилей в панели администратора
        return self.user.get_username()

class Tag(models.Model):				# модель данных о категориях
    name = models.CharField(max_length=50, unique=True)	# поле имени

    def __str__(self):
        return self.name

class Post(models.Model):						# модель поста
    class Meta:								# подкласс для сортировки постов по дате публикации
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)		# заголовок
    subtitle = models.CharField(max_length=255, blank=True)		# подзаголовок
    slug = models.SlugField(max_length=255, unique=True)		# уникальная часть URL поста
    body = models.TextField()						# контент
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)	# Аргумент on_delete = models.PROTECT для поля author гарантирует, что при удалении постов мы случайно не удалим автора
    tags = models.ManyToManyField(Tag, blank=True)			# Каждый тег может быть связан со многими сообщениями, поэтому для поля tags используется отношение ManyToManyField
