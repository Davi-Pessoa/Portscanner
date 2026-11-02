import nmap


scanner = nmap.PortScanner()
print("seja bem-vindo ao DIO Scanner")
print("<------------------------------------->")
ip = input("Digite o IP a ser verificado: ")
print("O IP digitado foi: ", ip)
type(ip)

menu = input ("""""\nEscolha o tipo de varredura a ser feita:
1 - Varredura do tipo SYN
2 - Varredura do tipo UDP
3 - Varredura do tipo intensa
digite a opção desejada: """)

print('a opção escolhida foi: ', menu)

if menu == '1':
    print('Versão do NMAP: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
elif menu == '2':
    print('Versão do NMAP: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print("Portas abertas: ", scanner[ip]['udp'].keys())
    print('scan realizada com sucesso!')
    print('scan realizada com sucesso!')
elif menu == '3':
    print('Versão do NMAP: ', scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print('')
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
    print('scan realizada com sucesso!')
else:
    print("Opção inválida, digite uma opção válida.")
    