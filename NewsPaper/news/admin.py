from django.contrib import admin
from .models import Comment, PostCategory, Post, Category, Author


def delete_news(modeladmin, request, queryset): # request — объект хранящий информацию о запросе
    # queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
    delete_news.short_description = 'Delete News'

# создаём новый класс для представления новостей в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями,
    # которые хотим видеть в таблице с товарами
    # генерируем список имён всех полей
    # для более красивого отображения
#    list_display = [field.name for field in Post._meta.get_fields()]
    list_display = ('author', 'date_created')
    # добавляем фильтры в админку
    list_filter = ('author', 'date_created', 'post_category')
    search_fields = ('author__authorUser__username', 'date_created', 'post_category__category_name')
    actions = [delete_news]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'rating')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('category_name', 'subscribers')
    search_fields = ('category_name', 'subscribers__username')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_time', 'user', 'comment_rating')
    list_filter = ('comment_time', 'user', 'comment_rating')
    search_fields = ('comment_time', 'user__username')


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Author, AuthorAdmin)
# admin.site.unregister(Post) # разрегистрируем