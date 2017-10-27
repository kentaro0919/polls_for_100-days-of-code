from django.db import models
from django.conf import settings
from django_extensions.db.fields import (CreationDateTimeField,
                                         ModificationDateTimeField)


class IngredientMaster(models.Model):
    name = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=200, default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class Recipe(models.Model):
    title = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __str__(self):
        return f"{self.title}"

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class QuantityMaster(models.Model):
    quantity = models.CharField(max_length=200, default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredientMaster = models.ForeignKey(
        IngredientMaster, on_delete=models.CASCADE)
    quantity = models.ForeignKey(QuantityMaster, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200, default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    name = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=200, default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class RecipeHistory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
# 写真　コメント


class IngredientPhoto(models.Model):
    name = models.CharField(max_length=255, default="")
    ingredient = models.ForeignKey(IngredientMaster, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Ingredient')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class RecipePhoto(models.Model):
    name = models.CharField(max_length=255, default="")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Recipe')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()


class RecipeStepPhoto(models.Model):
    name = models.CharField(max_length=255, default="")
    recipe = models.ForeignKey(RecipeStep, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='RecipeStep')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
