from datetime import datetime
from elasticsearch import Elasticsearch

# Connessione a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Verifica della connessione
if es.ping():
    print(" Connessione a Elasticsearch stabilita!")
else:
    print(" Impossibile connettersi a Elasticsearch!")
    exit()

# Indice per i documenti
index_name = "libri"

# Definizione dei documenti
books = [
    {"title": "Il nome della rosa", "author": "Umberto Eco", "genere": "Storico", "published_date": "1980-01-01"},
    {"title": "La coscienza di Zeno", "author": "Italo Svevo", "genere": "Romanzo", "published_date": "1923-05-15"},
    {"title": "Il Gattopardo", "author": "Giuseppe Tomasi di Lampedusa", "genere": "Storico", "published_date": "1958-01-01"},
    {"title": "Il Signore degli Anelli", "author": "J.R.R. Tolkien", "genere": "Fantasy", "published_date": "1976-03-02"},
    {"title": "PESTO", "author": "GENOVA", "genere": "Comico", "published_date": "1923-05-15"},
    {"title": "il mio fantasy", "author": "Giuseppe Savojoardi", "genere": "Fantasy", "published_date": "1958-01-01"},
    {"title": "Dallas my ", "author": "Jr. Junior", "genere": "Fantasy", "published_date": "1976-03-08"},
]

# Creazione dell'indice (se non esiste)
try:
    es.indices.get(index=index_name)
    print(f" L'indice '{index_name}' esiste già.")
except:
    es.indices.create(index=index_name)
    print(f" Indice '{index_name}' creato con successo.")

# Indicizzazione documenti
try:
    for i, book in enumerate(books):
        res = es.index(index=index_name, id=i+1, document=book)
        print(f" Documento {i+1} indicizzato: {res['result']}")
except Exception as e:
    print(f" Errore durante l'indicizzazione: {e}")

# Query per ricerca di libri storici
query = {
    "query": {
        "match": {
            "genere": "Storico"
        }
    }
}

try:
    res = es.search(index=index_name, body={"query": query["query"]})
    print("\n Risultati della ricerca per libri storici:")
    for hit in res['hits']['hits']:
        print(hit["_source"])
except Exception as e:
    print(f"Errore durante la ricerca: {e}")

