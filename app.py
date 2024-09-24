from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Immortales.html')

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/family-story')
def family_story():
    return render_template('family-story.html')

@app.route('/cultural')
def cultural():
    return render_template('cultural.html')

@app.route('/kids')
def kids():
    return render_template('kids.html')

if __name__ == '__main__':
    app.run(debug=True)
