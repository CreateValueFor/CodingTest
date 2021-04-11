#파이썬에선 딕셔너리가 기본적으로 해시의 역할과 동일하다. 


adressBook = {'kim' : 'Seoul', 'james' : 'NewYork', 'ami' : 'Tokyo', 'karm' : 'Paris',
'yami' : 'Busan', 'lee' : 'Incheon',
'park' : 'London', 'potter' : 'Madrid',
'kuda' : 'Rome', 'euna' : 'Seoul',
}

class node:
    # def __init__(self, (key, value)):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 17
        self.count = 0
        self.hashArray = [None for _ in range(self.size)]

    def hashFunction(self,strData, mod):
        hf = 0
        for s in strData:
            hf = hf * 137 + ord(s)
        return hf % mod

    def add(self, key, value):
        if self.count >= self.size:
            return
        hf = self.hashFunction(key, self.size)

        #Chaining
        if self.hashArray[hf] == node((key,value))