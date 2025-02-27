brew install docker colima
cd ~/Desktop/
git clone https://github.com/agamkohli9/renewal_letters.git
cd renewal_letters
docker build -t latex .
python3 -m venv venv
source venv/bin/activate
pip install pandas
