import requests


usuarioA={"username":"userA","password":"usera123456"}
response1=requests.post('http://localhost:8000/login/',json=usuarioA)
print(response1.json())

usuarioB={"username":"userB","password":"userb123456"}
response2=requests.post('http://localhost:8000/login/',json=usuarioB)
print(response2.json())

#response=requests.get('http://localhost:8000/artistas/')
#print(response.status_code)

#artista={'nombre':'df7f7fd72fd27g'}
#response=requests.post('http://localhost:8000/artistas/',json=artista)
#print(response.status_code)


#response=requests.put('http://localhost:8000/artistas/22/',data={'nombre':'5rtf6gfwh'})
#print(response.status_code)

#response=requests.delete('http://localhost:8000/artistas/22/')
#print(response.status_code)

#header={'Authorization':'Token 3f665daa5dcdfd7073b8542684cc03a9a62cbf49'}
#response=requests.get('http://localhost:8000/artistas/',headers=header)
#print(response.status_code)

#artista={'nombre':'wasd'}
#response=requests.post('http://localhost:8000/artistas/',headers=header,json=artista)
#print(response.status_code)

#response=requests.put('http://localhost:8000/artistas/19/',headers=header,data={'nombre':'tttttgghyt'})
#print(response.status_code)

#response=requests.delete('http://localhost:8000/artistas/19/',headers=header)
#print(response.status_code)

#header={'Authorization':'Token f0633c6402fef3aa4ab11b0e1e78fa5ee87809c9'}
#response=requests.get('http://localhost:8000/artistas/',headers=header)
#print(response.status_code)

#artista={'nombre':'qwerty'}
#response=requests.post('http://localhost:8000/artistas/',headers=header,json=artista)
#print(response.status_code)

#response=requests.put('http://localhost:8000/artistas/23/',headers=header,data={'nombre':'uiop'})
#print(response.status_code)

#response=requests.delete('http://localhost:8000/artistas/23/',headers=header)
#print(response.status_code)

#response=requests.get('http://localhost:8000/artistas/23')
#print(response.status_code)