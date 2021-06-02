from threading import Thread, Lock
import random
import time

saldo = 1000
vetop = []
threads = []
mutex = Lock()

for i in range(100):
    vetop.append(
        random.randint(-500, 500)
    )

def Operacao(tid):
    global saldo, mutex, vetop
    
    
    valorop = 0
    
    while True:
        with mutex:
            if len(vetop) == 0:
                break
            valorop = vetop.pop()
            saldotmp = saldo
            saldotmp += valorop
            time.sleep(random.randint(0,2))
            saldo = saldotmp
            print(f'Posição: {len(vetop)} - Saldo: {saldotmp}')
    
    print(f'Thread {tid} morrendo... Saldo {saldo}')

def main():
    
    for i in range(3):
        print(f'caixa atual {i}')
        
        threads.append(Thread(
            target=Operacao, args=(i,)
            )
        )
        threads[-1].start()
        
    for i in range(3):
        print(f'Esperando pelo caixa {i}')
        threads[i].join()

    print(f'Saldo final = {saldo}')
    

if __name__ == "__main__":
    main()
