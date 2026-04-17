# contador.py
# Versión inicial correcta

def siguiente(n):
    return n + 1

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        valor = int(sys.argv[1])
        print(siguiente(valor))
# Log: añadido comentario 1
