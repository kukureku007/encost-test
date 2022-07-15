from django.db import models

class Client(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='equipments'
    )
    client_id = ...
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Mode(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'


class Duration(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    equipment_id = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    start = models.TextField()
    stop = models.TextField()
    mode_id = models.ForeignKey(
        Mode,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'
