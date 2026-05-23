<h1>MicroPython-button-counter</h1>

<h2>Description</h2>

This MicroPython project uses a push button connected to GPIO14 to count button presses and display the total through the serial console.

The program monitors the button input using the `machine.Pin` module with an internal pull-down resistor enabled. A simple software debounce method is used to prevent multiple counts from a single press by waiting for the button to be released before registering another input.

Each successful button press increases the counter value and prints the updated total in real time. This project demonstrates basic GPIO input handling, button debouncing, and event counting using MicroPython.
<br />


<h2>Technologies Used</h2>

- MicroPython
- Python (embedded systems)
- Software Debouncing
- machine.Pin

<h2>Hardware Used</h2>

- Microcontroller Raspberry Pi Pico 
- Push Button 
- Pull-down Resistor (internal)
- Breadboard and jumper wires
  <br />
  
<h2>🔌 Wiring Connections (GPIO Pins)</h2>

<ul>
  <li>GPIO14 → Push Button Input</li>
  <li>GND → Button Ground Connection</li>
  <li>Internal Pull-down Resistor Enabled (No external resistor needed)</li>
</ul> 
<br />

<h2>How It Works</h2>

<p>The program continuously monitors a push button connected to GPIO14 using MicroPython.</p>

<p>When the button is pressed, a debounce delay is applied to avoid false triggers. The program then waits for the button to be released before registering the press.</p>

<p>Each valid press increases a counter, and the updated value is printed to the serial console in real time.</p>

<br/>

<!--
```diff
- red text (errors)
+ green text (adds)
! orange text (warnings)
# gray text (notes)
@@ purple bold text (important)@@
