from elements.web_element import WebElement


class LanguageSelector:
    LOQ_POPUP_MENU = 'languageSwitcherBtn'
    LOC_LANG_KA = '//img[@alt="georgian"][1]'
    LOQ_LANG_SVANURI = '//p[text()="სვანური"]'
    LOQ_LANG_MEGRULI = '//p[text()="მეგრული"]'

    def __init__(self, browser):
        self.browser = browser
        self.popup_menu = WebElement(self.browser, self.LOQ_POPUP_MENU)
        self.georgian_lang = WebElement(self.browser, self.LOC_LANG_KA)
        self.popup_megruli_lang = WebElement(self.browser, self.LOQ_LANG_MEGRULI)
        self.popup_svanuri_lang = WebElement(self.browser, self.LOQ_LANG_SVANURI)

    def click_btn_open_popup(self):
        self.popup_menu.click()

    def click_btn_georgian_lang(self):
        self.georgian_lang.click()

    def click_btn_svanuri_lang(self):
        self.popup_svanuri_lang.click()

    def click_btn_megruli_lang(self):
        self.popup_megruli_lang.click()
