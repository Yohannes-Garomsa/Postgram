import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission,
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404




class UserManager(BaseUserManager):
    # def get_object_by_public_id(self,public_id):
    #     try:
    #         instance=self.get(public_id=public_id)
    #         return instance
    #     except  (ObjectDoesNotExist, ValueError, TypeError):
    #         raise Http404
    
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a User with email, username and password."""
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('User must have an email')
        if password is None:
            raise TypeError('User must have a password')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a User with superuser (admin) permissions."""
        if password is None:
            raise TypeError("Superuser must have a password")
        if email is None:
            raise TypeError("Superuser must have an email")
        if username is None:
            raise TypeError("Superuser must have a username")
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True, default="")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    posts_liked = models.ManyToManyField("core_post.Post", related_name="liked_by")

    groups = models.ManyToManyField(
        Group,
        related_name="core_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="core_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    



