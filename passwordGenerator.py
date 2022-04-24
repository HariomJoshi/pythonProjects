import random
from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF


# below class generates a password
class passGenerator:
    encrypt_dict = {0: "4(x",1: "a@", 2: "#3b", 3: "y$4", 4: "*", 5: "&^", 6: "!9",
                    7: "~2V", 8: ");", 9: "?B"}

    def generate(self):
        password = ""
        for i in range(4):
            key = random.randrange(0, 10, 1)
            password = password + self.encrypt_dict[key]

        return password
 


class file:
    # makes a file named password.pdf and writes all the password in it
    def fileWriter(self, website, password):
        with open("passwords.txt", 'a') as file:
            file.write("\n")
            file.write(f"{website} -> {password}\n")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        with open("passwords.txt", 'r') as file:
            for line in file:
                pdf.cell(40, 10, file.readline(), ln=1, align="C")

        pdf.output("passwords.pdf")


    # encrypts the file passed to it as pdf_file
    def encrypt_file(self, pdf_file):
        fileIn = PdfFileReader(pdf_file)
        fileOut = PdfFileWriter()

        length = fileIn.numPages  # getting the length of pdf

        # iterating through the pdf pages, and copying pages in fileOut
        for pageIdx in range(length):
            page = fileIn.getPage(pageIdx)
            fileOut.addPage(page)

        fileOut.encrypt("Hariom")  # encrypting the file in which we just added the pages

        with open("passwords.pdf", 'wb') as f:
            fileOut.write(f)  # we copied fileOUt to f


# main function, program executes from here
if __name__ == '__main__':
    passW = passGenerator.generate(passGenerator)
    website = input("For which website do you want password for? ")
    file.fileWriter(file, website, passW)
    file.encrypt_file(file, "passwords.pdf")

    print(f"Generated Password: {passW}")
