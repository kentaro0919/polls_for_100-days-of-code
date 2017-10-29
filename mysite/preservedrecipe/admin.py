from django.contrib import admin
import nested_admin
from .models import (
    RecipeHistory, Classification,
    Recipe, IngredientMaster, RecipeStep, IngredientRecipe,
    RecipePhoto, IngredientPhoto, RecipeStepPhoto)


class IngredientMasterAdmin(admin.ModelAdmin):
    pass


class RecipeStepPhotoInline(nested_admin.NestedTabularInline):
    model = RecipeStepPhoto


class IngredientPhotoInline(nested_admin.NestedTabularInline):
    model = IngredientPhoto


class IngredientRecipeInline(nested_admin.NestedTabularInline):
    model = IngredientRecipe


class RecipeStepInline(nested_admin.NestedTabularInline):
    model = RecipeStep
    inlines = [RecipeStepPhotoInline]


class RecipePhotoInline(nested_admin.NestedStackedInline):
    model = RecipePhoto


class RecipeAdmin(nested_admin.NestedModelAdmin):
    inlines = [IngredientRecipeInline, RecipePhotoInline, RecipeStepInline, ]


class RecipeHistoryAdmin(admin.ModelAdmin):
    pass


class ClassificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeHistory, RecipeHistoryAdmin)
admin.site.register(IngredientMaster, IngredientMasterAdmin)
admin.site.register(Classification, ClassificationAdmin)
