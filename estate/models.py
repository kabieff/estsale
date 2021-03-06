from django.db import models

class EstateType(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
            return self.name

		
class DealType(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class StructureType(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class BalconyType(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class BathroomType(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Address(models.Model):
    parent_id = models.IntegerField(max_length=30)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    is_agency = models.BooleanField()
    phone = models.IntegerField()
    address = models.ForeignKey(Address)
    def __unicode__(self):
        return self.name

class Estate(models.Model):
    type = models.ForeignKey(EstateType)
    address = models.ForeignKey(Address)
    house = models.CharField(max_length=30)
    structure_type = models.ForeignKey(StructureType)
    floor = models.IntegerField(max_length=30)
    floor_count = models.IntegerField(max_length=30)
    room_count = models.IntegerField(max_length=30)
    total_space = models.IntegerField(max_length=30)
    living_space = models.IntegerField(max_length=30)
    kitchen_space = models.IntegerField(max_length=30)
    bathroom_type = models.ForeignKey(BathroomType)
    balcony_type = models.ForeignKey(BalconyType)
    def __unicode__(self):
        return '%s %s' % (self.type, self.address)


class EstateAttribute(models.Model):
    name = models.ManyToManyField(Estate, through="EstateAttributes")
    def __unicode__(self):
        return '%s' % (self.name)


class Announcement(models.Model):
    estate = models.OneToOneField(Estate, primary_key=True)
    text = models.TextField(max_length=1000)
    deal_type = models.ForeignKey(DealType)
    cost = models.IntegerField()
    publisher = models.ForeignKey(User)
    is_ictive = models.BooleanField()
    is_busy = models.BooleanField()
    publication_date = models.DateField()
    date = models.DateField()
    data = models.TextField(max_length=1000)
    def __unicode__(self):
        return '%s %s' % (self.deal_type, self.cost)


class Media(models.Model):
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    announcement = models.ForeignKey(Announcement)
    def __unicode__(self):
        return self.title


class EstateAttributes(models.Model):
    attribute_id = models.ForeignKey(EstateAttribute)
    estate_id = models.ForeignKey(Estate)
    def __unicode__(self):
        return '%s %s' % (self.attribute_id, self.estate_id)