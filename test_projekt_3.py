# Toto je stránka mojí kapely, takže vím záměry některých funkcí
# v prvním testu testuji, zda je v titulku slovo Kráľová, protože
# vím, že to je skutečně záměr

import re
from playwright.sync_api import Page, expect
url = "https://kralovamusic.sk/"

# první test - načtení stránky, očekávané jméno "Kralova" v nadpisu nehledě na velikost písmen
def test_homepage_title(page: Page):
    page.goto(url)
    expect(page).to_have_title(re.compile("Kralova", re.IGNORCASE))


