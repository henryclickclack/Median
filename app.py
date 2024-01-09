from openai import AsyncOpenAI
import chainlit as cl
from typing import Optional

client = AsyncOpenAI(base_url="https://api.together.xyz/v1",api_key="649cc8a63fe72e596207ad8e8ce409d63494dae61c1818f06fa99c226d53e970")


settings = {
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.User]:
  # Fetch the user matching username from your database
  # and compare the hashed password with the value stored in the database
  if (username, password) == ("admin", "admin"):
    return cl.User(identifier="admin", metadata={"role": "admin", "provider": "credentials"})
  else:
    return None

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [
           {"role": "system", "content": """You are a helpful FAQ assistant for the german real estate company Vonovia. You have access to the entire FAQ. Answer only with information from the FAQ. If you cant anwser a question, just say 'I dont know'. Answer short and consise. Only add to your answer what is relevant to the question. Not more!!
            Wo bekomme ich Unterstützung beim Thema Mietzahlung?

Sollten Sie Unterstützung bei Ihren Mietzahlungen benötigen, weil die finanziellen Mittel ausgehen, sind mögliche Anlaufstellen das Jobcenter oder das Amt für Wohnen und Grundsicherung – zwingend notwendig bei ausländischen Mitbewohnern ist eine Aufenthaltsgenehmigung für Antragsteller.

Bitte geben Sie uns bei Rückfragen immer Ihre Mietvertragsnummer an, damit wir Ihr Anliegen schnell und unkompliziert lösen können.

Welche Anliegen muss ich schriftlich an Vonovia richten?

Es gibt viele Anliegen, die direkt telefonisch erledigt werden können. Bitte wenden Sie sich – vor allen aus rechtlichen Gründen – für folgende Anliegen jedoch immer schriftlich an uns. In den meisten Fällen können Sie dafür auch unsere Kunden-App „Mein Vonovia“ nutzen.

Vertragsänderungen (z. B. Namensänderung oder Entlassung aus dem Mietvertrag)
Änderung Ihrer Bankverbindung
Kündigung Ihres Mietvertrages (Achtung: Alle Vertragspartner müssen die Kündigung unterschreiben)
Beschwerden
Einspruch zur Nebenkostenabrechnung
Anfrage zur Mietminderung
Wie kann ich ein SEPA-Lastschriftmandat erteilen?

Ein SEPA-Lastschriftmandat können Sie mit wenigen Klicks in unserer Kunden-App „Mein Vonovia“ im Bereich „Verträge“ unter „Zahlungsart“ erteilen.

Alternativ können Sie unseren telefonischen Kundenservice kontaktieren, dann senden wir Ihnen per Post ein Formular für die Erteilung eines SEPA-Lastschriftmandats zu.

Was ist ein SEPA-Mandat?

Für regelmäßig anfallende Rechnungen, wie z. B. Ihre Miete, ziehen wir als Vermieter mittels des SEPA-Basis-Lastschriftverfahrens automatisch von Ihrem Konto ein – sofern Sie dies gestatten. Als Kunde müssen Sie sich um nichts weiter kümmern und zahlen immer pünktlich.

Wie ist der aktuelle Stand meines Mietkontos?

Den aktuellen Stand Ihres Mietkontos können Sie in unserer Kunden-App „Mein Vonovia“ im Bereich „Verträge“ unter „Mein Mietkonto“ einsehen.

Sie sehen den Saldo Ihres Mietkontos sowie eine Übersicht der letzten Mietkontobewegungen. Sie haben auch die Möglichkeit, sich einen Kontoauszug anzeigen zu lassen und als PDF zu speichern.

Kann ich meine Zahlungen für die verschiedenen Verträge (Garage/Wohnung/Energie) auf eine Bankverbindung zahlen? 

Bitte unbedingt beachten: Jeder Vertrag hat seine eigene Bankverbindung! Nutzen Sie für Ihre Mietzahlung ausschließlich die für diesen Vertrag angegebene Bankverbindung. Zahlungen, die auf den falschen Vertrag geleistet werden, können nicht automatisch umgebucht werden. Hier kann es zu Mahnungen und damit verbundenen Mahngebühren kommen.

Was muss ich im Verwendungszweck bei einer Überweisung beachten oder ist dieser irrelevant?

Bitte geben Sie im Verwendungszweck die Mietvertragsnummer des jeweiligen Mietvertrages an.

Die Miete/Kaution wird vom Amt gezahlt? Teilen Sie auch dem Amt unbedingt die Bankverbindung und den Verwendungszweck mit, damit die Mietzahlungen richtig verbucht werden können.

Wichtiger Hinweis: Jährlich wird eine Abrechnung Ihrer Betriebs- und/oder Heizkosten vorgenommen. Die monatlichen Vorauszahlungen werden mit Ihrem jeweiligen Verbrauch aufgerechnet. Sollte das Abrechnungsergebnis eine Nachforderung ergeben, bitten wir die Änderung zur Anpassung der jeweiligen Vorauszahlung der Betriebskosten und/oder Heizkosten bei den nächsten Mietzinszahlungen zu beachten.

Wichtig: Wird Ihre Miete vom Amt gezahlt, legen Sie diesem umgehend die Abrechnung vor, damit Guthaben oder Nachzahlungen bei weiteren Mietzahlungen berücksichtigt werden können.

Kann sich meine Mietzahlung verändern?

Verschiedene Faktoren können Ihre Miethöhe beeinflussen. Die häufigsten Gründe zur Änderung der Höhe Ihrer Mietzahlung sind:

Ergebnisse der Nebenkostenabrechnung
Nachzahlungen aus dem Vorjahr bewirken eine Erhöhung Ihrer Vorauszahlung
Guthaben aus dem Vorjahr bewirken in der Regel eine Reduzierung der Vorauszahlung
Ausnahmen: Vorhersehbare Kostenänderung, wie z. B. der Energiepreise

Weitere Gründe für eine Veränderung der Miethöhe:

Grundmietanpassung auf die ortsübliche Vergleichsmiete
Grundmietanpassung aufgrund von Modernisierungsmaßnahmen
Darf ich bei mir grillen?

Viele Mieterinnen und Mieter nutzen die sonnigen Tage, um beim Grillen zu entspannen. Damit dabei auch die Brandschutzbestimmungen eingehalten werden, verwenden Sie zum Grillen auf den Grünflächen der Wohnanlage oder auf Ihrem Balkon oder Ihrer Loggia einen Elektrogrill.

Die Verwendung von festen oder flüssigen Brennstoffen (z. B. Kohle oder Gas) ist nicht gestattet.

Bitte nehmen Sie gegenseitig Rücksicht und achten Sie darauf, dass Ihre Nachbarn durch entstehende Gerüche beim Grillen nicht gestört werden.

Wozu gibt es eine Hausordnung?

Für ein harmonisches Miteinander in der Nachbarschaft informiert die Hausordnung über die wichtigsten Regeln. Dies ist uns so wichtig, dass die Hausordnung Bestandteil des Mietvertrages ist.

Wenn Sie Ihre Hausordnung nicht direkt zur Hand haben, können Sie diese mit wenigen Klicks in unserer Kunden-App „Mein Vonovia“ im Bereich „Service“ unter „Bescheinigungen“ anfordern.

Wie sind die Ruhezeiten geregelt?

Gegenseitige Rücksichtnahme ist das A und O beim Zusammenleben. Das gilt besonders für die Ruhezeiten zwischen 13:00 und 15:00 Uhr sowie zwischen 22:00 und 08:00 Uhr.

Bitte vermeiden Sie in dieser Zeit laute Musik zu hören oder Arbeiten wie Bohren und Hämmern in Ihrer Wohnung durchzuführen. Sonn- und Feiertage genießen einen besonderen Schutz, hier sollte ganztägig auf Lärm verzichtet werden. Genießen Sie stattdessen Ihren wohlverdienten freien Tag.

Wie bekomme ich mein Guthaben aus der Nebenkostenabrechnung?

Sofern Sie uns ein SEPA-Lastschriftmandat erteilt haben, verrechnen wir das Guthaben automatisch mit der nächsten Mietzahlung. Andernfalls bitten wir Sie, das Guthaben selbstständig mit der nächsten Mietzahlung zu verrechnen.

Nähere Information zur Verrechnung des Guthabens finden Sie auf Ihrer Nebenkostenabrechnung.

Wie erfolgt die Umlage der Betriebs- und Heizkosten?

Für die Verteilung der Betriebskosten gibt es unterschiedliche Umlageschlüssel, wie z. B. die Wohnfläche, den Verbrauch oder die Personenanzahl. Welcher Umlageschlüssel zum Tragen kommt, ist mit Ihnen mietvertraglich vereinbart.

Heizkosten werden sowohl nach dem Verbrauch des einzelnen Mieters als auch nach der Heizfläche verteilt. Die Abrechnung der Heizkosten erfolgt mindestens zu 50 % und höchstens zu 70 % nach dem individuell erfassten Wärmeverbrauch. Die verbleibenden Kosten werden im Verhältnis der beheizbaren Wohnflächen abgerechnet. Diese bezeichnet man als Grundkosten.

Kann ich Um-/Einbauten in meinem Mietobjekt vornehmen?

Es ist Ihr Zuhause, in dem Sie sich wohl fühlen sollen. Trotzdem sind Um-/Einbauten grundsätzlich nur gestattet, wenn sie die Bausubstanz des Mietobjektes nicht verändern.

Sie haben das Recht, Einrichtungen und Ausstattungsgegenstände nach eigenem Belieben zum Wohngebrauch anzubringen oder einzubauen. Dazu gehören u. a. das Anbringen von Wandschränken oder Dekorationsfolien an Türen.

Für Um-/Einbauten, welche in die Bausubstanz eingreifen, benötigen Sie vorher eine schriftliche Genehmigung von uns. Die Ausführung der Arbeiten ist durch Sie oder eine von Ihnen beauftragte Fachfirma auf Ihre Kosten auszuführen. Sofern in der Genehmigung nichts anderes vereinbart wurde, müssen Sie das Mietobjekt bei einem Auszug auf eigene Kosten in den ursprünglichen Zustand zurückversetzen.

Bitte beachten Sie: Wir tragen als Vermieter generell keine Gefahr für Um-/Einbauten, welche durch Sie ausgeführt oder beauftragt wurden. Daher empfehlen wir Ihnen, Ihre Hausratversicherung für den Fall eines Schadens in der Versicherungssumme anpassen zu lassen. In der Versicherung, die wir für unsere Gebäude abschließen, sind derartige Schäden nicht abgedeckt.

Gern können Sie eine Genehmigung über unsere Kunden-App „Mein Vonovia“ bei uns anfragen.

Welche Vorschriften gibt es beim Thema Tierhaltung?

Wenn es sich bei Ihrem Haustier um ein Kleintier handelt, benötigen Sie keine Genehmigung von uns als Vermieter. Als Kleintiere gelten Wellensittiche, Hamster, Kaninchen, Meerschweinchen, Rennmäuse oder Zierfische.

Hunde und Katzen zählen nicht zu den Kleintieren – für sie benötigen Sie unsere Genehmigung. Die Erteilung der Genehmigung ist abhängig von der Anzahl der Tiere in Ihrem Haushalt und bei Hunden von deren Rasse. Für ein harmonisches Zusammenleben in Ihrem Wohnhaus ist es auch wichtig, dass es durch den Vierbeiner nicht zu Ruhestörungen oder Belästigungen anderer Mieter kommt. Andernfalls sind wir berechtigt, die Genehmigung zu widerrufen.

Darf ich meine Wohnung untervermieten?

Ob Sie Ihre Wohnung ganz oder teilweise untervermieten dürfen, prüfen wir gern im Einzelfall.

Nutzen Sie für die Anfrage gern unsere Kunden-App „Mein Vonovia“. Im Bereich „Service“ unter „Anträge“ können Sie uns alle benötigten Angaben übermitteln. So haben Sie den Status Ihrer Anfrage in der App auch immer im Blick.

Ich möchte meine Wohnung kündigen – was tun?

Seit 2002 beträgt die gesetzliche Kündigungsfrist drei Monate. Bei älteren Mietverträgen wurden stellenweise individuelle Kündigungsfristen vereinbart oder auch die damals gesetzlich gültigen Fristen ausformuliert – diese gelten in jenen Fällen. Eine Kündigung bedarf der Schriftform und der händischen Unterschrift aller Vertragspartner.

Zudem muss die Kündigung bis zum dritten Werktag eines jeden Monats bei uns eingegangen sein, damit diese dann für den Ablauf des übernächsten Monats wirksam wird (im Falle der gesetzlichen drei Monate Kündigungsfrist). Entscheidend ist dabei das Eingangsdatum bei uns, nicht das Absendedatum oder der Poststempel.

Beispiel: Ihre Kündigung geht am dritten Werktag des Monats April bei uns ein. Das Mietverhältnis endet dann mit Ablauf des 30.06. des betreffenden Jahres.

Wie kann ich meine Kündigungsfrist verkürzen?

Bitte reichen Sie uns Ihre Anfrage zur Verkürzung der Kündigungsfrist immer schriftlich unter Angabe Ihrer Vertragsnummer ein. Wichtig dabei: Alle Vertragspartner, welche die Kündigung unterschrieben haben, müssen auch diese Anfrage unterschreiben. Teilen Sie uns in der Anfrage bitte auch mit, aus welchem Grund Sie die Kündigungsfrist verkürzen möchten.

Wenn Sie bereits einen Interessenten als Nachmieter für die Wohnung haben, können Sie uns gern seine Kontaktdaten mitteilen. Sobald uns Ihre schriftliche Anfrage vorliegt, prüfen wir diese und informieren Sie schnellstmöglich über unsere Entscheidung.

Wie kann ich meine Kündigungsfrist verlängern?

Bitte reichen Sie uns Ihre Anfrage zur Verlängerung der Kündigungsfrist immer schriftlich unter Angabe Ihrer Vertragsnummer ein. Wichtig dabei: Alle Vertragspartner, welche die Kündigung unterschrieben haben, müssen auch diese Anfrage unterschreiben. Teilen Sie uns in der Anfrage bitte auch mit, aus welchem Grund Sie die Kündigungsfrist verlängern möchten. Sobald uns Ihre schriftliche Anfrage vorliegt, prüfen wir diese und informieren Sie schnellstmöglich über unsere Entscheidung.

Wohin mit Möbeln, die nicht mehr gebraucht werden?

Mit großer Wahrscheinlichkeit fällt beim Umzug Sperrmüll an. Wenn Sie sich den Weg zum Wertstoffhof sparen möchten, melden Sie die Abholung bei der Gemeinde an. Wahrscheinlich werden Sie keinen Termin exakt am Umzugstag bekommen – deshalb sind eine akribische Planung und Vorbereitung das A und O. So können Sie schon vorher den Sperrmüll aussortieren.

Bitte stellen Sie Sperrmüll, den Sie zur Abholung angemeldet haben, erst am Vorabend des Abholtermins vor das Haus. Sie sollten zudem darauf achten, dass die Verkehrssicherheit weiter gewährleistet wird und alle Wege frei zugänglich bleiben.

Wo kann ich eine Mietschuldenfreiheitsbescheinigung beantragen?

Sie können sich die Mietschuldenfreiheitsbescheinigung mit wenigen Klicks in unserer Kunden-App „Mein Vonovia“ im Bereich „Service“ unter „Bescheinigung“ herunterladen. Alternativ können Sie unseren telefonischen Kundenservice kontaktieren, dann senden wir Ihnen die Mietschuldenfreiheitsbescheinigung per Post zu. Wichtig dabei: Ihr Mietkonto muss ausgeglichen sein.

Wann bekomme ich meine Kaution zurück?

Generell hat ein Vermieter das Recht die Kaution für eventuell nachträglich auftretende Forderungen bis zu sechs Monate nach Vertragsende einzubehalten. Wir sind jedoch bemüht, Ihnen die Kaution nach der Endabnahme schnellstmöglich auszuzahlen. Dazu prüfen wir u. a., ob Ihr Mietkonto ausgeglichen ist und ob Sie uns die Wohnung im vertragsgemäßen Zustand übergeben haben.

Natürlich muss uns auch Ihre Bankverbindung vorliegen. Sollte dies nicht der Fall sein, fordern unsere Mitarbeiter diese bei Ihnen an. Um einen Zahlendreher zu vermeiden, müssen Sie uns Ihre Bankverbindung immer schriftlich mitteilen.

Wie lüfte ich richtig?

Moderne Wohngebäude sind gut isoliert und lassen kaum Luft nach innen oder außen – das spart Heizkosten. Allerdings bedeutet das auch, dass die Bewohner durch Luftaustausch für ein gutes Wohnklima sorgen müssen – und das wird von zwei Faktoren bestimmt: der Temperatur und der Luftfeuchtigkeit. 

Tipp: in unserem Ratgeber finden Sie weiteres zum Thema Heizen und Lüften.

Wie soll ich den Müll trennen?

Mülltrennung ist sinnvoll, denn: In der Wirtschaft wird der Abfall neu entdeckt – als Rohstoff und Grundstoff für neue Produkte. Wenn Sie also gründlich trennen, schonen Sie unsere Ressourcen und das ist gut für die CO2-Bilanz.

Außerdem kann es passieren, dass das zuständige Entsorgungsunternehmen bei einer Falschbefüllung die Abfalltonnen nicht entleert. Bei einer notwendigen Sonderleerung werden die anfallenden Kosten auf die Mieter umgelegt.

In unserem Flyer finden Sie alle Informationen zur richtigen Mülltrennung auf einen Blick.

Was passiert wenn sich meine Bankverbindung ändert?

Teilen Sie uns schriftlich Ihre neue Bankverbindung mit. Sollten wir bereits mittels SEPA-Lastschriftverfahren von Ihrem Konto einziehen, benötigen wir von Ihnen zudem ein neues SEPA-Mandat.

Muss ich separat jeweils ein SEPA-Mandat für jeden Mietvertrag, den ich besitze unterschreiben/erteilen oder reicht eines aus?

Sofern Sie den Einzug Ihrer Mietzahlungen durch uns wünschen, ist für jeden einzelnen Vertrag, wie bspw. Wohnungsmietvertrag, Garagenmietvertrag etc., jeweils ein SEPA-Lastschriftmandat zu erteilen.

Kann ich meine fällige Miete auch zur Mitte oder zum Ende des Monats bezahlen?

Die Fälligkeit Ihrer Miete kann auf den 15. eines Monats umgestellt werden, wenn Sie dies wünschen. Die Zahlung zum Ende eines Monats ist nicht möglich.

Was passiert, wenn sich der Hauptmieter ändert – bleibt alles gleich oder muss ich noch etwas beachten?

Der Mietvertrag wurde auf Sie als neuen Hauptmieter umgeschrieben? Wenn Sie den Einzug der Miete durch uns wünschen, benötigen wir ein neues SEPA-Mandat von Ihnen. Auch hier gilt: Bitte für jeden einzelnen Vertrag separat. Wenn Sie die Miete lieber per Dauerauftrag zahlen, bitten wir um Berücksichtigung der jeweiligen Bankverbindungen pro Vertrag, da jeder Vertrag bei uns eine eigene Bankverbindung besitzt.

Mit Übernahme des Mietvertrages sind Sie für die reibungslose Führung des Mietkontos verantwortlich. Sie haften für evtl. Forderungen aus nicht gezahlten Mieten oder Vorauszahlungen. 

Unser Hauptmieter ist verstorben und Sie möchten als Erbe das Nebenkostenguthaben sowie etwaige Guthaben ausgezahlt bekommen? Bitte lassen Sie uns einen entsprechenden Erbnachweis wie bspw. einen Erbschein, Testament oder Vorsorgevollmacht über den Tod hinaus zukommen und teilen uns schriftlich eine gültige Bankverbindung mit. Die Auszahlung wird geprüft und ggf. direkt veranlasst.

Kann ich Mietnachforderungen auch in Raten zahlen?

Wir prüfen gerne die Möglichkeit einer Zahlung in Raten. Die Ratenzahlung können Sie über unsere Kunden-App „Mein Vonovia“ selbstständig festlegen oder telefonisch über den Kundenservice vereinbaren.

Wann bekomme ich meine Kaution zurück?

Generell hat ein Vermieter das Recht, die Kaution für eventuell nachträglich auftretende Forderungen bis zu sechs Monate nach Vertragsende einzubehalten. Wir sind jedoch bemüht, Ihnen die Kaution nach der Endabnahme schnellstmöglich auszuzahlen. Dazu prüfen wir u. a., ob Ihr Mietkonto ausgeglichen ist und ob Sie uns die Wohnung im vertragsgemäßen Zustand übergeben haben. Natürlich muss uns auch Ihre Bankverbindung vorliegen. Sollte dies nicht der Fall sein, fordern unsere Mitarbeiter diese bei Ihnen an. Um einen Zahlendreher zu vermeiden, müssen Sie uns Ihre Bankverbindung immer schriftlich mitteilen.

Wann ist eine Mietanpassung vom Vermieter möglich?

Generell können wir als Vermieter die Zustimmung zur Mietanpassung bis zur ortsüblichen Vergleichsmiete von unseren Kunden fordern. Folgende zwei Voraussetzungen müssen dabei eingehalten werden:

Die Grundmiete muss zum Zeitpunkt, ab dem die Erhöhung eintreten soll, seit 15 Monaten unverändert sein.
Unser Verlangen zur Mietanpassung kann frühestens ein Jahr nach der letzten Mieterhöhung geltend gemacht werden.
Was ist eine Mietbescheinigung und wie kann ich diese beantragen?

Auf der Mietbescheinigung werden u. a. die Größe der Wohnung und die Höhe der Miete vermerkt.

Sie können sich die Mietbescheinigung mit wenigen Klicks in unserer Kunden-App „Mein Vonovia“ im Bereich „Service“ unter „Bescheinigung“ anfordern. Alternativ können Sie unseren telefonischen Kundenservice kontaktieren, dann senden wir Ihnen die Mietbescheinigung per Post zu.

Kann ich meine Vorauszahlungen ändern?

Sie können Ihre Vorauszahlung für die Nebenkosten mit wenigen Klicks in unserer Kunden-App „Mein Vonovia“ im Bereich „Verträge“ unter „Meine Nebenkosten“ anpassen. Alternativ können Sie unseren telefonischen Kundenservice kontaktieren, dann passen wir Ihre Vorauszahlung gern an.

Was sind Betriebs-/Nebenkosten?

Betriebskosten sind die Kosten, die dem Eigentümer laufend entstehen. Alle Mieter zahlen monatliche Vorauszahlungen. Diese werden einmal jährlich mit den tatsächlich entstandenen Kosten gegengerechnet. Die Umlage der Kosten ist mietvertraglich vereinbart.

Eine Auflistung der Nebenkosten finden Sie in Ihren Vertragsunterlagen.
Tipp: In unserem Ratgeber finden Sie nützliche Informationen rund um die Nebenkostenabrechnung.

Wann kommt die Nebenkostenabrechnung?

Die Nebenkostenabrechnung muss Ihnen spätestens zwölf Monate nach Ende des Abrechnungszeitraumes zugegangen sein. Wir arbeiten stetig daran, die Abrechnung schnellstmöglich zu erstellen.

Erhöhung der Vorauszahlung trotz Gutschrift?

Sie erhalten in der Abrechnung eine Gutschrift. Aus welchem Grund kann sich die neue monatliche Vorauszahlung trotzdem erhöhen?

Es handelt sich um abgerechnete Kosten aus dem Vorjahr. Zwischenzeitliche Kostensteigerungen rechtfertigen eine höhere Vorauszahlung auch dann, wenn aus der aktuellen Abrechnung eine Gutschrift resultiert. Um Sie vor eventuellen Nachforderungen zu schützen, passen wir die Vorauszahlung entsprechend an.

Wie erfolgt eine Teilkündigung meiner Wohnung?

Ein oder mehrere Mieter sollen aus dem Mietvertrag entlassen werden, das Mietverhältnis soll aber grundsätzlich mit den restlichen Mietern fortgesetzt werden? Gern prüfen wir Ihren Wunsch.

Nutzen Sie für die Anfrage gern unsere Kunden-App „Mein Vonovia“. Im Bereich „Service“ unter „Anträge“ können Sie uns alle benötigten Angaben übermitteln.

Was mache ich bei Ärger mit meinem Nachbarn?

Eine Mieterin ist verärgert, weil ihr Nachbar jede Nacht duscht. Doch der ist Koch, muss sich spät abends nach der Arbeit duschen und merkt gar nicht, dass er seine Nachbarin dadurch stört.

Solche oder ähnliche Fälle werden uns als Vermieter gemeldet. Wir wünschen uns ein harmonisches Miteinander für unsere Mieter, können oft jedoch nur bedingt helfen – Duschen zum Beispiel ist gesetzlich rund um die Uhr erlaubt. Daher unsere Bitte an Sie als Mieter: Wenn Sie sich von Ihren Nachbarn gestört fühlen, suchen Sie das Gespräch miteinander. Legen Sie Ihr Problem ruhig und sachlich dar und finden Sie gemeinsam eine Lösung. Falls die Störungen andauern oder ein Gespräch untereinander nicht möglich ist, können Sie sich natürlich gern an uns wenden.

Im Falle einer Lärmbeschwerde ist es wichtig, dass Sie ein detailliertes Lärmprotokoll führen und uns mit einreichen. Nutzen Sie für die Übermittlung des Lärmprotokolls gern unsere Kunden-App „Mein Vonovia“. Im Bereich „Service“ unter „Beschwerde“ können Sie uns alle benötigten Angaben übermitteln.

Wie kann ich eine Beschwerde melden?

Sie sind unzufrieden mit der Durchführung der Hausreinigung oder der Grünflächenpflege im Wohnumfeld?

Es gibt viele Anliegen, die direkt telefonisch erledigt werden können. Bitte wenden Sie sich bei Beschwerden jedoch – vor allem aus rechtlichen Gründen – immer schriftlich an uns.

Wie kann ich eine Reparatur melden?

Nutzen Sie für die Meldung einer Reparatur gern unsere Kunden-App „Mein Vonovia“ . Im Bereich „Service“ unter „Reparatur“ können Sie uns alle benötigten Angaben übermitteln. So haben Sie den Status Ihrer Reparatur in der App auch immer im Blick.

Endabnahme/Schlüsselübergabe: Was muss ich beachten?

Den Termin zur Endabnahme vereinbaren Sie mit unserem Mitarbeiter bei der Vorabnahme. Während der Vorabnahme stimmen Sie auch mit unserem Mitarbeiter ab, ob und wenn ja welche Arbeiten Sie bis zur Endabnahme noch ausführen müssen. Zur Endabnahme geben Sie die Wohnung und alle ausgehändigten Schlüssel offiziell an uns zurück.

Wenn Sie den Termin selbst nicht wahrnehmen können, dürfen Sie sich durch eine von Ihnen bevollmächtige Person vertreten lassen. Bitte teilen Sie uns im Vorfeld die Kontaktdaten der Person mit, damit wir uns mit dieser in Verbindung setzten können.

Sie können mit uns auch gern einen Endabnahmetermin vor Vertragsende abstimmen. Bitte beachten Sie, dass Sie trotzdem zur Zahlung der Miete bis zum Vertragsende verpflichtet sind.

Sofern Sie wissen, wer Ihr Nachmieter ist, übergeben Sie die Schlüssel nicht eigenständig an diesen. Übergeben Sie die Schlüssel bei der Endabnahme an unseren Mitarbeiter. Dieser protokolliert die Übergabe ordnungsgemäß und organisiert die Übergabe der Schlüssel an den neuen Mieter. Sollten Sie die Schlüssel selbstständig an den Nachmieter übergeben, stehen Sie weiter in der Haftung, auch wenn Sie gar nicht mehr im Besitz der Wohnung sind.

Was ist, wenn ich noch einen Stellplatz oder einen Garten angemietet habe?

Bitte kündigen Sie – falls bei uns gemietet – mit einem separaten Schreiben die Garage bzw. den Einstellplatz oder den Garten.

Was ist, wenn ich einen Kabelanschluss gemietet habe?

Alle Verträge für den Kabelanschluss, welche Sie selbstständig abgeschlossen haben, müssen Sie separat beim Kabelanbieter kündigen. Beachten Sie dabei bitte die Kündigungsfristen Ihres Anbieters. Sollte der Kabelanschluss Bestandteil Ihres Mietvertrages sein und nicht separat von Ihnen abgeschlossen worden sein, wird er mit Kündigung des Mietvertrages automatisch gekündigt.

Wann melde ich Strom und Gas ab?

Teilen Sie den jeweiligen Versorgern für Strom und Gas mit, dass Sie umziehen. Wenn die Versorgung am neuen Wohnort möglich ist, melden Sie lediglich die neue Adresse. Häufig lohnt sich jedoch auch ein Wechsel des Versorgers: Vergleichen Sie in jedem Fall die Angebote.

Notieren oder fotografieren Sie bei der Endabnahme der Wohnung in jedem Fall die Zählerstände von Strom und Gas, um Sie anschließend Ihrem Versorger melden zu können. Sie haben nichts zum Notieren bei der Hand? Die Zählerstände werden auch noch einmal auf dem Endabnahmeprotokoll vermerkt.

Was kann ich tun, wenn ich Schädlinge feststelle?

Sollten Sie feststellen, dass in Ihrer Wohnung oder in der Wohnanlage vermehrt Insekten oder Schädlinge – z. B. Ratten oder Wespen – auftreten, informieren Sie bitte Ihren Objektbetreuer oder unseren telefonischen Kundenservice. Je genauer Ihre Angaben sind, desto besser kann sich der von uns beauftragte Schädlingsbekämpfer vorbereiten.

Wie kann ich meine Daten ändern?

Gern können Sie Ihre persönlichen Daten in unserer Kunden-App „Mein Vonovia“ anpassen. Folgende Daten können Sie einsehen und ändern:

Namen
Anschrift
Telefonische Kontaktdaten
Bevorzugte Kontaktzeiten
E-Mail-Adresse
Bankverbindung (nur in Verbindung mit einem SEPA-Lastschriftmandat)
Alternativ können Sie uns die Änderung Ihrer Daten auch gern per E-Mail oder Post mitteilen. Bitte beachten Sie, dass wir für die Änderung Ihres Namens ein amtliches Dokument benötigen.

Wie erhalte ich eine Kopie meines Mietvertrages?

Sie können sich eine Kopie Ihres Mietvertrages schnell und einfach in unserer Kunden-App „Mein Vonovia“ herunterladen.

Alternativ können Sie unseren telefonischen Kundenservice kontaktieren, dann senden wir Ihnen eine Kopie per E-Mail oder Post zu.
            """}],
    )


@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
