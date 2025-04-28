'''Programul gestioneaza angajatii dintr-o firma.

Aplicatia permite:
- adaugarea de noi angajati
- cautarea unui angajat dupa cnp-ul acestuia
- modificarea datelor unui angajat selectat pe baza cnp-ului
- stergerea unui angajat pe baza cnp-ului acestuia
- afisarea tuturor angajatilor
- calcularea costului total al salariilor din firma
- calcularea costului total al salariilor dintr-un departament
- realizarea fuluturasului de salar pentru un angajat
- afisarea tuturor angajatilor cu o anumita senioritate
- afisarea tuturor angajatilor dintr-un departament

Datele stocate referitor la un angajat sunt:
- nume
- prenume
- cnp
- varsta
- salar
- departament
- senioritate
'''


import json


def meniu():
    '''Afiseaza meniul, citeste optiunea introdusa de utilizator
    si verifica daca e valida. Daca e valida, va apela
    functionalitatea corespunzatoare.

    Arguments:
    None

    Returns:
    optiune: str -> valoarea optiunii introdusa de catre utilizator
    '''

    meniu = '''
    ----- Meniu principal -----
    1. Adaugare angajat
    2. Cautare angajat in functie de CNP
    3. Modificare date angajat in functie de CNP
    4. Stergere angajat
    5. Afisare angajati
    6. Calculator cost total salarii
    7. Calculator cost total salarii departament
    8. Calculator fluturas salariu angajat
    9. Afisarea angajatilor cu o anumita senioritate
    10. Afisarea angajatilor dintr-un departament
    11. Iesire
    '''

    print(meniu)
    try:
        optiune = int(input('Introduceti optiunea: '))
        if not 1 <= optiune <= 11:
            print('Optiune invalida! Introduceti una din optiunile disponibile.')

    except ValueError:
        print('Optiune invalida! Optiunea trebuie sa fie un numar prezent in meniu!')

    return optiune


def validare_nume(nume):
    '''Verifica daca numele este corespunaztor (contine numai litere, incepe cu litera mare)

    Arguments:
    nume: str - numele persoanei introduse

    Returns:
    bool - True daca e valid, False in caz contrar
    '''

    return nume.isalpha() and nume[0].isupper()


def validare_cnp(cnp):
    '''Verifica daca CNPul este corespunzator (contine numai cifre, are 13 caractere)

    Arguments:
    cnp: str - CNPul persoanei introduse

    Returns:
    bool - True daca e valid, False in caz contrar
    '''

    return cnp.isdigit() and cnp.isascii() and len(cnp) == 13


def validare_varsta(varsta):
    '''Verifica daca varsta este corespunzatoare (contine 2 cifre, este cuprinsa intre 18 si 65)

    Arguments:
    varsta: str - Varsta persoanei introduse

    Returns:
    bool - True daca e valida, False in caz contrar
    '''

    return varsta.isdigit() and varsta.isascii() and len(varsta) == 2 and 18 <= int(varsta) <= 65


def validare_salar(salar):
    '''Verifica daca salarul este corespunzator (este peste minimul pe economie - 4050lei)

    Arguments:
    salar: float - Salarul persoanei introduse

    Returns:
    bool - True daca e valid, False in caz contrar
    '''

    return salar >= 4050


def validare_departament(departament):
    '''Verifica daca departamentul face parte din lista predefinita si ca este un string format
    numai din caractere

    Arguments:
    nume: str - numele departamentului

    Returns:
    bool - True daca e valid, False in caz contrar
    '''

    departamente = ['HR', 'Marketing', 'IT', 'Finance']

    return departament in departamente and departament.isalpha()


def validare_senioritate(senioritate):
    '''Verifica daca departamentul face parte din lista predefinita si ca este un string format
    numai din caractere

    Arguments:
    nume: str - senioritatea angajatului

    Returns:
    bool - True daca e valida, False in caz contrar
    '''

    senioritati = ['junior', 'mid', 'senior']

    return senioritate in senioritati and senioritate.isalpha()


def introducere_date_angajat(lista_angajati, adaug_cnp=True):
    '''Citeste informatiile despre un nou angajat, le valideaza, iar in cazul in care
    sunt valide adauga noul angajat in lista de angajati ai firmei.

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    while True:
        nume = input('Introduceti numele: ')
        if validare_nume(nume):
            break
        else:
            print('Numele nu este valid! Trebuie sa contina numai litere si sa inceapaca cu litera mare.')

    while True:
        prenume = input('Introduceti prenumele: ')
        if validare_nume(prenume):
            break
        else:
            print('Prenumele nu este valid! Trebuie sa contina numai litere si sa inceapaca cu litera mare.')

    if adaug_cnp:
        while True:
            cnp = input('Introduceti CNPul: ')
            if validare_cnp(cnp):
                break
            else:
                print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

    while True:
        varsta = input('Introduceti varsta: ')
        if validare_varsta(varsta):
            break
        else:
            print('Varsta introdusa este invalida! Trebuie ca angajatul sa aiba peste 18 ani.')


    while True:
        try:
            salar = float(input('Introduceti salarul: '))
            if validare_salar(salar):
                break
            else:
                print('Salarul introdus nu este conform! Trebuie sa fie peste minimul pe economie.')
        except ValueError:
            print('Salarul introdus este invalid! Trebuie sa fie un numar rational.')

    while True:
        departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
        if validare_departament(departament):
            break
        else:
            print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

    while True:
        senioritate = input('Introduceti senioritatea (junior, mid, senior): ')
        if validare_senioritate(senioritate):
            break
        else:
            print('Senioritatea introdusa nu este valida! Trebuie sa fie una din lista mentionata.')

    angajat = {
        'Nume': nume,
        'Prenume': prenume,
        'CNP': cnp,
        'Varsta': varsta,
        'Salar': salar,
        'Departament': departament,
        'Senioritate': senioritate
    }

    lista_angajati.append(angajat)
    if adaug_cnp:
        print('Angajatul a fost introdus cu succes!')
    else:
        print('Datele angajatului au fost modificate cu succes!')


def afisare_angajat(angajat):
    '''Afiseaza datele angajatului primit ca si parametru sub o forma mai estetica

    Arguments:
    angajat: Dict -> informatiile unui angajat

    Returns:
    None
    '''

    delimitator = 10 * '-'
    afisaj = f'\n{delimitator}\nNume: {angajat.get("Nume")}\nPrenume: {angajat.get("Prenume")}\nCNP: {angajat.get("CNP")}\
               \nVarsta: {angajat.get("Varsta")}\nSalar: {angajat.get("Salar")}\nDepartament: {angajat.get("Departament")}\
               \nSenirotate: {angajat.get("Senioritate")}'
    print(afisaj)


def cautare_angajat_cnp(lista_angajati):
    '''Cauta un angajat in lista de angajati ai firmei dupa CNP-ul acestuia si afiseaza datele
    angajatului

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    while True:
        cnp = input('Introduceti CNP-ul: ')
        if validare_cnp(cnp):
            break
        else:
            print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

    found = False
    for angajat in lista_angajati:
        if angajat.get('CNP') == cnp:
            found = True
            afisare_angajat(angajat)
            break

    if not found:
        print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


def modificare_angajat_cnp(lista_angajati):
    '''Modifica datele unui angajat pe baza cnp-ului furnizat de catre utilizator

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    while True:
        cnp = input('Introduceti CNP-ul: ')
        if validare_cnp(cnp):
            break
        else:
            print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

    found = False
    for angajat in lista_angajati:
        if angajat.get('CNP') == cnp:
            found = True
            print('Datele curente ale angajatului:')
            afisare_angajat(angajat)
            introducere_date_angajat(lista_angajati, adaug_cnp=False)
            print('Noile date ale angajatului sunt:')
            afisare_angajat(angajat)
            break

    if not found:
        print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


def stergere_angajat_cnp(lista_angajati):
    '''Sterge un angajat din lista angajatilor firmei pe baza cnp-ului introdus de catre utilizator

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    while True:
        cnp = input('Introduceti CNP-ul: ')
        if validare_cnp(cnp):
            break
        else:
            print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

    found = False
    for angajat in lista_angajati:
        if angajat.get('CNP') == cnp:
            found = True
            lista_angajati.remove(angajat)
            break

    if not found:
        print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')
    else:
        print('Angajatul a fost sters cu succes!')


def afisare_angajati(lista_angajati, departament=False, senioritate=False):
    '''Afiseaza toti angajatii prezenti in sistem

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    if departament:
        while True:
            departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
            if validare_departament(departament):
                break
            else:
                print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

    if senioritate:
        while True:
            senioritate = input('Introduceti senioritatea (junior, mid, senior): ')
            if validare_senioritate(senioritate):
                break
            else:
                print('Senioritatea introdusa nu este valida! Trebuie sa fie una din lista mentionata.')

    for angajat in lista_angajati:
        if departament:
            if angajat.get('Departament') == departament:
                afisare_angajat(angajat)
        elif senioritate:
            if angajat.get('Senioritate') == senioritate:
                afisare_angajat(angajat)
        else:
            afisare_angajat(angajat)


def calculator_cost_salarii(lista_angajati, firma=True):
    '''Calculeaza costul salariilor la nivel de firma sau la nivel de departament in cazul in care departamentul
    este specificat.

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar
    total: bool -> daca este True se calculeaza pentru toata firma, iar daca este False este necesara introducerea
                         departamentului pentru care se face calculul

    Returns:
    None
    '''

    departament = None
    if not firma:
        while True:
            departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
            if validare_departament(departament):
                break
            else:
                print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

    cost_salarii = 0
    for angajat in lista_angajati:
        if not departament:
            cost_salarii += angajat.get('Salar')
        else:
            if angajat.get('Departament') == departament:
                cost_salarii += angajat.get('Salar')

    if not firma:
        print(f'Costul total al salariilor din departamentul {departament} este: {cost_salarii} lei')
    else:
        print(f'Costul total al salariilor este: {cost_salarii} lei')


def calculator_fluturas_salar(lista_angajati):
    '''Genereaza fluturasul de salar pentru un angajat.

    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    while True:
        cnp = input('Introduceti CNP-ul: ')
        if validare_cnp(cnp):
            break
        else:
            print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

    found = False
    for angajat in lista_angajati:
        if angajat.get('CNP') == cnp:
            found = True
            salar = angajat.get('Salar')
            cas = 0.1 * salar
            cass = 0.25 * salar
            impozit = (salar - cas - cass) * 0.1
            net = salar - cas - cass - impozit

            delimitator = 10 * '-'
            afisaj = f'\n{delimitator}\nNume: {angajat.get("Nume")}\nPrenume: {angajat.get("Prenume")}\nBrut: {angajat.get("Salar")}\n\
                       \nCAS: {cas}\nCASS: {cass}\nImpozit: {impozit}\nNet: {net}'
            print(afisaj)
            break

    if not found:
        print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


def incarca_date_json():
    '''Citeste datele angajatilor din fisierul json folosit ca baza de date

    Arguments:
    None

    Returns:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar
    '''

    lista_angajati = []
    try:
        with open('date_angajati.json', 'r') as json_file:
            lista_angajati = json.load(json_file)
    except FileNotFoundError:
        print('Fisierul JSON care contine informatiile despre angajati nu a fost gasit! Initializare angajati nereusita.')
    except json.JSONDecodeError:
        print('Eroare la decodarea fisierului JSON! Initializare angajati nereusita.')
    except Exception as exception:
        print('A intervenit o eroare neasteptata! Initializare angajati nereusita.')

    return lista_angajati


def salveaza_date_json(lista_angajati):
    '''Salveaza datele angajatilor in fisierul json folosit ca baza de date

    Arguments:
    lista_angajati: List -> lista care contine angajatii firmei sub forma de dictionar

    Returns:
    None
    '''

    with open('date_angajati.json', 'w') as json_file:
        json.dump(lista_angajati, json_file, indent=4)


def app():
    '''Functie principala care ruleaza aplicatia

    Arguments:
    None

    Returns:
    None
    '''

    lista_angajati = incarca_date_json()

    while True:
        optiune = meniu()
        match optiune:
            case 1: introducere_date_angajat(lista_angajati)
            case 2: cautare_angajat_cnp(lista_angajati)
            case 3: modificare_angajat_cnp(lista_angajati)
            case 4: stergere_angajat_cnp(lista_angajati)
            case 5: afisare_angajati(lista_angajati)
            case 6: calculator_cost_salarii(lista_angajati)
            case 7: calculator_cost_salarii(lista_angajati, firma=False)
            case 8: calculator_fluturas_salar(lista_angajati)
            case 9: afisare_angajati(lista_angajati, senioritate=True)
            case 10: afisare_angajati(lista_angajati, departament=True)
            case 11:
                print('Iesire din program.')
                salveaza_date_json(lista_angajati)
                break


if __name__ == '__main__':
    app()
