from core.models.FoundItem import FoundItem
from core.models.LostItem import LostItem

class Controller(object):
    def __init__(self):
        self.foundObjs = []
        self.lostObjs = []

    def addFoundObject(self, title, description, date):
        foundItem = FoundItem(title, description, date)
        self.foundObjs.append(foundItem)

    def addLostObject(self, title, description, date):
        lostItem = LostItem(title, description, date)
        self.lostObjs.append(lostItem)
