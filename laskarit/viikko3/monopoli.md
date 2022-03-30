```mermaid
 classdiagram
      Noppa '2' <-- '1' Pelaaja
      Noppa '2' --> '1' Pelinappula
      Pelaaja '1' --|> '1' Pelinappula
      Pelilauta '1' --|> '40' Ruutu
      Ruutu '1' <-- '1' Pelinappula
      class Noppa{}
      class Pelaaja{}
      class Pelilauta{}
      class Ruutu{}
      class Pelinappula{}
```
