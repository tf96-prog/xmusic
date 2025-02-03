import requests

#artista

usuarioA={"username":"userA","password":"usera123456"}
response1=requests.post('http://localhost:8000/login/',json=usuarioA)
token=response1.text
print(token)

#usuarioB={"username":"userB","password":"userb123456"}
#response2=requests.post('http://localhost:8000/login/',json=usuarioB)
#print(response2.json())

response3=requests.get('http://localhost:8000/artistas/')
assert response3.status_code == 200, "La respuesta deberia ser 200"

artista={'nombre':'df7f7fd72fd27g'}
response4=requests.post('http://localhost:8000/artistas/',json=artista)
assert response4.status_code==403, "La respuesta deberia ser 403"

response5=requests.put(f'http://localhost:8000/artistas/1/',json={'nombre':'5rtf6gfwh'})
assert response5.status_code==401, "La respuesta deberia ser 401"

response6=requests.delete(f'http://localhost:8000/artistas/1/')
assert response6.status_code==401, "La respuesta deberia ser 401"

header={'Authorization':token}
response7=requests.get('http://localhost:8000/artistas/',headers=header)
assert response7.status_code==200, "La respuesta deberia ser 200"

artista={'nombre':'wasd'}
response8=requests.post('http://localhost:8000/artistas/',headers=header,json=artista)
assert response8.status_code==403, "La respuesta deberia ser 403"

response9=requests.put(f'http://localhost:8000/artistas/1/',headers=header,data={'nombre':'tttttgghyt'})
assert response9.status_code==401, "La respuesta deberia ser 401"

response10=requests.delete(f'http://localhost:8000/artistas/1/',headers=header)
assert response10.status_code==401, "La respuesta deberia ser 401"

header2={'Authorization':'Token f0633c6402fef3aa4ab11b0e1e78fa5ee87809c9'}
response11=requests.get('http://localhost:8000/artistas/',headers=header2)
assert response11.status_code==200, "La respuesta deberia ser 200"

artista={'nombre':'asdf'}
response12=requests.post('http://localhost:8000/artistas/',headers=header2,json=artista)
artista_id=response12.json().get('id')
assert response12.status_code==201, "La respuesta deberia ser 201"
assert response12.json().get('nombre')==artista.get('nombre')

artista_actualizado={'nombre':'uiop'}
response13=requests.put(f'http://localhost:8000/artistas/{artista_id}/',headers=header2,json=artista_actualizado)
assert response13.status_code==200, "La respuesta deberia ser 200"
assert response13.json().get('nombre')==artista_actualizado.get('nombre')

response14=requests.delete(f'http://localhost:8000/artistas/{artista_id}/',headers=header2)
assert response14.status_code==200, "La respuesta deberia ser 200"

response15=requests.get(f'http://localhost:8000/artistas/{artista_id}/')
assert response15.status_code==404, "La respuesta deberia ser 404"





#album

response16=requests.get('http://localhost:8000/albumes/')
assert response16.status_code==200, "La respuesta deberia ser 200"

album={'artista':3,'nombre':'h7h5hj5','anio':1980}
response17=requests.post('http://localhost:8000/albumes/',json=album)
assert response17.status_code==403, "La respuesta deberia ser 403"

response18=requests.put(f'http://localhost:8000/albumes/1/',json={'artista':5,'nombre':'9i99898h','anio':2004})
assert response18.status_code==401, "La respuesta deberia ser 401"

response19=requests.delete(f'http://localhost:8000/albumes/1/')
assert response19.status_code==401, "La respuesta deberia ser 401"

header3={'Authorization':token}
response20=requests.get('http://localhost:8000/albumes/',headers=header3)
assert response20.status_code==200, "La respuesta deberia ser 200"

album={'artista':4,'nombre':'vtrgv5yb6','anio':1980}
response21=requests.post('http://localhost:8000/albumes/',headers=header3,json=album)
assert response21.status_code==403, "La respuesta deberia ser 403"

response22=requests.put(f'http://localhost:8000/albumes/1/',headers=header3,json={'nombre':'tttttgghyt'})
assert response22.status_code==401, "La respuesta deberia ser 401"

response23=requests.delete(f'http://localhost:8000/albumes/1/',headers=header3)
assert response23.status_code==401, "La respuesta deberia ser 401"

header4={'Authorization':'Token f0633c6402fef3aa4ab11b0e1e78fa5ee87809c9'}
response24=requests.get('http://localhost:8000/albumes/',headers=header4)
assert response24.status_code==200, "La respuesta deberia ser 200"

album={'artista':5,'nombre':'nbobonb9r','anio':2005}
response25=requests.post('http://localhost:8000/albumes/',headers=header4,json=album)
album_id=response25.json().get('id')
assert response25.status_code==201, "La respuesta deberia ser 201"

response26=requests.put(f'http://localhost:8000/albumes/{album_id}/',headers=header4,json={'artista':4,'nombre':'zxzcxvcbhy','anio':1994})
assert response26.status_code==200, "La respuesta deberia ser 200"

response27=requests.delete(f'http://localhost:8000/albumes/{album_id}/',headers=header4)
assert response27.status_code==200, "La respuesta deberia ser 200"

response28=requests.get(f'http://localhost:8000/albumes/{album_id}/')
assert response28.status_code==404, "La respuesta deberia ser 404"