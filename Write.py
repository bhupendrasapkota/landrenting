def write_to_file(customer_firstname, customer_lastname, invoice_num, invoice_text):
    with open(f'{customer_firstname}_{customer_lastname}_{invoice_num}.txt', 'w') as invoice_file:
        invoice_file.write(invoice_text)