def header():
    print("Month Dictionary\n")
    print("Find out which month is associated with each number!")

def footer():
    print("Exiting...\nGood Bye.")

def main(num, monthDictionary):
    print(f"The month related to {num} is: {monthDictionary.get(num, 'Invalid, Enter from 1-12.')}")

monthDictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

header()

while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        footer()
        break
    main(num, monthDictionary)