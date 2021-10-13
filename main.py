def verificare_prim(n):
    '''
    -determina daca un numar dat n este prim sau nu
    Input:
    -parametru: n (de tip intreg)
    Output:
    -va returna True, daca n este prim, sau False, in caz contrar(de tip bool)
    '''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2+1, 2):
        if n%i == 0:
            return False
    return True


def nr_divizori(n):
    '''
    -determina numarul de divizori ai unui numar n dat
    Input:
    -parametru: n (de tip intreg)
    Output:
    -va returna nr(tip intreg) care va fi numarul de divizori ai lui n
    '''
    if n==0:
        return 0
    if n==1:
        return 1
    nr=2
    for i in range(2,n//2+1):
        if n % i == 0:
            nr+=1
    return nr


def citire(lista):
    nr_elemente=int(input("Dati numarul de elemente:"))
    for i in range(nr_elemente):
        lista.append(int(input("Dati numar:")))
    return lista


def verificare_secventa_prim(lista):
    '''
    -verifica daca toate elementele din lista data sunt numere prime
    Input:
    -o lista lista[] cu date de tip int
    Output:va returna True, daca lista are toate elementele prime
    sau False, in caz contrar(de tip bool)
    -
    '''
    for i in lista:
        if not verificare_prim(i):
            return False
    return True


def get_longest_all_primes(lista):
    '''
    - determina cea mai lunga subsecventa de numere prime dintr-o lista
    Input:
    - o lista lista[] cu date de tip int
    Output:
    - o lista secv_max_prim[] cu date de tip int ce va contine secventa maxima ceruta
    '''
    secv_max_prim=[]
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if verificare_secventa_prim(lista[i:j+1]) and len(lista[i:j+1])>len(secv_max_prim):
                secv_max_prim=lista[i:j+1]
    return secv_max_prim


def test_get_longest_all_primes():
    assert get_longest_all_primes([3,5,7,8])==[3,5,7]
    assert get_longest_all_primes([12,4,8,9])==[]
    assert get_longest_all_primes([3,7,15,2,3,5])==[2,3,5]
    assert get_longest_all_primes([3,7,13,17,23])==[3,7,13,17,23]


def verificare_secventa_div(lista):
    '''
    -verifica daca toate elementele din lista data au acelasi numar de divizori
    Input:
    - o lista lista[] cu date de tip int
    Output: va returna True, daca toate elementele din lista au acelasi nr de divizori
    sau False, in caz contrar(de tip bool)
    -
    '''
    nr_div_element1=nr_divizori(lista[0])
    for i in lista:
        if nr_divizori(i)!=nr_div_element1:
            return False
    return True


def get_longest_same_div_count(lista):
    '''
    - determina cea mai lunga secventa de numere ce au acelasi numar de divizori
    Input:
    - o lista lista[] cu date de tip int
    Output
    - o lista secv_max_div[] cu date de tip int ce va contine secventa maxima ceruta
    '''
    secv_max_div=[]
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if verificare_secventa_div(lista[i:j+1]) and len(lista[i:j+1])>len(secv_max_div):
                secv_max_div=lista[i:j+1]
    return secv_max_div


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([4, 2,3,6]) == [2,3]
    assert get_longest_same_div_count([12, 3, 15, 25, 9, 16]) == [25,9]
    assert get_longest_same_div_count([1,2,1,1]) == [1,1]
    assert get_longest_same_div_count([12,2,6]) == [12]


def verificare_secventa_neprim(lista):
    '''
        -verifica daca toate elementele din lista data sunt numere neprime
        Input:
        -o lista lista[] cu date de tip int
        Output:va returna True, daca lista are toate elementele neprime
        sau False, in caz contrar(de tip bool)
        -
        '''
    for i in lista:
        if verificare_prim(i):
            return False
    return True



def get_longest_all_not_prime(lista):
    '''
        - determina cea mai lunga secventa de numere neprime
        Input:
        - o lista lista[] cu date de tip int
        Output
        - o lista secv_max_neprim[] cu date de tip int ce va contine secventa maxima ceruta
        '''
    secv_max_neprim=[]
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if verificare_secventa_neprim(lista[i:j+1]) and len(lista[i:j+1])>len(secv_max_neprim):
                secv_max_neprim=lista[i:j+1]
    return secv_max_neprim

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2,3,5]) == []
    assert get_longest_all_not_prime([7,12,6,8,11]) == [12,6,8]
    assert get_longest_all_not_prime([2,13,4]) == [4]


def main():
    test_get_longest_all_primes()
    test_get_longest_same_div_count()
    test_get_longest_all_not_prime()
    while True:
        print("1.Citire date.")
        print("2.Determinare cea mai lunga subsecventa de numere prime.")
        print("3.Determinare cea mai lunga subsecventa de numere ce au acelasi nr de divizori.")
        print("4.Determinare cea mai lunga subsecventa de numere neprime.")
        print("5.Iesire.")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista=[]
            citire(lista)
        elif optiune == "2":
            print(get_longest_all_primes(lista))
        elif optiune == "3":
            print(get_longest_same_div_count(lista))
        elif optiune == "4":
            print(get_longest_all_not_prime(lista))
        elif optiune == "5":
            print("Meniul se va inchide.")
            break
        else:
            print("Optiune invalida.Reincercati!")


if __name__ == '__main__':
    main()
