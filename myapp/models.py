from django.db import models
from django.contrib.auth.models import User
# Create your models here.
todos=[

    {"id":1,"task_name":"gbillpay","user":"ram"},
    {"id":2,"task_name":"task2","user":"ravi"},
    {"id":3,"task_name":"task3","user":"arjun"},
    {"id":4,"task_name":"task4","user":"aravind"},
    {"id":5,"task_name":"task5","user":"arjun"},
    {"id":6,"task_name":"task6","user":"hari"},

    
]

class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.task_name




# ORM object relational mapping

# create
# list
# update
# delete
# detail
 
# orm query for creating an object
# ----------------------------------------------------


# ModelName.objects.create(field1="value1",field2="value2"...............fieldn="valuen")

# Todos.objects.ceate(task_name="ebill",user="ram")


# orm query for fetching all objects
# ------------------------------------------------------------
# variablename=Modelname.objects.all()
# qs=Todos.objects.all


#  orm query for fetching a specific(single) object
# ----------------------------------------------------------------
#  variablename=modelname.objects.get()
#  td=Todos.objects.get(id=2)
#  td.task_name
#  td.user

# orm query for fetching multiple objects
# ----------------------------------------------------------

# variablename=modelname.objects.filter()
#  qs=Todos.objects.get(user="ravi")


#  orm query for update an object
# -----------------------------------------------------------

# modelname.objects.filter().update()
# Todos.objects.filter(id=1).update(task_name="electricitybill")


#  orm query for update an object
# ------------------------------------------------
# modelname.objects.filter().delete()
# Todos.objects.filter(id=1).delete()



# orm query to display without one 

# variablename=Modelname.objects.all().exclude()
# data=Todos.objects.all().exclude(user="ravi")


