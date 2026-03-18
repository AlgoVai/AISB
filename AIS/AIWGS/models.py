from django.db import models

# Create your models here.

class Users(models.Model):
    userId=models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30,null=False)
    LastName = models.CharField(max_length=30,null=False)
    Age = models.IntegerField(null=False)
    url = models.CharField(null=True,max_length=1000)
    Phone = models.CharField(null=False,max_length=50)
    Password = models.CharField(null=True,max_length=50)
    Email = models.CharField(null=False,max_length=255)
    InstituteId = models.IntegerField(null=False)
    BranchId = models.IntegerField(null=True)
    userTypeId = models.IntegerField(null=False)
    IsActive = models.BooleanField(null=False)
    def __str__(self):
        return self.FirstName
    class Meta:
        db_table = "Users"
        ordering = ['-userId']
    

class DataStatusType(models.Model):
    typeId  = models.IntegerField(primary_key=True)
    typeName = models.CharField(null=False,max_length=222)
    def __str__(self):
        return self.typeName
    class Meta:
        ordering= ['-typeId']
    


class DataStatus(models.Model):
    StatusId = models.IntegerField(primary_key=True)
    StatusTypeId = models.ForeignKey(DataStatusType,
                                     on_delete=models.CASCADE)
    StatusName = models.CharField(null=False,max_length=255)
    createdAt = models.DateTimeField(null=False)
    IsActive = models.BooleanField(null=False,default=True)
    def __str__(self):
        return self.StatusName
    class Meta:
        ordering = ['-StatusId']



    








    

    

    




    
