from flask import Flask
#from .testFunctions import seanFunc as sf
import os 

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Home'
    return sf(1,2)

print('**********NEW TRY***************')
print(os.environ['PYTHONPATH'])
print(os.getcwd())
with os.scandir(os.getcwd()) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            print(entry.name)

#if __name__ == '__main__':
#    app.run(use_reloader=False)


