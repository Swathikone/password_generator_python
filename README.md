<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Password Generator</h1>

<p>
    This project is a Python-based password generator that creates secure, random passwords based on user-defined criteria such as the number of letters, numbers, and special characters. The project consists of two main files:
</p>

<ul>
    <li><strong>password_generator.py:</strong> This file contains the core logic for generating a random and secure password based on user input.</li>
    <li><strong>password_generator_gui.py:</strong> This file extends the functionality of the password generator with a graphical user interface (GUI) using <code>tkinter</code>, allowing users to easily generate passwords through a simple, interactive interface.</li>
</ul>

<h2>Features</h2>
<ul>
    <li>Generate a secure password by specifying:</li>
    <ul>
        <li>Number of letters</li>
        <li>Number of numbers</li>
        <li>Number of special characters</li>
    </ul>
    <li>Easy-to-use graphical interface with <code>tkinter</code>.</li>
    <li>Passwords are randomly generated to ensure security.</li>
</ul>

<h2>How to Use</h2>
<p><strong>1. Basic Password Generator (CLI):</strong></p>
<ul>
    <li>Run the <code>password_generator.py</code> script.</li>
    <li>Input the number of letters, numbers, and special characters when prompted.</li>
    <li>The program will output a secure, randomly generated password.</li>
</ul>

<p><strong>2. Password Generator with GUI:</strong></p>
<ul>
    <li>Run the <code>password_generator_gui.py</code> script.</li>
    <li>Enter the desired number of letters, numbers, and special characters in the provided fields.</li>
    <li>Click "Generate Password" to display the generated password within the GUI.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>tkinter</code> (for the GUI)</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/yourusername/password-generator.git</code></pre>

    <li>Navigate to the project directory:</li>
    <pre><code>cd password-generator</code></pre>

    <li>Run the password generator:</li>
    <ul>
        <li>For the command-line version:
            <pre><code>python password_generator.py</code></pre>
        </li>
        <li>For the GUI version:
            <pre><code>python password_generator_gui.py</code></pre>
        </li>
    </ul>
</ol>

<h2>License</h2>
<p>
    This project is open-source and available under the <a href="LICENSE">MIT License</a>.
</p>

<h2>Contributions</h2>
<p>
    Feel free to submit pull requests or open issues for any improvements or bug fixes.
</p>

</body>
</html>
