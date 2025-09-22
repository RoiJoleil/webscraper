import webscraper


text = """
Impressum

Paniceus Gastro Systemzentrale GmbH
Breite Straße 1-5
23552 Lübeck
KONTAKT

Tel.: +49 (0) 451 989 065 60
Fax: +49 (0) 451 989 065 70
E-Mail: info@paniceus.de

Für eine Tisch-Reservierung wähle bitte die jeweilige Telefonnummer des Restaurants oder reserviere online einen Tisch.

Geschäftsführer: Patrick Junge
Handelsregister: AG Lübeck, HRB 13077HL
Umsatzsteuer-Identifikationsnummer gemäß §27 a Umsatzsteuergesetz: DE350326082
AUFSICHTSBEHÖRDE

Hansestadt LÜBECK: Umwelt-, Natur- und Verbraucherschutz

Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV:

Paniceus Gastro Systemzentrale GmbH

Patrick Junge
Breite Straße 1-5
23552 Lübeck
"""
print(f"EMAIL: {webscraper.find.email(text)}")
print(f"TELEPHONE: {webscraper.find.telephone(text)}")
print(f"ANSPRECHPARTNER: {webscraper.find.contact(text)}")