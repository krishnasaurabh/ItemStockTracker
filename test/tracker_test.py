from code import Tracker
import os

# Unit tests for tracker.py
# Tests the reload_state, modify the status, save_state
# @author qchen59


s = Tracker.State()
powerSupply = "Power Supply"
url = "https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244"

file = open("testtracker.txt", "w")
file.write(
    """Item:
GeForce RTX 3070,https://www.amazon.com/Gigabyte-Protection-WINDFORCE-DisplayPort-Mytrix_HDMI/dp/B09DR8C9B8/ref=sr_1_1_sspa?dchild=1&keywords=graphic+card&qid=1631860747&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NMTjRET1ZHUU9CJmVuY3J5cHRlZElkPUEwNDIyMDMxM1A5T0VUWVE4OEtETiZlbmNyeXB0ZWRBZElkPUEwNzE5Nzg1MzlTTFBWVEw2RklLQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=
Lunch Bag,https://www.amazon.com/adidas-Santiago-Lunch-Black-White/dp/B07KDSWWXK/ref=sr_1_3?crid=10JP8TVHSQW3E&dchild=1&keywords=limited+time+deal&qid=1631860841&s=apparel&sprefix=limited%2Cfashion%2C166&sr=1-3
RTX 3080,https://www.bestbuy.com/site/evga-rtx-3080-xc3-ultra-gaming-10g-p5-3885-kh-pci-express-4-0-lhr/6471615.p?skuId=6471615
Power Supply,https://www.bestbuy.com/site/corsair-rmx-series-rm850x-80-plus-gold-fully-modular-atx-power-supply-black/6459244.p?skuId=6459244
Bedside Table,https://www.walmart.com/ip/KingSo-Bedside-Table-Nightstand-Tall-Wood-Accent-End-Tables-for-Bedroom-Living-Room-Brown/258766761
Lip Colour,https://www.walmart.com/ip/Maybelline-SuperStay-24hr-2-Step-Lipcolor-Always-Blazing/126088124
Alert:
Email,test@email.com
Setting:
5
Minimize:
False
LaunchAtStartup:
True"""
)
file.close()
full_path = os.path.abspath("testtracker.txt")


def test_readState():
    """
    Tests if the reading of the tracker.txt file is correct
    or not (to load preferences from previous run).
    """
    Tracker.read_state(full_path, s)
    assert len(s.item) == 6, "Should be 4 items"
    assert s.email == "test@email.com", "Should be test@email.com"
    assert len(s.alert) == 1, "Should be only 1 alert"
    assert s.alert[0] == "Email", "The alert should be email"
    assert s.setting == "5", "The setting interval should be 5"
    assert s.Minimize == "False", "The setting interval should be False"
    assert s.LaunchAtStartup == "True", "The setting interval should be True"


def test_updateStatus():
    """
    Tests if the stock status change is updated properly.
    """
    Tracker.read_state(full_path, s)
    s.updateStatus(powerSupply, url, "In Stock", "$200")
    assert (
        s.getStatus(powerSupply, url).get("status") == "In Stock"
    ), "Should be In Stock"


def test_deleteAlert():
    """
    Tests if alert gets removed properly.
    """
    Tracker.read_state(full_path, s)
    initial_size = len(s.alert)
    s.deleteAlert("Email")
    s.deleteEmail()
    assert len(s.alert) == initial_size - 1, "Alert was not removed!"
    assert s.email == "", "Should be empty"


def test_saveState():
    Tracker.save_state(full_path, s)
