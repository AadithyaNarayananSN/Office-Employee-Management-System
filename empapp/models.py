from django.db import models

# Create your models here.


from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name


class department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.name


# both of the above model codes should be coded above employee model code.Otherwise there will
# be error in Foreignkey .In () of foreign key we have metioned model name of that key.so if the
# code is not above employee model code,those model name will return name error.


class employee(models.Model):
    firstname = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50)
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField()
    hiredate = models.DateField()
    def __str__(self):
        return "%s  " %(self.firstname)








class regmodel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)


