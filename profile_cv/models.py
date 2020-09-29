from django.db import models


# Create your models here.


class Technical_Skills(models.Model):
    category = models.CharField(max_length=250)
    skill = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}--{}'.format(self.category,self.skill)


class Award_Achievements(models.Model):
    time_line = models.CharField(max_length=250)
    des = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}--{}'.format(self.time_line,self.des)


class Draco_Profile_Image(models.Model):
    image = models.ImageField(upload_to='uploads/%d/%m/')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Work_Experiences(models.Model):
    time_line = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    website = models.URLField(null=True,blank=True)
    job = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'I worked at {} as {},{}'.format(self.location,self.job,self.time_line)


class Draco_Profile(models.Model):
    user = models.ForeignKey('auth.User',related_name='profile_cv',on_delete=models.CASCADE)
    profile_image = models.ForeignKey(Draco_Profile_Image,related_name='my_profile_image',on_delete=models.CASCADE,
                                      blank=True,null=True)
    awards = models.ManyToManyField(Award_Achievements,related_name='my_award',blank=True)
    works = models.ManyToManyField(Work_Experiences,related_name='my_works',blank=True)
    skills = models.ManyToManyField(Technical_Skills,related_name='my_skills',blank=True)
    location = models.CharField(max_length=250)
    des = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.location

# user = Draco_Profile.objects.get(user_id=1)
# user.profile_image.title
# user.profile_image.image.url
# works = user.works.all()
# awards = user.awards.all()
# tech = user.skills.all()
