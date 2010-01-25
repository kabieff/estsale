from estsale.estate.models import DealType
from estsale.estate.models import EstateType
from estsale.estate.models import StructureType
from estsale.estate.models import BalconyType
from estsale.estate.models import BathroomType
from estsale.estate.models import Address
from estsale.estate.models import User
from estsale.estate.models import Estate
from django.contrib import admin 

admin.site.register(DealType)
admin.site.register(EstateType)
admin.site.register(StructureType)
admin.site.register(BalconyType)
admin.site.register(BathroomType)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Estate)