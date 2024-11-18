from network import WLAN, STA_IF
from microdot import Microdot, send_file

# station interface
wlan = WLAN(STA_IF)

# activate wlan
wlan.active(True)

# connect to router
wlan.connect('<ssid>', '<password>')

# wait for wifi to connect
while not wlan.isconnected():
    machine.idle() 

# get ip
ip = wlan.ipconfig('addr4')
print(ip)

# init web server
app = Microdot()

# handle index
@app.route('/')
async def index(request):
    return send_file('/build/index.html')

# handle wildcard route
@app.route('/<path:path>')
async def static(request, path):
    # serve svelte-kit build
    return send_file('/build/' + path)

# start the server
app.run(debug=True)
