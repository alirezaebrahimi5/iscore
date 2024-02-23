from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# from django_jalali.db import models as jmodels


class AllUser(BaseUserManager):
    def create_user(self, nid, mobile, password=None, **kwargs):

        if not mobile:
            raise ValueError('کاربر باید شماره تلفن داشته باشد')
        
        if not nid:
            raise ValueError('کاربر باید کدملی داشته باشد')

        user = self.model(
            nid=nid,
            mobile=mobile,
            **kwargs,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, nid, mobile, password):
        user = self.create_user(
            mobile=mobile,
            password=password,
            nid=nid
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, nid, mobile, password):
        user = self.create_user(
            mobile=mobile,
            password=password,
            nid=nid
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class Role:
    Management = 1
    Sales_Manager = 2
    Supporter = 3
    Consultant = 4
    Accounting = 5
    MEDREP_Visitor = 6
    Visitor = 7
    
    ROLES = (
        (Management, 'مدیر'),
        (Sales_Manager, 'سرپرست فروش'),
        (Supporter, 'پشتیبانی'),
        (Consultant, 'مشاور'),
        (Accounting, 'حسابدار'),
        (MEDREP_Visitor, 'پخش کننده نماینده پزشکی'),
        (Visitor, 'پخش کننده'),
    )


class User(AbstractBaseUser):
    alphanumeric       = RegexValidator(r'^[0-9a-zA-Z]*$', message='فقط نمادهای الفبایی و اعداد پذیرفته میشوند')
    numbers            = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    nid = models.CharField(max_length=11, unique=True, validators=[numbers], verbose_name='شماره ملی')
    mobile             = models.CharField(max_length=11, unique=True, validators=[numbers], verbose_name='شماره همراه')
    is_active          = models.BooleanField(default=False, null=False, verbose_name='وضعیت فعالیت')
    is_staff           = models.BooleanField(default=False, null=False, verbose_name='دسترسی ادمین')
    is_superuser       = models.BooleanField(default=False, null=False, verbose_name='مدیر')
    joined_at          = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    objects = AllUser()

    USERNAME_FIELD  = 'nid'
    REQUIRED_FIELDS = ['mobile']

    def __str__(self) -> str:
        return f"{self.nid}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_otp")
    counter = models.IntegerField(default=3)
    otp  = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    first_name         = models.CharField(max_length=30, null=True, blank=True, verbose_name='نام')
    last_name          = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    address            = models.CharField(max_length=4096, null=True, blank=True, verbose_name = '')
    pic        = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name = 'عکس پروفایل')
    role       = models.PositiveSmallIntegerField(default=0, verbose_name='نقش کاربر')

    @property
    def fullName(self):
        return str(self.first_name) + " " + str(self.last_name)
    
    def __str__(self) -> str:
        return f"{self.user} {self.role}"
