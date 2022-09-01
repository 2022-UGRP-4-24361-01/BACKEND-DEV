from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Cal(models.Model):
    ROOM = 'R'
    USER = 'U'
    OWNER_CLASSES = [
        (ROOM, 'Room'),
        (USER, 'User')
    ]
    
    id = models.AutoField(primary_key=True)  # DO NOT REVEAL TO CLIENT
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(get_user_model(), unique=True, related_name='uuid+', to_field='uuid', db_column='owner', on_delete=models.CASCADE)
    owner_class = models.CharField(max_length=1, choices=OWNER_CLASSES)
    icalURL = models.URLField(max_length=200)

    class Meta:
        db_table = 'calendar'

class CalPermissionTable(models.Model):
    id = models.AutoField(primary_key=True)
    cal_uuid = models.ForeignKey(Cal, related_name='uuid+', to_field='uuid', db_column='cal_uuid', on_delete=models.CASCADE)
    user_uuid = models.ForeignKey(get_user_model(), related_name='uuid+', to_field='uuid', db_column='user_uuid', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'calendar_permission'
