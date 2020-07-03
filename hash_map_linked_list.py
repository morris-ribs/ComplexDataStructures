from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for i in range(array_size)]
  
  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        item[1] = value
        return
    
    list_at_index.insert(payload)

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None
