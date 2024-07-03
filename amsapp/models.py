from django.db import models


class cart(models.Model):
    user=models.CharField(max_length=50,blank=False)
    productid=models.IntegerField(max_length=4,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
    class Meta:
        db_table="cart_table"

class Registration(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=100, blank=False)
    role=models.IntegerField(max_length=2,blank=True,default=0)
    wallet = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    last_login=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "registration_table"


class Feedback(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=50, blank=False)
    feedback = models.TextField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Feedback_table"

class product(models.Model):
    pid=models.IntegerField(max_length=10, blank=False,unique=True)
    name = models.CharField(max_length=50, blank=False)
    price=models.IntegerField(max_length=10,blank=False,default=0)
    des=models.TextField(max_length=200, blank=False)
    imgurl=models.CharField(max_length=1000, blank=False)
    cid=models.IntegerField(max_length=4,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table="products_table"

class categories(models.Model):
    cid=models.IntegerField(max_length=4,blank=False,unique=True)
    name = models.CharField(max_length=50, blank=False)
    imgurl = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table="categories_table"

class payments(models.Model):
    user=models.CharField(max_length=40,blank=False)
    payid=models.CharField(max_length=30,blank=False,unique=True)
    amount=models.IntegerField(max_length=10,blank=False,default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_to=models.CharField(max_length=20)

    def __str__(self):
        return self.user

    class Meta:
        db_table="payments_table"









#a wallet for payments
# first every user has an extra field wallet default set to zero
#a new page to add money to wallet can be paid by paypal
#cart page shows both paypal and wallet as payment options but a hint that wallet payments are safer and faster