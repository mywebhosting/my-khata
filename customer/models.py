from django.db import models

from login.models import AccountStatus

# Create your models here.

class CustomerAccount(models.Model):
	account_id = models.CharField(max_length=50, primary_key=True)
	first_name = models.CharField(max_length=100, null=False)
	middle_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=False)
	email_id = models.CharField(max_length=100, unique=True, null=False)
	phone_no = models.PositiveIntegerField(null=False)
	verify_email_id = models.BooleanField(default=False,null=False)
	verify_phone_no = models.BooleanField(default=False,null=False)
	status_id = models.ForeignKey(AccountStatus,on_delete=models.CASCADE)
	created_by = models.CharField(max_length=100, null=False)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'customer_account'

	def __str__(self):
		return self.account_id
