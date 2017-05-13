from django.db import models

# Create your models here.


class Screenshot(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='screenshot/')
	pos_x = models.IntegerField(default=0, blank=True, null=True)
	pos_y = models.IntegerField(default=0, blank=True, null=True)
	
	def __str__(self):
		return self.name
	def set_position(self, x, y):
		self.pos_x = x
		self.pos_y = y
		self.save()

