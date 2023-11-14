from django.db import models


class Publisher(models.Model):
    title = models.CharField(max_length=31, blank=False, verbose_name='نام')


class Category(models.Model):
    title = models.CharField(max_length=31, blank=False, verbose_name='نام')


class Book(models.Model):
    title = models.CharField(max_length=31, blank=False, verbose_name='نام')
    create_date = models.DateField(null=True, blank=True, verbose_name='تاریخ ایجاد')
    last_update = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='books', blank=False)
    publisher = models.ForeignKey(Publisher, related_name='books', null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت')

    def __str__(self):
        return f"{self.title} - {self.create_date}"

    # def clean(self):
    #     if self.price > 10000:
    #         super(Book, self).clean()
    #     else:
    #         raise ValidationError('price > 10.000')

    # def save(self, *args, **kwargs):
    #     if self.price < 2000:
    #         raise ValueError('price < 2000')
    #     super(Book, self).save()
