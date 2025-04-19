from django.db import models
from django.core.validators import MinValueValidator

from decimal import Decimal

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name 
    
    

class Book(models.Model):
    status_book = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Rental', 'Rental'),
    ]

    title = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photos', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rental_price_day = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rental_period = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])

    # ✅ هذا الحقل سيتم حسابه تلقائيًا، لذلك لا يظهر في الفورم
    total_rental = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)

    active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=status_book, default='Available')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.status == 'Rental' and self.rental_price_day and self.rental_period:
            self.total_rental = Decimal(self.rental_price_day) * Decimal(self.rental_period)
            print("📦 total_rental being calculated:", self.total_rental)
        else:
            self.total_rental = None
            print("📦 total_rental = None")
        super().save(*args, **kwargs)
        
    class Meta:
        unique_together = ('title', 'author')



    def __str__(self):
        return self.title or "كتاب بدون عنوان"




