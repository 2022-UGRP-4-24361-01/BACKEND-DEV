from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Cal(models.Model):
    ROOM = 'R'
    USER = 'U'
    # PUBLIC = True
    # PRIVATE = False
    OWNER_CLASSES = [
        (ROOM, 'Room'),
        (USER, 'User')
    ]
    
    id = models.AutoField(primary_key=True)  # DO NOT REVEAL TO CLIENT
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(get_user_model(), related_name='+', to_field='uuid', db_column='fk', editable=False, on_delete=models.CASCADE)
    owner_class = models.CharField(max_length=1, choices=OWNER_CLASSES, editable=False)
    # policy = models.BooleanField(default=PUBLIC)
    icalURL = models.URLField(max_length=200)

    class Meta:
        db_table = 'calendar'
