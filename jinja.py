from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    is_logged_in = True
    nama = "SISKA AULIA UTAMI"
    items = 'Apel','Pisang','Strawbery'
    return render_template('index2.html', 
                           is_logged_in=is_logged_in, 
                           nama=nama,
                           items=items)

if __name__ =='__main__':
    app.run(debug=True)