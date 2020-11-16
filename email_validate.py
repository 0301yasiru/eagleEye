from validate_email import validate_email
import argparse

def read_file(file_name):
    with open(file_name, 'r') as base_file:
        content = base_file.read().split('\n')

    return content

def write_file(file_name, content):
    with open(file_name, 'w') as output:
        for item in content:
            output.write(item)
            output.write('\n')

def verify_emails(email, verify=False):
    if verify:
        return validate_email(email, verify=True)
    else:
        return validate_email(email)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('emails', help="Path to file which contains guessed emails", type=str)
    parser.add_argument('-o', '--output', help='Path to the file contains results', type=str)
    parser.add_argument('-v', '--verify', help='Verify Existance', default=False, type=str)
    parser.add_argument('-s', '--silent', help='Work in silent mode', default=False, type=bool)
    args = parser.parse_args()

    email_list = read_file(args.emails)
    verified_emails = []

    for email in email_list:
        if email:
            status = verify_emails(email, args.verify)

            if status:
                verified_emails.append(email)

            if not args.silent:
                print('{}\t--> {}'.format(status, email))

    if args.output:
        write_file(args.output, verified_emails)
    
    print('[+]Done!!')
    

if __name__ == '__main__':
    main()
