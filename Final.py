'''
Ejercicio Final Devasc: Examen de Habilidades 
Alumno: Alejandro Medicina
Propuesta:
1 - Obtener los id de las organizaciones.
2 - Obtener las redes de una organización a partir de la elección de un id del servicio anterior, tener en cuenta de obtenerlo desde el json y no de forma harcodeada.
3 - Obtener los dispositivos de la red pasándole como parámetro el  networkid  obtenido en el paso anterior.
4 - Obtener datos de la  red con el networkid.
5 - Obtener infomación de un dispositivo con el serial id.
6 - Obtener información del SSID para el network ID
'''
import requests
import json


#Add the Meraki API
api_key ="6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
headers = {"X-Cisco-Meraki-API-Key":api_key}
base_url = "https://api.meraki.com/api/v1"

print("-"*50+"INICIO"+"-"*50)
print("Step 2: Get the Organization ID")
#https://api.meraki.com/api/v1/organizations
url_org = base_url + "/organizations"
response_org = requests.get(url_org,headers=headers)
response_json_org = response_org.json()
print(json.dumps(response_json_org, indent=2))
print("-"*100)

#Obtener ID de una organizacion
id_org = response_json_org[0]['id']

print("Step 3: Get the networks in the organization - ",id_org)
#https://api.meraki.com/api/v1/organizations/{{organizationId}}/networks
url_net = url_org+"/{}/networks".format(id_org)
response_net = requests.get(url_net,headers=headers)
response_json_net = response_net.json()
print(json.dumps(response_json_net, indent=2))
print("-"*100)

#Obtener Id_net 
Id_net = response_json_net[2]['id']

print("Step 4: Get the devices in a network - ",Id_net)
#https://api.meraki.com/api/v1/networks/{{Id_net}}/devices
url_net_dev = base_url+"/networks/{}/devices".format(Id_net)
response_net_dev = requests.get(url_net_dev,headers=headers)
response_json_net_dev = response_net_dev.json()
print(json.dumps(response_json_net_dev, indent=2))
print("-"*100)


print("Step 5: Get network information - ",Id_net)
#https://api.meraki.com/api/v1/networks/{{Id_net}}
url_net_id = base_url+"/networks/{}".format(Id_net)
response_netid = requests.get(url_net_id,headers=headers)
response_json_netid = response_netid.json()
print(json.dumps(response_json_netid, indent=2))
print("-"*100)

Id_serial = response_json_net_dev[0]['serial']

print("Step 6: Get device information - ",Id_serial)
#https://api.meraki.com/api/v1/networks/{{Id_net}}/devices/{{serial}}
url_serial_id = base_url+"/networks/{}/devices/{}".format(Id_net,Id_serial)
response_serialid = requests.get(url_serial_id,headers=headers)
response_json_serialid = response_serialid.json()
print(json.dumps(response_json_serialid, indent=2))
print("-"*100)


print("Step 7: Get SSID information - ",Id_net)
#https://api.meraki.com/api/v1/networks/{{Id_net}}/wireless/ssids
url_SSID = base_url+"/networks/{}/wireless/ssids".format(Id_net)
response_ssid = requests.get(url_SSID,headers=headers)
response_json_ssid = response_ssid.json()
print(json.dumps(response_json_ssid, indent=2))
print("-"*50+"FIN"+"-"*50)