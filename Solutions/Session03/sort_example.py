def sort_key(item):
    name = item[0]
    last_name = name.split()[1]
    return last_name.upper()

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

print(sorted(donor_db, key=sort_key))
print()
print(sorted(donor_db, key=sort_key, reverse=True))
