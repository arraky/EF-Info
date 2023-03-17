# API Cheat Sheet

## Was ist eine API
Eine API ist das Werkzeug, das die Daten einer Website für einen Computer verständlich macht. Über sie kann ein Computer Daten anzeigen und bearbeiten, genau wie ein Mensch, indem er Seiten lädt und Formulare einreicht. Wie ein Computer, hält sich die API an strikte Protokolle. Der Unterschied zu unserem SimpleWebServer ist, dass man mittels einer API leicht mit dem Server kommunizieren kann, man leicht auf einer Website navigieren kann.
## JSON Format

Nutzt Javascript:

```jsx
{
"crust": "original", //Crust is a key, original a value
"toppings": ["cheese", "pepperoni", "garlic"],
"status": "cooking",
"customer": { //nested object **⇒ ***Associative array*****
  "name": "Brian",
  "phone": "573-111-1111"
	}
}

```

## XML Format

```xml
<order> #block called node
    <crust>original</crust> #childs
    <toppings>
        <topping>cheese</topping>
        <topping>pepperoni</topping>
        <topping>garlic</topping>
    </toppings>
    <status>cooking</status>
</order>
```
## HTTP Request:

### URL

Adressen, die dem Server sagen, mit welchen Ressourcen der Client interagieren will.

### Methoden

**Es gibt vier Methoden:**

**GET:** fragt den Server nach Daten.

**POST:** fragt den Server neue Daten zu erstellen

**PUT:** ändert existierende Daten auf dem Server

**DELETE:** löscht Daten vom Server

### Headers

**Schickt Daten über die Datennachfrage/Request** (z.B. auf welchem Typ Gerät der Nutzer eine Request stellt, sodass das richtige Format der Website gegeben werden kann. Enthält ausserdem die Methode.

### Body

Enthält die Daten, die der Client an den Server schicken will. Dementsprechend können Daten im Body vom Client frei geändert werden


## HTTP Status Codes
Geben dem Client Informationen über den Status ihrer Request. Häufige Codes sind:
- **200**: Gute Request
- **404** Keine Antwort, weil keine vorhandenen Ressourcen in dieser URL
- **503:** Die Website ist zurzeit down
## Endpunkte
Eine API definiert Endpunkte in der URL. Beispiel (https://xyz312.onrender.com/**api/tex2emo**).
## Polling
**Repetitives Fragen nach der selben Ressource:** Zum Beispiel beim Bestellen einer Pizza wird der Status immer wieder aktualisiert auf Lieferantenseite. Der Client kann mittels Polling den Server immer wieder nach dem Status fragen.
