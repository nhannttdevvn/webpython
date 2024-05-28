from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Change forms register Django


class Catelogy(models.Model): 
    sub_catelory = models.ForeignKey('self',on_delete=models.CASCADE, related_name='sub_catelories',null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class CreateUserForm(UserCreationForm): #KE THUA CUA django
     class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image  = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id) 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])   
        return total 
    @property   
   
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems if item.product is not None])   
        return total 
    
    def get_total_for_product(self, product_id):
        product = Product.objects.get(id=product_id)
        order_items = self.orderitem_set.filter(product=product)
        total = sum([item.get_total for item in order_items])
        return total
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True,db_column='quality')
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        if self.product is not None:
            total = self.product.price * self.quantity
            return total
        else:
            return 0  

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    cyti = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    date_added = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.address