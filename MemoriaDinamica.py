def main():
    frutas = []

    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Uvas")
    print(frutas)

    frutas.pop(0)
    frutas.pop(1)
    
    frutas.append("Sandía")
    print(frutas)

if __name__ == "__main__":
    main()
