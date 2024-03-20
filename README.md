<h1>Micropython Infrared Project</h1>
This is a project for NEC8 protocol to capture the IR signal and then replay it or attempt to brute force all addresses and values!
<h3>Requirements</h3>
  <ul>
  <li>Infrared Receiver</li>
  <li>Infrared Transmitter</li>
  <li>RP2040 board w/ Micropython</li>
  <li>https://github.com/peterhinch/micropython_ir</li>
</ul>

<p>From the ir_rx library get the files __init__, acquire, print_error and nec.py <br>
   From the ir_tx library get the files __init__, nec, rp2_rmt.py
</p>

<h3>Optionals</h3>
<ul>
  <li>WS2812 Pin 23</li>
</ul> 

<p>In case of error remove neopixel code <br>
Uncomment and replace the interrupt handler function to whatever function you want</p>
<table>
<tr>
    <th>Parts</th>
    <th>Pins</th>
  </tr>
  <tr>
    <td>Infrared Receiver</td>
    <td>16</td>
  </tr>
  <tr>
    <td>Infrared Transmitter</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Button</td>
    <td>24</td>
  </tr>
  <tr>
    <td>LED</td>
    <td>23</td>
  </tr>
</table>

<h2>Upcoming</h2>
NEC16 and Sony protocols
