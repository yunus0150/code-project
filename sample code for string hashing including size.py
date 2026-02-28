#write a sample code for string hashing including size
class hashtable:
   def __init__(self,size):
      self.size= size
      self.table= [[] for _ in range(size)]