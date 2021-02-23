# Sensor data

## Introduzione.
```sh
Questo programma richiama dei dati, che in particolare riguardano contenuto volumetrico dell'acqua, la temperatura del suolo,
quella ambientale, e l'umidità, dal sito del "Corriere della Sera", che li ha memorizzati e li classifica in base alla città.
Il programma richiama anche la posizione geografica al momento della cattura dei dati (latitudine e longitudine), insieme ad
un ID unico che specifica da dove proviene il dato.
```

## Esempio di utilizzo

Una rapida spiegazione di come funziona il nostro programma.

```sh
Prima di iniziare, è opportuno sapere che ogni capoluogo di provincia presente nella lista del "Corriere della Sera" 
è caratterizzato da un codice numerico. All'interno del nostro programma python abbiamo realizzato una funzione "URL",
che permette di riuscire a ricavare i dati di quel relativo nodo. Tutto questo è possibile grazie alla funzione "node_code",
a cui è connesso un vettore che scorrendo sceglie la città a cui fa riferimento il codice.
```


## Membri del gruppo e responsabilità

```sh
make install
npm test
```

## Release History

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
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
