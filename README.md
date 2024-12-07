<h1>Home Automation  Web UI </h1>

<h2>1. Introduction</h2>
This project describes the development of a home automation system using  Flask-based web UI for remote control of electronic appliances via GPIO pins. This report delves into the project's objectives, technical implementation, key functionalities, security measures, and outcomes.
<h2>2. Project Objectives</h2>
Develop a user-friendly and secure web interface for controlling various home appliances (bulbs, fans, ACs, geyser, TV, motor pump) using a smartphone from anywhere.
<h2>3. Technical System Overview</h2>
<h2>Hardware:</h2>
Raspberry Pi as the central processing unit.
GPIO pins connected to electronic devices through relays or transistors.
<h2>Software:</h2>
Python programming language.
Flask web framework for the web UI.
RPi.GPIO library for GPIO pin control.
pip install Flask-BasicAuth

<h2>4. Functionality & Implementation Details</h2>
<h2>Web UI:</h2>
<li>The web UI (index.html) displays six sections, each representing a room with various appliances.</li>
<li>Each appliance has secure toggle buttons (instead of separate on/off buttons) that send POST requests to the Flask server with appropriate authentication measures.</li>
<li>The server processes the requests, verifies the user's password, extracts the GPIO pin and action ("on" or "off"), and calls the gpio function.</li>
<li>The gpio function sets the corresponding pin high (on) or low (off) using RPi.GPIO.</li>
Security:
<li>Implement a username and password protection mechanism for accessing the web UI.</li>
<li>Validate user before processing any requests.</li>
<li>“To ensure secure access to the web interface, I implemented Flask-BasicAuth. Users are prompted to enter their username and password, which are stored in the python program. Only authorized users can control appliances, preventing unauthorized access. The login process is streamlined and user-friendly, requiring minimal interaction. In the future, I plan to potentially explore role-based authorization for more granular control.”</li>

<h2>6. Conclusion</h2>
This project demonstrates the feasibility of building a secure Web-based home automation system using Flask. The project successfully showcases remote control of appliances through a user-friendly and secure web UI. 
<h2>7. Additional Information</h2>
Provide system diagrams or screenshots for visualization.
<img src="https://github.com/GEC-ian/Home-Automation-With-AI/blob/main/IMG_20240214_210525.jpg" width="400" >
<img src="https://github.com/GEC-ian/Home-Automation-With-AI/blob/main/IMG_20240217_211034.jpg" width="400">
<img src="https://github.com/GEC-ian/Home-Automation-With-AI/blob/main/IMG_20240220_181303.jpg" width="400">

<h2>Project Report</h2>

Download the PDF to view it: 👇
 <a href="https://github.com/GEC-ian/Home-Automation-With-AI/blob/main/Report%20file.pdf">Download PDF</a>
 
Project Video : 👇
 <a href="https://youtu.be/KS58KkNq-jo">Click Here</a>

