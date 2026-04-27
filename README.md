# HR Hospital Module (Odoo)

## Description
The **HR Hospital** module was developed as part of an Odoo training task.  
Its purpose is to implement a basic hospital management system for handling patients, doctors, and appointments.

The module extends Odoo functionality and demonstrates the use of models, relationships, and business logic.

---

## Features

### Patients
- Create and manage patient records
- Store information such as:
  - Name
  - Date of birth
  - Gender
  - Medical history

### Doctors
- Manage doctor records
- Store specialization
- Link doctors with patients

### Appointments
- Schedule appointments
- Define relationships between:
  - Patient and doctor
- Set date and time
- Track status

---

## Technical Details

- Framework: Odoo 19.0
- Language: Python
- ORM: Odoo ORM for database operations

---

## Installation

1. Place the module in the `custom_addons` directory
2. Update app list in Odoo
3. Install the module