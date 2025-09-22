import re

# ============= EMAIL =============
email_regex = r'''
    ([a-zA-Z0-9._-]+)                  # local part
    (?:[ \t]*[\(\[\{]*\s*(?i:@|at)\s*[\)\]\}]*[ \t]*)  # @ part, allow spaces/tabs
    ([a-zA-Z0-9.-]+)                   # domain
    (?:[ \t]*[\(\[\{]*\s*(?i:\.|dot)\s*[\)\]\}]*[ \t]*)  # dot, allow spaces/tabs
    ([a-zA-Z]{2,})                     # TLD
'''
email_pattern = re.compile(email_regex, re.VERBOSE)

# ============= TELEHPONE =============
telephone_regex = r'''
    (?=[+0-9]) # must start with + or digit
    [0-9\+\/\-\(\)\[\]\{\} \t]+ # number
'''
telehpone_pattern = re.compile(telephone_regex, re.VERBOSE)

# ============= CONTACT =============
suchwort = [
    "fr", "hr", "frau", "herr",
    "Geschäftsführer", "GeschäftsführerIn", "Geschäftsführer/in", "Geschäftsführer:in",
    "Inhaber", "Inhaberin",
    "Vorsitzender", "Vorsitzende", "Vorstand",
    "Leiter", "Leiterin",
    "Ansprechpartner", "Ansprechperson",
    "Redaktion", "Redaktionsteam",
    "CEO", "Managing Director", "Owner",
    "Director", "Head", "Contact Person",
    "Editor", "Editorial Team"
]
escaped_suchwort = [re.escape(s) for s in suchwort]
suchwort_pattern = "|".join(escaped_suchwort)
contact_regex = rf'''
    (?i)                # case-insensitive
    \b
    ({suchwort_pattern})[.:,;]?  # Suchwort, allow optional dot
    \s+
    ([A-ZÄÖÜ][a-zäöüß]*\.?)   # Vorname or initial
    \s+
    ([A-ZÄÖÜ][a-zäöüß]*\.?)   # Nachname
'''
contact_pattern = re.compile(contact_regex, re.VERBOSE)