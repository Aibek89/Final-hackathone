from django.contrib import admin

from post.models import Post, Like, Image, Favorite, Contact

admin.site.register(Like)
admin.site.register(Image)
admin.site.register(Favorite)
admin.site.register(Contact)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    list_display = ['id', 'title', 'text']


admin.site.register(Post, PostAdmin)
