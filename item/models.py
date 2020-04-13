from django.db import models

from django.db.models import Max

from login.models import AccountStatus, ShopKeeperAccount

from api.naming_series import ImageName, DataBaseNaming

# Create your models here.

class ProductQtyType(models.Model):
	qty_type_id = models.CharField(max_length=50, primary_key=True)
	qty_type_name = models.CharField(max_length=50, null=False)
	idx = models.IntegerField(default=1)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "product_qty_type"

	def save(self, *args, **kwargs):
		self.idx = 1 if ProductQtyType.objects.aggregate(Max('idx'))['idx__max'] == None else ProductQtyType.objects.aggregate(Max('idx'))['idx__max']+1
		self.qty_type_id = DataBaseNaming(item_type="QTY", idx=self.idx)
		super(ProductQtyType, self).save(*args, **kwargs)

	def __str__(self):
		return self.qty_type_name

class Product(models.Model):
	product_id = models.CharField(max_length=50, primary_key=True)
	product_name = models.CharField(max_length=250, null=False)
	product_qty_type = models.ForeignKey(ProductQtyType,on_delete=models.CASCADE)
	product_qty = models.DecimalField(max_digits=10, decimal_places=2)
	product_price = models.DecimalField(max_digits=10, decimal_places=2)
	status = models.ForeignKey(AccountStatus,on_delete=models.CASCADE)
	idx = models.IntegerField(default=1)
	added_by = models.ForeignKey(ShopKeeperAccount, on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "product"

	def save(self, *args, **kwargs):
		self.idx = 1 if Product.objects.aggregate(Max('idx'))['idx__max'] == None else Product.objects.aggregate(Max('idx'))['idx__max']+1
		self.product_id = DataBaseNaming(item_type="PRO", idx=self.idx)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.product_name+" - "+self.product_id
