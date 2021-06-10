from flask import Flask
#from .testFunctions import seanFunc as sf
import os 

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Home'
    return sf(1,2)

print(os.environ['PYTHONPATH'])
print(os.getcwd())
for entry in os.scandir('.'):
    if entry.is_file():
        print(entry.name)

#if __name__ == '__main__':
#    app.run(use_reloader=False)


