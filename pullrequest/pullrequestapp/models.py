from django.db import models

# Create your models here.
class User(models.Model):
    github-handle = models.CharField(max_length=50)
    connections = models.CharField()

    def __str__(self):
        return f'{self.github-handle} ({self.connections})'

class Connection(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user2 = models.CharField(User, on_delete=models.SET_NULL, null=True)
    isPending = models.BooleanField()
    messages = models.TextField()

    def __str__(self):
        return f'{self.user1} {self.user2} ({self.messages})'

class Message(models.Model):
    sender = models.ForeignKey(Connection, on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(Connection, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f'{self.sender} {self.recipient} ({self.timestamp} ({self.content}))'