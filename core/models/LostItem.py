from datetime import datetime,  date, timedelta
from core.models.Item import Item
from core.models.ItemState import ItemState

class LostItem(Item):

    def __init__(self, title, description, date):
        Item.__init__(self, title, description, date)
        self.state = ItemState.LOST
