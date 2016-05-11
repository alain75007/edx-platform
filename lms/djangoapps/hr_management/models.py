from django.db import models

from django.contrib.auth.models import User

# NOTE: V1 - NYIF admins will be given access to this /admin interface
#            where they wil be able to assign the HrManager role to existing users
#            
class HrManager(models.Model):
    user = models.OneToOneField(User, unique=True, db_index=True)

    # figure out where to tie user in (microsite or organization)
    #   NOTE: organization probably needs to use db driven microsites
    #         because it has a db model for Organization
    #         
    #organization = models.ManyToManyField(Org)
