"""
Definition of models.
"""

from django.db import models



# Create your models here.


class StateModel(models.Model):
    name = models.CharField(max_length=50)
    finalstate = models.BooleanField()    
    
class TransitionModel(models.Model):
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)
    shortValidationArg =  models.CharField(max_length=1)
    