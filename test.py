from urllib.request import urlopen
def findNameFromEmail(email):
    y = email[:email.find("@")]
    website, found =urlopen("https://www.ecs.soton.ac.uk/people/" + y), bool(False)
    while found == False:
        z = str(website.readline())
        if z.find("heading-m inline-block text-prussianDark") != -1:
            found, startname, endname = True, z.find(">") + 1, z.find("/") - 1
            name = z[startname:endname]
            print(f"{y}@soton.ac.uk is {name}")
emailFile = open("emails.txt", "r")
while True:
    print("Waiting For email\n")
    email = input()
    if email == "":
        break
    findNameFromEmail(email)