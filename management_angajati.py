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


class Angajat:
    def __init__(self, nume, prenume, cnp, varsta, salar, departament, senioritate):
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp
        self.varsta = varsta
        self.salar = salar
        self.departament = departament
        self.senioritate = senioritate

    def afisare(self):
        delimitator = 10 * '-'
        afisaj = f'\n{delimitator}\nNume: {self.nume}\nPrenume: {self.prenume}\nCNP: {self.cnp}\nVarsta: {self.varsta}\nSalar: {self.salar}\nDepartament: {self.departament}\nSenioritate: {self.senioritate}'
        print(afisaj)


class Companie:
    def __init__(self):
        self.angajati = []

    def initializare(self):
        try:
            with open('date_angajati.json', 'r') as json_file:
                json_data = json.load(json_file)
            for item in json_data:
                    angajat = Angajat(item.get('Nume'), item.get('Prenume'), item.get('CNP'), item.get('Varsta'), item.get('Salar'), item.get('Departament'), item.get('Senioritate'))
                    self.angajati.append(angajat)

        except FileNotFoundError:
            print('Fisierul JSON care contine informatiile despre angajati nu a fost gasit! Initializare angajati nereusita.')
        except json.JSONDecodeError:
            print('Eroare la decodarea fisierului JSON! Initializare angajati nereusita.')
        except Exception as exception:
            print('A intervenit o eroare neasteptata! Initializare angajati nereusita.')
            print(f'Eroare: {exception}')


    def salvare_informatii(self):
        lista_angajati = []
        for angajat in self.angajati:
            item = {
                'Nume': angajat.nume,
                'Prenume': angajat.prenume,
                'CNP': angajat.cnp,
                'Varsta': angajat.varsta,
                'Salar': angajat.salar,
                'Departament': angajat.departament,
                'Senioritate': angajat.senioritate
            }
            lista_angajati.append(item)

        with open('date_angajati.json', 'w') as json_file:
            json.dump(lista_angajati, json_file, indent=4)


    def introducere_date_angajat(self, cnp=None, index=None):
        while True:
            nume = input('Introduceti numele: ')
            if self._validare_nume(nume):
                break
            else:
                print('Numele nu este valid! Trebuie sa contina numai litere si sa inceapaca cu litera mare.')

        while True:
            prenume = input('Introduceti prenumele: ')
            if self._validare_nume(prenume):
                break
            else:
                print('Prenumele nu este valid! Trebuie sa contina numai litere si sa inceapaca cu litera mare.')

        if not cnp:
            while True:
                cnp = input('Introduceti CNPul: ')
                if self._validare_cnp(cnp):
                    break
                else:
                    print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

        while True:
            varsta = input('Introduceti varsta: ')
            if self._validare_varsta(varsta):
                break
            else:
                print('Varsta introdusa este invalida! Trebuie ca angajatul sa aiba peste 18 ani.')

        while True:
            try:
                salar = float(input('Introduceti salarul: '))
                if self._validare_salar(salar):
                    break
                else:
                    print('Salarul introdus nu este conform! Trebuie sa fie peste minimul pe economie.')
            except ValueError:
                print('Salarul introdus este invalid! Trebuie sa fie un numar rational.')

        while True:
            departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
            if self._validare_departament(departament):
                break
            else:
                print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

        while True:
            senioritate = input('Introduceti senioritatea (junior, mid, senior): ')
            if self._validare_senioritate(senioritate):
                break
            else:
                print('Senioritatea introdusa nu este valida! Trebuie sa fie una din lista mentionata.')

        angajat = Angajat(nume, prenume, cnp, varsta, salar, departament, senioritate)
        if not index:
            self.angajati.append(angajat)
            print('Angajatul a fost introdus cu succes!')
        else:
            self.angajati[index] = angajat
            print('Datele angajatului au fost modificate cu succes!')


    def cautare_angajat_cnp(self):
        while True:
            cnp = input('Introduceti CNP-ul: ')
            if self._validare_cnp(cnp):
                break
            else:
                print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

        found = False
        for angajat in self.angajati:
            if angajat.cnp == cnp:
                found = True
                angajat.afisare()
                break

        if not found:
            print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


    def modificare_angajat_cnp(self):
        while True:
            cnp = input('Introduceti CNP-ul: ')
            if self._validare_cnp(cnp):
                break
            else:
                print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

        found = False
        for index, angajat in self.angajati:
            if angajat.cnp == cnp:
                found = True
                print('Datele curente ale angajatului:')
                angajat.afisare()
                self.introducere_date_angajat(cnp, index)
                break

        if not found:
            print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


    def stergere_angajat_cnp(self):
        while True:
            cnp = input('Introduceti CNP-ul: ')
            if self._validare_cnp(cnp):
                break
            else:
                print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

        found = False
        for angajat in self.angajati:
            if angajat.cnp == cnp:
                found = True
                self.angajati.remove(angajat)
                break

        if not found:
            print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')
        else:
            print('Angajatul a fost sters cu succes!')


    def afisare_angajati(self, departament=False, senioritate=False):
        if departament:
            while True:
                departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
                if self._validare_departament(departament):
                    break
                else:
                    print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

        if senioritate:
            while True:
                senioritate = input('Introduceti senioritatea (junior, mid, senior): ')
                if self._validare_senioritate(senioritate):
                    break
                else:
                    print('Senioritatea introdusa nu este valida! Trebuie sa fie una din lista mentionata.')

        for angajat in self.angajati:
            if departament:
                if angajat.departament == departament:
                    angajat.afisare()
            elif senioritate:
                if angajat.senioritate == senioritate:
                    angajat.afisare()
            else:
                angajat.afisare()


    def calculator_cost_salarii(self, firma=True):
        departament = None
        if not firma:
            while True:
                departament = input('Introduceti departamentul (HR, IT, Marketing, Finance): ')
                if self._validare_departament(departament):
                    break
                else:
                    print('Departamentul introdus este invalid! Trebuie sa fie unul din lista mentionata.')

        cost_salarii = 0
        for angajat in self.angajati:
            if not departament:
                cost_salarii += angajat.salar
            else:
                if angajat.get('Departament') == departament:
                    cost_salarii += angajat.salar

        if not firma:
            print(f'Costul total al salariilor din departamentul {departament} este: {cost_salarii} lei')
        else:
            print(f'Costul total al salariilor este: {cost_salarii} lei')


    def calculator_fluturas_salar(self):
        while True:
            cnp = input('Introduceti CNP-ul: ')
            if self._validare_cnp(cnp):
                break
            else:
                print('CNPul introdus nu este valid! Trebuie sa contina 13 cifre!')

        found = False
        for angajat in self.angajati:
            if angajat.cnp == cnp:
                found = True
                salar = angajat.get('Salar')
                cas = 0.1 * salar
                cass = 0.25 * salar
                impozit = (salar - cas - cass) * 0.1
                net = salar - cas - cass - impozit

                delimitator = 10 * '-'
                afisaj = f'\n{delimitator}\nNume: {angajat.nume}\nPrenume: {angajat.prenume}\nBrut: {angajat.salar}\n\
                        \nCAS: {cas}\nCASS: {cass}\nImpozit: {impozit}\nNet: {net}'
                print(afisaj)
                break

        if not found:
            print(f'Angajatul cu CNP-ul: {cnp} nu a fost gasit! Verificati si reintroduceti CNP-ul corect.')


    def _validare_nume(self, nume):
        return nume.isalpha() and nume[0].isupper()


    def _validare_cnp(self, cnp):
        return cnp.isdigit() and cnp.isascii() and len(cnp) == 13


    def _validare_varsta(self, varsta):
        return varsta.isdigit() and varsta.isascii() and len(varsta) == 2 and 18 <= int(varsta) <= 65


    def _validare_salar(self, salar):
        return salar >= 4050


    def _validare_departament(self, departament):
        departamente = ['HR', 'Marketing', 'IT', 'Finance']
        return departament in departamente and departament.isalpha()


    def _validare_senioritate(self, senioritate):
        senioritati = ['junior', 'mid', 'senior']
        return senioritate in senioritati and senioritate.isalpha()


class Aplicatie:
    def __init__(self):
        self.companie = Companie()
        self.companie.initializare()


    def ruleaza(self):
        while True:
            optiune = self._meniu()
            match optiune:
                case 1: self.companie.introducere_date_angajat()
                case 2: self.companie.cautare_angajat_cnp()
                case 3: self.companie.modificare_angajat_cnp()
                case 4: self.companie.stergere_angajat_cnp()
                case 5: self.companie.afisare_angajati()
                case 6: self.companie.calculator_cost_salarii()
                case 7: self.companie.calculator_cost_salarii(firma=False)
                case 8: self.companie.calculator_fluturas_salar()
                case 9: self.companie.afisare_angajati(departament=True)
                case 10: self.companie.afisare_angajati(departament=True)
                case 11:
                    self.companie.salvare_informatii()
                    print('Iesire din program.')
                    break


    def _meniu(self):
        meniu = '''
            ---------------- Meniu principal ----------------
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
            -------------------------------------------------
            '''

        print(meniu)
        try:
            optiune = int(input('Introduceti optiunea: '))
            if not 1 <= optiune <= 11:
                print('Optiune invalida! Introduceti una din optiunile disponibile.')

        except ValueError:
            print('Optiune invalida! Optiunea trebuie sa fie un numar prezent in meniu!')

        return optiune


if __name__ == '__main__':
    aplicatie = Aplicatie()
    aplicatie.ruleaza()
