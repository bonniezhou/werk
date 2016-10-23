from flask import Flask, render_template, json, request, send_file
from fdfgen import forge_fdf
from subprocess import call

app = Flask(__name__)

@app.route("/")
def main():
	name = 'BONNIE'
	return render_template('index.html', name=name)

@app.route("/signUp")
def signUp():
	return render_template('signUp.html')

@app.route("/form", methods=['POST'])
def form():
	return render_template('form.html')

@app.route("/checklist", methods=['POST'])
def checklist():
	name = request.form['name']
	citizenship = request.form['citizenship']
	ssn = request.form['ssn']

	with open("output.fdf", "w") as output_file:
		with open("template.fdf","r") as template_file:
			for line in template_file:
				if 'PLACEHOLDERNAME' in line:
					output_file.write(line.replace('PLACEHOLDERNAME', name))
				elif 'PLACEHOLDERSSN' in line:
					output_file.write(line.replace('PLACEHOLDERSSN', ssn))
				elif 'PLACEHOLDERCOUNTRY' in line:
					output_file.write(line.replace('PLACEHOLDERCOUNTRY', citizenship))
				else:
					output_file.write(line)

	call(["pdftk", "i-765.pdf", "fill_form",
      "output.fdf", "output", "output.pdf", "flatten"])
	return render_template('checklist.html')

@app.route("/output")
def output():
	return send_file('output.pdf',
         attachment_filename='output.pdf',
         as_attachment=True)

if __name__ == "__main__":
    app.run()