import webscraper


text = """
"""
print(f"EMAIL: {webscraper.find.email(text)}")
print(f"TELEPHONE: {webscraper.find.telephone(text)}")
print(f"ANSPRECHPARTNER: {webscraper.find.contact(text)}")