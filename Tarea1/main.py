# main.py by Paulina Cámara (2021)
# Implementación de estructura de datos: stack, queue y hash 

from datastruct import Stack
from datastruct import Queue
from datastruct import Hash

#Implementacion de stacks
def testStack():
    print('*** STACK ***')
    stest = Stack()
    print('Stack inicial: ' + str(stest.top()))
    print('Añadir 1')
    stest.push(1)
    print('Top: ' + str(stest.top()))
    print('Añadir 2, 3, 4')
    stest.push(2)
    stest.push(3)
    stest.push(4)
    print('Pop: ' + str(stest.pop()))
    print('Pop: ' + str(stest.pop()))
    print('Top: ' + str(stest.top()))

#Implementacion de queues
def testQ():
    print('------------------------------------')
    print('*** QUEUE ***')
    qtest = Queue()
    print('Queue inicial: ' + str(qtest.front()))
    print('Añadir 1')
    qtest.push(1)
    print('Front: ' + str(qtest.front()))
    print('Añadir 2, 3, 4')
    qtest.push(2)
    qtest.push(3)
    qtest.push(4)
    print('Pop: ' + str(qtest.pop()))
    print('Pop: ' + str(qtest.pop()))
    print('Front: ' + str(qtest.front()))

#Implementacion de Hash
def testHash():
    print('------------------------------------')
    print('*** HASH ***')
    htest = Hash()
    print(htest.hashfunc('JK'))
    print(htest.hashfunc('Diez'))
    print('Añadir valores a Hash')
    htest.add('JK', 'Jungkook')
    htest.add('EU', 'Eunwoo')
    htest.add('Diez', 10)
    print('Valor de JK: ' + str(htest.getVal('JK')))
    print('Valor de EU: ' + str(htest.getVal('EU')))
    print('Valor de Diez: ' + str(htest.getVal('Diez')))
    htest.delete('Diez')
    print('Valor de Diez (despues de borrar): ' + str(htest.getVal('Diez')))
    htest.delete('EU')
    print('Valor de EU (despues de borrar): ' + str(htest.getVal('EU')))


if __name__ == "__main__":
    testStack()
    testQ()
    testHash()