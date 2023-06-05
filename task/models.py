from accounts.models import User
from django.db import models

# Create your models here.


class TodoList(models.Model):
    
    STATUS =[ 
            ("No Progress","No Progress"),
            ("In Progress","In Progress"),
            ("Completed","Completed")
            ]
    
    PRIORITY =[("Low","Low"),
               ("High","High")
               ]
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    status          = models.CharField(max_length=200,choices=STATUS, default="No Progress")
    priority        = models.CharField(max_length=200,choices=PRIORITY)
    due_date        = models.DateField(auto_now_add=False,null=True,blank=True)
    assign_to       = models.ManyToManyField(User,related_name="assign_to")
    created_by      = models.ForeignKey(User,on_delete = models.CASCADE ,blank=True,null=True,related_name='created_by')
    
    
    class Meta:
        permissions = (
           ("view", "Can view the task "),
           ("can_create", "Can create a task"),
     )
    
    def __str__(self):
        return self.title

