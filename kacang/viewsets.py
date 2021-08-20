from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import filterset, rest_framework as filters
from . import models
from . import serializers


class Discord_MemberViewset(viewsets.ModelViewSet):
    queryset = models.tMember_Discord.objects.all()
    serializer_class = serializers.Discord_MemberSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class Member_GuildViewset(viewsets.ModelViewSet):
    queryset = models.tGuild_Discord.objects.all()
    serializer_class = serializers.Member_GuildSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Guild_ChannelViewset(viewsets.ModelViewSet):
    queryset = models.tGuild_Channel.objects.all()
    serializer_class = serializers.Guild_ChannelSerializer


class Member_BankViewset(viewsets.ModelViewSet):
    queryset = models.tMember_Bank.objects.all()
    serializer_class = serializers.Member_BankSerializer


class Guild_BankViewset(viewsets.ModelViewSet):
    queryset = models.tGuild_Bank.objects.all()
    serializer_class = serializers.Guild_BankSerializer


class Shop_DiscordViewset(viewsets.ModelViewSet):
    queryset = models.tShop_Discord.objects.all()
    serializer_class = serializers.Shop_DiscordSerializer


class Shop_ItemViewset(viewsets.ModelViewSet):
    queryset = models.tShop_Item.objects.all()
    serializer_class = serializers.Shop_ItemSerializer


class Guild_Shop_ItemViewset(viewsets.ModelViewSet):
    queryset = models.tGuild_Shop_Item.objects.all()
    serializer_class = serializers.Guild_Shop_ItemSerializer


class Member_InventoryFilter(filters.FilterSet):
    class Meta:
        model = models.tMember_Inventory
        fields = {
            "member_id": ["exact"],
            "item_id": ["exact"],
        }


class Member_InventoryViewset(viewsets.ModelViewSet):
    queryset = models.tMember_Inventory.objects.all()
    serializer_class = serializers.Member_InventorySerializer
    filterset_class = Member_InventoryFilter


class Member_ConditionViewset(viewsets.ModelViewSet):
    queryset = models.tMember_Condition.objects.all()
    serializer_class = serializers.Member_ConditionSerializer
