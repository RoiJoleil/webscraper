import spacy
from typing import Union, overload
from webscraper.patterns import email_pattern as _email_pattern
from webscraper.patterns import telehpone_pattern as _telehpone_pattern

NLP = spacy.load("de_core_news_sm")


# ============= EMAIL =============
@overload
def email(text: list[str]) -> set[str]:
    ...

@overload
def email(text: str) -> list[str]:
    ...

def email(text: Union[str, list[str]]) -> set[str]:
    """Return a set of email adresses"""
    if not isinstance(text, list):
        text = [text]
    
    result = set()
    for t in text:
        emails = (["{}@{}.{}".format(local, domain, tld) for local, domain, tld in _email_pattern.findall(t)])
        for e in emails:
            # We don’t want to scrape example/test emails
            if any(bad in e.lower() for bad in ['example', 'test']):
                continue
            result.add(e)

    return result


# ============= TELEPHONE =============
@overload
def telephone(text: list[str]) -> set[str]:
    ...

@overload
def telephone(text: str) -> set[str]:
    ...

def telephone(text: Union[str, list[str]]) -> set[str]:
    """Return a set of telephone number"""
    if not isinstance(text, list):
        text = [text]
    
    result = set()
    for t in text:
        candidates = _telehpone_pattern.findall(t)
        for c in candidates:
            # Length has to correlate with phone number length
            num_digits = sum(d.isdigit() for d in c)
            if not 7 <= num_digits <= 15:
                continue

            # Number has to start with 0 (local) or + (country-code)
            if not c[0] in ["0", "+"]:
                continue

            result.add(c)

    return result


# ============= CONTACT =============
@overload
def contact(text: list[str]) -> set[tuple[str, str, str]]:
    ...

@overload
def contact(text: str) -> set[tuple[str, str, str]]:
    ...

def contact(text: Union[str, list[str]]) -> set[tuple[str, str, str]]:
    """Return a set of contacts
    Tuple structure is: Title, first-name, last-name"""
    if not isinstance(text, list):
        text = [text]
    
    result = set()
    for t in text:
        doc = NLP(t)
        for ent in doc.ents:
            if ent.label_ == "PER":
                result.add(ent.text)
    return result


__all__ = ["email", "telephone", "contact"]