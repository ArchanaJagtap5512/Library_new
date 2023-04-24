from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)      # data new add karte hai to default = true 

    def __str__(self):
        return self.name   # price, author jo diy ao milega 
    

    class Meta:
        db_table = "book"   # table name 


#--------------------------------------------------------------------------------------


class BookForm(models.Model): # django create form
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length = 200)
    email = models.EmailField(null=True)


    def _str_(self):
        return self.name

    class Meta:
        db_table = "form"






# relation model

# class CommonName(models.Model):
#     name = models.CharField(max_length=100)


#     def __str__(self):
#         return self.name
    

# class College(CommonName):
#     address = models.CharField(max_length=100)


#     class Meta:
#         db_table = "College"


# class Principal(CommonName):
#     exprince = models.CharField(max_length=100)
#     College = models.OneToOneField(College, on_delete=models.CASCADE, related_name="principal")

#     class Meta:
#         db_table = "Principal"

    
# class Department(CommonName):
#     library = models.CharField(max_length=100)
#     College = models.ForeignKey(College, on_delete=models.CASCADE, related_name="Department")


#     class Meta:
#         db_table = "Department" 


# class Student(CommonName):
#     marks = models.IntegerField()
#     age = models.IntegerField()
#     dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="student")   # one to many 
    
    
    
#     class Meta:
#         db_table = "student"


# class Subjects(CommonName):
#     is_practical = models.BooleanField(default=False)
#     student = models.ManyToManyField(Student)
#     dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subject")
    


#     class Meta:
#         db_table = "subject"

