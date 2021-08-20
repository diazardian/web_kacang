from kacang.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("DiscordMember", Discord_MemberViewset)
router.register("MemberGuild", Member_GuildViewset)
router.register("GuildChannel", Guild_ChannelViewset)
router.register("MemberBank", Member_BankViewset)
router.register("GuildBank", Guild_BankViewset)
router.register("ShopDiscord", Shop_DiscordViewset)
router.register("ShopItem", Shop_ItemViewset)
router.register("GuildShopItem", Guild_Shop_ItemViewset)
router.register("MemberInventory", Member_InventoryViewset)
router.register("MemberCondition", Member_ConditionViewset)