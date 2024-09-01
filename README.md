# antisocial-personality-sound

# Quick Start
python3 ./main.py


docker build -t my-app .
docker run -it --rm my-app

pyinstaller --onefile --name myapp --add-data "assets/sound/mechanical_switch/*:assets/sound/mechanical_switch" src/main.py
pyinstaller myapp.spec
