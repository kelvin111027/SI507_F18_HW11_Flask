from flask import Flask, render_template
import secrets_example as sec
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome!</h1>"


@app.route('/user/<nm>')
def result(nm):
    base_url = 'https://api.nytimes.com/svc/mostpopular/v2/mostviewed/Technology/1.json'
    params = { 'api-key': sec.api_key }
    results = requests.get(base_url, params).json()
    title_url = []
    for a in results['results'][:5]:
        str = a['title'] + ' (' + a['url'] + ')'
        title_url.append(str)
    return render_template('user.html', name=nm, title="Today's top headers in technology are...", my_list=title_url)



if __name__ == '__main__':
    app.run(debug=True)
