from django.contrib import admin
from .models import (Recipe, IngredientMaster, RecipeHistory,
                     RecipeStep, RecipePhoto)


class RecipeStepInline(admin.TabularInline):
    model = RecipeStep


class RecipePhotoInline(admin.TabularInline):
    model = RecipePhoto


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeStepInline, RecipePhotoInline]


class IngredientMasterdmin(admin.ModelAdmin):
    pass


class RecipeHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientMaster, IngredientMasterdmin)
admin.site.register(RecipeHistory, RecipeHistoryAdmin)
