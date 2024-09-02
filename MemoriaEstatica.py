def main():
    calificaciones = []

    for i in range(5):
        calificacion = int(input(f"Captura la calificación {i + 1}: "))
        calificaciones.append(calificacion)
    
    for i in range(5):
        print(f"Calificación {i + 1}: {calificaciones[i]}")

if __name__ == "__main__": 
    main()
