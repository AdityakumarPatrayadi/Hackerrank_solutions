import re
for _ in range(int(input())):
    str1 = input()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", str1) and not re.search(r"([\d])\1\1\1", str1.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")