import requests
import os 


def download_image(uri, path):
	try:		
		r = requests.get(uri)
	except requests.exceptions.RequestException as err:
		print("X request err", err)
	if r.status_code == 200 and validate_or_create_path(uri, path):
		try:	
			with open(path, 'wb') as f:
				for chunk in r:
					f.write(chunk)
				return True
		except IOError as err:
			print("X File err", err)

def validate_or_create_path(uri, path):
	ext_uri = uri.split('.')[-1]
	ext_path = path.split('.')[-1]
	path_dir = "/".join(path.split('/')[:-1])

	if not ext_uri==ext_path:
		print("extensiones no coincide")

	if not ext_uri in ['png', 'jpg', 'gif','svg']:
		print("Solo aceptamos formatos ['png', 'jpg', 'gif', 'svg'] para la URL")
		return False		

	if not os.path.exists(path_dir) and path_dir!="":
		try:
			os.mkdir(path_dir)
		except Exception as err:
			print("X error mkdir", err)

	if os.path.exists(path):
		overwrite = input("existe un archivo con ese nombre desea continuar (s/n)")
		if overwrite == 'n':
			return False 
	return True

if __name__ == "__main__":
	uri = input("ingrese URL de la imagen: ")
	path = input ("ingrese ruta para almacenar: ") 
	download_image(uri, path)
	