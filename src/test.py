import io
import json
import pytest
from collect_info_and_order import collect_info
from class_for_customer import Customer
from add_update_menu import *


# Test for collect info function
# class TestCollectInfo:
#     def test_collect_name(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('56'))
#         try:
#             collect_info()
#         except ValueError:
#             assert False

#     def test_value_error(self):
#         with pytest.raises(ValueError):
#             name = 'Alex'
#             name == float(name)

# Test for order function
name = Customer('Sam')

# class TestOrderFunction:
#     def test_order(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('Yum Yum Hana'))
#         assert name.order() is True

#     def test_invalid_order(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('Yum Yum'))
#         assert name.order() is False

# # Test for repeat order function
# def test_repeat_order(monkeypatch):
#     monkeypatch.setattr('sys.stdin', io.StringIO('N'))
#     assert name.repeat_order() is True

# # Test for add_membership function
# class TestAddMembership:
#     def test_add_membership(self):
#         assert name.add_membership() == ['Alex', 'Sam']
#         customer_list = ['Alex']
#         with open('Customer_list.json', 'w', encoding='utf8') as customer:
#             json.dump(customer_list, customer)


#     def test_not_add_rewards_membership(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('N'))
#         assert name.add_rewards_membership() == ['Alex']

#     def test_add_rewards_membership(self, monkeypatch):
#         monkeypatch.setattr('sys.stdin', io.StringIO('Y'))
#         assert name.add_rewards_membership() == ['Alex', 'Sam']
#         rewards_customer_list = ['Alex']
#         with open('Rewards_customer_list.json', 'w', encoding='utf8') as rewards_customer:
#             json.dump(rewards_customer_list, rewards_customer)

# Test add_update function
class TestAddUpdateMenu:
    def test_invalidinput_add_update_menu(self, monkeypatch):
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:Hana')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0, "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}

    def test_invalidprice_add_update_menu(self, monkeypatch):
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:0')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0, "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}

    def test_add_update_menu(self, monkeypatch):
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:10')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0, "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0, "Hana": 10.0}   
        menu = {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0, "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}
        with open('Menu.json', 'w') as menu_list:
            json.dump(menu, menu_list)