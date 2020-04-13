from django.db import models

from django.db.models import Max

from api.naming_series import ImageName, DataBaseNaming

# Create your models here.

class AllImage(models.Model):
	image_id = models.CharField(max_length=50, primary_key=True)
	image_name = models.CharField(max_length=100, null=False)
	image_data = models.CharField(max_length=5000, null=False)
	parent_type = models.CharField(max_length=50, null=False)
	parent_id = models.CharField(max_length=50, null=False)
	display_image = models.BooleanField(default=False)
	idx = models.IntegerField(default=1)
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "image"

	def save(self, *args, **kwargs):
		self.idx = 1 if AllImage.objects.aggregate(Max('idx'))['idx__max'] == None else AllImage.objects.aggregate(Max('idx'))['idx__max']+1
		self.image_id = DataBaseNaming(item_type="IMG", idx=self.idx)
		super(AllImage, self).save(*args, **kwargs)

	def __str__(self):
		return self.image_id
