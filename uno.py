from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def inserHtml():
    return render_template('./tour.html')

@app.route('/link1', methods=['GET'])
def link1():
    return render_template('./prezzobilgietto.html')

@app.route('/link2', methods=['GET'])
def link2():
    return render_template('./prezzobilgietto1.html')

@app.route('/link3', methods=['GET'])
def link3():
    return render_template('./prezzobilgietto2.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma