from django.db import models

class Poonjee_Users(models.Model):
    email = models.CharField(max_length=200, primary_key = True)
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=1)
    status = models.CharField(max_length=1, default='A')
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return (self.email + '<>' + self.user_id)


class User_Credentials(models.Model):
    email = models.ForeignKey(Poonjee_Users, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return (self.password)

class Inventories(models.Model):
    inventory_name = models.CharField(max_length=30, blank=False)        
    description = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

class Products(models.Model):
    barcode = models.CharField(max_length=150, blank=False)
    product_name = models.CharField(max_length=200)
    cost_price = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    selling_price = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)

class Seller_Info(models.Model):
    seller_name = models.CharField(max_length=50, blank=False, null=False)
    seller_desc = models.CharField(max_length=50, blank=False, null=False)
    seller_address = models.CharField(max_length=50, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=True)

class Accounts_Info(models.Model):
    account_name = models.CharField(max_length=50, blank=False, null=False)
    account_desc = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(Poonjee_Users, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True, blank=True)

class Purchase_Transactions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    seller_id = models.ForeignKey(Seller_Info, on_delete=models.CASCADE)
    user = models.ForeignKey(Poonjee_Users, on_delete=models.CASCADE)
    account_used = models.ForeignKey(Accounts_Info, on_delete=models.CASCADE)
    transaction_amt = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

class Product_Location(models.Model):
    barcode = models.ForeignKey(Products, on_delete=models.CASCADE)   
    inventory = models.ForeignKey(Inventories, on_delete = models.CASCADE) 
    transaction_id = models.ForeignKey(Purchase_Transactions, on_delete = models.CASCADE)
    total_qty = models.IntegerField(blank=False,null=False)

class Sales_Transactions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    sale_type = models.CharField(max_length=15, blank=False, null=False)
    user = models.ForeignKey(Poonjee_Users, on_delete=models.CASCADE)
    transaction_amt = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    account_used = models.ForeignKey(Accounts_Info, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, blank=False)

class Sales_Details(models.Model):
    transaction_id = models.IntegerField()
    barcode = models.CharField(max_length=150, blank=False)
    cost_price = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    selling_price = models.DecimalField(max_digits=22, decimal_places=2, blank=False, null=False)
    sale_date = models.DateTimeField(auto_now_add=True, blank=False)

class Product_Shelf_Duration(models.Model):
    barcode = models.ForeignKey(Products, on_delete=models.CASCADE)
    latest_in_date = models.DateTimeField(auto_now_add=False, blank=True)    
    latest_out_date = models.DateTimeField(auto_now_add=False, blank=True)
