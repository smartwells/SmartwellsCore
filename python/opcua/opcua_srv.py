import sys
#from opcua import ua

from opcua import Server

server = Server()
#можно прописать IP адрес сетевого интерфейса сервера, если их несколько
server.set_endpoint("opc.tcp://0.0.0.0:4840/")
#Записываем название сервера
server.set_server_name("Server")
#здесь указываем расположение сертификатов шифрования
# можно обойтись и без них , тогда данные между клиентом и сервером не будут шифроваться
#server.load_certificate("server_cert.der")
#server.load_private_key("server_private_key.pem")
#настраиваем собственное пространство имен
uri = "http://server"
idx = server.register_namespace(uri)
#получаем ссылку на объект где будут располагаться наши узлы
objects = server.get_objects_node()
#создаем объект и присваиваем ему имя
Object_1 =objects.add_object(idx,'MyFirstObject')
Object_2 =objects.add_object(idx,'MySecondObject')
Object_3 =objects.add_object(idx,'MyThirdObject')
#теперь создаем переменные
Discret_1 = Object_1.add_variable(idx,'Discret_1',[0,0,0,0,0,0,0,0])
Discret_2 = Object_2.add_variable(idx,'Discret_2',[0,0,0,0,0,0,0,0])
Analog_3  = Object_3.add_variable(idx,'Analog_3',[10,20,30,40,50])
#запускаем сервер
server.start()
