# T-Mobile unlimited aanvuller
Python script om de T-Mobile 2GB aanvaller automatisch te activeren.

Pas het script aan met je eigen telefoonnummer en T-Mobile wachtwoord.

## Cronjob
Dit script kan mooi als cronjob ingesteld worden.
```
* * * * * cd pad/van/script && python t-mobile-aanvuller.py > /pad/naar/logfile.log 2>&1
```
