# PDF cracking using brute force attack, Roy Ben Avraham 05/03/2023 16:11
from pypdf import PdfReader
filename = 'roy_pdf_example.pdf'
# Go over the whole 4-digit password possibilities
for i in range(10000):
    password = f'{i:04}'  # Format the password with leading zeros
    print(password)
    pdf_file = open(filename, 'rb')
# Create a PDF reader object
    pdf_reader = PdfReader(pdf_file)
# Check if the PDF file is encrypted
    if pdf_reader.is_encrypted:
        # Attempt to decrypt the PDF file using the password
        print(password)
        if pdf_reader.decrypt(password) != 0:
            # If the password is correct, print the password and exit
            print(f'The password for {filename} is {password}.')
            break
# Close the PDF file
    pdf_file.close()


