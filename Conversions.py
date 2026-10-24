'''n=672
binary=bin(n)
print(binary)
octal=oct(n)
print(octal)
hexadecimal=hex(n)
print(hexadecimal)
#binary to decimal
binary="1101"
decimal=int(binary, 2)
print(decimal)
#octal to decimal
octal="243"
decimal=int(octal, 8)
print(decimal)
#hexadecimal to decimal
hexadecimal="89A"
decimal=int(hexadecimal, 16)
print(decimal)

#binary to octal
binar="g1101"
decimal=int(binary, 2)
octal=oct(decimal)
print(octal)

#binary to hexadecimal
binary="1010"
decimal=int(binary, 2)
hexadecimal=hex(decimal)
print(hexadecimal)

#octal to binary
octal= input("Enter an octal number:")
binary=bin(int(octal, 8))
print(binary)
#octal to hexadecimal
octal= input("Enter an octal number:")
hexadecimal= hex(int(octal, 8))
print(hexadecimal)'''

#hexadecimal to binary
hexadecimal="12A6"
binary=bin(int(hexadecimal, 16))
print(binary)

#hexadecimal to octal
hexadecimal="A23"
octal=oct(int(hexadecimal, 16))
print(octal)
            
