from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):

    category_title = models.CharField(max_length=100, verbose_name='название')
    category_description = models.TextField(verbose_name='описание')
    category_image = models.ImageField(upload_to='categories/', verbose_name='изображение', **NULLABLE)
    # administrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='администратор')

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Service(models.Model):

    services_title = models.CharField(max_length=100, verbose_name='название')
    services_description = models.TextField(verbose_name='описание')
    services_image = models.ImageField(upload_to='services/', verbose_name='изображение', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    deadline = models.CharField(max_length=100, verbose_name='срок выполнения')
    # administrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='администратор')

    def __str__(self):
        return self.services_title

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

#
# class Appointment(models.Model):
#
# service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='услуга')
# client = models.ForeignKey(users.User, on_delete=models.CASCADE, verbose_name='клиент')
# date = models.DateTimeField(verbose_name='дата и время')
#
# def __str__(self):
# return f'{self.client} - {self.service}, {self.date}'
# #
# class Meta:
# verbose_name = "запись на услугу"
# verbose_name_plural = "записи на услугу"
