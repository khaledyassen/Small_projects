import base64

def combine_files(user_file, password_file):
    with open(user_file, 'r') as users, open(password_file, 'r') as passwords:
        user_lines = users.readlines()
        password_lines = passwords.readlines()

        combined_credentials = []
        for user_line in user_lines:
            for password_line in password_lines:
                user = user_line.strip()
                password = password_line.strip()
                credentials = f"{user}:{password}"
                combined_credentials.append(credentials)

        return combined_credentials

def encode_base64(data):
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

# Example usage
user_file = 'users.txt'  # Replace with the path to your user file
password_file = 'passwords.txt'  # Replace with the path to your password file

combined_credentials = combine_files(user_file, password_file)

for credentials in combined_credentials:
    encoded_credentials = encode_base64(credentials)
    print(encoded_credentials)
