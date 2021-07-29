from django.conf import settings
from graphene_django import DjangoObjectType

from blog import models
import graphene

from django.contrib.auth import get_user_model

# классы для каждой модели
# Имя каждого класса должно заканчиваться на Type, потому что каждое из них соответствует типу GraphQL
class UserType(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

'''
класс Query, наследуемый от graphene.ObjectType
Этот класс объединит все созданные нами классы типов, и мы добавим к нему методы,
указывающие способы запроса моделей
Для каждого из атрибутов мы создадим метод решения запроса.
Мы разрешаем запрос, беря информацию, предоставленную в запросе,
и возвращая в ответ соответствующий запрос Django.
Метод каждого преобразователя должен начинаться с resolve_,
а остальная часть имени должна соответствовать атрибуту.
Например, метод разрешения запросов для атрибута all_posts
должен называться resolve_all_posts
'''
class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

# Создаем переменную схемы, которая обертывает класс Query в graphene.Schema, чтобы связать все это вместе
schema = graphene.Schema(query=Query)
