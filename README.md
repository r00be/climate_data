# PCTO2021: Approccio serverless al processamento di dati provenienti da sensori 

## Obiettivi del progetto
> Introduzione

```sh
Questo programma richiama dei dati, che in particolare riguardano contenuto volumetrico dell'acqua, la temperatura del suolo,
quella ambientale, e l'umidità, dal sito del "Corriere della Sera", che li ha memorizzati e li classifica in base alla città.
Il programma richiama anche la posizione geografica al momento della cattura dei dati (latitudine e longitudine), insieme ad
un ID unico che specifica da dove proviene il dato.
```

> Una rapida spiegazione di come funziona il nostro programma.

```sh
Prima di iniziare, è opportuno sapere che ogni capoluogo di provincia presente nella lista del "Corriere della Sera" 
è caratterizzato da un codice numerico. All'interno del nostro programma python abbiamo realizzato una funzione "URL",
che permette di riuscire a ricavare i dati di quel relativo nodo. Tutto questo è possibile grazie alla funzione "node_code",
a cui è connesso un vettore che scorrendo sceglie la città a cui fa riferimento il codice.
```

## Architettura (componenti software/hardware e loro interazione)
```sh
Per la realizzazione del progetto è stato utilizzato:
-AWS (Amazon Web Services): offre servizi di cloud computing.
-DBeaver:è uno strumento di amministrazione del database, che ci permette di gestire il db creato da AWS
-Visual Studio Code - Python(3.9.1): in python viene scritto il codice che genera i dati dei nodi e invia il JSON all'API Gateway
-Alexa Developer: mediante Alexa viene fatta una richiesta e la Lambda restituisce il risultato

I servizi utilizzati da AWS sono stati:
-API Gateway: questa interfaccia richiama le Lambda function in base alle HTTP request.

-Lambda function:    vengono utilizzate due lambda function, entrambe in linguaggio python, ma con metodi diversi:
                        1. metodo POST: si connette al database
                        2. metodo GET:  esetrapola dei dati dal database e li restituisce in JSON


-RDS (Relational Database Service): viene creato un database PostgreSQL che, una volta configurato, viene gestito da DBeaver 

```


### Elenco dei tool che utilizzate (non deve essere un tutorial, piuttosto usate link esterni)
```sh

API Gateway: https://console.aws.amazon.com/apigateway/home?region=us-east-1#/apis/gcm2ijz2qa/resources/uil15qngw1
Alexa Developer: https://developer.amazon.com/alexa/console/ask/build/custom/amzn1.ask.skill.9a0eacce-aebe-4054-9a97-7aedf882dd66/development/it_IT/dashboard

```

## Simulazione in Python dei dati necessari all'applicazione
```sh
![Simulazione dati](/1st_json.PNG)
```
## Struttura del database: schema ER e schema logico, eventuali vincoli di integrità referenziale
## Lambda function per il data injection e per l’elaborazione dei dati nel database
## Spiegate il ruolo del HTTP 
## Stato di avanzamento del progetto e sviluppi futuri
> Un rapido resoconto dei risultati ottenuti fino ad ora.


* 0.2.1 (Mar 23 Feb 2021)
    * Continuazione redazione file READMI
    * Prima revisione dei risultati ottenuti
    
* 0.2.0 (Lun 22 Feb 2021)
    * Continuazione dell'implementazione della funzione lambda al programma in python
    * Inizio redazione file README
    
* 0.1.1 (Gio 18 Feb 2021)
    * Continuazione del lavoro su python per connettere al database
    * Sviluppo funzione lambda e tentativi di implementazione in python
    
* 0.1.0 (Mar 16 Feb 2021)
    * Creazione struttura database con due tabelle
    * Inizio programmazione file python con lista json delle varie città.
    
* 0.0.1 (Lun 15 Feb 2021)
    * Inizio lavoro, divisione del lavoro ed organizzazione responsabilità
    * Creazione dei vari account: postman, github, aws.
    * 
## Considerazioni finali

## Il gruppo di lavoro
> Elenco di presentazione dei membri che partecipano attivamente alla creazione del programma.


- **Contigiani Roberto** (_referente gruppo_): parte dello sviluppo codice e connessione al relativo database;
- **Sgalippa Stefano**: parte relativa allo sviluppo del database;
- **Capparelli Claudio**: parte relativa alla creazione e gestione della pagina GitHub, creazione del file README.md



## Sezione relativa agli sviluppi su Amazon AWS

![Amazon AWS]


## Link che hanno aiutato alla realizzazione del progetto

1. 
