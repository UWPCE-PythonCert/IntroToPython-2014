donors = [
    ['John Lennon', 100.00, 50.00, 586.78],
    ['Paul McCartney', 200.00, 150.00],
    ['Ringo Starr', 1.00],
    ['George Harrison', 1000.00, 500.00, 1586.78],
    ['Yoko Ono', 275.50, 5.00]
]

menu = input("Enter '1' to send a thank you. Enter '2' to create a report.")

if menu == '1':
    full_name = input("Enter the donor's full name or type 'list' to see all donors.")

while full_name == 'list':
    for donor in donors:
        print(donor[0])
    full_name = input("Enter the donor's full name or type 'list' to see all donors.")
    break

if full_name not in donors:
    donors.append([full_name])

donation_amount = input('Enter the donation amount.')
# this doesnt work for floats. fix or change to strings since you're not doing any math with them?
while not donation_amount.isnumeric():
    donation_amount = input('Enter the donation amount as a whole number.')
    break

for donor in donors:
    if full_name == donor[0]:
        donor.append(donation_amount)

thank_you = """Dear {},
Thank you for your generous donation of {} dollars. You're
the best!

Sincerely,
Your favorite charity """.format(full_name, donation_amount)

print(thank_you)

menu = input("Enter '1' to send a thank you. Enter '2' to create a report.")



