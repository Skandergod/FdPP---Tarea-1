import os
import subprocess
import sys
from datetime import datetime

orig_stdout = sys.stdout
f = open('Salida - Reduction Estatica.txt', 'w')
sys.stdout = f

startTime = datetime.now()

subprocess.check_output(['g++', 'e7 - Reduction Estatica.c', '-fopenmp'])
print('e7 - Reduction Estatica.c')

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '2'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '2'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '2'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print("4 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '4'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '4'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '4'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print("8 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '8'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '8'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '8'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print("16 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '16'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '16'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '16'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print("20 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '20'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '20'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '20'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print("100 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '100'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '100'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '100'])
    output = str(output,'utf-8')
    output.rstrip()
    print(output)

print(datetime.now() - startTime)

sys.stdout = orig_stdout
f.close()