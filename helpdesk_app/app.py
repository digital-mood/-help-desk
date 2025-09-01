import uuid
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def get_next_status(current_status):
    """Define transiciones de estado más lineales."""
    status_transitions = {
        'nuevo': ['en revision'],
        'en revision': ['en progreso'],
        'en progreso': ['en espera', 'resuelto'],
        'en espera': ['en progreso', 'resuelto'],
        'resuelto': ['cerrado', 'reabierto'],
        'cerrado': [],
        'reabierto': ['en revision']
    }
    return status_transitions.get(current_status, [])

@app.route('/')
def index():
    tickets = load_data('tickets.json')
    employees_data = load_data('employees.json')
    groups = employees_data.get('groups', [])
    employees = employees_data.get('employees', [])
    
    group_map = {group['id']: group['name'] for group in groups}
    employee_map = {emp['id']: emp['name'] for emp in employees}

    return render_template('index.html', 
                           tickets=tickets, 
                           groups=groups,
                           employees=employees,
                           group_map=group_map,
                           employee_map=employee_map,
                           get_next_status=get_next_status)

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    title = request.form['title']
    description = request.form['description']
    group_id = request.form['group_id']
    ticket_type = request.form['ticket_type']
    
    new_ticket = {
        'id': str(uuid.uuid4()),
        'title': title,
        'description': description,
        'status': 'nuevo',
        'group_id': group_id,
        'assigned_to': None,
        'ticket_type': ticket_type # Nuevo campo
    }
    tickets = load_data('tickets.json')
    tickets.append(new_ticket)
    save_data(tickets, 'tickets.json')
    return redirect(url_for('index'))

@app.route('/update_status/<ticket_id>/<new_status>')
def update_status(ticket_id, new_status):
    tickets = load_data('tickets.json')
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['status'] = new_status
            break
    save_data(tickets, 'tickets.json')
    return redirect(url_for('index'))

@app.route('/assign_ticket/<ticket_id>', methods=['POST'])
def assign_ticket(ticket_id):
    employee_id = request.form['employee_id']
    tickets = load_data('tickets.json')
    
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['assigned_to'] = employee_id
            # También podemos cambiar el estado a 'en revision' al asignar
            if ticket['status'] == 'nuevo':
                ticket['status'] = 'en revision'
            break
    
    save_data(tickets, 'tickets.json')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)