import tools
permitidos=[0,1,2,3]
ingresados=[]
tableros=[
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ],
  
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ],
  
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ],
  
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ]

]
turno=2
print(tools.imprimir_tablero(tableros))
while tools.revisar_vacios(tableros)==True and tools.revisar_ganador(tableros)==0:
  turno=[1,2][turno%2]
  x,y,z="a","a","a"
  while x not in [0,1,2,3] or y not in [0,1,2,3] or z not in [0,1,2,3] or [x,y,z] in ingresados:
    print("Turno del judador", str(turno)+":")
    x,y,z=int(input("x: ")),int(input("y: ")),int(input("z: "))
    print("")
  ingresados.append([x,y,z])
  if turno==1:  tableros[z][y][x]=1
  elif turno==2:  tableros[z][y][x]=-1
  print(tools.imprimir_tablero(tableros))
if tools.revisar_ganador(tableros)!=0:  print("Gano el jugador", str(turno)+".")
else: print("¡¡¡Empate!!!")
