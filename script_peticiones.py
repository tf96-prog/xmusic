import requests

#artista

usuarioA={"username":"userA","password":"usera123456"}
response1=requests.post('http://localhost:8000/login/',json=usuarioA)
token=response1.json().get('token')
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

response20=requests.get('http://localhost:8000/albumes/',headers=header)
assert response20.status_code==200, "La respuesta deberia ser 200"

album={'artista':4,'nombre':'vtrgv5yb6','anio':1980}
response21=requests.post('http://localhost:8000/albumes/',headers=header,json=album)
assert response21.status_code==403, "La respuesta deberia ser 403"

response22=requests.put(f'http://localhost:8000/albumes/1/',headers=header,json={'artista':4,'nombre':'tttttgghyt','anio':1998})
assert response22.status_code==401, "La respuesta deberia ser 401"

response23=requests.delete(f'http://localhost:8000/albumes/1/',headers=header)
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



#cancion

response29=requests.get('http://localhost:8000/canciones/')
assert response29.status_code==200, "La respuesta deberia ser 200"

cancion={'album':2,'nombre':'f34f3f3f3','duracion':230,'genero':'kiju','colaboradores':[2,3]}
response30=requests.post('http://localhost:8000/canciones/',json=cancion)
assert response30.status_code==403, "La respuesta deberia ser 403"

response31=requests.put(f'http://localhost:8000/canciones/1/',json={'album':3,'nombre':'bwfwgeh6','duracion':310,'genero':'vsdgrsdsd','colaboradores':[2,4]})
assert response31.status_code==401, "La respuesta deberia ser 401"

response32=requests.delete(f'http://localhost:8000/canciones/1/')
assert response32.status_code==401, "La respuesta deberia ser 401"

response33=requests.get('http://localhost:8000/canciones/',headers=header)
assert response33.status_code==200, "La respuesta deberia ser 200"

cancion2={'album':1,'nombre':'khgklh','duracion':270,'genero':'hg48hg8g','colaboradores':[2,3]}
response34=requests.post('http://localhost:8000/canciones/',headers=header,json=cancion2)
cancion_id=response34.json().get('id')
assert response34.status_code==201, "La respuesta deberia ser 201"

response35=requests.put(f'http://localhost:8000/canciones/{cancion_id}/',headers=header,json={'album':1,'nombre':'ccvvcbcb','duracion':330,'genero':'nnjnjmj','colaboradores':[3,5]})
assert response35.status_code==200, "La respuesta deberia ser 200"

response36=requests.delete(f'http://localhost:8000/canciones/{cancion_id}/',headers=header)
assert response36.status_code==200, "La respuesta deberia ser 200"

header6={'Authorization':'Token f0633c6402fef3aa4ab11b0e1e78fa5ee87809c9'}
response37=requests.get('http://localhost:8000/canciones/',headers=header6)
assert response37.status_code==200, "La respuesta deberia ser 200"

cancion3={'album':2,'nombre':'xvbcbfbcb','duracion':230,'genero':'sawqwefd','colaboradores':[2,4]}
response38=requests.post('http://localhost:8000/canciones/',headers=header6,json=cancion3)
cancion_id2=response38.json().get('id')
assert response38.status_code==201, "La respuesta deberia ser 201"

response39=requests.put(f'http://localhost:8000/canciones/{cancion_id2}/',headers=header6,json={'album':4,'nombre':'uuhjutijg','duracion':200,'genero':'nbjgjgj','colaboradores':[1,2]})
assert response39.status_code==200, "La respuesta deberia ser 200"

response40=requests.delete(f'http://localhost:8000/canciones/{cancion_id2}/',headers=header6)
assert response40.status_code==200, "La respuesta deberia ser 200"

response41=requests.get(f'http://localhost:8000/canciones/{cancion_id2}/')
assert response41.status_code==404, "La respuesta deberia ser 404"


#lista de reproduccion

response42=requests.get('http://localhost:8000/listas/')
assert response42.status_code==200, "La respuesta deberia ser 200"

lista={'nombre':'f34f3f3f3','canciones':[2,3]}
response43=requests.post('http://localhost:8000/listas/',json=lista)
assert response43.status_code==400, "La respuesta deberia ser 400"

response44=requests.put(f'http://localhost:8000/listas/1/',json={'nombre':'e2r2r2r2','canciones':[2,3]})
assert response44.status_code==403, "La respuesta deberia ser 403"

response45=requests.delete(f'http://localhost:8000/listas/1/')
assert response45.status_code==403, "La respuesta deberia ser 403"

response46=requests.get('http://localhost:8000/listas/',headers=header)
assert response46.status_code==200, "La respuesta deberia ser 200"

lista2={'nombre':'cbvhytyyg','canciones':[1,4]}
response47=requests.post('http://localhost:8000/listas/',headers=header,json=lista2)
lista_id=response47.json().get('id')
assert response47.status_code==201, "La respuesta deberia ser 201"

response48=requests.put(f'http://localhost:8000/listas/{lista_id}/',headers=header,json={'album':1,'nombre':'ccvvcbcb','duracion':330,'genero':'nnjnjmj','colaboradores':[3,5]})
assert response48.status_code==200, "La respuesta deberia ser 200"

response49=requests.delete(f'http://localhost:8000/listas/{lista_id}/',headers=header)
assert response49.status_code==200, "La respuesta deberia ser 200"

header8={'Authorization':'Token f0633c6402fef3aa4ab11b0e1e78fa5ee87809c9'}
response50=requests.get('http://localhost:8000/listas/',headers=header8)
assert response50.status_code==200, "La respuesta deberia ser 200"

lista3={'album':2,'nombre':'xvbcbfbcb','duracion':230,'genero':'sawqwefd','colaboradores':[2,4]}
response51=requests.post('http://localhost:8000/listas/',headers=header8,json=lista3)
lista_id2=response51.json().get('id')
assert response51.status_code==201, "La respuesta deberia ser 201"

response52=requests.put(f'http://localhost:8000/listas/{lista_id2}/',headers=header8,json={'album':4,'nombre':'uuhjutijg','duracion':200,'genero':'nbjgjgj','colaboradores':[1,2]})
assert response52.status_code==200, "La respuesta deberia ser 200"

response53=requests.delete(f'http://localhost:8000/listas/{lista_id2}/',headers=header8)
assert response53.status_code==200, "La respuesta deberia ser 200"

response54=requests.get(f'http://localhost:8000/listas/{lista_id2}/')
assert response54.status_code==404, "La respuesta deberia ser 404"