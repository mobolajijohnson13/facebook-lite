from django.test import TestCase

# Create your tests here.

from typing import Text
from django.db.models.fields import TextField, json
from django.db.models.fields.related import ForeignKey
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Comments, Like,Post
from django.db import models


class PostTests(APITestCase):
    def test_create_post(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="lami", password="password123")

        url = reverse('post-list')
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

#     def test_get_post(self):
#             """
#             Ensure we can create a new tweet object.
#             """
        
#             user_instance = User.objects.create_user(username="lami", password="password123")#this is admin that create the tweet
#             post =Post.objects.create(text="this is a simple tweet", user=user_instance)#this is admin that create the tweet

#             url = reverse('post-detail', kwargs={'pk': post.id})
#             response = self.client.get(url)
#             response_data = response.json()
#             # print()

#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(Post.objects.count(), 1)
#             self.assertEqual(response_data['text'], post.text)


#     def test_get_one_post(self):
#         """
#         Ensure we can create a new tweet object.
#         """

#         user_instance = User.objects.create_user(username="lami", password="password123")#this is admin that create the tweet
#         post =Post.objects.create(text="this is a simple post", user=user_instance)#this is admin that create the tweet

#         url = reverse('post-list')
#         response = self.client.get(url)
#         response_data = response.json()
#         # print()

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Post.objects.count(), 1)
#         self.assertEqual(response_data[0]['text'],post.text)



#     def test_put_post(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('post-detail', kwargs={'pk': post.id})
#         data = {'tweet': post.id, "user": user.id,'text':'this is a simple tweet'}
#         response = self.client.put(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


#     def test_patch_post(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('post-detail', kwargs={'pk': post.id})
#         data = {'post': post.id, "user": user.id,'text':'this is a simple tweet'}
#         response = self.client.patch(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)



#     def test_put_post(self):
#         """
#         Ensure we can create a new tweet object.
#         """
#         user = User.objects.create_user(username="lami", password="password123")
#         post =Post.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('post-detail',kwargs={'pk': post.id})
#         data = {'text': 'DabApps', "user": user.id}
#         response = self.client.put(url, data, format='json')
#         response_data = response.json()
#         print()

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        


# class LikeTests(APITestCase):
#     def test_create_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('like-list')
#         data = {'post': post.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class LikeTests(APITestCase):
#     def test_get_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         # like = Like.objects.create(ForeignKey(tweet,on_delete=models.CASCADE))

#         url = reverse('like-list')
#         data = {'post': post.id, "user": user.id}
#         response = self.client.get(url)
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Like.objects.count(), 0)
#         # self.assertEqual(Like.objects.get().text, data['text'])
#         # self.assertEqual(response_data['text'], data['text'])



#     def test_post_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
        
#         url = reverse('like-list')
#         data = {'post': post.id, "user": user.id}
#         response = self.client.post(url,data,format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Like.objects.count(), 1)
        

#     def test_delete_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
        
#         url = reverse('like-detail',kwargs={'pk': post.id})
#         data = {'post': post.id, "user": user.id}
#         response = self.client.delete(url,data,format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(Like.objects.count(), 0)
        
# class CommentsTests(APITestCase):
#     def test_create_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """

#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post=post)

#         url = reverse('comments-list')
#         data = {'post': post.id, "user": user.id,'text':'babaaaaa eba lo le shey  babaaaaa'}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#     def test_get_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """

#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post=post)

#         url = reverse('comments-list')
#         data = {'post': post.id, "user": user.id,'text':'babaaaaa eba lo le shey  babaaaaa'}
#         response = self.client.get(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


#     def test_post_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """

#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post = post)

#         url = reverse('comments-list')
#         data = {'post': post.id, "user": user.id,'text':'babaaaaa eba lo le shey  babaaaaa'}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
#     def test_patch_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """

#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post=post)

#         url = reverse('comments-detail', kwargs={'pk': post.id})
#         data = {'tweet': post.id, "user": user.id,'text':'babaaaaa eba lo le shey  babaaaaa'}
#         response = self.client.patch(url, data, format='json')
#         response_data = response.json()
#         print(response_data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_comments(self):
#         """
#         Ensure we can get a new commnt object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post=post)

#         url = reverse('comments-list')
#         response = self.client.get(url, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Comments.objects.count(), 1)
#         self.assertEqual(response_data[0]['text'], comment.text)
          
#     def test_put_comments(self):
#         """
#         Ensure we can put a comment object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comments", user=user, post=post)

#         url = reverse('comments-detail', kwargs={'pk': comment.id})
#         data = {'post': post.id, "user": user.id,'text':'oloyede ni awon angeli'}
#         response = self.client.put(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Comments.objects.count(), 1)
           
#     def test_delete_comments(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
#         comment = Comments.objects.create(text="this is a comment", user=user, post=post)

#         url = reverse('comments-detail', kwargs={'pk': comment.id})
#         response = self.client.delete(url)

#         print(response.content)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Comments.objects.count(), 0)
     
#     def test_patch_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="john", password="password123")
#         post = Post.objects.create(text="this is a simple tweet", user=user)
        

#         url = reverse('like-detail', kwargs={'pk': post.id})
#         data = {'tweet': post.id, "user": user.id}
#         response = self.client.patch(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Like.objects.count(), 1)  

