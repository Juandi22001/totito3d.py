def revisar_vacios(tableros):
  for tablero in tableros:
    for fila in tablero:
      for celda in fila:
        if celda==0:	return True
  return False
          
def revisar_ganador(tableros):
  sumas = []
  
  # horizontales
  for tablero in tableros:
    for fila in tablero:
        sumas.append(sum(fila))
    d1 = d2 = 0
    for i in range(len(tablero)):
        suma = 0
        for fila in tablero:
          suma += fila[i]
          
        # Verticales
        sumas.append(suma)
  
        # Diagonales
        d1 += tablero[i][i]
        d2 += tablero[i][len(tablero) - i - 1]
    sumas.extend([d1, d2])
  
  #columnas_profundas
  sumas_profundas=0
  for a in range(4):
    for b in range(4):
      for z in range(4):
        sumas_profundas+=tableros[z][a][b]
      sumas.append(sumas_profundas)
      sumas_profundas=0
    	
  #diagonales_profundas
  suma_dp1,suma_dp2,suma_dp3,suma_dp4=0,0,0,0
  for a in range(4):
    suma_dp1+=tableros[a][a][a]
    suma_dp2+=tableros[a][a][3-a]
    suma_dp3+=tableros[a][3-a][a]
    suma_dp4+=tableros[a][3-a][3-a]	
  sumas.extend([suma_dp1,suma_dp2,suma_dp3,suma_dp4])
  
  # escalers profundas de enfrente
  suma_ep1,suma_ep2=0,0
  for a in range(4):
  	for b in range(4):
  		suma_ep1+=tableros[b][b][a]
  		suma_ep2+=tableros[3-b][b][a]
  	sumas.extend([suma_ep1,suma_ep2])
  	suma_ep1,suma_ep2=0,0
  	
  # escaleras profundos de lado
  suma_epl1,suma_epl2=0,0
  for a in range(4):
  	for b in range(4):
  		suma_epl1+=tableros[b][a][b]
  		suma_epl2+=tableros[b][a][3-b]
  	sumas.extend([suma_epl1,suma_epl2])
  	suma_epl1,suma_epl2=0,0

  if 4 in sumas: return 1
  elif -4 in sumas: return -1
  return 0

def imprimir_tablero(tableros):
  impresion="\n"+"Tableros:"+"\n"
  for a in range(4):
    for b in range(4):
      for celda in tableros[b][a]:
        if celda==1:	impresion+="x "
        elif celda==-1:	impresion+="O "
        else:	impresion+="• "
      impresion+="   "
    impresion+="\n"
  return impresion
