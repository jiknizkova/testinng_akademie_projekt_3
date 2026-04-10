# Toto je stránka mojí kapely, takže vím záměry některých funkcí
# v prvním testu testuji, zda je v titulku slovo Kráľová, protože
# vím, že to je skutečně záměr

import re
from playwright.sync_api import Page, expect
url = "https://kralovamusic.sk/"

# první test - načtení stránky, očekávané jméno "Kráľová" v nadpisu nehledě na velikost písmen
def test_homepage_title(page: Page):
    page.goto(url)
    expect(page).to_have_title(re.compile("Kráľová", re.IGNORECASE))
    # passed

# druhý test - zkontrolujeme, zda se na stránce nachází nějaký odkaz
def test_link_exists(page: Page):
    page.goto(url)
    odkaz=page.locator("a")
    assert odkaz.count() > 0
    # passed


# třetí test - zkusíme kliknout na odkaz "o nás" s zkontrolujeme, že se url správně změnila
def test_link_o_nas(page:Page):
    page.goto(url)
    nova_url = page.get_by_role("link", name="O nás").click()

    assert nova_url =="https://kralovamusic.sk/o-nas/"