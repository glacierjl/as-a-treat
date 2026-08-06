# test file with significantly reduced capacity
# the original can be found at ./defaultarrays.py

# Format: {folx} can have {treat}, as a treat
# UNLESS the treat uses alternate wording, in which case the format is: {folx} {treat}, as a treat

# Note: The case of these will not be changed.
FOLX = [
    "Transfems",
    "Foxgirls",
    "Foxes",
    "Transmascs",
    "Catgirls",
    "Catboys",
    "Wolfgirls",
    "Wolfboys",
    "Puppygirls",
    "Dogboys",
    "Furries",
    "Ratgirls",
    "Wyverns",
    "Deergirls",
    "We&",
    "Simor Haskiner",
]

# Note: The case of these will not be changed.
# either give a string or a JSON object
# with "text" and "alt_wording" keys
TREATS = [
    '{"content_warning": "True", "warning_text": "lewd", "text": "steaming hot lesbian sex"}',
    '{"content_warning": "True", "warning_text": "nsfw", "alt_wording": "True", "text": "can fuck someone senseless"}',
    "huggies",
    '{"alt_wording": "True", "text": "can get in a cuddle pile"}',
]
