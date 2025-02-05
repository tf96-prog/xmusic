import requests

superuser={"username":"tfigueroa","password":"tomy1996"}
response0=requests.post('http://localhost:8000/login/',json=superuser)
token_admin=response0.json().get('token')
print(token_admin)

usuarioA={"username":"userA","password":"usera123456"}
response1=requests.post('http://localhost:8000/login/',json=usuarioA)
tokenA=response1.json().get('token')
print(tokenA)

usuarioB={"username":"userB","password":"userb123456"}
response2=requests.post('http://localhost:8000/login/',json=usuarioB)
tokenB=response2.json().get('token')
print(tokenB)

#artista

response3=requests.get('http://localhost:8000/artistas/')
assert response3.status_code == 200, "La respuesta deberia ser 200"

artista={'nombre':'df7f7fd72fd27g'}
response4=requests.post('http://localhost:8000/artistas/',json=artista)
assert response4.status_code==403, "La respuesta deberia ser 403"

response5=requests.put(f'http://localhost:8000/artistas/1/',json={'nombre':'5rtf6gfwh'})
assert response5.status_code==401, "La respuesta deberia ser 401"

response6=requests.delete(f'http://localhost:8000/artistas/1/')
assert response6.status_code==401, "La respuesta deberia ser 401"

string_tokenA="Token " + tokenA
header_usuarioA={'Authorization':string_tokenA}
response7=requests.get('http://localhost:8000/artistas/',headers=header_usuarioA)
assert response7.status_code==200, "La respuesta deberia ser 200"

artista={'nombre':'wasd'}
response8=requests.post('http://localhost:8000/artistas/',headers=header_usuarioA,json=artista)
assert response8.status_code==403, "La respuesta deberia ser 403"

response9=requests.put(f'http://localhost:8000/artistas/1/',headers=header_usuarioA,data={'nombre':'tttttgghyt'})
assert response9.status_code==401, "La respuesta deberia ser 401"

response10=requests.delete(f'http://localhost:8000/artistas/1/',headers=header_usuarioA)
assert response10.status_code==401, "La respuesta deberia ser 401"

string_token_superuser='Token ' + token_admin
header_superuser={'Authorization':string_token_superuser}
response11=requests.get('http://localhost:8000/artistas/',headers=header_superuser)
assert response11.status_code==200, "La respuesta deberia ser 200"

artista2={'nombre':'asdf'}
response12=requests.post('http://localhost:8000/artistas/',headers=header_superuser,json=artista2)
artista_id=response12.json().get('id')
assert response12.status_code==201, "La respuesta deberia ser 201"
assert response12.json().get('nombre')==artista2.get('nombre')

artista_actualizado={'nombre':'uiop'}
response13=requests.put(f'http://localhost:8000/artistas/{artista_id}/',headers=header_superuser,json=artista_actualizado)
assert response13.status_code==200, "La respuesta deberia ser 200"
assert response13.json().get('nombre')==artista_actualizado.get('nombre')

response14=requests.delete(f'http://localhost:8000/artistas/{artista_id}/',headers=header_superuser)
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

response20=requests.get('http://localhost:8000/albumes/',headers=header_usuarioA)
assert response20.status_code==200, "La respuesta deberia ser 200"

album={'artista':4,'nombre':'vtrgv5yb6','anio':1980}
response21=requests.post('http://localhost:8000/albumes/',headers=header_usuarioA,json=album)
assert response21.status_code==403, "La respuesta deberia ser 403"

response22=requests.put(f'http://localhost:8000/albumes/1/',headers=header_usuarioA,json={'artista':4,'nombre':'tttttgghyt','anio':1998})
assert response22.status_code==401, "La respuesta deberia ser 401"

response23=requests.delete(f'http://localhost:8000/albumes/1/',headers=header_usuarioA)
assert response23.status_code==401, "La respuesta deberia ser 401"

response24=requests.get('http://localhost:8000/albumes/',headers=header_superuser)
assert response24.status_code==200, "La respuesta deberia ser 200"

album={'artista':5,'nombre':'nbobonb9r','anio':2005}
response25=requests.post('http://localhost:8000/albumes/',headers=header_superuser,json=album)
album_id=response25.json().get('id')
assert response25.status_code==201, "La respuesta deberia ser 201"

response26=requests.put(f'http://localhost:8000/albumes/{album_id}/',headers=header_superuser,json={'artista':4,'nombre':'zxzcxvcbhy','anio':1994})
assert response26.status_code==200, "La respuesta deberia ser 200"

response27=requests.delete(f'http://localhost:8000/albumes/{album_id}/',headers=header_superuser)
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

response33=requests.get('http://localhost:8000/canciones/',headers=header_usuarioA)
assert response33.status_code==200, "La respuesta deberia ser 200"

cancion2={'album':1,'nombre':'khgklh','duracion':270,'genero':'hg48hg8g','colaboradores':[2,3]}
response34=requests.post('http://localhost:8000/canciones/',headers=header_usuarioA,json=cancion2)
cancion_id=response34.json().get('id')
assert response34.status_code==201, "La respuesta deberia ser 201"

string_tokenB="Token " + tokenB
header_usuarioB={'Authorization':string_tokenB}
response_userB_editar=requests.put(f'http://localhost:8000/canciones/{cancion_id}/',headers=header_usuarioB,json={'album:':2,'nombre':'e3r4t5y6','duracion':410,'genero':'gfrju','colaboradores':[3,4]})
assert response_userB_editar.status_code==403, "la respuesta deberia ser 403"

response_userB_eliminar=requests.delete(f'http://localhost:8000/canciones/{cancion_id}/',headers=header_usuarioB)
assert response_userB_eliminar.status_code==403, "La respuesta deberia ser 403"

response35=requests.put(f'http://localhost:8000/canciones/{cancion_id}/',headers=header_usuarioA,json={'album':1,'nombre':'ccvvcbcb','duracion':330,'genero':'nnjnjmj','colaboradores':[3,5]})
assert response35.status_code==200, "La respuesta deberia ser 200"

response36=requests.delete(f'http://localhost:8000/canciones/{cancion_id}/',headers=header_usuarioA)
assert response36.status_code==200, "La respuesta deberia ser 200"

response37=requests.get('http://localhost:8000/canciones/',headers=header_superuser)
assert response37.status_code==200, "La respuesta deberia ser 200"

cancion3={'album':2,'nombre':'xvbcbfbcb','duracion':230,'genero':'sawqwefd','colaboradores':[2,4]}
response38=requests.post('http://localhost:8000/canciones/',headers=header_superuser,json=cancion3)
cancion_id2=response38.json().get('id')
assert response38.status_code==201, "La respuesta deberia ser 201"

response39=requests.put(f'http://localhost:8000/canciones/{cancion_id2}/',headers=header_superuser,json={'album':4,'nombre':'uuhjutijg','duracion':200,'genero':'nbjgjgj','colaboradores':[1,2]})
assert response39.status_code==200, "La respuesta deberia ser 200"

response40=requests.delete(f'http://localhost:8000/canciones/{cancion_id2}/',headers=header_superuser)
assert response40.status_code==200, "La respuesta deberia ser 200"

response41=requests.get(f'http://localhost:8000/canciones/{cancion_id2}/')
assert response41.status_code==404, "La respuesta deberia ser 404"


#lista de reproduccion

response42=requests.get('http://localhost:8000/listas/')
assert response42.status_code==403, "La respuesta deberia ser 403"

lista={'nombre':'f34f3f3f3','canciones':[2,3]}
response43=requests.post('http://localhost:8000/listas/',json=lista)
assert response43.status_code==403, "La respuesta deberia ser 403"

response44=requests.put(f'http://localhost:8000/listas/1/',json={'nombre':'e2r2r2r2','canciones':[2,3]})
assert response44.status_code==403, "La respuesta deberia ser 403"

response45=requests.delete(f'http://localhost:8000/listas/1/')
assert response45.status_code==403, "La respuesta deberia ser 403"

response46=requests.get('http://localhost:8000/listas/',headers=header_usuarioA)
assert response46.status_code==200, "La respuesta deberia ser 200"

lista2={'nombre':'cbvhytyyg','canciones':[1,4]}
response47=requests.post('http://localhost:8000/listas/',headers=header_usuarioA,json=lista2)
lista_id=response47.json().get('id')
assert response47.status_code==201, "La respuesta deberia ser 201"

response_userB_editar_lista=requests.put(f'http://localhost:8000/listas/{lista_id}/',headers=header_usuarioB,json={'nombre':'savchgyt','canciones':[3,4]})
assert response_userB_editar_lista.status_code==403, "la respuesta deberia ser 403"

response_userB_eliminar_lista=requests.delete(f'http://localhost:8000/listas/{lista_id}/',headers=header_usuarioB)
assert response_userB_eliminar_lista.status_code==403, "La respuesta deberia ser 403"

response48=requests.put(f'http://localhost:8000/listas/{lista_id}/',headers=header_usuarioA,json={'nombre':'jnjnmnk','canciones':[1,2,3]})
assert response48.status_code==200, "La respuesta deberia ser 200"

response49=requests.delete(f'http://localhost:8000/listas/{lista_id}/',headers=header_usuarioA)
assert response49.status_code==200, "La respuesta deberia ser 200"

response50=requests.get('http://localhost:8000/listas/',headers=header_superuser)
assert response50.status_code==200, "La respuesta deberia ser 200"

lista3={'nombre':'nbnbhjhjk','canciones':[2,3,4,5]}
response51=requests.post('http://localhost:8000/listas/',headers=header_superuser,json=lista3)
lista_id2=response51.json().get('id')
assert response51.status_code==201, "La respuesta deberia ser 201"

response52=requests.put(f'http://localhost:8000/listas/{lista_id2}/',headers=header_superuser,json={'nombre':'mnmhjjhiykg','canciones':[1,2,3,4]})
assert response52.status_code==200, "La respuesta deberia ser 200"

response53=requests.delete(f'http://localhost:8000/listas/{lista_id2}/',headers=header_superuser)
assert response53.status_code==200, "La respuesta deberia ser 200"

response54=requests.get(f'http://localhost:8000/listas/{lista_id2}/')
assert response54.status_code==404, "La respuesta deberia ser 404"