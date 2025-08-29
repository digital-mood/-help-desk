import uuid # Para generar IDs únicos
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Función para cargar los tickets desde el archivo JSON
def load_tickets():
    try:
        with open('tickets.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Función para guardar los tickets en el archivo JSON
def save_tickets(tickets):
    with open('tickets.json', 'w') as file:
        json.dump(tickets, file, indent=4)

# Ruta principal que muestra todos los tickets
@app.route('/')
def index():
    tickets = load_tickets()
    return render_template('index.html', tickets=tickets)

# Ruta para crear un nuevo ticket
@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    title = request.form['title']
    description = request.form['description']
    
    new_ticket = {
        'id': str(uuid.uuid4()), # Genera un ID único para el ticket
        'title': title,
        'description': description,
        'status': 'abierto' # El estado inicial es "abierto"
    }

    tickets = load_tickets()
    tickets.append(new_ticket)
    save_tickets(tickets)
    
    return redirect(url_for('index'))

# Ruta para cambiar el estado de un ticket
@app.route('/close_ticket/<ticket_id>')
def close_ticket(ticket_id):
    tickets = load_tickets()
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['status'] = 'resuelto'
            break
    save_tickets(tickets)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)