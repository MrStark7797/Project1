from urllib.request import urlopen

def findNameFromEmail(email):
    x = email.find("@")
    y = email[:x]
    weblink = "https://www.ecs.soton.ac.uk/people/" + y
    website = urlopen(weblink)
    found = False
    while found == False:
        z = website.readline()
        z = str(z)
        check =z.find("heading-m inline-block text-prussianDark")
        if check != -1:
            found = True
            startname = z.find(">") + 1
            endname = z.find("/") - 1
            name = z[startname:endname]
            print(f"{y}@soton.ac.uk is {name}")

emailFile = open("emails.txt", "r")
for x in emailFile:
    findNameFromEmail(x)