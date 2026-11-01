# Omicron Operator

Nove strumenti da tasca in una sola pagina (drum machine, synth, chiptune, sampler, voce), con un clock condiviso. Si usano uno alla volta sul telefono o tutti insieme su iPad, con lo zoom. Funziona senza rete una volta installata.

## Contenuto della cartella

- `index.html` — l'app completa (grafica, motore audio, sequencer) in un solo file
- `manifest.webmanifest` — nome, icona e colori per l'installazione come app
- `sw.js` — service worker: tiene in cache l'app e i font, così si apre anche offline
- `icons/` — icone per schermata Home e scheda del browser
- `build.py` — ricostruisce `index.html` dal sorgente `od16.html` (`python3 build.py ../od16.html`)

## Come usarla

### 1. Subito, senza installare nulla
Apri `index.html` nel browser del computer. Tutto funziona tranne il service worker e il microfono (che richiedono https o localhost).

### 2. Come app sul telefono (consigliato)
L'app va messa su un indirizzo https, per esempio GitHub Pages:

1. Crea un repository (o usa quello dei giochi) e copia dentro tutta la cartella.
2. Attiva Pages dalle impostazioni del repository.
3. Apri l'indirizzo dal telefono:
   - **iPhone / iPad**: in Safari tocca Condividi → *Aggiungi alla schermata Home*. L'icona si apre a schermo intero, senza barra del browser.
   - **Android** (Chrome, Edge, Samsung Internet): menu ⋮ → *Installa app*, oppure il pulsante *Installa come app* nel menu ≡ dell'app.
4. La prima apertura va fatta online: da quel momento l'app, i font e le icone restano in cache e funzionano offline.

Per provarla in locale: `python3 -m http.server 8000` dentro la cartella, poi `http://localhost:8000/`.

### 3. Aggiornamenti
Sostituisci i file su Pages. Il service worker scarica la nuova versione alla prima apertura online e la usa dall'apertura successiva. Se cambi `index.html`, alza `VERSION` in `sw.js` (es. `omicron-operator-v3`) per forzare l'aggiornamento della cache.

## Cosa resta salvato

- Pattern, catene, parametri dei suoni, tempo, volumi e swing: nel browser (`localStorage`), per ogni dispositivo.
- Campioni di K.O. e Voce, con le fette tagliate: nel browser (`IndexedDB`), quindi sopravvivono alla chiusura dell'app.
- Menu ≡ → *Scarica file .json* / *Apri file .json* per spostare pattern e parametri tra dispositivi (i campioni audio non sono nel file).

Cancellando i dati del sito dal browser si perde tutto: fai un file .json prima.

Per ricominciare da capo, nel menu ≡ → *Ricomincia da capo*: svuota i 16 pattern del dispositivo attuale, svuota tutti i pattern di tutti i dispositivi (suoni, campioni, tempo e volumi restano), oppure torna ai pattern di fabbrica. Ogni pulsante chiede conferma con un secondo tocco.

## Campionamento

Nel menu ≡ scegli la sorgente:
- **Dal mix**: REC + tasto registra quello che stanno suonando gli altri dispositivi (serve un clock in moto).
- **Dal microfono**: REC + tasto registra dal microfono finché tieni premuto, anche a clock fermo. Il browser chiede il permesso la prima volta; richiede https (o localhost).
- In entrambi i casi puoi anche caricare un file audio con ⬆ FILE sull'LCD, nello slot selezionato.

Limiti di memoria come gli originali: K.O. 40 secondi in totale, Voce 8 secondi per slot.

## Barra del clock

Sotto le linguette: BPM comune a tutti (− / +, tenendo premuto scorre; TAP per battere il tempo), **▶ TUTTI** avvia insieme i dispositivi che hanno qualcosa nel pattern o nella catena, **■** ferma tutto. Mentre suona, i LED dei tasti lampeggiano sul suono che parte e l'ampolla sull'LCD si riempie col livello d'uscita del dispositivo.

## Libro dei pattern e copia tra operator

Il pulsante **LIBRO** nella barra del clock apre i 54 pattern di "16 step in linea": cerca per nome, genere o suono, guarda la griglia, scegli una variante e applicala a un operator e a uno slot (con tempo e swing del pattern, se vuoi). *Band* mette la batteria su OD-32, il basso su OD-14 e gli accordi su OD-16 nello stesso slot. I pattern a due battute occupano due slot e diventano una catena; i due pattern a 12 step (terzine) non si possono applicare perché gli operator hanno 16 step fissi.

Le tracce del libro passano per ruolo: cassa, rullante o clap, hat chiuso o aperto, perc (rim, ride, shaker, tom/conga, campanaccio secondo l'etichetta), basso e accordi, ciascuna sul suono più vicino dell'operator. Sui modelli con un solo kit di batteria (micro drum di OD-14/16/28, fette di K.O., kit Tonic di Voce) un solo colpo per step: vince cassa, poi rullante, poi perc, poi hat. Ghost note e accenti: accento sì, ghost come colpo normale (gli operator non hanno velocità per step).

La scheda **Copia tra operator** copia un pattern o tutti i 16 (con la catena) e li incolla su un altro dispositivo: identici tra modelli uguali, convertiti per ruolo tra modelli diversi. C'è anche il formato testo del libro (`kick x...x...x...x...`) per copiare e incollare pattern a mano.

## Le due viste

- **▭ Uno alla volta**: un dispositivo per schermata, si scorre di lato o dalle linguette. In orizzontale sul telefono l'LCD e i knob vanno a sinistra e i 16 tasti a destra, così entra tutto senza scorrere.
- **▦ Tutti insieme**: i nove dispositivi affiancati, con lo zoom: cursore, + e −, pizzico con due dita, e *ADATTA* che li fa entrare tutti nello schermo (su iPad in orizzontale stanno su due file). Il dispositivo toccato per ultimo ha il bordo colorato e riceve la tastiera. Su iPad l'app parte in questa vista.

## Note sui comandi

- In REC, un tocco su FX (o su KEY/CHORD) lo arma per il tasto successivo; per cancellare gli effetti o gli stili registrati nel pattern tienilo premuto da solo per un secondo. Su K.O. e Voce gli effetti si cancellano con FX + 16.
- Mentre un pattern o una catena suona, le modifiche (step, lock, accenti, FX) vanno al pattern che si sente in quel momento, che è quello mostrato in PTN sull'LCD; se hai appena scelto un altro pattern con PATTERN + tasto, le modifiche vanno a quello.

## Tastiera (desktop)

Tasti 1-16: `1234` `QWER` `ASDF` `ZXCV`. Modificatori (posizione fisica dei tasti, qualunque layout): `⇧` SOUND, `P` PATTERN, `B` BPM, `N` FX, `M` WRITE, `G` terzo tasto, `SPAZIO` play/stop, `←` `→` cambia dispositivo.

## Note

- Su iPhone l'audio parte solo dopo un tocco e segue l'interruttore silenzioso.
- Quando l'app va in secondo piano il clock si ferma (i browser rallentano i timer): è voluto, per non sfasare i dispositivi.
- Grafica, nomi, suoni e codice sono originali. I comportamenti (sequencer, effetti, combinazioni di tasti) sono ricostruiti dalle guide ufficiali dei Pocket Operator e da un post del 2017 di Magnus Lidström (Sonic Charge) sugli effetti del motore Tonic.
