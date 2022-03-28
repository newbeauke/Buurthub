import paho.mqtt.client as mqtt
import TelegramModule as telegram

nfcTopic = "v3/buurthub@ttn/devices/eui-70b3d57ed004e699/up"
sensorTopic = "v3/buurthub@tnn/devices/eui-70b3d57ed004e8b9/up"

checkedIn = False

# Callbacks
def on_connect(client, userdata, flags, rc):
    print("[Buurthub] Succesvol verbonden. (Code {0})".format(str(rc)))
    telegram.send_start()

def on_message(client, userdata, msg):
    print("[Voor ontwikkelaars] Inkomend bericht van: {0}".format(msg.topic))
    global checkedIn
    if msg.topic == nfcTopic:
        checkedIn = not checkedIn
        if checkedIn:
            print("[Buurthub] Ingecheckt.")
        else:
            print("[Buurthub] Uitgecheckt.")
    else:
        if checkedIn:
            print("[Buurthub] Sensor geactiveerd.")
        else:
            print("[Buurthub] Sensor geactiveerd terwijl de gebruiker is uitgecheckt")
            telegram.send_message("Sensor geactiveerd! Mogelijke inbraak gaande.")

# Initialize client
client = mqtt.Client()

# Subscribe callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect client
client.username_pw_set("buurthub@tnn", "NNSXS.B6T7NUQYKIED2DKBZID73USSNAQDK3DVZ3XKYSI.YSPFUXW4SNND57LLYMO4ICFKCWJO23NMG7BTOYDGUZVRMWQBAJRA")
client.connect("eu1.cloud.thethings.network", 1883, 3600)
client.subscribe('#')

# Loop to receive callbacks
client.loop_forever(3600, 10, False)