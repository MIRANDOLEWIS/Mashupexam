from django.db import models
from django.contrib.auth.models import User


class Medicine(models.Model):
    id = models.AutoField(primary_key=True,help_text="Medicine Id")
    med_name = models.CharField(help_text="Enter The Medicine Name",max_length=1000)
    med_price = models.IntegerField(help_text="Price")
    disease = models.CharField(help_text="Disease (eg:Fever,Body Pain etc)",max_length=1000)
    main_user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return f"{self.id}:{self.med_name} : {self.disease}"

    
