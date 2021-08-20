from django.db.models import fields
from rest_framework import serializers
from .models import *


class Discord_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = tMember_Discord
        fields = "__all__"


class Member_GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = tGuild_Discord
        fields = "__all__"


class Guild_ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = tGuild_Channel
        fields = "__all__"

class Member_BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = tMember_Bank
        fields = "__all__"

class Guild_BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = tGuild_Bank
        fields = "__all__"

class Shop_DiscordSerializer(serializers.ModelSerializer):
    class Meta:
        model = tShop_Discord
        fields = "__all__"

class Shop_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = tShop_Item
        fields = "__all__"

class Guild_Shop_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = tGuild_Shop_Item
        fields = "__all__"

class Member_InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = tMember_Inventory
        fields = "__all__"

class Member_ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = tMember_Condition
        fields = "__all__"
