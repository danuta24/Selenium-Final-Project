import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# # ### DANE TESTOWE:
valid_inputsearch = "woski"
valid_inputnosearch = "zestawy prezentowe"


# # Projekt: Danuta Jasińska
# # Data utworzenia: 27 maja 2021
# # Scenariusz testowy:
# # # Wyszukanie poprawnej i niepoprawnej wartości w polu tekstowym SZUKAJ na stronie www.soyalight.pl
class SoyaLightInputSearch(unittest.TestCase):
    # # Warunki wstępne:
    def setUp(self):
        #     # 1. Uruchomiona przeglądarka
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        #     # Maksymalizacja okna
        self.driver.maximize_window()
        #     # 2. Na stronie https://soyalight.pl#/
        self.driver.get("https://soyalight.pl#/")
        #
        #     # Włączenie implicitly wait - mechanizmu czekania na elementy max.30 sekund
        self.driver.implicitly_wait(30)

    # # Przejście do inputu Szukaj
    # # Wypełnienie inputu poprawną wartością
    #
    def testInvalidSearch(self):
        driver = self.driver
        title = driver.title
        print(title)
        self.assertEqual('SoyaLight', title)
        # Weryfikacja strony internetowej, na której przeprowadzone będą testy automatyczne

        #   # Przypadek testowy 001:
        #         # KROKI:
        #         # 1. Kliknij w pole tekstowe SZUKAJ
        #         # Metoda odszuka input Szukaj i wpiszę poprawną wartość
        wyszukaj_input = driver.find_element_by_xpath('//input[@placeholder="Szukaj"]')
        wyszukaj_input.click()
        #         # 2. Wpisz poprawną wartość w pole tekstowe SZUKAJ
        #         # Metoda odszuka napis Szukaj w polu tekstowym i zwróci poprawną wpisaną wartość
        wyszukaj_input.send_keys(valid_inputsearch, Keys.ENTER)
        informacja_komunikat = driver.find_element_by_xpath('//span[text()="Znaleziono produktów: 1"]')
        informacja_komunikat_tekst = informacja_komunikat.text
        self.assertEqual("Znaleziono produktów: 1", informacja_komunikat_tekst)
        sleep(5)
        #   3. Przejście do nazwy "woski do kominka", które przenoszą do podstrony danej oferty sprzedażowej
        # Metoda przejścia do produktu zwraca poprawną wartość wpisaną w polu Szukaj
        woskidokominka_btn = driver.find_element_by_class_name("productname")
        woskidokominka_btn.click()
        sleep(5)
        #   4.Iterowanie po liście dostępnych zapachów wosków do kominka
        lista_wybierz = driver.find_element_by_id("option_9")
        lista_wybierz.click()
        # 5. Wybór wartości z listy Wybierz
        zapachywoskow = driver.find_element_by_xpath('//select[@id="option_9"]/option[@value="41"]')
        zapachywoskow.click()
        sleep(5)
        # 6. Naciśnięcie buttona Do koszyka
        # Metoda spowoduje,że wybrany produkt o podanym zapachu zostanie dodany do koszyka
        dodaniedokoszyka = driver.find_element_by_xpath(
            '//fieldset[@class="addtobasket-container"]//button[@type="submit"]')
        dodaniedokoszyka.click()
        informacja_komunikat_dodaniedokoszyka = driver.find_element_by_xpath('//div[@class="alert-success alert"]//p')
        self.assertEqual('Produkt dodany do koszyka.', informacja_komunikat_dodaniedokoszyka.text)
        sleep(5)
        # 7. Kliknij w pole tekstowe SZUKAJ
        #   # Metoda odszuka input Szukaj i wpiszę niepoprawną wartość "zestawy prezentowe"
        wyszukaj_input_niepoprawnawartosc = driver.find_element_by_xpath('//input[@placeholder="Szukaj"]')
        wyszukaj_input_niepoprawnawartosc.click()
        sleep(5)
        # 8. Wpisanie w pole Szukaj niepoprawną wartość
        # Metoda wyszuka niepoprawną wartość
        wyszukaj_input_niepoprawnawartosc.send_keys(valid_inputnosearch)
        buttonlupka = driver.find_element_by_xpath(
            '//button[@class="js__search-submit-btn search-btn search__input-area-item'
            ' btn btn-red search__btn-search r--l-flex r--l-flex-vcenter r--l-flex-hcenter"]')
        buttonlupka.click()
        sleep(5)
        informacja_komunikat_nieznalezionawartosc = driver.find_element_by_xpath(
            '//span[text()="Znaleziono produktów: 0"]')
        informacja_komunikat_nieznalezionawartosc_tekst = informacja_komunikat_nieznalezionawartosc.text
        self.assertEqual('Znaleziono produktów: 0', informacja_komunikat_nieznalezionawartosc_tekst)
        sleep(5)

    #    #Oczekiwany rezultat testu: Sprawdzenie czy znajduje poprawną i niepoprawną wartość w polu Search dla strony soyalight.pl
    #    #Rezultat testu: Poprawnie działająca walidacja, która zwraca komunikat na niebieskim polu
    #    # Przeniesienie do nowego widoku, który zwraca poprawny komunikat
    # #
    def tearDown(self):
        # #     # Zakończenie testu
        self.driver.quit()


# #
# # # Jeśli uruchamiamy z tego pliku
if __name__ == "__main__":
    # #     # Użyjmy metody main(), która zajmie się resztą
    unittest.main(verbosity=2)
