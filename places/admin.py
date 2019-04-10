from django.contrib import admin
from .models import Article
from .models import Comment
from .models import Category,Gallery


class CategoryAdmin(admin.ModelAdmin):
	list_display=('name',)





admin.site.register(Category , CategoryAdmin)
#
admin.site.register(Gallery)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author','date','category','status')
    list_filter = ('date', 'author')
    search_fields = ('title','body')
    prepopulated_fields= {'slug':('title',)}
    raw_id_fields = ('author',)
admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display =('user','post','content','timestamp',)
    list_filter = ( 'user','timestamp',)
    search_fields = ('post','timestamp')
admin.site.register(Comment, CommentAdmin)

