from os import name
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone

# Create your models here.
class tMember_Discord(models.Model):
    id_discord = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255)
    user_join = models.CharField(max_length=100)
    user_create = models.CharField(max_length=100)
    guild_id = models.ForeignKey("tGuild_Discord", on_delete=models.CASCADE, null=True)
    bank_id = models.ForeignKey("tMember_Bank", on_delete=models.CASCADE, null=True)
    condition_id = models.ForeignKey(
        "tMember_Condition", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tGuild_Discord(models.Model):
    id_guild = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    name = models.CharField(max_length=100)
    bank_id = models.ForeignKey("tGuild_Bank", on_delete=models.CASCADE, null=True)
    shop_id = models.ForeignKey("tShop_Discord", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tGuild_Channel(models.Model):
    id_channel = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    status = models.IntegerField(null=True)
    guild_id = models.ForeignKey("tGuild_Discord", on_delete=CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tMember_Bank(models.Model):
    id_bank = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    cash_money = models.IntegerField(null=True)
    bank_money = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_bank


class tMember_Inventory(models.Model):
    id_inventory = models.AutoField(primary_key=True, null=False, unique=True)
    member_id = models.ForeignKey(
        "tMember_Discord", on_delete=models.CASCADE, null=True
    )
    item_id = models.ForeignKey("tShop_Item", on_delete=models.CASCADE, null=True)
    item_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_inventory


class tMember_Condition(models.Model):
    id_condition = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    condition_value = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_condition


class tGuild_Bank(models.Model):
    id_bank_guild = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    bank_money = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_bank_guild


class tShop_Discord(models.Model):
    id_shop = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tGuild_Shop_Item(models.Model):
    id_shop_item = models.AutoField(primary_key=True, null=False, unique=True)
    shop_id = models.ForeignKey("tShop_Discord", on_delete=models.CASCADE, null=True)
    item_id = models.ForeignKey("tShop_Item", on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shop_id


class tShop_Item(models.Model):
    CATEGORY_CHOICES = (
        ("food", "Food"),
        ("drink", "Drink"),
        ("weapon", "Weapon"),
        ("armor", "Armor"),
        ("item", "Item"),
        ("other", "Other"),
    )
    id_item = models.CharField(
        max_length=100, primary_key=True, null=False, unique=True
    )
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.IntegerField(null=True)
    value_misc = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
