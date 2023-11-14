from django.contrib import admin

from product.models import Book, Category, Publisher


class BookCategoriesInline(admin.StackedInline):
    model = Book.categories.through


class BookPublisherInline(admin.StackedInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'last_update')
    search_fields = ('title', 'year')
    readonly_fields = ('last_update',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookCategoriesInline]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookPublisherInline]
