import paho.mqtt.client as mqtt
import requests

botToken = "5172717646:AAE9oqTf0dWm2h9DIYhZp1dqNHsv9ACSx7A"
botChatId = "-627172603"

# Callbacks
def on_connect(client, userdata, flags, rc):
    client.subscribe("$SYS/#")
    print("[Buurthub] Connected (code {0})".format(str(rc)))
    requests.post("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text=Als+je+dit+ziet,+kan+je+de+tyfus+krijgen.".format(botToken, botChatId))

def on_message(client, userdata, msg):
    print("[Buurthub] Incoming message...")
    print(msg.topic+" "+str(msg.payload))
    requests.post("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text=Inkomend+bericht+van+de+Hub:+{2}".format(botToken, botChatId, msg.payload))

# Initialize client
client = mqtt.Client()

# Subscribe callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect client
client.username_pw_set("buurthub@tnn", "NNSXS.B6T7NUQYKIED2DKBZID73USSNAQDK3DVZ3XKYSI.YSPFUXW4SNND57LLYMO4ICFKCWJO23NMG7BTOYDGUZVRMWQBAJRA")
client.connect("eu1.cloud.thethings.network", 1883, 60)

# Loop to receive callbacks
client.loop_forever(3600, 10, False)