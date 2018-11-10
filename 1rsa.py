#Bob desea realizar una compra por internet y por ende debe enviar sus datos personales por medio de un canal inseguro. Para hacer esto de manera segura, su navegador (cliente) debe cifrar su número de tarjeta de crédito para que llegue a la tienda virtual de compras (servidor) protegida. De esta forma, se hará uso del algoritmo RSA para realizar el proceso de cifrado y descifrado del número de la tarjeta de crédito. Para lo anterior, usar p = 47, q = 71, e = 79, m (número de tarjeta de crédito) = 6882 3268 7966 6683 y t = 6, y:

#a. Hallar la llave pública.
#b. Hallar la llave privada.
#c. Realizar el proceso de cifrado para m y obtener c.
#d. Realizar el proceso de descifrado para c y obtener m.

#Nota: ver las especificaciones del algoritmo en la página del curso (Topics > Public-Key Cryptosystems).


#def prime_mod_inv(x, mod):
#    return pow(x, mod - 2, mod)


def npublica(p,q):
    n=p*q
    return (n)

def opublica(p,q):
    o=(p-1)*(q-1)
    return (o)

def gcd(e,n):
    while n>0:
        e,n=n,e%n
        pass
    return e

def eclave(o):
    #aumento el e mientras  el gcd no sea 1
    e = 2
    while gcd(e,o) !=1:
        e+=1
        return e
#dclave basado de https://teampython.wordpress.com/
def dclave(e, m):
    x = lasty = 0
    lastx = y = 1
    while m != 0:
        #desde python 3 division entera //
        q = e // m
        e, m = m, e % m
        x, lastx = lastx - q*x, x
        y, lasty = lasty - q*y, y
    return lastx


def clave(p,q):
    #n: p*q 0:(p-1)*(q-1), e:coprimo de o, d:privada usando inv
    n=npublica(p,q)
    o=opublica(p,q)
    #e=eclave(o)
    e=79
    d = dclave(e, o)
    while d < 0:
        d += o
    #print("p",p,'q',q,'n=p*q',n,'o=(p-1)*(q-1)',o,'e',e,'d',d)
    return [n, e, d]

def c_relleno(list1):
    lista = []
    rango = len(list1)
    if rango >3:
        for m in range (3):
            lista.append(list1[m])
    elif rango ==3:
        return list1
    elif rango < 3:
        for m in range (rango):
            lista.append(list1[m])
        for m in range (3-rango):
            if m ==1:
                m = rango
            lista.append('1')

    else:
        print ("tamano lista error menor que cero WDF!")
    #print ('relleno',lista)
    return lista
def c_unir (list1,list2):
    lista = []
    rango1=len(list1)
    rango2=len(list2)
    rango = int(rango1+rango2)
    for m in range(rango):
        if (m) < (rango):
            lista.append(list1[m])
        elif (m) >= (rango):
            lista.append(list2[m-rango])
        else:
            print("paso algo inesperado ome")
    return lista

def mrsa(p,q,e,m,t):
    a,b,c=clave(p,q)
    #print('a,b,c',a,b,c)
    b=e
    rango=len(m)
    salir=0
    #print('rango:',rango,'b',b)
    list2=[]
    while salir <= rango:
        list1=[]
        #list2=[]
        #print('list1:',list1,'salir:',salir,'rango:',rango)

        for i in range (3):
            #i+=1
            #a=(i+salir)
            #print('i', i, 'i+salir',a)
            if(salir+i)>= rango:
                list1=c_relleno(list1)
            elif salir <= rango:
                list1.append(m[i+salir])
            else:
                print("algo paso error rango")



        #print('list1',list1,'list2',list2,'len',(len(list2)))
        salir+=3
        c=int(''.join(list1))
        #print('str1 list1',str1)



        #c = int(input("Number to encode: "))

        if not c:
            return
        #print('c',c,'b',b,'a',a)
        valor=(pow(c, b, a))
        list2.append(valor)
        #print('list2',list2)
    return list2

def drsa(p,q,e,m,t):
    a,b,c=clave(p,q)
    #print('a,b,c',a,b,c)
    b=e
    rango=len(m)

    #print('rango:',rango,'b',b)
    list2=[]
    for z in range (rango):
        w=m[z]
        valor=(pow(w, c, a))
        list2.append(valor)



        #print('list2',list2,'len',(len(list2)))

        #c=int(''.join(list1))
        #print('str1 list1',str1)


        #c = int(input("Number to encode: "))

        if not c:
            return
        #print('c',c,'b',b,'a',a)

        #print('list2',list2)
    return list2

#Main
card=list('6882326879666683')
#p,q,e,car,d, bloques
crsa=mrsa(47,71,79,card,6 )
print('cifrado rsa:',crsa)
dmrsa=drsa(47,71,79,crsa,6)
print('decifrado rsa:',dmrsa)
#print('decifrado rsa:',crsa)
#lista=list('4')
#crsa=mrsa(11,23,3,lista,6)
