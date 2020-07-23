from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=100)
    type_2 = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    hp = models.DecimalField(max_digits=10, decimal_places=3)
    attack = models.DecimalField(max_digits=10, decimal_places=3)
    defense = models.DecimalField(max_digits=10, decimal_places=3)
    sp_atk = models.DecimalField(max_digits=10, decimal_places=3)
    sp_def = models.DecimalField(max_digits=10, decimal_places=3)
    speed = models.DecimalField(max_digits=10, decimal_places=3)
    generation = models.DecimalField(max_digits=10, decimal_places=3)
    legendary = models.BooleanField()

    def has_type(self, type):
        """Check both types of model

        Args:
            type (str): Pokemon type

        Returns:
            bool: True if pokemon has the given type indicator
        """
        if self.type_1 == type or self.type_2 == type:
            return True
        else:
            return False
    