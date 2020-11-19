from django.db import models


class Category(models.Model):
    category = models.CharField('Категориия', max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Note(models.Model):
    note = models.ForeignKey(Category, on_delete=models.CASCADE)
    note_name = models.CharField('Заметка', max_length=50)

    def __str__(self):
        return self.note_name

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Content(models.Model):
    note_name = models.OneToOneField(Note, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=50)
    note_text = models.TextField('Статья')
    coded_text = models.TextField('Зашифрованный текст')
    password = models.IntegerField('Пароль')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
