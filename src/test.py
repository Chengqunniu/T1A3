import io
import json
import pytest
from collect_info_and_order import collect_info
from class_for_customer import Customer, Order
from add_update_menu import add_update, add_sold_out_stickers
from main import check_password


# Test for collect info function
class TestCollectInfo:
    '''Test for collect info function
    '''
    def test_collect_name(self, monkeypatch):
        '''Test for invalid input
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('56'))
        try:
            collect_info()
        except ValueError:
            assert False


    def test_value_error(self):
        '''Test ValueError
        '''
        with pytest.raises(ValueError):
            name = 'Alex'
            name == float(name)

# Test for order function
name = Customer('Sam')
customer = Order('Sam')


class TestOrderFunction:
    '''Test order function
    '''
    def test_order(self, monkeypatch):
        '''Sticker name in the menu
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('Yum Yum Hana'))
        assert customer.order() is True


    def test_invalid_order(self, monkeypatch):
        '''Sticker name not in the menu
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('Yum Yum'))
        assert customer.order() is False


# Test for repeat order function
def test_repeat_order(monkeypatch):
    '''Test repeat order function
    '''
    monkeypatch.setattr('sys.stdin', io.StringIO('N'))
    assert customer.repeat_order() is True


# Test for add_membership function
class TestAddMembership:
    '''Test add membership function
    '''
    def test_add_membership(self):
        '''Automatically add customer to the customer list
        '''
        assert name.add_membership() == ['Alex', 'Sam']
        customer_list = ['Alex']
        with open('Customer_list.json', 'w', encoding='utf8') as customer:
            json.dump(customer_list, customer)
        customer_ordeer_history = []
        with open('Customer_order_history.json',
                 'w', encoding='utf8') as order_history:
            json.dump(customer_ordeer_history, order_history)


    def test_not_add_rewards_membership(self, monkeypatch):
        '''Choosing not to add customers to the rewards customer list
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('N'))
        assert name.add_rewards_membership() == ['Alex']


    def test_add_rewards_membership(self, monkeypatch):
        '''Choosing to add customers to the rewards customer list
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('Y'))
        assert name.add_rewards_membership() == ['Alex', 'Sam']
        rewards_customer_list = ['Alex']
        with open('Rewards_customer_list.json',
                 'w', encoding='utf8') as rewards_customer:
            json.dump(rewards_customer_list, rewards_customer)


# Test add_update function
class TestAddUpdateMenu:
    '''Test add and update function
    '''
    def test_invalidinput_add_update_menu(self, monkeypatch):
        '''Test with invalid price, which is a string
        '''
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:Hana')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0,
                               "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}


    def test_invalidprice_add_update_menu(self, monkeypatch):
        '''Test with invalid price, which is ess than 1.0
        '''
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:0')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0,
                               "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}


    def test_add_update_menu(self, monkeypatch):
        '''Test with valid input
        '''
        monkeypatch.setattr('builtins.input',  lambda _: 'Hana:10')
        assert add_update() == {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0,
                               "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0, "Hana": 10.0}   
        menu = {"Yum Yum Hana": 5.0, "Winter Vibes": 5.0,
               "Spring Vibes": 5.0, "Summer Vibes": 5.0, "Autumn Vibes": 5.0}
        with open('Menu.json', 'w', encoding='utf8') as menu_list:
            json.dump(menu, menu_list)


# Test add_sold_out_stickers function
class TestAddSoldOutStickers:
    '''Test add sold out stickers function
    '''
    def test_invalid_add_sold_out_stickers(self, monkeypatch):
        '''Sticker entered is not in the menu
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('Winter'))
        assert add_sold_out_stickers() == []


    def test_add_sold_out_stickers(self, monkeypatch):
        '''Sticker entered is in the menu
        '''
        monkeypatch.setattr('sys.stdin', io.StringIO('Winter Vibes'))
        assert add_sold_out_stickers() == ['Winter Vibes']


# Test for check_password function
def test_password(monkeypatch):
    '''Test check password function
    '''
    monkeypatch.setattr('builtins.input',  lambda _: 'password')
    assert check_password() is False