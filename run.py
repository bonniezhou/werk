from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def main():
	name = 'BONNIE'
	return render_template('index.html', name=name)

@app.route("/form")
def form():
	return render_template('form.html')

@app.route("/submit", methods=['POST'])
def submit():
	if request.method == 'POST':
		name = request.form['name']
		dob = request.form['dob']
		#return render_template('submit.html', name=name, dob=dob)
		return json.dumps({
			'name': name,
			'dob': dob
			})

if __name__ == "__main__":
    app.run()