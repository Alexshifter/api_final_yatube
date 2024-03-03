from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import CHAR_LIMIT

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг категории'
    )
    description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:CHAR_LIMIT]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписки'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='%(app_label)s _ %(class)s _unique_relationships',
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
        ]
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'[:CHAR_LIMIT]


class Post(models.Model):
    text = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Изображение')

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория',
    )

    class Meta:
        default_related_name = 'posts'
        ordering = ['pub_date']
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.author} добавил публикацию {self.text}'[:CHAR_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='К публикации'
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField('Дата добавления',
                                   auto_now_add=True,
                                   db_index=True)

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} добавил комментарий:{self.text}'[:CHAR_LIMIT]
