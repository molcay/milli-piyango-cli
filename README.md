# milli-piyango-cli

You can retrieve information about 5 different game (listed below) results from [Milli Piyango](http://www.mpi.gov.tr/) on command line.

* Piyango: [Game Spec](http://www.mpi.gov.tr/?q=node/1) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_piyango.php)
* Sayısal Loto: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/33) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_sayisal.php)
* Şans Topu: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/31) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_sanstopu.php)
* On Numara: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/8) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_onnumara.php)
* Süper Loto: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/32) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_superloto.php)

### Usage:
```bash
  mp games
  mp dates <game>
  mp result <game> <date>
  mp piyango <date> <ticketNo>
```

### Dependencies:
* [docopt](https://github.com/docopt/docopt)
* [MilliPiyango](https://github.com/molcay/milli-piyango/)
