<h1>Micropython Infrared Project</h1>

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
  <li>WS2812</li>
</ul> 

<p>In case of error remove neopixel library
Uncomment and replace the handler function to whatever function</p>
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
</table>
