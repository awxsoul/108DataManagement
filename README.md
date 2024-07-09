# 108 Ambulance Database Management System

The 108 Ambulance Database Management System (DBMS) is designed to efficiently manage and track emergency calls, ambulance dispatch, patient information, and hospital interactions. This system ensures timely response to emergency situations, facilitating the seamless flow of information between callers, ambulance personnel, and medical facilities.

## Key Features

- **Efficient Call Handling**: Streamlines the process of receiving, categorizing, and prioritizing emergency calls based on criticality.
- **Optimized Resource Allocation**: Ensures prompt dispatch of ambulances to designated locations, considering factors such as proximity, traffic conditions, and criticality of the patient's condition.
- **User-Friendly Interface**: Designed with an intuitive interface for easy navigation and accessibility.

## Modules

### 1. View Patients in Database Module

- **Frontend**: Users can view and sort a list of patients transported by ambulance.
- **Backend**: Retrieves ambulance data from the MySQL database using Flask and Jinja2.

### 2. Add Patient Entries to Database Module

- **Functionality**: Allows the addition of new entries based on new calls received by the emergency call center.

## Backend Design

- **Framework**: Implemented using Python and Flask.
- **Database Interaction**: Utilizes SQL operations.
- **Security**: Implements authentication and authorization mechanisms.
- **Error Handling and Logging**: Includes robust error handling and logging functionalities.

## Frontend Design

- **User Interface**: Clean and intuitive design for usability and accessibility.
- **Dashboard**: Main hub for accessing key functionalities and information.
- **Patient Management**: Allows viewing and updating patient records.
- **Responsive Design**: Ensures compatibility across various devices and screen sizes.

## Applications

The 108 Ambulance Database Management System serves as a critical tool in improving the efficiency and effectiveness of emergency medical services (EMS). Its applications include:

- **Emergency Response Coordination**: Facilitates rapid and organized response to emergency calls.
- **Resource Optimization**: Enhances the allocation and utilization of ambulances and other resources.
- **Patient Care Management**: Provides real-time updates and information on patient status and location.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/awxsoul/108DataManagement.git
    ```
2. Navigate to the project directory:
    ```sh
    cd 108DataManagement
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the database and configure environment variables as needed.

## Usage

1. Run the Flask server:
    ```sh
    python app.py
    ```
2. Access the frontend interface through your web browser at `http://localhost:5000`.
