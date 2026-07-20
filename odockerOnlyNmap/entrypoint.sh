#!/bin/bash
set -e

echo "FLAG{FakiTPkjnQJCQrTiwDwsoUGZOOOHktyz}" > /challenge/flag.txt

# others can't access
chmod o-rwx /challenge

python3 /challenge/app.py >/dev/null 2>&1 &

useradd --create-home challenge_user

# disable showing typed text in the terminal
stty -echo

# Switch to challenge_user and start a bash session without login messages
exec su - challenge_user -s /bin/bash