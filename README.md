# milenage

Milenage er en protokoll for etablering av integritet. Når man har etablert kontakt mellom klient og server er det mulig å bruke nøklene som er laget å utvikle sikre tilkoblinger.
Hva prøver MILENAGE å oppnå?
Nettverket skal kunne bevise at det kjenner abonnentens hemmelige nøkkel K.
SIM-kortet skal kunne bevise at det kjenner samme nøkkel K.
Ingen skal trenge å sende K over nettet.
Begge parter skal kunne utlede sesjonsnøkler (CK og IK) for videre sikker kommunikasjon.


I Milenage er det krypteringsalgoritmer som er vel kjente og man må med forbehold bruke unike hemmelige nøkler.

Etter den første AES-beregningen produseres en mellomverdi.
Denne mellomverdien:
XOR-es med OPc
Roteres
XOR-es med forskjellige konstanter (c1, c2, ...)

for å skape forskjellige input til nye AES-kall.

Konseptuelt kan milenage viser ved disse stegene:


Spørsmål:
Hvordan dokumenterer man bruk av KI? Er et noen begrensninger 

Hvordan skal man referere til dokumentasjonen? Hvordan dokumenterer man og hva er cirka nok?

