cd ~/Desktop/renewal_letters
source venv/bin/activate
python generate_renewal_letters.py
cd tmp
for file in *; do docker run --rm -i -v "$PWD":/data latex pdflatex $file; done
cd ..
mkdir -p renewal_letters_pdf
mv tmp/*.pdf renewal_letters_pdf
echo DONE
