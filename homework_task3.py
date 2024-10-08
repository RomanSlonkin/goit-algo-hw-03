"Module providing regex"
import re

phone_numbers = ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

def clean_phone(phone_number):
    "function to format given phone number or numbers"
    if isinstance(phone_number, list):
        for phone in phone_number:
            cleaned_number = re.sub(r'\D', '', phone)
            if not cleaned_number.startswith("+"):
                if cleaned_number.startswith("380"):
                    cleaned_number = "+" + cleaned_number
                else:
                    cleaned_number = "+38" + cleaned_number
            print(cleaned_number)
    else:
        cleaned_number = re.sub(r'\D', '', phone_number)
        if not cleaned_number.startswith("+"):
            if cleaned_number.startswith("380"):
                cleaned_number = "+" + cleaned_number
            else:
                cleaned_number = "+38" + cleaned_number
        print(cleaned_number)

clean_phone("38050-111-22-22")
clean_phone(phone_numbers)
# End-of-file (EOF)