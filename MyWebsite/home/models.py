from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=1000, null=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Equity', 'Equity'),
			('Debt', 'Debt'),
			('Liquid ', 'Liquid'),
			('Others', 'Others'),
			)

	scheme_name	 = models.CharField(max_length=200, null=True)
	AMC = models.ManyToManyField(Tag)
	asset_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
	folio_No= models.CharField(max_length=200, null=True)
	investment_date	 = models.DateField(null=True)
	units = models.FloatField(null=True)
	purchase_nav = models.IntegerField(null=True)
	purchase_value = models.IntegerField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.scheme_name




class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Accept', 'Accept'),
		('Rejected', 'Rejected'),
	)

	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



