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
    (?=[+0-9])
    [0-9\-\–\+\/\(\)\[\]\{\} \t]+
'''
telehpone_pattern = re.compile(telephone_regex, re.VERBOSE)
