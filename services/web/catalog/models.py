from django.db import models
from django.conf import settings

class ProductOffer(models.Model):
    MARKETPLACE_CHOICES = [
        ('ozon', 'Ozon'),
        ('wb', 'Wildberries'),
        ('ym', 'Yandex Market'),
    ]
    marketplace = models.CharField(max_length=25, choices=MARKETPLACE_CHOICES, 
    default='ozon', verbose_name="Marketplace", 
    help_text="Выберите маркетплейс, на котором размещено предложение.")

    title = models.CharField(max_length=200)

    external_id = models.CharField(max_length=100, unique=True, db_index=True, 
    verbose_name="ID товара", 
    help_text="Уникальный идентификатор предложения на маркетплейсе.")

    url = models.URLField(max_length=1000, verbose_name="ссылка на предложение",
    help_text="URL предложения на маркетплейсе.")

    image_url = models.URLField(max_length=1000, verbose_name="ссылка на изображение",
    help_text="URL изображения товара на маркетплейсе.")

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена",
    help_text="Цена предложения на маркетплейсе.")

    created_by = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания",
    help_text="Дата и время создания предложения в системе.")

    updated_by = models.DateTimeField(auto_now=True, verbose_name="Дата обновления",
    help_text="Дата и время последнего обновления предложения в системе.")

    class Meta:
        verbose_name = "Предложение товара"
        verbose_name_plural = "Предложения товаров"
        unique_together = ('marketplace', 'external_id')

    def __str__(self):
        return f"{self.title} ({self.marketplace}) {self.price} ₽"
    
class FavoriteItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
    related_name='favorite_items', verbose_name="Пользователь", 
    help_text="Пользователь, который добавил предложение в избранное.")

    product = models.ForeignKey(ProductOffer, on_delete=models.CASCADE, 
    related_name='favorited_by', verbose_name="Предложение товара", 
    help_text="Предложение товара, добавленное в избранное пользователем.")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления",
    help_text="Дата и время добавления предложения в избранное.")

    class Meta:
        verbose_name = "Избранное предложение"
        verbose_name_plural = "Избранные предложения"
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
    
class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
    related_name='search_queries', verbose_name="Пользователь", 
    help_text="Пользователь, который выполнил поиск.")

    query = models.CharField(max_length=255, verbose_name="Поисковый запрос", 
    help_text="Текст поискового запроса, введенного пользователем.")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата поиска",
    help_text="Дата и время выполнения поискового запроса.")

    class Meta:
        verbose_name = "Поисковый запрос"
        verbose_name_plural = "Поисковые запросы"
        ordering = ['-created_at']

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{username} - {self.query}"
    