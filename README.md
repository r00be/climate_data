# Progetto

> Introduzione


```sh
Questo programma richiama dei dati, che in particolare riguardano contenuto volumetrico dell'acqua, la temperatura del suolo,
quella ambientale, e l'umidità, dal sito del "Corriere della Sera", che li ha memorizzati e li classifica in base alla città.
Il programma richiama anche la posizione geografica al momento della cattura dei dati (latitudine e longitudine), insieme ad
un ID unico che specifica da dove proviene il dato.
```

## Esempio di utilizzo

> Una rapida spiegazione di come funziona il nostro programma.


```sh
Prima di iniziare, è opportuno sapere che ogni capoluogo di provincia presente nella lista del "Corriere della Sera" 
è caratterizzato da un codice numerico. All'interno del nostro programma python abbiamo realizzato una funzione "URL",
che permette di riuscire a ricavare i dati di quel relativo nodo. Tutto questo è possibile grazie alla funzione "node_code",
a cui è connesso un vettore che scorrendo sceglie la città a cui fa riferimento il codice.
```


## Membri del gruppo e responsabilità

> Elenco di presentazione dei membri che partecipano attivamente alla creazione del programma.


```sh
- Contigiani Roberto (rappresentante gruppo): parte dello sviluppo codice e connessione al relativo database;
- Sgalippa Stefano: parte relativa allo sviluppo del database;
- Capparelli Claudio: parte relativa alla creazione e gestione della pagina GitHub, creazione del file README.md
```

## Cronologia delle varie release

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
    
* 0.1.0

    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
    
* 0.0.1 (Lun 15 Feb 2021)

    * Inizio lavoro


## Link che hanno aiutato alla realizzazione del progetto

1. Link del Corriere della Sera, sezione meteo (https://meteo.corriere.it/)
