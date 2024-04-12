from dmenu import DynamicMenu
from filedb import FileDB


# class PrivateKey:
#     path = '../files/'
#     last_key_id = int
#     last_key = None
#      def __init__(self):
#          self.last_key_id = PrivateKey.last_key_id + 1
#          self.last_key = PrivateKey.last_key_id
#          PrivateKey.last_key_id = self.last_key_id
#          PrivateKey.last_key = self.last_key


class Task(DynamicMenu, FileDB):
    pass



