# PassGenLite

**PassGenLite** is a minimalist Python CLI tool that creates random passwords. It supports:
- Custom length (default 16 characters)
- Choice of character groups: lowercase, uppercase, digits, symbols
- One‑line usage for rapid password generation

## Installation
```bash
# Clone the repo (or copy the single file)
git clone https://github.com/yourusername/PassGenLite.git
cd PassGenLite
# No external dependencies required – just Python 3.6+
```

## Usage
```bash
# Default: 16‑character password with all groups
python passgen.py

# Specify length (e.g., 24 characters)
python passgen.py --length 24

# Choose character groups (e.g., only letters and digits)
python passgen.py --no-symbols

# Combine options
python passgen.py --length 32 --no-symbols --no-uppercase
```

## Options
- `-l, --length` – Desired password length (minimum 4, default 16)
- `--no-lowercase` – Exclude lowercase letters
- `--no-uppercase` – Exclude uppercase letters
- `--no-digits` – Exclude digits
- `--no-symbols` – Exclude symbols (`!@#$%^&*()-_=+[]{}|;:,.<>?`)

## License
MIT – see the repository for details.

## Contributing
Feel free to fork, submit issues, or open pull requests. This project aims to stay tiny and dependency‑free.