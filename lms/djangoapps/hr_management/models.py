from django.db import models

from django.contrib.auth.models import User
from organizations.models import Organization

# NOTE: V1 - NYIF admins will be given access to this /admin interface
#            where they wil be able to assign the HrManager role to existing users
#            
class HrManager(models.Model):
    user = models.OneToOneField(User)
    organization = models.OneToOneField(Organization)

    def __str__(self):
        return '{}: {}'.format(self.user, self.organization)
    #organization = models.ManyToManyField(Org)
