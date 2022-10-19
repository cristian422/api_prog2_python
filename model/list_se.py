from model.kid import Kid
from model.kidDTO import KidByPositionDTO
from model.node import Node


class ListSE:
    def __init__(self):
        self.head = None
        self.size =0

    def add(self, kid:Kid):
        if self.head == None:
            self.head = Node(kid)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            # Estoy parado en el último
            temp.next = Node(kid)
        self.size+=1

    def add_to_start(self, kid:Kid):
        if self.head == None:
            self.head = Node(kid)
        else:
            newNode = Node(kid)
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def invert(self):
        if self.head != None:
            temp = self.head
            listCp = ListSE()
            while temp != None:
                listCp.add(temp.data)
                temp = temp.next
            self.head = listCp.head

    def add_by_position(self,position:int,kid:Kid):
        if position == 1:
            self.add_to_start(kid)
        else:
            postemp =1
            temp = self.head;
            while postemp < (position-1):
                temp = temp.next
                postemp = postemp +1

            newNode = Node(kid)
            newNode.next = temp.next
            temp.next = newNode
            self.size += 1

    def mix_by_gender(self):
        if self.size > 1:
            contM =1
            contF = 2
            temp = self.head
            listCp = ListSE()
            while temp != None:
                if temp.data.gender =='M':
                    if contM > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contM, temp.data)
                    contM += 2
                else:
                    if contF > listCp.size:
                        listCp.add(temp.data)
                    else:
                        listCp.add_by_position(contF, temp.data)
                    contF += 2
                temp = temp.next
            self.head = listCp.head

    def firs_and_last(self):
        temp=self.head
        lista=ListSE()
        while(temp.next.next!=None):
            temp=temp.next
            lista.add(temp.data)
        lista.add_to_start(temp.next.data)
        lista.add(self.head.data)
        self.head=lista.head

    def count(self):
        if self.head.data==None:
            return 0;
        temp=self.head
        counter=1
        while temp.next!=None:
            counter=counter+1
            temp=temp.next
        return counter

    def male_female(self):
        lista=ListSE()
        temp=self.head
        while temp.next!=None!=None:
            if temp.data.gender=='H':
                lista.add_to_start(temp.data)
            else:
                lista.add(temp.data)
        if temp.data.gender=='M':
            lista.add_to_start(temp.data)
        else:
            lista.add(temp.data)
        temp=temp.data
        self.head=lista.head

    def delet_position(self,i:int):
        temp=self.head
        contador=1
        if i==1:
            self.head=temp.next
        while contador<i:
            if contador==i-1:
                temp.next=temp.next.next
            temp=temp.next
            contador=contador+1
        self.size=self.size-1

    def less_7_years(self):
        lista=ListSE()
        temp=self.head
        for i in range(self.size):
            if temp.data.age<=7:
                lista.add(temp.data)
            temp=temp.next
        self.head=lista.head

    def delet_3years_kids(self):
        temp=self.head
        lista=ListSE()
        if self.head.data.age<3:
            self.head=temp.next
        while temp.next!=None:
            if temp.data.age>=3:
                lista.add(temp.data)
            temp=temp.next
        if temp.data.age>=3:
            lista.add(temp.data)
        self.head=lista.head

    def kidsbyrange(self,rangeinicial:int,rangeend:int):
        temp=self.head
        contador=0
        while temp!=None:
            if temp.data.age>=rangeinicial and temp.data.age<=rangeend:
                contador=contador+1

            temp=temp.data







        

