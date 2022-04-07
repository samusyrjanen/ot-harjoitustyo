```mermaid
 classDiagram
      Kayttoliittyma "1" -- "1" Repository
      Kayttoliittyma "1" ..> "1" Database_connection
      Initialize_database ..> "1" Database_connection
      Repository "1" ..> "1" Database_connection
```