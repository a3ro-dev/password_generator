# Password Generator

This is a Python program that generates random passwords of a specified length and stores them in a database to ensure that each generated password is unique.

## Requirements

- Python 3
- sqlite3

## Usage

To use the password generator, run the `password_generator.py` file in Python. The program will prompt you to enter the desired password length, and then it will generate a random password of that length. If the generated password already exists in the database, the program will generate a new password until it generates a unique one.

The generated password will be output to the user and also stored in the `passwords` table of the `passwords.db` SQLite database.

## Notes

- The `passwords.db` database must be located in the `db` directory. If the database does not exist, it will be created when the program is run for the first time.
- The `passwords` table in the database must have a single `password` column of type `text`. If the table does not exist, it will be created when the program is run for the first time.

## Example

```bash
Enter the desired password length: 12
Your generated password is: cOZa2dQIxzvb
```
