from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for contacts (list of dictionaries)
contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        id = len(contacts) + 1
        contacts.append({'id': id, 'name': name, 'phone': phone, 'email': email, 'address': address})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    return render_template('search.html', results=results)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    contact = next((c for c in contacts if c['id'] == id), None)
    if not contact:
        return "Contact not found", 404
    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        contact['address'] = request.form['address']
        return redirect(url_for('index'))
    return render_template('update.html', contact=contact)

@app.route('/delete/<int:id>')
def delete(id):
    global contacts
    contacts = [c for c in contacts if c['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)