from flask import Flask, render_template
from data import Diseases

app=Flask(__name__)

#Diseases=Diseases()
@app.route('/')

def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/diseases')
def diseases():
    return render_template('diseases.html', diseases=Diseases())

@app.route('/disease/<string:id>')
def disease(id):
    return render_template('disease.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
