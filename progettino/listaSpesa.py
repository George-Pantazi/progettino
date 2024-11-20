lista_della_spesa = []

#2
def aggiungi_elemento():
    elemento = input("Inserisci l'elemento da aggiungere alla lista: ")
    lista_della_spesa.append(elemento)
    print(f"{elemento} è stato aggiunto alla lista!")


#3
def visualizza_lista():
    if lista_della_spesa:
        print("\nLista della spesa:")
        for i, elemento in enumerate(lista_della_spesa):
            print(f"{i}. {elemento}")
    else:
        print("La lista della spesa è vuota.")

#4 
def rimuovi_elemento():
    if len(lista_della_spesa) == 0:
        print("La lista è vuota, non puoi rimuovere nulla.")
        return
    visualizza_lista()
    try:
        indice = int(input("Inserisci il numero dell'elemento da rimuovere (ad esempio 1 per il primo): ")) - 1
        if 0 <= indice < len(lista_della_spesa):
            elemento_rimosso = lista_della_spesa.pop(indice)
            print(f"{elemento_rimosso} è stato rimosso dalla lista.")
        else:
            print("Indice non valido.")
    except ValueError:
        print("Per favore inserisci un numero valido.")