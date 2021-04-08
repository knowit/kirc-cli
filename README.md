**Hvordan kjøre CLIet**

Stegene under beskriver hvordan man kjører CLIet (Command Line Interface) i terminalen. Om du har problemer underveis eller lurer på noe er det bare å spørre en av veilederne om hjelp :) 

1. Åpne en terminal (`cmd` eller `PowerShell` i Windows), og sjekk om du har `python3.4` eller høyere ved å kjøre kommandoen `$ python --version` eller `$ python3 --version` (uten dollartegn -- dollartegnet er kun for å vise at det er en terminal-kommando). Dersom du får en output som `Python 3.x.y` e.l. der `x >= 4` kan du gå videre til steg 3. 
2. Installer Python ved å følge guiden [her](https://docs.python-guide.org/starting/installation/) for ditt operativsystem. 
3. Klon repoet ved å kjøre kommandoen `$ git clone https://github.com/knowit/kirc-cli.git && cd kirc-cli` (om du ikke har Git fra før må du [installere det](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)).
4. Installer `pipenv` som er et verktøy for håndtering av virtuelle miljø i Python ved å kjøre `$ pip install --user pipenv`. Dette steget (og steg 5) kan hoppes over om du har et verktøy for virtuelle miljø fra før (som `conda`) og du vet hvordan det brukes. 
5. Kjør kommandoen `$ python -m pipenv install` (her må du kanskje bytte `python` ut med `python3`)
6. Det vil bli lastet opp en fil kalt `.env`  med credentials. Denne må lastes inn i shellet med kommandoen source .env  manuelt, eller man kan bruke [Direnv](https://direnv.net) for å laste det automatisk. Hvis denne filen mangler, si fra.
7. (Om du bruker `pipenv` som miljøhåndteringsverktøy) Kjør klienten med `$ python -m pipenv run python sqs_client.py` (eventuelt `python3` istedenfor `python`)og følg instruksene. 

**STYLING SENDT FRA CLI**

*OBS*: Frontenden forventer styling som strenger på formen "key1: value1; key2: value2;" osv., f.eks. "font-size: 48px; background-color: pink;", så om dere vil at styling skal dukke opp i frontenden er det dette formatet som CLIet til slutt må sende. 