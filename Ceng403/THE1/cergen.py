# -*- coding: utf-8 -*-
"""cergenupdated.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OrY0xykopLHFyHygblKvzMnUeNqIk9Xw

# CENG403 - Spring 2024 - THE1

In this take-home-exam, you will implement your own tensor library, called CerGen (short for CENG Gergen -- gergen: one of the Turkish translations of the term tensor).

Example usage:

```python
from cergen import rastgele_gercek,rastgele_dogal,cekirdek, gergen

boyut = ()
aralik = (0, 10)
g0 = rastgele_gercek(boyut, aralik)
print(g0)
0 boyutlu skaler gergen:
8

g1 = gergen([[1, 2, 3], [4, 5, 6]])
print(g1)
2x3 boyutlu gergen:
[[1, 2, 3]
 [4, 5, 6]]

g2 = gergen(rastgele_dogal((3, 1)))
print(g2)
3x1 boyutlu gergen
[[6],
[5],
[2]]

print((g1 * g2))


g3 = (g1 * (g2 + 3)).topla()

```

## 1 Task Description
In this homework, we introduce the gergen class, a custom data structure designed to provide a
hands-on experience with fundamental array operations, mirroring some functionalities typically
found in libraries like NumPy.

## Fundamental Operations:
Random number generation:
"""

import random

def cekirdek(sayi: int):
    random.seed(sayi)
    #Sets the seed for random number generation
    pass
def rastgele_dogal(boyut, aralik=(0,100), dagilim='uniform'):
    if dagilim != 'uniform':
        raise ValueError
    if(len(boyut)) == 0:
        return random.randint(aralik[0],aralik[1])
    def rdhelper(boyut2):
        if len(boyut2) == 1:
            eklenecek = []
            for k in range(boyut2[0]):
                eklenecek += [random.randint(aralik[0],aralik[1])]
            return eklenecek
        else:
            for p in range(0,boyut2[0]):
                return [rdhelper(boyut2[1:]) for _ in range (boyut2[0])]


    return rdhelper(boyut)


    """
    Generates data of specified dimensions with random integer values and returns a gergen object.

    Parameters:
    boyut (tuple): Shape of the desired data.
    aralik (tuple, optional): (min, max) specifying the range of random values. Defaults to (0,100), which implies a default range.
    dagilim (string, optional): Distribution of random values ('uniform'). Defaults to 'uniform'.

    Returns:
    gergen: A new gergen object with random integer values.
    """
    pass

def rastgele_gercek(boyut, aralik=(0.0, 1.0), dagilim='uniform'):
    if dagilim != 'uniform':
        raise ValueError
    if(len(boyut)) == 0:
        return random.uniform(aralik[0],aralik[1])
    def rdhelper(boyut2):
        if len(boyut2) == 1:
            eklenecek = []
            for k in range(boyut2[0]):
                eklenecek += [random.uniform(aralik[0],aralik[1])]
            return eklenecek
        else:
                return [rdhelper(boyut2[1:]) for _ in range (boyut2[0])]
    return rdhelper(boyut)

    son = gergen(rdhelper(boyut))

    """
    Generates a gergen of specified dimensions with random floating-point values.

    Parameters:
    boyut (tuple): Shape of the desired gergen.
    aralik (tuple, optional): (min, max) specifying the range of random values. Defaults to (0.0, 1.0) for uniform distribution.
    dagilim (string, optional): Distribution of random value ('uniform'). Defaults to 'uniform'.

    Returns:
    gergen: A new gergen object with random floating-point values.
    """
    pass

"""Operation class implementation:"""

class Operation:
    def __call__(self, *operands):
        """
        Makes an instance of the Operation class callable.
        Stores operands and initializes outputs to None.
        Invokes the forward pass of the operation with given operands.

        Parameters:
            *operands: Variable length operand list.

        Returns:
            The result of the forward pass of the operation.
        """
        self.operands = operands
        self.outputs = None
        return self.ileri(*operands)

    def ileri(self, *operands):
        """
        Defines the forward pass of the operation.
        Must be implemented by subclasses to perform the actual operation.

        Parameters:
            *operands: Variable length operand list.

        Raises:
            NotImplementedError: If not overridden in a subclass.
        """
        raise NotImplementedError

import math
from typing import Union

class gergen:

    __veri = None #A nested list of numbers representing the data
    D = None # Transpose of data
    __boyut = None #Dimensions of the derivative (Shape)


    def __init__(self, veri=None):
        tup = ()
        self.__veri = veri
        x=0
        cur = self.__veri
        while True:
            if type(cur) == list:
                tup += (len(cur),)
                cur = cur[0]
            else:
                break
        self.__boyut = tup
        if(self.__boyut != () and len(self.__boyut)!= 1):
          yeni_boyut = ()
          for i in range(len(self.__boyut)):
              yeni_boyut +=(self.__boyut[len(self.__boyut)-1-i],)
          def duz2(self):

              def hardc(boyut2, lis2):

                if len(boyut2) == 1:
                    eklenecek = []
                    for k in range(boyut2[0]):
                        eklenecek += [lis2[k]]
                    return eklenecek
                else:
                    yeni = []
                    for p in range(0,boyut2[0]):
                        yeni += [hardc(boyut2[1:], lis2[p])]
                    return yeni

              stack = hardc( self.__boyut, self.__veri)
              yeni = []
              while len(stack) != 0:
                  cur = stack.pop()

                  if isinstance(cur, list):
                      stack.extend(cur)
                  else :
                      yeni += [cur]
              return yeni
          duzlist = duz2(self)
          duzlist.reverse()



          def rdhelper(lis2,boyut2,yer,artis):
              if len(boyut2) == 1:
                  artis*=self.__boyut[1]
                  eklenecek = []
                  for k in range(boyut2[0]):
                      eklenecek += [lis2[yer]]
                      yer+=artis
                  return eklenecek
              else:
                  yeni = []
                  artis =1
                  for q in range (len(self.__boyut) -len(boyut2)):
                      artis*= self.__boyut[len(self.__boyut)-1 -q]
                  for p in range(0,boyut2[0]):
                      yeni += [rdhelper(lis2,boyut2[1:],yer,artis)]
                      if(len(boyut2) == len(self.__boyut)):
                          yer+=1
                      else:
                          yer += artis
                  return yeni

          x = rdhelper(duzlist,yeni_boyut,0,1)
          self.D = x
        else:
          self.D = self.__veri




    # The constructor for the 'gergen' class.
    #
    # This method initializes a new instance of a gergen object. The gergen can be
    # initialized with data if provided; otherwise, it defaults to None, representing
    # an empty tensor.
    #
    # Parameters:
    # veri (int/float, list, list of lists, optional): A nested list of numbers that represents the
    # gergen data. The outer list contains rows, and each inner list contains the
    # elements of each row. If 'veri' is None, the tensor is initialized without data.
    #
    # Example:
    # To create a tensor with data, pass a nested list:
    # tensor = gergen([[1, 2, 3], [4, 5, 6]])
    #
    # To create an empty tensor, simply instantiate the class without arguments:
    # empty_tensor = gergen()
        pass

    def __getitem__(self, index):
        g5 = gergen(self.__veri[index])
        return g5
    #Indexing for gergen objects
        pass

    def __str__(self):
        #print(self.__boyut)
        #print(self.__veri)
        s = ""
        if(len(self.__boyut) == 0):
          s+= f"0 boyutlu gergen:\n" + str(self.__veri)
          return s
        elif len(self.__boyut) == 1:
          s+= f"1 boyutlu gergen:\n" + str(self.__veri)
          return s
        else:

          for i in self.__boyut[:len(self.__boyut)-1]:
            s+=str(i)
            s+='x'
          s+=str(self.__boyut[len(self.__boyut)-1])
          s+=" boyutlu gergen:\n"
          def p(liste):
                  if(type(liste[0]) != list):
                    return str(liste)
                  else:
                      a='['
                      for l in liste[:len(liste)-1]:
                        a+=p(l)
                        a+='\n'
                      a+=p(liste[len(liste)-1])
                      a+=']'
                      return a
          s+=p(self.__veri)

          return s
        #Generates a string representation

    pass

    def __mul__(self, other: Union['gergen', int, float]) -> 'gergen':

        if type(other) != type(self) and type(other) != int and type(other) != float:
            raise TypeError
        elif type(other) == type(self):
            if other.boyut() != self.__boyut:
                if(other.boyut() == ()):
                  d= self*other.listeye()
                  return d
                if(self.__boyut == ()):
                  d = (other*self.__veri)
                  return d
            if len(other.boyut()) == 0 and 0 == len(self.__boyut):
                d = self.__veri*other.listeye()
                g2 = gergen(d)
                return g2
            else:
                def rdhelper(boyut2, lis1, lis2):
                    if len(boyut2) == 1:
                        eklenecek = []
                        for k in range(boyut2[0]):
                            eklenecek += [lis1[k]*lis2[k]]
                        return eklenecek
                    else:
                        yeni = []
                        for p in range (boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis1[p], lis2[p])]
                        return yeni
                a= rdhelper(self.__boyut,self.__veri,other.listeye())
                g2 = gergen(a)
                return g2
        else:
              if(len(self.__boyut) == 0):
                a = self.__veri*other
                t = gergen(a)
                return t
              def rdhelper(boyut2, lis2):
                  if len(boyut2) == 1:
                      eklenecek = []
                      for k in range(boyut2[0]):
                          eklenecek += [lis2[k]*other]
                      return eklenecek
                  else:
                      yeni = []
                      for p in range(boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis2[p])]
                      return yeni
              a= rdhelper(self.__boyut,self.__veri)
              g2 = gergen(a)
              return g2





        """
        Multiplication operation for gergen objects.
        Called when a gergen object is multiplied by another, using the '*' operator.
        Could be element-wise multiplication or scalar multiplication, depending on the context.
        """
        pass

    def __truediv__(self, other: Union['gergen', int, float]) -> 'gergen':


        if type(other) != type(self) and type(other) != int and type(other) != float:
            raise TypeError
        elif type(other) == type(self):
            if other.boyut() != self.__boyut:
                if(other.boyut() == ()):
                  d= self/other.listeye()
                  return d
                if(self.__boyut == ()):
                  d = (other/self.__veri).us(-1)
                  return d
            if len(other.boyut()) == 0 and 0 == len(self.__boyut):
                d = self.__veri/other.listeye()
                g2 = gergen(d)
                return g2
            else:
                def rdhelper(boyut2, lis1, lis2):
                    if len(boyut2) == 1:
                        eklenecek = []
                        for k in range(boyut2[0]):
                            eklenecek += [lis1[k]/lis2[k]]
                        return eklenecek
                    else:
                        yeni = []
                        for p in range (boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis1[p], lis2[p])]
                        return yeni
                a= rdhelper(self.__boyut,self.__veri,other.listeye())
                g2 = gergen(a)
                return g2
        else:
              if(len(self.__boyut) == 0):
                a = self.__veri/other
                t = gergen(a)
                return t
              def rdhelper(boyut2, lis2):
                  if len(boyut2) == 1:
                      eklenecek = []
                      for k in range(boyut2[0]):
                          eklenecek += [lis2[k]/other]
                      return eklenecek
                  else:
                      yeni = []
                      for p in range(boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis2[p])]
                      return yeni
              a= rdhelper(self.__boyut,self.__veri)
              g2 = gergen(a)
              return g2




        """
        Division operation for gergen objects.
        Called when a gergen object is divided by another, using the '/' operator.
        The operation is element-wise.
        """
        pass


    def __add__(self, other: Union['gergen', int, float]) -> 'gergen':

        if type(other) != type(self) and type(other) != int and type(other) != float:
            raise TypeError

        elif type(other) == type(self):
            if other.boyut() != self.__boyut:
                if(other.boyut() == ()):
                  d= self+other.listeye()
                  return d
                if(self.__boyut == ()):
                  d = (other+self.__veri)
                  return d
            if len(other.boyut()) == 0 and 0 == len(self.__boyut):
                d = self.__veri+other.listeye()
                g2 = gergen(d)
                return g2
            else:
                def rdhelper(boyut2, lis1, lis2):
                    if len(boyut2) == 1:
                        eklenecek = []
                        for k in range(boyut2[0]):
                            eklenecek += [lis1[k]+lis2[k]]
                        return eklenecek
                    else:
                        yeni = []
                        for p in range (boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis1[p], lis2[p])]
                        return yeni
                a= rdhelper(self.__boyut,self.__veri,other.listeye())
                g2 = gergen(a)
                return g2
        else:
              if(len(self.__boyut) == 0):
                a = self.__veri+other
                t = gergen(a)
                return t
              def rdhelper(boyut2, lis2):
                  if len(boyut2) == 1:
                      eklenecek = []
                      for k in range(boyut2[0]):
                          eklenecek += [lis2[k]+other]
                      return eklenecek
                  else:
                      yeni = []
                      for p in range(boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis2[p])]
                      return yeni
              a= rdhelper(self.__boyut,self.__veri)
              g2 = gergen(a)
              return g2


        """
        Defines the addition operation for gergen objects.
        Called when a gergen object is added to another, using the '+' operator.
        The operation is element-wise.
        """
        pass

    def __sub__(self, other: Union['gergen', int, float]) -> 'gergen':


        if type(other) != type(self) and type(other) != int and type(other) != float:
            raise TypeError
        elif type(other) == type(self):
            if other.boyut() != self.__boyut:
                if(other.boyut() == ()):
                  d= self-other.listeye()
                  return d
                if(self.__boyut == ()):
                  d = (other-self.__veri)*-1
                  return d
            if len(other.boyut()) == 0 and 0 == len(self.__boyut):
                d = self.__veri-other.listeye()
                g2 = gergen(d)
                return g2
            else:
                def rdhelper(boyut2, lis1, lis2):
                    if len(boyut2) == 1:
                        eklenecek = []
                        for k in range(boyut2[0]):
                            eklenecek += [lis1[k]-lis2[k]]
                        return eklenecek
                    else:
                        yeni = []
                        for p in range (boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis1[p], lis2[p])]
                        return yeni
                a= rdhelper(self.__boyut,self.__veri,other.listeye())
                g2 = gergen(a)
                return g2
        else:
              if(len(self.__boyut) == 0):
                a = self.__veri-other
                t = gergen(a)
                return t
              def rdhelper(boyut2, lis2):
                  if len(boyut2) == 1:
                      eklenecek = []
                      for k in range(boyut2[0]):
                          eklenecek += [lis2[k]-other]
                      return eklenecek
                  else:
                      yeni = []
                      for p in range(boyut2[0]):
                          yeni += [rdhelper(boyut2[1:], lis2[p])]
                      return yeni
              a= rdhelper(self.__boyut,self.__veri)
              g2 = gergen(a)
              return g2

        """
        Subtraction operation for gergen objects.
        Called when a gergen object is subtracted from another, using the '-' operator.
        The operation is element-wise.
        """
        pass

    def uzunluk(self):
        if len(self.__boyut) == 0:
          return 0
    # Returns the total number of elements in the gergen
        cur = self.__boyut
        sayi = len(cur)
        i=0
        tot = 1
        while i<sayi:
            tot *= cur[i]
            i += 1
        return tot
        pass

    def boyut(self):
    # Returns the shape of the gergen
        return self.__boyut
        pass






























    def devrik(self):
        if(self.__boyut == ()):
           g3 = gergen(self.__veri)
           return g3
        yeni_boyut = ()
        for i in range(len(self.__boyut)):
            yeni_boyut +=(self.__boyut[len(self.__boyut)-1-i],)

        def duz2(self):

            def hardc(boyut2, lis2):

              if len(boyut2) == 1:
                  eklenecek = []
                  for k in range(boyut2[0]):
                      eklenecek += [lis2[k]]
                  return eklenecek
              else:
                  yeni = []
                  for p in range(0,boyut2[0]):
                      yeni += [hardc(boyut2[1:], lis2[p])]
                  return yeni

            stack = hardc( self.__boyut, self.__veri)
            yeni = []
            while len(stack) != 0:
                cur = stack.pop()

                if isinstance(cur, list):
                    stack.extend(cur)
                else :
                    yeni += [cur]
            return yeni
        duzlist = duz2(self)
        duzlist.reverse()



        def rdhelper(lis2,boyut2,yer,artis):
            if len(boyut2) == 1:
                artis*=self.__boyut[1]
                eklenecek = []
                for k in range(boyut2[0]):
                    eklenecek += [lis2[yer]]
                    yer+=artis
                return eklenecek
            else:
                yeni = []
                artis =1
                for q in range (len(self.__boyut) -len(boyut2)):
                    artis*= self.__boyut[len(self.__boyut)-1 -q]
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(lis2,boyut2[1:],yer,artis)]
                    if(len(boyut2) == len(self.__boyut)):
                        yer+=1
                    else:
                        yer += artis
                return yeni

        x = rdhelper(duzlist,yeni_boyut,0,1)
        g3 = gergen(x)
        return g3


    # Returns the transpose of gergen
        pass

























    def sin(self):
        if(self.__boyut == ()):
          g3 = gergen(math.sin(self.__veri))
          return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [math.sin(lis2[k])]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3

        #son = gergen(a)
    #Calculates the sine of each element in the given `gergen`.
        pass

    def cos(self):
        if(self.__boyut == ()):
            g3 = gergen(math.cos(self.__veri))
            return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [math.cos(lis2[k])]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3
    #Calculates the cosine of each element in the given `gergen`.
        pass

    def tan(self):
        if(self.__boyut == ()):
          g3 = gergen(math.tan(self.__veri))
          return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [math.tan(lis2[k])]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3
    #Calculates the tangent of each element in the given `gergen`.
        pass

    def us(self, n: int):
        if(self.__boyut == ()):
          g3 = gergen(self.__veri**n)
          return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [lis2[k]**n]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3
    #Raises each element of the gergen object to the power 'n'. This is an element-wise operation.
        pass

    def log(self):
        if(self.__boyut == ()):
          g3 = gergen(math.log10(self.__veri))
          return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [math.log10(lis2[k])]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3

    #Applies the logarithm function to each element of the gergen object, using the base 10.
        pass

    def ln(self):
        if(self.__boyut == ()):
          g3 = gergen(math.log(self.__veri))
          return g3
        def rdhelper(boyut2, lis2):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    if(k >= len(lis2)):
                        break
                    eklenecek += [math.log(lis2[k])]
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(boyut2[1:], lis2[p])]
                return yeni
        a= rdhelper(self.__boyut,self.__veri)
        g3 = gergen(a)
        return g3
    #Applies the natural logarithm function to each element of the gergen object.
        pass

    def L1(self):
    # Calculates and returns the L1 norm
        if(self.__boyut == ()):
          return abs(self.__veri)
        yeni = 0
        stack = self.__veri

        while len(stack) != 0:
            cur = stack.pop()

            if isinstance(cur, list):
                stack.extend(reversed(cur))
            else :
                yeni += abs(cur)
        return yeni

        pass

    def L2(self):
        if(self.__boyut == ()):
            return abs(self.__veri)
    # Calculates and returns the L2 norm
        yeni = 0
        stack = self.__veri

        while len(stack) != 0:
            cur = stack.pop()

            if isinstance(cur, list):
                stack.extend(reversed(cur))
            else :
                yeni += cur*cur
        return yeni**(0.5)
        pass

    def Lp(self, p):
        if(self.__boyut == ()):
          return abs(self.__veri)
        yeni = 0
        stack = self.__veri

        while len(stack) != 0:
            cur = stack.pop()

            if isinstance(cur, list):
                stack.extend(reversed(cur))
            else :
                yeni += abs(cur**(p))
        return yeni**(1/p)
        pass
    # Calculates and returns the Lp norm, where p should be positive integer
        pass

    def listeye(self):
        return self.__veri
    #Converts the gergen object into a list or a nested list, depending on its dimensions.
        pass

    def duzlestir(self):
        if(self.__boyut == ()):
          if(type(self.__veri)) == int or (type(self.__veri)) == float:
            return [self.__veri]
          else:
            return self.__veri
        yeni = []
        stack = self.__veri

        while len(stack) != 0:
            cur = stack.pop()

            if isinstance(cur, list):
                stack.extend(cur)
            else :
                yeni += [cur]
        yeni.reverse()
        g3 = gergen(yeni)
        return g3


    #Converts the gergen object's multi-dimensional structure into a 1D structure, effectively 'flattening' the object.
        pass

    def boyutlandir(self, yeni_boyut):

        if(self.__boyut == () and yeni_boyut == ()):
          return
        c = 1
        for i in yeni_boyut:
          c*=i
        if(self.uzunluk() != c):
          raise ValueError
        def duz2(self):

            def hardc(boyut2, lis2):

                if len(boyut2) == 1:
                    eklenecek = []
                    for k in range(boyut2[0]):
                        eklenecek += [lis2[k]]
                    return eklenecek
                else:
                    yeni = []
                    for p in range(0,boyut2[0]):
                        yeni += [hardc(boyut2[1:], lis2[p])]
                    return yeni

            stack = hardc( self.__boyut, self.__veri)

            yeni = []
            while len(stack) != 0:
                cur = stack.pop()

                if isinstance(cur, list):
                    stack.extend(cur)
                else :
                    yeni += [cur]
            return yeni
        duzlist = duz2(self)
        duzlist.reverse()
        def rdhelper(lis2,boyut2,yer):
            if len(boyut2) == 1:
                eklenecek = []
                for k in range(boyut2[0]):
                    eklenecek += [lis2[yer]]
                    yer+=1
                return eklenecek
            else:
                yeni = []
                for p in range(0,boyut2[0]):
                    yeni += [rdhelper(lis2,boyut2[1:],yer)]
                    k=1
                    for t in range(len(boyut2)-1):
                        k*= boyut2[t+1]
                    yer+=k
                return yeni

        x = rdhelper(duzlist,yeni_boyut,0)
        g3 = gergen(x)
        return g3



    #Reshapes the gergen object to a new shape 'yeni_boyut', which is specified as a tuple.
        pass
    def take(self):
      return self.veri

    def ic_carpim(self, other):
        if(type(other) != type(self)):
            raise TypeError
        if(len(self.__boyut) > 2 or len(other.boyut())>2 or self.__boyut[1] != other.boyut()[0]):
            raise ValueError
        #if(isinstance(self.__veri,int))
        x= rastgele_dogal((self.__boyut[0],other.boyut()[1]))
        for a in range(self.__boyut[0]):
          for b in range(other.boyut()[1]):
            x[a][b] = 0
            for c in range(self.__boyut[1]):

              x[a][b] += self.__veri[a][c] * other.listeye()[c][b]

        g3 = gergen(x)
        return g3


    #Calculates the inner (dot) product of this gergen object with another.
        pass

    def dis_carpim(self, other):
      if(type(other) != type(self)):
          raise TypeError
      if(len(self.__boyut)>= 3 or len(self.__boyut)<1):
        raise ValueError
      if(self.__boyut[1]!= 1 or other.boyut()[1] != 1) :
          raise ValueError
      x = rastgele_dogal((self.__boyut[0], other.boyut()[0]))
      for a in range (self.__boyut[0]):
          for b in range (other.boyut()[0]):
            x[a][b] = self.__veri[a][0] * other.listeye()[b][0]

      g3 = gergen(x)
      return g3;


    #Calculates the outer product of this gergen object with another.
      pass





    def topla(self, eksen=None):
      if(eksen == None):
         return self.L1()
      if type(eksen) != None and type(eksen) != int :
        raise TypeError
      if(eksen>= len(self.__boyut)):
        raise ValueError
      else:
        boy = self.__boyut[eksen]
        tup = ()
        tup2 = ()
        for a in range(len(self.__boyut)):
            if a<= eksen:
              tup += (self.__boyut[a],)
            if a>eksen:
              tup2 += (self.__boyut[a],)

        def rdhelper2(boyut2, lis1, lis2):
                    if len(boyut2) <= 1:
                        eklenecek = []
                        if len(boyut2) == 0:

                          return lis1 + lis2
                        for k in range(boyut2[0]):
                            eklenecek += [lis1[k]+lis2[k]]
                        return eklenecek
                    else:
                        yeni = []
                        for p in range (boyut2[0]):
                          yeni += [rdhelper2(boyut2[1:], lis1[p], lis2[p])]
                        return yeni

        def rdhelper(lis2,boyut2):
            if len(boyut2) <= 1:
                eklenecek = rastgele_dogal(tup2,(0,0))
                if len(tup2) == 0:
                  eklenecek = 0
                for i in range(0,boy):
                  eklenecek =rdhelper2(tup2,eklenecek,lis2[i])
                return eklenecek
            else:
              yeni = []
              for h in range(0,boyut2[0]):
                  yeni += [rdhelper(lis2[h],boyut2[1:])]
              return yeni

        x = rdhelper(self.__veri,tup)
        g5 = gergen(x)
        return g5
    #Sums up the elements of the gergen object, optionally along a specified axis 'eksen'.
      pass





    def ortalama(self, eksen=None):

        g4 = self.topla(eksen)
        if(len(self.__boyut) == 0):

          return g4
        if(eksen == None):
          g5 = g4 / self.uzunluk()
          return g5
        s = (g4/self.__boyut[eksen])
        return s



    #Calculates the average of the elements of the gergen object, optionally along a specified axis 'eksen'.
        pass

"""## 2 Compare with NumPy"""

import numpy as np       # NumPy, for working with arrays/tensors
import time              # For measuring time

"""**Example 1:**
Using rastgele_gercek(), generate two gergen objects with shapes (64,64) and calculate the a.ic carpim(b). Then, calculate the same function with NumPy and report the time and difference.
"""

def example_1():
    #Example 1
    boyut = (64,64)
    g1 = rastgele_gercek(boyut)
    g2 = rastgele_gercek(boyut)
    g3 = gergen(g1)
    g4 = gergen(g2)
    start = time.time()
    g3.ic_carpim(g4)
    #TODO        print("duz=", duzlist)
    #Apply given equation
    end = time.time()

    start_np = time.time()
    np.dot(g1,g2)
    #Apply the same equation for NumPy equivalent
    end_np = time.time()

    #TODO:
    #Compare if the two results are the same
    #Report the time difference
    print("Time taken for gergen:", end-start)
    print("Time taken for numpy:", end_np-start_np)

"""**Example 2:**
Using rastgele_gercek(), generate three gergen’s a, b and c with shapes (4,16,16,16). Calculate given equation:

> (a×b + a×c + b×c).ortalama()

Report the time and whether there exists any computational difference in result with their NumPy equivalent.
"""

def example_2():

    #Example 2
    #TODO:
     boyut = (4,16,16,16)
     g1 = rastgele_gercek(boyut)
     g2 = rastgele_gercek(boyut)
     g3 = rastgele_gercek(boyut)
     gg1 = gergen(g1)
     gg2 = gergen(g2)
     gg3 = gergen(g3)
     ng1 = np.array(g1)
     ng2 = np.array(g2)
     ng3 = np.array(g3)
     start = time.time()
     gg3 = (gg1*gg2 + gg1*gg3 + gg2*gg3).ortalama()

     end = time.time()


     start_np = time.time()
     ng3 = np.average(np.add(np.add(np.multiply(ng1,ng2),np.multiply(ng1,ng3)),np.multiply(ng2,ng3)))

     end_np = time.time()

      #TODO:
      #Compare if the two results are the same
      #Report the time difference
     print("Time taken for gergen:", end-start)
     print("Time taken for numpy:", end_np-start_np)
     pass

"""**Example 3**: Using rastgele_gercek(), generate three gergen’s a and b with shapes (3,64,64). Calculate given equation:


> $\frac{\ln\left(\left(\sin(a) + \cos(b)\right)^2\right)}{8}$


Report the time and whether there exists any computational difference in result with their NumPy equivalent.

"""

def example_3():
    boyut = (3,64,64)
    g1 = rastgele_gercek(boyut)
    g2 = rastgele_gercek(boyut)
    gg1 = gergen(g1)
    gg2 = gergen(g2)
    ng1 = np.array(g1)
    ng2 = np.array(g2)

    start = time.time()
    gg3 = gg1.sin() + gg2.cos()
    gg3 = gg3.us(2)
    gg3 = gg3.ln()
    gg3 = gg3/8

    #TODO        print("duz=", duzlist)
    #Apply given equation
    end = time.time()

    start_np = time.time()
    ng3 = np.add(np.sin(ng1),np.cos(ng2))
    ng3 = np.power(ng3,2)
    ng3=np.log(ng3)
    ng3 = np.divide(ng3,8)


    #Apply the same equation for NumPy equivalent
    end_np = time.time()

    #TODO:
    #Compare if the two results are the same
    #Report the time difference
    print("Time taken for gergen:", end-start)
    print("Time taken for numpy:", end_np-start_np)

    pass

example_1()
example_2()
example_3()



