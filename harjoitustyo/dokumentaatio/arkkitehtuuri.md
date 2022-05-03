## rakenne

```mermaid
 classDiagram
      index --> UI
      Service "1" <--> "1" File_reader
      Initialize_database ..> "1" Database_connection
      File_reader "1" <..> "1" Database_connection
      UI "1" --> "1" FrontView
      UI "1" --> "1" LoginView
      LoginView "1" --> "1" Service
      FrontView "1" <..> "1" LoginView
      FrontView "1" <--> "1" Service
```

## sovelluslogiikka

Suuri osa sovelluksen toiminnoista noudattaa seuraavaa kaavaa.  
tietojen poistaminen repositoriosta: 

```mermaid
sequenceDiagram
    FrontView->>+Service: delete_all_data()
    Service->>+Repository: clear()
    Repository-->>-Service: 
    Service-->>-FrontView: 
    FrontView->>+FrontView: initialize_data()
    alt Data_View != None
        FrontView->>+DataView: destroy()
        DataView-->>-FrontView: 
    end
    FrontView->>DataView: 
    DataView->>+DataView: initialize()
    DataView->>-DataView: 
    DataView-->>FrontView: 
    FrontView->>+DataView: pack()
    DataView-->>-FrontView: 
    FrontView->>-FrontView: 
```

## tallennus

Data tallennetaan SQLite-tietokantaan (harjoitustyo/src/repositories/data.db). Tietokantaa lukee ja kirjoittaa File_reader.py tiedostossa oleva Repository -luokka. Tietokannan schema on tallennettu schema.sql tiedostoon. Tietokannassa on taulut income, expenses, wealth ja users.