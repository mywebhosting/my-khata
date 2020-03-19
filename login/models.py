from django.db import models

# Create your models here.

class AccountStatus(models.Model):
	status_id = models.CharField(max_length=50, primary_key=True)
	status_name = models.CharField(max_length=50, null=False)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'account_status'

	def __str__(self):
		return self.status_name

class ShopKeeperAccount(models.Model):
	account_id = models.CharField(max_length=200, primary_key=True)
	first_name = models.CharField(max_length=100, null=False)
	middle_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=False)
	email_id = models.CharField(max_length=100, unique=True, null=False)
	phone_no = models.PositiveIntegerField(null=False)
	status_id = models.ForeignKey(AccountStatus,on_delete=models.CASCADE)
	created_by = models.CharField(max_length=100, null=False)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'shop_keeper_account'

	def __str__(self):
		return self.email_id

class LoginDetail(models.Model):
	login_detail_id = models.CharField(max_length=100, primary_key=True)
	login_id = models.CharField(max_length=100, unique=True, null=False)
	password = models.CharField(max_length=300, null=False)
	salt = models.CharField(max_length=10, null=False)
	account_type = models.CharField(max_length=20, null=False)
	account_id = models.ForeignKey(ShopKeeperAccount,on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'login_detail'

	def __str__(self):
		return self.login_id