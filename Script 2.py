import os
import subprocess
import sys
from datetime import datetime

orig_stdout = sys.stdout
f = open('Salida - Parallel.txt', 'w')
sys.stdout = f

startTime = datetime.now()

subprocess.check_output(['g++', 'e7 - Parallel.c', '-fopenmp'], cwd='D:\Workbench\FdPP\Tarea 1')
print("e7 - Parallel.c")
print("2 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '2'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '2'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '2'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

print("4 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '4'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '4'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '4'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

print("8 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '8'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '8'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '8'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

print("16 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '16'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '16'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '16'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

print("20 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '20'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '20'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '20'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

print("100 Hilos")

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '1000000', '100'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '2500000', '100'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)

for i in range(3):
    output = subprocess.check_output(['a.exe', '1', '5000000', '100'], cwd='D:\Workbench\FdPP\Tarea 1')
    output = output.decode("utf-8")
    output.rstrip()
    print(output)


print(datetime.now() - startTime)

sys.stdout = orig_stdout
f.close()