#!/usr/bin/env python3
"""PassGenLite – tiny password generator.

Usage examples:
    python passgen.py                # default 16‑char password with all groups
    python passgen.py --length 24    # custom length
    python passgen.py --no-symbols    # omit symbols
"""
import argparse
import secrets
import string
import sys

def build_charset(args):
    charset = ''
    if not args.no_lowercase:
        charset += string.ascii_lowercase
    if not args.no_uppercase:
        charset += string.ascii_uppercase
    if not args.no_digits:
        charset += string.digits
    if not args.no_symbols:
        # Common safe symbols for passwords
        charset += '!@#$%^&*()-_=+[]{}|;:,.<>?'
    if not charset:
        sys.stderr.write('Error: No character groups selected. Enable at least one.\n')
        sys.exit(1)
    return charset

def generate_password(length, charset):
    # secrets.choice is cryptographically strong
    return ''.join(secrets.choice(charset) for _ in range(length))

def parse_args():
    parser = argparse.ArgumentParser(description='Tiny random password generator')
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Length of the password (minimum 4, default 16)')
    parser.add_argument('--no-lowercase', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    args = parser.parse_args()
    if args.length < 4:
        parser.error('Minimum password length is 4')
    return args

def main():
    args = parse_args()
    charset = build_charset(args)
    pwd = generate_password(args.length, charset)
    print(pwd)

if __name__ == '__main__':
    main()
