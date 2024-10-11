"Module providing regex"
import re

def normalize_phone(phone_number):
    "function to format given phone number or numbers"
    cleaned_number = re.sub(r'\D', '', phone_number)
    if not cleaned_number.startswith("+"):
        if cleaned_number.startswith("380"):
            cleaned_number = "+" + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    return cleaned_number
# End-of-file (EOF)