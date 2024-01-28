from django.db import models
from django.conf import settings

from product.models import Product


User = settings.AUTH_USER_MODEL


class VisitorTask(models.Model):
    sale_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saleManager")
    user         = models.ManyToManyField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="visitor")
    tasks        = models.ManyToManyField(Product, on_delete=models.CASCADE)
    start_at     = models.DateField()
    end_at       = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.sale_manager} {self.user} {self.start_at} {self.end_at}"


class VisitorTaskDone(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    compeleted_task = models.ForeignKey(VisitorTask, on_delete=models.CASCADE)
    task_done       = models.BooleanField()
    location        = models.Expression()
    
    def __str__(self) -> str:
        return f"{self.user} {self.compeleted_task} {self.task_done}"
