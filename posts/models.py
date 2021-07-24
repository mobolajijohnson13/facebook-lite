from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_num_of_likes(self):
        return Like.objects.filter(Post=self).count()
    
    
    
    def get_num_of_comments(self):
        return Comments.objects.filter(Post=self).count()



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ["user", "Posts"]




class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    

    class Meta:
        unique_together = ["user", "text"]
    
