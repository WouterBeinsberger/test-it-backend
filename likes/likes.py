class Likes:
  def __init__(self):
    self._data = None

  @property
  def data(self):
    return self._data

  @data.setter
  def data(self, value):
    self._data = value