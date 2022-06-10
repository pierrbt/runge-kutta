import numpy
import matplotlib.pyplot as plt


N = int(input("Combien d'intervales à mesurer : ")) 
vitesse_anal=(N+1)*[0]
vitesse_runge=(N+1)*[0]
erreur=(N+1)*[0]
ti=(N+1)*[0]
y=0
g=9.81
cd=0.25
m=68.1
t=0
dt=13/N
n=1
while n<N+1:
    k1=g-(cd/m)*y**2
    k2=g-(cd/m)*(y+dt*k1)**2
    y=y+(dt/2)*(k1+k2)
    t=t+dt
    ti[n]=t
    vitesse_runge[n]=y
    vitesse_anal[n]=51.69*numpy.tanh(t/5.27)
    erreur[n]=(vitesse_anal[n]-vitesse_runge[n])/vitesse_anal[n]
    n=n+1

chaine = 'Runge-Kutta : '
for i in vitesse_runge:
    chaine += str(round(i,1)) + ' - '
chaine += '\nAnalytique : '
for i in vitesse_anal:
    chaine += str(round(i,1)) + ' - '
chaine += '\nErreur : '
for i in erreur:
    chaine += str(round(i,5)) + ' - '
print(chaine)
plt.plot(ti,vitesse_runge,label="Runge-Kutta")
plt.plot(ti,vitesse_anal,label="Analytique")    
plt.plot(ti,erreur,label="Erreur")
plt.legend()
plt.show()



#connect to database
import mysql.connector as mysql
mysql.createConnection(host="localhost",user="root",passwd="",database="python")
cursor = mysql.cursor()
cursor.execute("SELECT * FROM table")
