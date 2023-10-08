from django.contrib import admin
from .models import Product, Category, Review, SizeCategory, ProductSize


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'product', 'content',
                    'rating', 'created_at', 'approved')
    search_fields = ('user', 'product', 'content')
    list_filter = ('approved', 'created_at')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('size_category', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(SizeCategory, SizeCategoryAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
