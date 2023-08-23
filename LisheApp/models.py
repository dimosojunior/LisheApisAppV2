from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not username:
#             raise ValueError("Your user name is required")
        
        

#         user=self.model(
#             email=self.normalize_email(email),
#             username=username,
            
            
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, username, password=None):
#         user=self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,

#         )
#         user.is_admin=True
#         user.is_staff=True
        
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user

    

  
# class MyUser(AbstractBaseUser):
#     email=models.EmailField(verbose_name="email", max_length=100, unique=True)
#     first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
#     username=models.CharField(verbose_name="user name", max_length=100, unique=True)
#     middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
#     last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
#     company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
#     phone=models.CharField(verbose_name="phone", max_length=15)
#     profile_image = models.ImageField(upload_to='media/', blank=True, null=True)
#     date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     # Role_Choices = (
#     #         ('MULTI TEACHER', 'MULTI TEACHER'),
#     #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
#     #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
#     #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
#     #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
#     #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
#     #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
#     #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
#     #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
#     #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
#     #     )

#     # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
#     last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
#     is_admin=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=True)
#     is_superuser=models.BooleanField(default=False)
#     hide_email = models.BooleanField(default=True)
    


#     USERNAME_FIELD="email"
#     REQUIRED_FIELDS=['username']
    
#     objects=MyUserManager()

#     def __str__(self):
#         return self.username


#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True






class Token(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="token")
    token = models.CharField(max_length=256, blank=True, null=True)



class Setting(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, default="settings_name")
    value = models.CharField(max_length=256, blank=True, null=False, default='')









class Lishe(models.Model):

    ItemName = models.CharField(max_length=500,blank=False,null=False)
    ItemDescription = models.TextField(max_length=1000,blank=True,null=True)
    ItemImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    status = models.CharField( default="LISHE", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Lishe"

    def __str__(self):
        return self.ItemName



class ElimuYaLishe(models.Model):

    Category = models.CharField(max_length=500,blank=False,null=False)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    Image = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    status = models.CharField( default="ELIMU YA LISHE", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ElimuYaLishe"

    def __str__(self):
        return self.Category


class BidhaaZetu(models.Model):

    ProductName = models.CharField(max_length=500,blank=False,null=False)
    ProductDescription = models.TextField(max_length=1000,blank=True,null=True)
    ProductImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    status = models.CharField( default="Bidhaa Zetu", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "BidhaaZetu"

    def __str__(self):
        return self.ProductName

#hii itavuta days zote na kuzidisplay

class Days(models.Model):
    #Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    DayName = models.CharField(default="Day one", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Days"

    def __str__(self):
        return self.DayName



class DayOne(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    #DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day one", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)



    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DayOne"

    def __str__(self):
        return self.Time


class DayTwo(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    #DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day two", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)


    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DayTwo"

    def __str__(self):
        return self.Time




class DayThree(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day three", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)



    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DayThree"

    def __str__(self):
        return self.Time


class DayFour(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day four", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)



    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DayFour"

    def __str__(self):
        return self.Time


class DayFive(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day five", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)



    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DayFive"

    def __str__(self):
        return self.Time


class DaySix(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day six", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)


    
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DaySix"

    def __str__(self):
        return self.Time


class DaySeven(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    DayName = models.CharField(default="Day seven", max_length=500, blank=False,null=False)
    Time_Choices = (
        ('ASUBUHI','ASUBUHI'),
        ('MCHANA', 'MCHANA'),
        ('JIONI', 'JIONI'),
        ('USIKU', 'USIKU'),
        )


    Time = models.CharField(max_length=100,choices=Time_Choices, blank=True,null=True)
    DayDescription = models.TextField(max_length=1000,blank=True,null=True)
    DayImage = models.ImageField(upload_to='media/ElimuYaLisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "DaySeven"

    def __str__(self):
        return self.Time






# class Vyakula(models.Model):
   
#     Name = models.CharField( default="WANGA", max_length=500,blank=False,null=False)
#     Created = models.DateTimeField(auto_now_add=True)
#     Updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = "Vyakula"

#     def __str__(self):
#         return self.Name




class MakundiYaChakula(models.Model):
   
    FoodCategory = models.CharField( default="WANGA", max_length=500,blank=False,null=False)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    Image = models.ImageField(upload_to='media/MakundiYaChakulaImages/',blank=True,null=True)
    status = models.CharField( default="ELIMU YA LISHE", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "MakundiYaChakula"

    def __str__(self):
        return self.FoodCategory



class PosterNaPicha(models.Model):
   
    Image = models.ImageField(upload_to='media/PosterNaPichaImages/',blank=False,null=False)
    status = models.CharField( default="ELIMU YA LISHE", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "PosterNaPicha"

    def __str__(self):
        return self.status













#-----------------------MWANZO WA LISHE OPTIONS-------------------






class Weeks(models.Model):
    #Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    WeekName = models.CharField(default="Wiki 1", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Weeks"

    def __str__(self):
        return self.WeekName




class TaarifaZaUjauzito(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="UJAZO WA MTOTO", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Mchanga kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaUjauzito"

    def __str__(self):
        return self.Title

class TaarifaZaUzitoZaidi(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="KUCHOKA MARA KWA MARA", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Wiki ya kwanza kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaUzitoZaidi"

    def __str__(self):
        return self.Title

class TaarifaZaWatoto(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="KULIA MARA KWA MARA", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Wiki ya kwanza kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaWatoto"

    def __str__(self):
        return self.Title

class TaarifaZaKisukari(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="MGONGO KUUMA", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Wiki ya kwanza kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaKisukari"

    def __str__(self):
        return self.Title

class TaarifaZaHiv(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="KUTOKWA NA VIPELE MWILINI", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Wiki ya kwanza kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaHiv"

    def __str__(self):
        return self.Title

class TaarifaZaFamilia(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="Description here", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Wiki ya kwanza kabisa",max_length=1000,blank=True,null=True)
    InformationImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "TaarifaZaFamilia"

    def __str__(self):
        return self.Title
        


class JeWajua(models.Model):
    Week = models.ForeignKey(Weeks, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)

    Title = models.CharField(default="WANGA", max_length=500,blank=False,null=False)
    Description = models.TextField(default="Inasaidia kuimarisha misuli ya tumbo", max_length=1000,blank=True,null=True)
    ItemImage = models.ImageField(upload_to='media/LisheImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "JeWajua"

    def __str__(self):
        return self.Title





class Week1(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 1", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week1"

    def __str__(self):
        return self.Time

class Week2(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 2", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week2"

    def __str__(self):
        return self.Time


class Week3(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 3", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week3"

    def __str__(self):
        return self.Time

class Week4(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 4", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week4"

    def __str__(self):
        return self.Time


class Week5(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 5", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week5"

    def __str__(self):
        return self.Time


class Week6(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 6", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week6"

    def __str__(self):
        return self.Time


class Week7(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 7", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week7"

    def __str__(self):
        return self.Time


class Week8(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 8", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week8"

    def __str__(self):
        return self.Time



class Week9(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 9", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week9"

    def __str__(self):
        return self.Time



class Week10(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 10", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week10"

    def __str__(self):
        return self.Time

class Week11(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 11", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week11"

    def __str__(self):
        return self.Time

class Week12(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 12", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week12"

    def __str__(self):
        return self.Time

class Week13(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 13", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week13"

    def __str__(self):
        return self.Time


class Week14(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 14", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week14"

    def __str__(self):
        return self.Time

class Week15(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 15", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week15"

    def __str__(self):
        return self.Time

class Week16(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 16", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week16"

    def __str__(self):
        return self.Time

class Week17(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 17", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week17"

    def __str__(self):
        return self.Time

class Week18(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 18", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week18"

    def __str__(self):
        return self.Time


class Week19(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 19", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week19"

    def __str__(self):
        return self.Time


class Week20(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 20", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week20"

    def __str__(self):
        return self.Time

class Week21(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 21", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week21"

    def __str__(self):
        return self.Time

class Week22(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 22", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week22"

    def __str__(self):
        return self.Time

class Week23(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 23", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week23"

    def __str__(self):
        return self.Time


class Week24(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 24", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week24"

    def __str__(self):
        return self.Time

class Week25(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 25", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week25"

    def __str__(self):
        return self.Time

class Week26(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 26", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week26"

    def __str__(self):
        return self.Time

class Week27(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 27", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week27"

    def __str__(self):
        return self.Time


class Week28(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 28", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week28"

    def __str__(self):
        return self.Time

class Week29(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 29", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week29"

    def __str__(self):
        return self.Time

class Week30(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 30", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week30"

    def __str__(self):
        return self.Time

class Week31(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 31", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week31"

    def __str__(self):
        return self.Time

class Week32(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 32", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week32"

    def __str__(self):
        return self.Time
class Week33(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 33", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week33"

    def __str__(self):
        return self.Time

class Week34(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 34", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week34"

    def __str__(self):
        return self.Time

class Week35(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 35", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week35"

    def __str__(self):
        return self.Time

class Week36(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 36", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week36"

    def __str__(self):
        return self.Time

class Week37(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 37", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week37"

    def __str__(self):
        return self.Time

class Week38(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 38", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week38"

    def __str__(self):
        return self.Time

class Week39(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 39", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week39"

    def __str__(self):
        return self.Time

class Week40(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 40", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week40"

    def __str__(self):
        return self.Time

class Week41(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 41", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week41"

    def __str__(self):
        return self.Time

class Week42(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 42", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week42"

    def __str__(self):
        return self.Time

class Week43(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 43", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week43"

    def __str__(self):
        return self.Time


class Week44(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 44", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week44"

    def __str__(self):
        return self.Time

class Week45(models.Model):
    Category = models.ForeignKey(Lishe, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    # DayName = models.ForeignKey(Days, max_length=500,on_delete=models.CASCADE, blank=False,null=False)
    WeekName = models.CharField(default="Wiki 45", max_length=500, blank=False,null=False)
    # Time_Choices = (
    #     ('ASUBUHI','ASUBUHI'),
    #     ('MCHANA', 'MCHANA'),
    #     ('JIONI', 'JIONI'),
    #     ('USIKU', 'USIKU'),
    #     )


    Time = models.CharField(default="BREAKFAST",max_length=100, blank=True,null=True)
    Description = models.TextField(max_length=1000,blank=True,null=True)
    FoodImage = models.ImageField(upload_to='media/WeekImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Week45"

    def __str__(self):
        return self.Time