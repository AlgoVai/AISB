from django.db import models

# Create your models here.


class DataStatusType(models.Model):
    typeId  = models.AutoField(primary_key=True)
    typeName = models.CharField(null=False,max_length=222)
    def __str__(self):
        return self.typeName
    class Meta:
        db_table = 'DataStatusType'
        ordering= ['-typeId']
    
class Institute(models.Model):
    InstituteId = models.AutoField(primary_key=True)
    Name = models.CharField(null=False)
    Url = models.ImageField(null=True,upload_to="InstituteImage/")
    Created_At = models.DateTimeField(null=False)
    Address = models.CharField(null=False)
    IsActive = models.BooleanField(default=False,null=False)
    class Meta:
        db_table = "Institute"
        ordering = ["-InstituteId"]


class Users(models.Model):
    userId=models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30,null=False)
    LastName = models.CharField(max_length=30,null=False)
    Age = models.IntegerField(null=False)
    url = models.ImageField(null=True,upload_to="userImages/")
    Phone = models.CharField(null=False,max_length=50)
    Password = models.CharField(null=True,max_length=50)
    Email = models.CharField(null=False,max_length=255)
    InstituteId = models.ForeignKey(Institute,on_delete=models.CASCADE,null=True)
    BranchId = models.IntegerField(null=True)
    userTypeId = models.IntegerField(null=False)
    IsActive = models.BooleanField(null=False)
    Created_At = models.DateTimeField(null=True)
    def __str__(self):
        return self.FirstName
    class Meta:
        db_table = "Users"
        ordering = ['-userId']
    



class DataStatus(models.Model):
    StatusId = models.AutoField(primary_key=True)
    StatusTypeId = models.ForeignKey(DataStatusType,
                                     on_delete=models.CASCADE)
    InstituteId = models.ForeignKey(Institute, on_delete=models.CASCADE)
    StatusName = models.CharField(null=False,max_length=255)
    createdAt = models.DateTimeField(null=False)
    IsActive = models.BooleanField(null=False,default=True)
    def __str__(self):
        return self.StatusName
    class Meta:
        db_table = "DataStatus"
        ordering = ['-StatusId']



class Roles(models.Model):
    Role_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=1000)
    IsActive = models.BooleanField(default=True)
    class Meta:
        db_table = "Roles"
        ordering = ["-Role_Id"]


class UserRoles(models.Model):
    userRoleId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    roleId = models.ForeignKey(Roles,on_delete=models.CASCADE)
    AssignedAt = models.DateTimeField()
    class Meta:
        db_table = "UserRoles"
        ordering = ["-userRoleId"]



class Modules(models.Model):
    moduleId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)
    Code = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    class Meta:
        db_table = "Modules"
        ordering = ["-moduleId"]


class Permissions(models.Model):
    permissionId = models.AutoField(primary_key=True)
    codeName = models.CharField(max_length=200)
    Name = models.CharField(max_length=500)
    modeuleId = models.ForeignKey(Modules,on_delete=models.CASCADE)
    httpMethod = models.CharField(max_length=1000)
    urlPatter  = models.CharField(null=True)
    IsActive = models.BooleanField(default=False)
    class Meta:
        db_table = "Permissions"
        ordering = ["-permissionId"]


class RolesPermissions(models.Model):
    rolePermissionId = models.AutoField(primary_key=True)
    roleId = models.ForeignKey(Roles,on_delete=models.CASCADE)
    PermissionId = models.ForeignKey(Permissions,on_delete=models.CASCADE)
    grantedAt = models.DateTimeField()
    class Meta:
        db_table = "RolePermissions"
        ordering = ["-rolePermissionId"]




    




    








    

    

    




    
