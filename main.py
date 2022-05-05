from pathlib import Path
import re

ipaddress_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
date_regex = "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
html_regex = "GET (/\D+)\.html"

dir_path = Path.cwd() / "logs"
for sub_path in dir_path.iterdir():
    log_file_path = sub_path
    print(f"Reading {log_file_path}")
    if log_file_path.exists():
        log_entry_list = []
        with log_file_path.open() as log_file:
            for line in log_file.readlines():
                if line != "\n":
                    log_entry_list.append(line.strip())
    for entry in range(0, 4):
        log_entry_list.pop(0)

    for entry in log_entry_list:
        try:
            valid_entry = re.search(html_regex, entry).group()
            valid_entry = valid_entry[4:]
            ip_address = re.search(ipaddress_regex, entry).group()
            date = re.search(date_regex, entry).group()
            print(f'{date} {valid_entry} {ip_address}')
        except:
            pass
    input('Press enter to continue\n')
