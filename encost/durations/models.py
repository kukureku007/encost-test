from django.db import models

class Client(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'
    
    def __str__(self):
        return self.name


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='equipments'
    )
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'
    
    def __str__(self):
        return self.name


class Mode(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'
    
    def __str__(self):
        return self.name


class Duration(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    start = models.DateTimeField()
    stop = models.DateTimeField()
    mode = models.ForeignKey(
        Mode,
        on_delete=models.CASCADE,
        related_name='durations'
    )
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'

    def __str__(self):
        return (
            f'{self.id}: {self.client}, {self.equipment}, {self.start}, '
            f'{self.stop}, {self.mode}, {self.minutes}.'
        )
