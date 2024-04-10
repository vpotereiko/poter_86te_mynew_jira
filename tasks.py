from projects import PrivateKey, FILES_PATH


# class PrivateKey:
#     path = '../files/'
#     last_key_id = int
#     last_key = None
#      def __init__(self):
#          self.last_key_id = PrivateKey.last_key_id + 1
#          self.last_key = PrivateKey.last_key_id
#          PrivateKey.last_key_id = self.last_key_id
#          PrivateKey.last_key = self.last_key


class Tasks:
    path = FILES_PATH


class Projects:
    proj_id = PrivateKey()

    def __init__(self, proj_name, proj_slug_name):
        self.proj_id = PrivateKey()
        self._proj_name = proj_name
        self._proj_slug_name = proj_slug_name

    @property
    def proj_slug_name(self):
        return self._proj_slug_name
