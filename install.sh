/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install docker colima python
cd ~/Desktop/
git clone https://github.com/agamkohli9/renewal_letters.git
cd renewal_letters
docker build -t latex .
python3 -m venv venv
source venv/bin/activate
pip install pandas
