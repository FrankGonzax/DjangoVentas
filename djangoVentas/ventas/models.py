from django.db import models

class person(models.Model):
    document = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return self.document

#Sale (venta) = llave foranea
class sale(models.Model):
    document_p = models.ForeignKey(person, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField("date published")

    def __str__(self):
        return self.document_p
