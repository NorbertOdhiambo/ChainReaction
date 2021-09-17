from django.db import models


class HomePage(models.Model):
    img1 = models.ImageField(upload_to='images/page1_imgs', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/page1_imgs', null=True, blank=True)
    img3 = models.ImageField(upload_to='images/page1_imgs', null=True, blank=True)
    img4 = models.ImageField(upload_to='images/page1_imgs', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)


class ServicePage(models.Model):
    img1 = models.ImageField(upload_to='images/service_page_imgs', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/service_page_imgs', null=True, blank=True)
    img3 = models.ImageField(upload_to='images/service_page_imgs', null=True, blank=True)
    video = models.FileField(upload_to='images/service_page_video', null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)


class BlogPage(models.Model):
    img1 = models.ImageField(upload_to='images/blog_page_imgs', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/blog_page_imgs', null=True, blank=True)
    img3 = models.ImageField(upload_to='images/blog_page_imgs', null=True, blank=True)
    video = models.FileField(upload_to='images/blog_page_video', null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)


class ServicesPage(models.Model):
    img1 = models.ImageField(upload_to='images/services_page_imgs', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/services_page_imgs', null=True, blank=True)
    # img3 = models.ImageField(upload_to='images/services_page_imgs', null=True, blank=True)
    # video = models.FileField(upload_to='images/services_page_video', null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)


class ContactPage(models.Model):
    img1 = models.ImageField(upload_to='images/contact_page_imgs', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/contact_page_imgs', null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)


class ScheduledRepair(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    scheduled_date = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
