```mermaid
 classDiagram
      Kayttoliittyma "1" -- "1" Repository
      Initialize_database ..> "1" Database_connection
      Repository "1" ..> "1" Database_connection
      Kayttoliittyma "1" ..> "1" Database_connection
```