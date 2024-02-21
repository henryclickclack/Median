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
  elif (username, password) == ("Median", "#Median2024!"):
    return cl.User(identifier="user", metadata={"role": "user", "provider": "credentials"})
  else:
    return None

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [
           {"role": "system", "content": """You are a helpful FAQ assistant for the german clinic company Median . You have access to the entire FAQ. Answer only with information from the FAQ. If you cant anwser a question, just say 'I dont know'. Answer short and consise. Only add to your answer what is relevant to the question. Not more!!
            Das ist die Telefonnummer: +49305300550 
            Das ist die Anschrift: MEDIAN Unternehmensgruppe B.V. & Co. KG Franklinstraße 28-29 10587 Berlin
            Das ist die E-Mail: info@median-kliniken.de
            FAQ Mediangruppe - Fragen zu Reha nach Corona
Das ist die Organisational Chart:
Group CFO: Philipp Schulte-Noelle (interim)
Group ControllingN.N.
Operatives Controlling: Sebastian Falk
Group Controlling: Hannes Endler
Leitung Group Projekte: Dr. Bettina Knop
Group SAP BI: Matthias Schneider
HR Shared Services: Anika Dicke
Group Finance Director: Henri RitschelKonzernrechnungswesen: Arno Tecklenborg
Financial Center: Ralf Nicklaus
Group Treasury: René Kahl
Group M&A: Ruta Hildebrand
Recht und Compliance: Elke Fromm
CEO MEDIAN: Dr. Marc Baenkler
Leitung HR: Maik SteudeRecruiting: Namuna Mandakhbileg
MEDIAN Akademie: Anke Peters
Strategische Projekte: N.N.
Projektmanagement Akut-Kliniken: Frank Teufel
Group COO: Philipp Schulte-Noelle
Group IT: Dr. Kai OeySAP: Ansgar Niestradt
ATOSS: Sabine Widera
KIS: Angela Eisehuer
IT Service Management: Christian Kagel
Field Service: Martin Dzienus
Digitale Gesundheit: Judith Dittmer
Marketing und Kommunikation: Arndt Hellmann
GB Services (Group): Jens KnoblichEinkauf: Christian Schröder
Catering: Luigi Magri
Dienstleistungen: Lisa Wellmann
Bau und FM: Andreas Hild
FM: René Naie
Medizinische Qualität: Ulrich Kräutter
Group Forschung und Innovation: Dr. Laura Golenia
GB Mitte: Andreas Finkel (interim)
GB Nord-Ost: Sebastian Bergholz
GB Ost: Dieter Stocker
GB Nord-West: Lars Vorsthoven
GB Süd-West: Andreas Wirth
GB Soziotherapie: Anja Cappeller
Medizinische Rehabilitation nach einer Covid-19-Erkrankung
Nach bisherigen Erkenntnissen überstehen die meisten Menschen eine Covid-19-Erkrankung relativ unbeschadet. Die Folgeschäden können jedoch bei einem relativ schweren Verlauf gravierend sein und nachhaltend die körperliche Leistungsfähigkeit negativ beeinträchtigen. Für Patienten, die im Zuge ihrer Covid-19 Erkrankung eine schwere Lungenentzündung erlitten haben und dabei langzeitbeatmet wurden und/oder ein Lungenversagen (ARDS) stattfand, empfiehlt sich im Anschluss eine spezielle pneumologische Rehabilitation. Im Vordergrund des Reha-Aufenthaltes steht dabei die Wiederherstellung der deutlich reduzierten Lungenfunktion. Der Verlauf einer Covid-19-Erkrankung muss jedoch nicht immer mit einer künstlichen Beatmung oder Lungenversagen einhergegangen sein, um eine Rehaklinik nach Corona sinnvoll zu machen. Schwere Covid-19-Verläufe können den Körper stark schwächen und die Belastbarkeit der Lunge und Atemmuskelkraft auch nach überstandener Erkrankung stark einschränken. Für diese Fälle bieten einige unserer MEDIAN Kliniken interdisziplinäre Post-Corona-Rehabilitationen an, um gebliebene Beeinträchtigungen zu verbessern.
Nicht zu unterschätzen sind darüber hinaus sämtliche Covid-19 assoziierten psychischen Folgestörungen wie Depressionen durch Verlust von Angehörigen, Angst- oder Zwangsstörungen. Eine spezielle psychosomatische Reha-Behandlung nach Covid-19 unterstützt dabei nicht nur Personen der Allgemeinbevölkerung sondern ebenso medizinisches Personal, das aufgrund hoher Belastungen im Gesundheitssektor unter Erschöpfungsdepressionen oder Traumafolgestörungen leidet. Psychische Folgestörungen aufgrund von Corona können sich jedoch genauso in Form von Abhängigkeitsverhalten äußern. Immer mehr Menschen entwickeln durch mangelnde soziale Unterstützung, Arbeitsplatzverluste, Existenzängste oder zuvor genannte psychische Belastungen Suchtverhalten wie Alkohol- oder Medikamentenabhängigkeiten. Dieses Suchtverhalten kann sich gleichermaßen auf den krankhaften PC-Internetgebrauch oder Glücksspiele beziehen. Spezifische Sucht-Post-Corona-Rehabilitationen helfen Patienten dabei, unterschiedliche mit Covid-19 assoziierte Abhängigkeiten zu bewältigen.
Die Rehabilitationsmaßnahmen für Langzeitfolgen im Zusammenhang mit dem Covid-19-Virus sind sehr unterschiedlich. Für alle Rehabilitanden der MEDIAN Kliniken wird aufgrund der unterschiedlichen persönlichen Krankheitsverläufe und Auswirkungen einer Covid-19-Erkrankung ein patientenindividueller Behandlungsplan zusammengestellt. Dieser ermöglicht eine auf den einzelnen Patienten abgestimmte Therapie durch unsere speziell geschulten, behandelnden Ärzte und Therapeuten als auch die betreuenden Pflegekräfte. Primäres Ziel ist dabei stets die Verbesserung des körperlichen und seelischen Gesamtzustandes unserer Patienten.

BEHANDLUNGSKONZEPTE
Voraussetzungen für eine Reha nach Corona
Abhängig vom jeweiligen Covid-19 Rehabilitationsangebot sind unterschiedliche Voraussetzungen nötig, damit unsere Rehakliniken Sie für die Behandlung nach einer Corona-Erkrankung aufnehmen können. Erfahren Sie mehr über die einzelnen Voraussetzungen und ab welchem Zeitpunkt eine Corona Rehabilitation in einer unserer MEDIAN Kliniken möglich ist unter den Informationsseiten der jeweiligen Behandlung nach Covid-19:
Behandlungsablauf einer Post-Corona-Reha
Die Covid-19-Therapiekonzepte der MEDIAN Kliniken wurden speziell für die individuellen Bedürfnisse unserer Patienten entwickelt, welche unter den körperlichen und/oder psychischen Belastungen einer Corona-Erkrankung leiden. Innerhalb des Reha-Aufenthaltes kommen dabei je nach Zielsetzung z.B. Atemmuskeltraining, Kraft- und Ausdauertraining, Atemphysiotherapie, als auch Covid-19 bezogene Gruppen- und Einzeltherapien sowie kreativtherapeutische Verfahren zum Einsatz.
Reha nach Corona beantragen
Die Reha nach Corona unterscheidet sich in der Beantragung nicht von anderen Rehabilitationsmaßnahmen. Ist die Covid-19 Erkrankung überstanden und der Reha-Anspruch geklärt, sind es nur wenige Schritte bis zum Beginn einer Reha. Hier finden Sie den Musterantrag der Gesetzlichen Krankenversicherung für die Rehabilitation nach Covid-19-Erkrankung.
REHA NACH CORONA
Spezifische Sucht-Post-Corona-Rehabilitation
Die aktuelle Corona-Pandemie birgt neben dem Risiko an Covid-19 zu erkranken auch die Verstärkung von Einsamkeit und Langeweile sowie die Entstehung von Ängsten. Mangelnde Ablenkung, mangelnde berufliche Verpflichtungen, mangelnde soziale Unterstützung, sowie die zuvor erwähnten …
Covid-19 assoziierte Suchterkrankungen
Die aktuelle Corona-Pandemie birgt neben dem Risiko an Covid-19 zu erkranken auch die Verstärkung von Einsamkeit und Langeweile sowie die Entstehung von Ängsten. Mangelnde Ablenkung, mangelnde berufliche Verpflichtungen, mangelnde soziale Unterstützung, sowie die zuvor erwähnten psychischen Belastungen können den Suchtmittelkonsum fördern und Abhängigkeitserkrankungen verursachen. Ziele der Suchtrehabilitation in der Rehaklinik nach Corona sind je nach Art der Erkrankung z.B. Suchtmittelabstinenz oder der Verzicht auf den pathologischen PC-Internetgebrauch und pathologisches Glücksspielen. Die Dauer der Suchtrehabilitation beträgt je nach Abhängigkeitserkrankung zwischen 12 und 15 Wochen.
Welche Abhängigkeitserkrankungen können im Rahmen der Suchtrehabilitation nach Corona behandelt werden?
Im Rahmen der Sucht-Post-Corona-Reha werden Abhängigkeitserkrankungen wie Alkoholabhängigkeit, Medikamentenabhängigkeit, Drogenabhängigkeit, Glücksspielsucht sowie PC- und Internetsucht behandelt, die im Zusammenhang mit der Covid-19-Pandemie entstanden oder schwerwiegender geworden sind. 
Welche Kriterien kennzeichnen eine Alkoholabhängigkeit nach Covid-19?
Nicht jedes regelmäßige oder riskante Trinkverhalten deutet auf eine Alkoholabhängigkeit hin. Dennoch gibt es verschiedene Kennzeichen, anhand denen man eine Alkoholabhängigkeit feststellen kann. Dazu zählen Wirkungsverminderung bei gleicher Trinkmenge, die Vernachlässigung von Interessen und Verpflichtungen sowie die Akzeptanz einer Selbstschädigung durch den Alkoholkonsum. Insbesondere bei sehr starkem Trinken sowie dem Versuch, den Alkoholkonsum zu verheimlichen, liegt vermutlich eine Alkoholproblematik vor.
Durch die Umstände der Covid-19-Pandemie oder durch eine Corona-Infektion können Rückfälle nach vorangehender Suchtmittelabstinenz gefördert werden. Auch ist es möglich, dass der Griff zur Flasche aufgrund des vermehrten Aufenthaltes zu Hause, verringertem sozialen Kontakt und Ängsten in Bezug auf die Pandemie als Ausweg aus Langeweile oder emotionaler Belastung gesehen wird. Im Mittelpunkt der Therapie steht daher neben der Erlangung einer Alkoholabstinenz das Erlernen von Bewältigungsstrategien, um Ängste und Sorgen, die mit der Covid-19-Pandemie assoziiert sind, ohne Alkoholkonsum verarbeiten werden können. 
Häufig entwickelt sich aus dem gewohnheitsmäßigen Konsum von Alkohol insbesondere im Zusammenhang mit psychischen Belastungen eine ernste Alkoholsucht: Die Alkoholabhängigkeit ist die häufigste Suchterkrankung in Deutschland, ungefähr 1,7 Millionen Bundesbürger leiden daran. Hier erfahren Sie mehr über Symptome, Folgen und Ursachen einer Alkoholabhängigkeit und deren Behandlung.
Welche Folgen hat die Alkoholsucht?
Ein schädlicher Gebrauch liegt vor, wenn trotz gesundheitlicher Schäden der Alkoholkonsum fortgesetzt wird.
Gesundheitliche Schäden auf körperlichem Gebiet sind: Lebererkrankungen, Herz-Kreislauf-Erkrankungen, Krebserkrankungen, Erkrankungen des Magen-Darmtraktes, Erkrankungen des Gehirns und des Nervengewebes, der Haut und anderer Organe.
Ebenso können psychische Störungen wie depressive Erkrankungen, Konzentrationsstörungen, Gedächtnisstörungen usw. auftreten.
Das Risiko für entsprechende Erkrankungen erhöht sich bereits deutlich bei einem täglichen Konsum von 15 bis 20 Gramm bei der Frau und etwa 30 bis 40 Gramm Alkohol pro Tag beim Mann.
Die Fakten sind eindeutig: Schon eine Flasche Bier enthält 20 Gramm Reinalkohol.
Auch ohne Vorliegen einer Alkoholabhängigkeit gilt: Bereits mehr als 24 Gramm Reinalkohol bei Männern und über zwölf Gramm bei Frauen täglich – z.B. ein bis zwei Flaschen Bier – können Gesundheitsschäden verursachen. Weiterer Konsum kann bei Alkoholabhängigkeit schwerwiegende Auswirkungen haben.
Körperliche Folgen von Alkoholabhängigkeit sind u.a.:
    • Erkrankungen der Leber und Verdauungsorgane
    • Schädigungen von Herz und Kreislauf
    • Beeinträchtigung von Gehirn und Nervengewebe
    • Erhöhung des Krebsrisikos
Seelische Folgen von Alkoholabhängigkeit sind u.a.:
    • Depressive Erkrankungen
    • Konzentrationsstörungen
    • Gedächtnisstörungen
Welche Ursachen hat Alkoholismus?
Alkoholabhängigkeit hat keine einzelne Ursache, sondern entsteht immer aus dem Zusammenwirken verschiedener Faktoren (psychisch, sozial, körperlich). Gefährdet sind unter anderem Personen, die:
    • Positiv auf Alkohol reagieren, ohne negative körperliche Folgen zu spüren
    • Bei seelischen Belastungen (s.a. Traumafolgestörung) über Suchtmittel Entspannung suchen
    • Im Umfeld von Alkoholherstellung und -vertrieb arbeiten
    • Durch Alkoholismus in der Herkunftsfamilie vorbelastet sind
    • Alkoholsucht im sozialen Umfeld erfahren
Auch die Lernerfahrungen in Kindheit und Jugend sowie spätere kritische Lebensereignisse können einen Beitrag zur Entwicklung einer Abhängigkeitserkrankung leisten.
Wie wird Alkoholabhängigkeit behandelt?
Sobald sich von Alkoholismus Betroffene entschließen, in ein Leben ohne Alkoholsucht zu starten, bestehen gute Aussichten auf Erfolg. Eine Alkoholismus-Therapie teilt sich üblicherweise in zwei Phasen:
    • Die Entgiftung dauert bei Alkoholismus i.d.R. sieben bis 14 Tage und bildet die Basis für die Entwöhnung von der Alkoholsucht.
(Die Entgiftung ist der medizinisch begleitete körperliche Entzug vom Alkohol. Sie findet für die Dauer von etwa sieben bis 14 Tagen in einem Krankenhaus vor der Entwöhnungsbehandlung statt. Die Kosten werden in der Regel von der Krankenkasse übernommen. Die Einweisung erfolgt durch den Hausarzt.)
In einigen MEDIAN Kliniken für Abhängigkeitserkrankungen kann auch eine Entgiftung vor Ort durchgeführt werden. So z.B. in der MEDIAN Klinik Lübeck für Drogenabhängige und in den Kliniken Daun, wenn die DRV Knappschaft-Bahn-See Kostenträger ist.
Die mehrmonatige Entwöhnung hat das Ziel, den von Alkoholabhängigkeit Betroffenen dauerhaft von seiner Alkoholsucht zu lösen.
    • Die Entwöhnung ist die Behandlung der automatisierten Verhaltensmuster und -gewohnheiten, die immer wieder zu Rückfällen führen. Sie kann ambulant in einer Beratungsstelle, ganztägig ambulant in einer Tagesklinik oder stationär in einer Fachklinik durchgeführt werden. Für die Kosten kommt der Rentenversicherer auf, weil sie eine sogenannte medizinische Rehabilitationsbehandlung ist. Nur wenn der Rentenversicherer nicht zuständig ist, zahlt die Krankenkasse. Die Behandlung muss daher beantragt werden.
    • Bei der ambulanten Behandlung geht der/die Patient/in über mehrere Monate einmal oder mehrfach wöchentlich heimatnah zu einer vom Rentenversicherer anerkannten Behandlungsstätte. Bei der ganztägig ambulanten Behandlung findet die Therapie in der Regel von Montag bis Samstagmittag in einer Tagesklinik statt. Die Abende und am Wochenende ist der/die Patient/in zu Hause.
    • Bei der häufigeren stationären Entwöhnung wird der/die Patient/in für die Dauer von drei bis vier Monaten in einer Fachklinik behandelt. Es gibt auch Kurzzeittherapien von ca. acht Wochen und Kombi-Behandlungen mit sechs Wochen stationärer Dauer und anschließend sechs Monaten ambulanter Weiterbehandlung.
    • Der Schwerpunkt der Behandlung liegt zum einen in der Gruppentherapie, ergänzt durch indikative Gruppen, Einzeltherapien, Sport- und Bewegungsangeboten, Ergotherapie, und zum anderen in Bausteinen wie der möglichen Einbeziehung von Angehörigen. Bei besonderen Problemen wie Arbeitslosigkeit, Wohnungslosigkeit oder sozialer Desintegration kann eine Adaptionsbehandlung wichtig sein, die von der Fachklinik bei erhöhter Rückfallgefährdung eingeleitet wird.
    • Ziel der Behandlung ist die Abstinenz. In der Therapie wird das Wissen um die Erkrankung, deren Ursachen und die Möglichkeiten eines suchtmittelfreien Lebens vermittelt. Wichtig ist dabei das Verhalten in Familie, Partnerschaft, Beruf und Arbeit, in Freizeit und anderen Lebensbereichen sowie das Vermeiden eines Rückfalles.
    • Grundlage jeder Entwöhnungsbehandlung ist die Akzeptanz der Suchterkrankung und der freiwillige Entschluss, sein Leben suchtmittelfrei führen zu wollen.
    • Um zwischen diesen Phasen Rückfälle zu vermeiden, wurde von Alkoholismus-Experten der MEDIAN Kliniken Daun ein neuartiges Therapiekonzept entwickelt: ISBA, die Integrierte stationäre Behandlung Abhängigkeitskranker. Nach dem Alkoholentzug folgt unmittelbar die Entwöhnungsphase in derselben Einrichtung. Patienten können ohne Zwangspausen während der Alkoholismus-Therapie reibungsloser in ein suchtfreies Leben zurück.

Wie erkennt man Medikamentenmissbrauch assoziiert mit Covid-19?
Die Covid-19-Pandemie befördert Ängste unterschiedlicher Art: Sorgen bezüglich einer Ansteckung, der Gesundheit von nahestehenden Personen, Arbeitsverlust oder Freundschaftsauflösung. Diese Ängste können wiederum zu Schlafstörungen führen, weswegen manche Personen zu Beruhigungs- oder Schlafmittel greifen oder Antidepressiva zur besseren Kontrolle von seelischen Belastungen einnehmen. Werden diese Medikamente für eine längere Zeit eingenommen, besteht die Gefahr einer Suchtentwicklung. Da sich Tablettensucht häufig im Bereich einer Niedrigdosisabhängigkeit bewegt, kann die Grenze zwischen medizinischer Einnahme und Tablettensucht verschwimmen. Medikamentenmissbrauch liegt vor, wenn die Medikamente länger als verordnet oder in größerem Umfang ans verordnet eingenommen werden, jedoch (noch) keine Suchterkrankung vorliegt. Von einer Medikamentenabhängigkeit spricht man, wenn die Medikamenteneinnahme zur Beeinflussung des eigenen Wohlbefindens erfolgt, ohne dass erkennbare
Schätzungen zufolge sind rund 1,9 Mio. Menschen in Deutschland von Medikamentenmissbrauch bzw. einer Medikamentenabhängigkeit (Tablettensucht)  betroffen. Auslöser für einen Medikamentenmissbrauch sind meist schmerzhafte Krankheiten oder schwere seelische Belastungen (s.a. Traumafolgestörung). Denn besonders bei Schmerz-, Schlaf- oder Beruhigungsmitteln ist der Weg von der regelmäßigen Einnahme bis zur Tablettensucht nicht weit. Das gilt auch für Antidepressiva, Neuroleptika oder Medikamente zur Gewichtsreduktion. Hier erfahren Sie mehr über Symptome, Folgen und Therapiemöglichkeiten.
Wie erkenne ich Medikamentenabhängigkeit (Tablettensucht) bzw. Medikamentenmissbrauch?
Die Diagnose einer Tablettensucht ist schwierig. Oft bewegt sich der Medikamentenmissbrauch im Rahmen der sogenannten Niedrigdosisabhängigkeit. Darüber hinaus sind von Medikamentenabhängigkeit Betroffene vergleichsweise unauffällig und sozial integriert.
Man spricht von Medikamentenmissbrauch, wenn Arzneimittel ohne erkennbare Beschwerden zur Beeinflussung des eigenen Wohlbefindens eingesetzt werden. Typische Hinweise auf eine Medikamentenabhängigkeit sind:
    • Dosissteigerung: Medikamente werden bei Tablettensucht länger oder in größeren Mengen eingenommen als eigentlich verordnet oder beabsichtigt
    • Fixierung: Das Leben dreht sich ausschließlich um den  Medikamentenmissbrauch. Reduktion oder Beendigung der Tabletteneinnahme sind nicht mehr vorstellbar
    • Indikationserweiterung: Medikamente werden bei Tablettensucht nicht bestimmungsgemäß eingenommen, Schlafmittel z.B. tagsüber, um sich zu beruhigen
    • Heimlichkeit: Von Medikamentenabhängigkeit Betroffene lassen sich oft die benötigten Präparate von verschiedenen Ärzten verschreiben oder kaufen sie auf illegalem Weg
Welche Folgen kann Medikamentenmissbrauch haben?
Aufgrund der deutlich erhöhten Unfall- und Sturzgefahr ist Medikamentenmissbrauch mit akuten Risiken verbunden. Vor allem zieht eine Tablettensucht jedoch schwere körperliche und seelische Folgen nach sich.
Mögliche körperliche Folgen von Medikamentenabhängigkeit:
    • Tablettensucht verursacht Gleichgewichts-, Bewegungs-, Konzentrations- und Sprachstörungen
    • Auch verschiedene Organschäden, wie z.B. Magenerkrankungen, Leberschädigungen oder sogar Nierenversagen, können bei Medikamentenmissbrauch auftreten
    • Führt die Medikamentenabhängigkeit zu einer Überdosierung von Schmerzmitteln, kann es zu Atemlähmungen kommen
Mögliche seelische Folgen von Medikamentenabhängigkeit:
    • Tablettensucht verursacht oft Interessenlosigkeit und eine Verflachung der Gefühle
    • Jahrelanger Medikamentenmissbrauch kann zu einer Änderung der Persönlichkeit führen
    • Stimmungsschwankungen, paradoxe Reaktionen, Depressionen und Ängste sind ebenfalls typische Folgen einer Medikamentenabhängigkeit
Welche Formen der Medikamentenabhängigkeit gibt es?
Auch wenn sich die Folgen des Medikamentenmissbrauchs zum Teil ähneln – Tablettensucht ist nicht gleich Tablettensucht. Verbreitete Formen der Medikamentenabhängigkeit sind:
    • Schmerzmittelsucht
    • Schlaf- und Beruhigungsmittelsucht
    • Medikamentenmissbrauch von Antidepressiva und Neuroleptika
    • Medikamentenabhängigkeit bei Mitteln zur Gewichtsreduktion
Schmerzmittelmissbrauch im Sport
Große Intensität oder sogar Verbissenheit bei Hobbysportlern können bis hin zum Schmerzmittelmissbrauch führen. Die Leistungserbringung und stetige -verbesserung stehen oft im Vordergrund und das Problembewusstsein ist häufig nicht vertreten. Der Körper wird dann mitunter wie ein Gerät betrachtet, dessen Funktionseinbußen man mit Medikamenten in den Griff zu bekommen versucht. Wenn Sportler allerdings nur noch mit Schmerzmitteln Sport treiben könnten, um ihren Körper über das hinauszubringen, was er eigentlich leisten kann, müsse ihnen vermittelt werden, die Schmerzen wieder als Warnsignal wahrzunehmen, das nicht überdeckt werden dürfe. Gerade im Breitensport geht es ja darum, lange aktiv sein zu können und nicht um Leistung um jeden Preis.

Dazu sollten Patienten stärker dahingehend befragt werden, wie viel und wie ehrgeizig sie Sport treiben und sie dabei aktiv auf die Einnahme von Schmerzmitteln ansprechen. Allein über die oft diffusen Nebenwirkungen eines übermäßigen Gebrauchs wie Übelkeit, Kopfschmerzen, Durchfall, Schlaflosigkeit oder Magenschmerzen hätten Ärzte kaum eine Chance, diese spezifische Ursache zu ermitteln.
Wo finde ich bei Medikamentenabhängigkeit (Tablettensucht) Hilfe?
Die MEDIAN Kliniken sind auf die qualifizierte Behandlung von Menschen mit Medikamentenabhängigkeit spezialisiert und bietet ein umfassendes Spektrum für die Therapie von Medikamentenmissbrauch und Medikamentenabhängigkeit (Tablettensucht).
Betroffene, die sich von ihrer Tablettensucht lösen und wieder ein unabhängiges Leben ohne Medikamentenmissbrauch führen möchten, finden in den MEDIAN-Kliniken professionelle Hilfe – von der Entwöhnung bis zur Adaptionsbehandlung.
Häufig gestellte Fragen zur Reha bei Medikamentenabhägigkeit:
Wie sieht die Therapie einer Medikamentenabhängigkeit aus?
Die die Therapie einer Medikamentenabhängigkeit bei MEDIAN reicht von der Entwöhnung bis hin zur Adaptationsbehandlung. Die Therapie erzielt das Lösen der Sucht und ein unabhängiges Leben.
Sollte bei einer Medikamentenabhängigkeit eine spezielle Entzugsklinik besucht werden?
Ja, es empfiehlt sich bei einer akuten Medikamentenabhängigkeit eine spezielle Entzugsklinik aufzusuchen für eine bestmögliche Behandlung. Kliniken, die auf Medikamentenabhängigkeit spezialisiert sind, sind zum Beispiel die MEDIAN Gesundheitsdienste Koblenz, die MEDIAN Klinik Tönisstein, die MEDIAN Psychotherapeutische Klinik Bad Liebenwerda oder die MEDIAN Klinik am Waldsee.
Wie überwinde ich eine Tablettensucht?
Um die Tablettensucht zu überwinden, finden Betroffene professionelle Hilfe in Form von Entwöhnungstherapien und/ oder Adaptionsbehandlungen.
Wird lange dauert die Behandlung einer Tablettensucht?
Es kann kein genauer Zeitraum für die Behandlung von Tablettensucht angegeben werden, da sehr viele Faktoren bei der Überwindung einer Medikamentensucht eine Rolle spielen.


Welche Kriterien kennzeichnen eine Glückspielsucht nach Covid-19?
Die Möglichkeit, sich bei pathologischem Glücksspiel Beratung und Hilfe zu holen, hat sich während der Pandemie erheblich reduziert. Andererseits haben sich persönliche Probleme, wirtschaftliche Sorgen und Ängste aller Art deutlich vermehrt. Glücksspielen bietet in diesen Fällen die Möglichkeit zur vorübergehenden Ablenkung, auch von Covid-assoziierten traumatischen Erfahrungen. Doch was als Ablenkung vom Alltag, Sorgen und Problemen mit dem Traum vom großen Geld beginnt, kann schnell in Geldnot und Spieldruck, das verlorene Geld wieder zu beschaffen, münden. Der Kick beim Gewinn geringer Geldmengen wird plötzlich von einer Abwärtsspirale des Geldverlusts, Frustration und im Äußersten sogar finanzielle Existenzangst. Damit es nicht so weit kommt, muss Glücksspielsucht frühzeitig erkannt und behandelt werden. Denn die finanziellen Nöte können weitreichende Folgen für Betroffene und deren Angehörige haben, wie Alkohol- und Drogenmissbrauch, Arbeitsplatzverlust, Verschuldung bis hin zu Wohnungsverlust. 
Das breite Angebot an Glücksspielen im Internet ermöglicht es, dem Bedürfnis nach einem „Kick“ auch während eines Lockdowns nachzugehen, ohne die Wohnung verlassen zu müssen. So kann sich ein krankhaftes Glücksspielen umso schneller entwickeln oder verschlechtern. Auch können Rückfälle bei zuvor abstinenten Glückspielern provoziert werden.
Glücksspiele üben auf Menschen seit jeher eine besondere Anziehung aus. Beim Spielen den Zufall und das Glück herauszufordern erzeugt eine besondere Spannung und einen besonderen Kick, der die Welt außerhalb des Spielgeschehens vergessen lässt. Die Möglichkeit, im Spiel den Alltag, Sorgen, Probleme und Nöte vergessen zu können, wird von vielen Menschen gesucht. Außerdem lockt die Aussicht, schnell und einfach über viel Geld zu verfügen und beflügelt die Träume auf ein besseres und problemfreies Leben.
Auch die Atmosphäre, die an vielen Spielorten herrscht, hat eine besondere Anziehungskraft. Es wird signalisiert: Hier findet etwas Anderes, etwas Besonderes statt, hier bist du wer. Der Alltag und deine persönlichen Schwierigkeiten sind hier nicht wichtig.
Doch die Realität des Glücksspielens wird häufig schnell eine andere. Hoffnungen und Wünsche erfüllen sich nicht. Es entsteht ein Druck, verlorenes Geld wieder hereinholen zu wollen. Das Leben beginnt sich immer mehr um das Spielen und die Geldbeschaffung dafür zu drehen.
GLÜCKSSPIELABHÄNGIGKEIT
Ursachen
Die Ursachen, mit dem Glücksspiel anzufangen, können vielfältig sein: Stress bei der Arbeit, mangelnder sozialer Anschluss, Langeweile, Hoffnung auf hohe Geldsummen und viele mehr. Gemeinsam ist ihnen meist der Wunsch nach Alltagsflucht und Nervenkitzel. Doch aus einem einmalig g…
Harmloser Einstieg
Die Ursachen, mit dem Glücksspiel anzufangen, können vielfältig sein: Stress bei der Arbeit, mangelnder sozialer Anschluss, Langeweile, Hoffnung auf hohe Geldsummen und viele mehr. Gemeinsam ist ihnen meist der Wunsch nach Alltagsflucht und Nervenkitzel. Doch aus einem einmalig geplanten Spieleinsatz kann schnell der Wunsch nach weiteren Spielen entstehen. Ist dieses Verlangen erst einmal entstanden, kann es schnell in die Spielsucht münden. 
Denn geringe Geldeinsätze lassen die Freude über unerwartete Gewinne umso größer erscheinen. Die Spieldauer und -einsätze nehmen zu, um vergleichbare Glücksgefühle zu erhalten. Verluste häufen sich an. Eine rasante Aufholjagd soll das wachsende Minus ausgleichen. Niederlagen werden äußeren Umständen zugeschrieben, Gewinne den eigenen Fähigkeiten. Die Hoffnung auf den großen Gewinn wird durch abergläubische Überzeugungen und Handlungen aufrechterhalten.
Wachsende Alltagsprobleme
Konflikte mit nahen Angehörigen, Freunden und Arbeitskollegen nehmen durch diese Ursachen der Spielsucht zu, Schuldenlast und Geldbeschaffung erhöhen den Stress. Das Glücksspielen gleicht einer verzweifelten Flucht hinein in die Scheinwelt der unbesiegbaren „Glücksritter“, um zumindest kurzfristig „abschalten“ zu können oder die Rolle des „großen Gewinners“ einzunehmen. Das unwiderstehliche Spielverlangen, Illusionen über die Kontrollierbarkeit des Spiels, Selbstisolation und die Einschränkung alternativer Erlebnismöglichkeiten bilden einen Teufelskreis der Selbstzerstörung. Der Betroffene verliert alle Hoffnung, sein Leben noch meistern zu können.
Vorhandene Probleme und Konflikte werden nicht gelöst, sondern türmen sich immer weiter auf und werden durch die Geldverluste beim Spielen noch verschlimmert. Ausreden werden erfunden, um das Spielen zu verheimlichen und um unangenehme Tatsachen und Folgen der Spielsucht zu verbergen. Es kann auch zu Betrug und anderen unredlichen Handlungen zur Geldbeschaffung kommen. Das Vertrauen anderer Menschen geht zunehmend verloren, Einsamkeit und Verzweiflung breiten sich aus.
Spielsucht - Symptome
Wenn bestimmte Gesichtspunkte beim Glücksspielen übermäßig in den Vordergrund treten, wird das Spielen pathologisch oder krankhaft.  Wie auch bei anderen Suchtformen dreht sich das Verhalten eines Spielsüchtigen fast ausschließlich um den Konsum, was in diesem Falle das Spielerlebnis ist. Symptome für eine Spielsucht sind:
    • Der Wunsch nach Verlassen der Realität und Vergessen von Problemen
    • Das Gefühl von Macht und Kontrolle beim Spielen oder durch das Spielen
    • Falsche Einschätzungen von Wahrscheinlichkeiten und Gewinnchancen
    • Die Illusion, das Spielgeschehen kontrollieren und beherrschen zu können
    • Trost im Glücksspielen bei Selbstwertproblemen, Depressivität und Ängsten
    • Auftreten von Verlangen und entzugsähnlichen Erscheinungen, wenn nicht gespielt werden kann
Mögliche Symptome für Außenstehende
Des Weiteren erkennen Außenstehende einen Spielsüchtigen häufig daran, dass sie nie Zeit und nie Geld haben, obwohl sie weder einen besonders zeitraubenden Beruf ausüben noch über ein schlechtes Gehalt verfügen.
Spielsucht - Folgen
Betroffene einer Glückspielsucht halten für ihre zeitliche Abwesenheit und andauernde Finanznot stets gute Ausreden parat. Hinter dieser Fassade verbirgt sich eine Abwärtsspirale in eine ausweglose Situation – verbunden mit viel Leid für die Betroffenen und natürlich deren Angehörige. Die Folgen dieser Erkrankung sind gravierend: Nicht selten führt Glücksspielsucht zum Verlust des Arbeitsplatzes oder der Wohnung sowie zu einer kaum zu bewältigenden Verschuldung, was wiederum die Trennung oder Scheidung durch den Partner als Konsequenz haben kann. Die Verzweiflung über hohe Schulden und den Verlust der Familie können wiederum zu weiteren Suchtformen wie Alkohol- und Drogenmissbrauch führen.
Die Folgen einer Spielsucht können sein: 
    • Schuld- und Schamgefühle
    • Psychosomatische Störungen, Depressionen und Selbstmordversuche
    • Alkohol- und Drogenmissbrauch
    • Familiäre Konflikte, Trennung und Scheidung
    • Berufliche Probleme und Arbeitsplatzverlust
    • Verschuldung und Wohnungsverlust
    • Unredliche Geldbeschaffung
Entzugserscheinungen als Folgen der Spielsucht
Ähnlich wie bei substanzgebundenen Süchten können auch bei substanzungebundenen Süchten Entzugserscheinungen auftreten, da sich regelmäßiges Glücksspiel auf das Belohnungssystem im Gehirn auswirken kann. Die Spannung, das Glück und den Zufall beim Glücksspiel herauszufordern, setzt Adrenalin frei. Kleine und große Gewinne beim Glücksspiel aktivieren zudem das Belohnungssystem, und es werden Glückshormone ausgeschüttet. Betroffene beginnen, mit dem Erlebnis des Glücksspiels Wohlbefinden zu suggerieren. Gewöhnt sich der Körper daran, können beim längeren Pausieren und Beenden des Spielens Entzugserscheinungen wie innere Unruhe, Unzufriedenheit und daraus resultierend das starke Verlangen nach erneuten Spielerfahrungen auftreten. Daher ist es ratsam, das Spielverhalten schrittweise zu reduzieren, um das Belohnungssystem vom „Kick“ beim Glückspiel zu „entwöhnen“.  
Spielsucht - Therapie
Das Pathologische Glücksspielen ist ein Störungsbild, dass sich bei fast allen Formen der Spielsucht entwickeln kann: Geldspielautomaten-, Kasino-, Karten- und Würfelspiele, Sportwetten, alle Formen von Online-Glücksspielen und andere. Seit 2001 ist es als eigenständige Erkrankung anerkannt, weswegen die Kosten für eine Therapie von den Rentenversicherungsträgern und Krankenkassen übernommen werden. Eine Reha bei Glücksspielsucht kann in Form einer ambulanten Betreuung oder einer stationären Behandlung stattfinden. Die Dauer der Therapie beträgt in der Regel fünf bis acht Wochen, kann jedoch je nach Schwere von Begleiterkrankungen, wie stoffgebundenen Suchterkrankungen, auch 15 bis 24 Wochen umfassen.
Ziele der Therapie bei Spielsucht
Die übergeordneten Ziele der Behandlung von Spielsucht sind:
    • Erlangen einer dauerhaften Glücksspielfreiheit
    • Verstehen, was die Auslöser für das exzessive Glücksspielen sind
    • Entdecken, welche Alternativen das Leben bietet
    • Lernen, konstruktiv mit unangenehmen Gefühlszuständen und Konflikten in Beziehungen umzugehen
    • Verbesserung des Umgangs mit Geld und Einleitung der Entschuldung
    • Hilfe bei allen alltäglichen, rechtlichen und beruflichen Problemen
Dabei umfasst die Therapie einer Spielsucht folgende Hilfsangebote:
    • Ein Team aus (Fach-)Ärzten, ärztlichen und  psychologischen Psychotherapeuten, Sport-, Ergo- und  Soziotherapeuten sowie Sozialarbeitern
    • Unterbringungsmöglichkeiten in einer therapeutischen Wohngruppe
    • Gemeinsamer, strukturierter Tagesablauf mit Sport, Bewegung und kreativer Beschäftigung sowie Unterstützung bei der Freizeitgestaltung
    • Einzel- und Gruppentherapie
    • Störungsspezifische Gruppentherapie mit gleich betroffenen Patienten
Weitere Aspekte einer Reha bei Spielsucht

Was bietet die Suchtrehabilitation nach Covid-19?
    • Für jeden Patienten wird abhängig von der Art der psychischen Beeinträchtigungen ein eigener Behandlungsplan erstellt.
    • Kernelement der Entwöhnung ist eine mehrmals wöchentlich stattfindende Suchtgruppentherapie, in der Betroffene sich auch eingehend über Covid-19 assoziierte Themen austauschen und eine Krankheitsverarbeitung angestoßen werden kann.
    • Interaktionelle Aspekte sind dabei ebenso Thema wie gemeinsames Problemlösen.
    • Eingangs wird viel Wert auf eine adäquate Psychoedukation gelegt. Krankheitseinsicht sowie emotionale -akzeptanz sollen etabliert werden.
    • Je nach Art und Schwere der vorliegenden psychischen Begleitstörungen erfolgt eine Zuteilung zu störungsspezifischen Gruppen, wie zum Beispiel einer angsttherapeutischen Gruppe, einer Depressionsgruppe oder einer Traumagruppe.
    • Eine bestehende Behandlung der körperlichen Folgen der Covid-Infektion wird fortgesetzt und durch Sport- und Bewegungstherapie unterstützt.
    • Entspannungstherapie und kreativtherapeutische Verfahren kommen ebenfalls zur Anwendung.
    • Eine berufliche Wiedereingliederung wird, sofern erforderlich, ebenfalls eingeleitet, begleitet durch soziotherapeutische Unterstützung soweit dies notwendig ist.
Ziel der Suchtrehabilitation je nach Erkrankung:
    • Suchtmittelabstinenz 
    • Verzicht auf den pathologischen PC-Internetgebrauch 
    • Verzicht auf das pathologische Glücksspielen
Voraussetzungen für die Suchtrehabilitation:
    • Virusfreiheit
    • eine positive Reha-Prognose
    • eine adäquate Motivation zur Durchführung der Suchtrehabilitation

Interdisziplinäre Post-Corona-Rehabilitation als Anschlußheilbehandlung nach Covid-19-Erkrankung
Für Patienten, die einen schweren Verlauf der Covid-19-Erkrankung überstanden haben und noch in deutlich geschwächtem Allgemeinzustand sind, empfiehlt sich eine anschließende Corona Rehabilitation. Diese ist speziell auf die Bedürfnisse nach der Covid-19-Erkrankung konzipiert worden und zielt auf die Wiederherstellung und Sicherung der Teilhabe am Alltagsleben ab. Besonderer Fokus gilt in dieser Behandlung nach Covid-19 der Verbesserung der Atemmuskelkraft, der pulmonalen Belastbarkeit sowie von psychomentalen Beeinträchtigungen. Der Aufenthalt in der Rehaklinik dauert insgesamt 21 Tage mit der Möglichkeit zur Verlängerung.
Das Rehabilitationsziel ist hierbei die Wiederherstellung und Sicherung der Teilhabe nach überstandener Covid-19-Erkrankung.
Dabei stehen im Fokus die Verbesserung:
    • der Atemnot
    • der Atemmuskelkraft und der pulmonalen Belastbarkeit
    • psychomentaler Beeinträchtigungen und/oder stressinduzierter seelischer Folgestörungen der Erkrankung
Voraussetzung für diese Reha
    • Kriterien zur Entlassung aus dem Krankenhaus bzw. aus der häuslichen Isolierung sind erfüllt 
    • eine stabile pulmonale Situation (in der Regel Sauerstoffsättigung > 93% und eine Atemfrequenz < 20/min)  
Was leistet diese Rehabilitation
Therapieziele:
    • allgemeinen Kräftigung und Mobilisierung
    • Normalisierung der Atemfunktionen
Hauptbestandteil der Therapie sind:
    • Atemgymnastik mit Atemmuskeltraining
    • Lösung der Verschleimung
Nach Bedarf werden ergänzt:
    • Gruppengespräche (1-2 Stunden pro Woche) zum Austausch über die Erfahrung der Corona-Erkrankung 
    • Entspannungstraining
    • supportive psychologische Beratung zur Trauma-, Angst- oder Depressionsbewältigung
Dauer: 21 Tage mit der Möglichkeit zur Verlängerung
Die interdisziplinäre Post-Corona-Rehabilitation bietet MEDIAN in folgenden Rehakliniken an:
    • MEDIAN Klinik Heiligendamm
    • MEDIAN Parkklinik Bad Rothefelde
    • MEDIAN Klinik Gyhum
    • MEDIAN Klinik Wilhelmshaven
    • MEDIAN Klinik am Südpark Bad Nauheim
    • MEDIAN Reha-Zentrum Wiesbaden Sonnenberg
    • MEDIAN Reha-Zentrum Bernkastel-Kues
    • MEDIAN AGZ Leipzig
    • MEDIAN Zentrum für Rehabilitation Schmannewitz
    • MEDIAN Saale Klinik Bad Kösen I
    • MEDIAN Klinik Bad Lausick
    • MEDIAN Klinik Bad Gottleuba
    • MEDIAN Reha-Zentrum Bad Berka Adelsberg-Klinik
    • MEDIAN Park-Klinik Bad Dürkheim
    • MEDIAN Klinik am Burggraben Bad Salzuflen
    • MEDIAN Klinik Flachsheide Bad Salzuflen
Häufige Fragen zur Interdisziplinären Post-Corona-Rehabilitation:
Wie kann ich eine interdisziplinäre Reha nach Corona beantragen?
Um eine interdisziplinäre Reha nach Corona zu beantragen, reichen Sie die Antragsunterlagen bei Ihrem Kostenträger ein. Sie erhalten einen entsprechenden Reha-Bescheid, der Auskunft über die Bewilligung der Reha und der entsprechenden Rehaklinik gibt. In den Unterlagen können Sie auch Ihre Wunschklinik angeben.
Was ist eine interdisziplinäre Anschlussheilbehandlung nach Corona?
Die Anschlussheilbehandlung nach Corona ist speziell auf die Bedürfnisse nach einer COVID-19-Erkrankung konzipiert. Sie ist abgestimmt auf Patienten, die einen schweren Verlauf der COVID-19-Erkrankung überstanden haben und noch in einem deutlich geschwächten Allgemeinzustand aufzeigen oder für Patienten mit eingeschränkter physischer/ psychischer Leistungsfähigkeit, die sich nur sehr langsam erholen von einer COVID-19 Erkrankung erholen, ist die Anschlussbehandlung nach Corona geeignet.
Welche interdisziplinären Therapien werden in der Reha nach Corona angewandt?
Speziell für die Therapie nach Corona bieten die MEDIAN Kliniken interdisziplinären Therapien an wie Atemtherapie und Atemeffizienztraining, Hirnleistungstraining, Kraft / Ausdauer, aber auch Sozialmedizin, Ergotherapie, Diät-/ Ernährungsberatung und weitere experimentelle Therapien.
Welche Voraussetzungen gibt es für die interdisziplinäre Post-Corona-Reha?
Patienten, erfüllen die Voraussetzungen für eine interdisziplinäre Post-Corona-Reha, wenn die Kriterien zur Entlassung aus dem Krankenhaus bzw. aus der häuslichen Isolierung erfüllt sind sowie eine stabile pulmonale Situation besteht. Das heißt in der Regel eine Sauerstoffsättigung von mindestens 93% und eine Atemfrequenz von weniger als 20 Atemzüge pro Minute.

Spezifische psychosomatische Post-Corona-Rehabilitation für Patienten mit Covid-19 assoziierten psychischen Störungen
Durch die Covid-19-Pandemie und deren Begleiterscheinungen können gravierende psychosomatische Störungen ausgelöst oder verstärkt werden. Hierzu zählen u.a. Angststörungen, depressive Befürchtungen, Zwangsstörungen durch besondere Hygienevorschriften oder auch Depressionen in Folge von besonders traumatischen Erlebnissen bei Angehörigen und/oder deren Todesfälle. Für sämtliche Covid-19 assoziierten psychischen Folgestörungen bieten diverse MEDIAN Kliniken mit einer Abteilung für Psychosomatik spezifische psychosomatische Post-Corona-Rehabilitationen an. Je nach Art der psychischen Beeinträchtigungen wird für diese Art der Post-Corona-Reha ein individueller Behandlungsplan erstellt, mit dem es den Patienten ermöglicht wird, wieder bestmöglich am Leben teilzuhaben.
Durch die Pandemie und deren Begleiterscheinungen ausgelöste oder verstärkte psychosomatische Störungen:
    • Angststörungen
    • depressive Befürchtungen
    • Zwangsstörungen durch besondere Hygienevorschriften
    • klaustrophobe Ängste durch Ausgangsrestriktionen 
    • prolongierte Trauerreaktionen
    • Depressionen durch als traumatisch erlebte Behandlungen von Angehörigen mit Covid-19 und/oder deren Todesfälle
Bei medizinischem Personal, das in der Corona-Behandlung eingesetzt wird, treten zudem auf:
    • Erschöpfungsdepressionen
    • Traumafolgestörungen
Hinzu kommen somatoforme Störungen und Somatisierungsstörungen als mögliche psychische Folgen der Corona-Erkrankung und deren Behandlung.
Voraussetzungen für eine psychosomatische Post-Corona-Reha nach einer Covid-19-Erkrankung:
    • Virusfreiheit
    • Rehabilitationsfähigkeit
    • eine positive Reha-Prognose
    • eine adäquate Behandlungsmotivation 
Was leistet die psychosomatische Post-Covid-Reha
Je nach Art der psychischen Beeinträchtigungen wird ein individueller Behandlungsplan erstellt:
    • Kernelement ist eine spezifische Covid-19 bezogene Gruppentherapie, in der sich Betroffene sich austauschen können und eine Krankheitsverarbeitung angestoßen werden kann.
    • Interaktionelle Aspekte sind dabei ebenso Thema wie gemeinsames Problemlösen.
    • Je nach Art und Schwere der vorliegenden psychischen Störung erfolgt eine Zuteilung zu störungsspezifischen indikativen Gruppen, wie zum Beispiel einer schmerztherapeutischen Gruppe oder einer Depressionsgruppe.
    • Traumatherapie bildet bei Covid-19 assoziierten psychischen Traumata einen zentralen Teil der Rehabilitationsbehandlung.
    • Spezifische Einzelpsychotherapie unterstützt bei Posttraumatischer Belastungsstörung und dissoziativen Störungen.
Soweit notwendig wird die Behandlung der körperlichen Folgen fortgesetzt und durch Maßnahmen zur körperlichen Kräftigung unterstütz.
    • Sporttherapie in der Gruppe dient hierbei nicht nur der körperlichen Ertüchtigung, sondern auch dem positiven Erleben des eigenen Körpers.
    • Entspannende Maßnahmen
Kreativtherapeutische Verfahren dienen der Ressourcenstärkung und ermöglichen einen gestalterischen Ausdruck des Traumas.
Die berufliche Wiedereingliederung wird, sofern erforderlich bzw. möglich, in die Wege geleitet und im Bedarfsfall durch Soziotherapeutische Unterstützungsmaßnahmen ergänzt.
Die spezifische psychosomatische Post-Corona-Rehabilitation bietet MEDIAN in folgenden Rehakliniken an:
    • MEDIAN Klinik Heiligendamm
    • MEDIAN Klinik Schweriner See
    • AHG Klinik Waren
    • MEDIAN Zentrum für Verhaltensmedizin Bad Pyrmont
    • MEDIAN Klinik Münchwies
    • MEDIAN Reha-Zentrum Bernkastel-Kues
    • MEDIAN Zentrum für Rehabilitation Schmannewitz
    • MEDIAN Klinik Bad Gottleuba
    • MEDIAN Reha-Zentrum Bad Berka Adelsberg-Klinik


Spezifische pneumologische Post-Corona-Rehabilitation für Patienten mit Covid-19 Infektion
Für Patienten, die im Zuge ihrer Covid-19 Erkrankung eine schwere Lungenentzündung erlitten haben und dabei langzeitbeatmet wurden und/oder ein Lungenversagen (ARDS) stattfand, empfiehlt sich im Anschluss eine spezielle pneumologische Reha bei Covid-19. 
Insbesondere die supportive Gabe von Sauerstoff und auch die Unterstützung durch nichtinvasive Beatmung im Zuge der Therapien schafft die Rahmenbedingung, um ein optimales Rehabilitationsergebnis zu erreichen. Unsere MEDIAN Kliniken mit einer Abteilung für Pneumologie können dabei auf die jahrelange Erfahrung in der Rehabilitation von Menschen mit Lungenkrankheiten jeglicher Genese – auch beatmeten Patienten – bauen. 
Das primäre Rehabilitationsziel bei dieser Behandlung nach Corona ist die Wiederherstellung der deutlich reduzierten Lungenfunktion nach der durch Covid-19 verursachten Lungenentzündung (Pneumonie). Dabei gilt es, die weiterhin eingeschränkte pulmonale Belastbarkeit zu berücksichtigen und die Atemmuskelkraft und Lungenfunktionen zu stärken. Hierauf sind die spezifischen Therapien innerhalb der pneumologischen Post-Corona-Rehabilitation ausgerichtet sowie die behandelnden Ärzte und Therapeuten als auch die betreuende Pflegekräfte speziell geschult. Mithilfe der rehabilitierenden Maßnahmen können Spätfolgen einer Corona-Infektion an der Lunge optimal behandelt werden.
Voraussetzung für diese Reha
    • Nachweis zweier negativer Covid-19 Abstriche
    • Keine einschränkenden Vorgaben durch das zuständige Gesundheitsamt
    • Patienten müssen in der Lage sein, sich selbständig zu versorgen (Barthel-Index 80) 
    • Sauerstoffpflichtige Patienten oder Patienten mit nicht invasiver häuslicher Beatmung können behandelt werden
    • Die Direktverlegung aus dem Akutkrankenhaus ist möglich
Was leistet die pneumologische Post-Corona-Rehabilitation
Therapieziele:
    • Verbesserung der Atemnot
    • Verbesserung der Atemmuskelkraft
    • Stärkung der Lungenfunktion
    • allgemeine Kräftigung und Mobilisierung

Hauptbestandteile der Therapie:
    • Atemgymnastik
    • Atemmuskeltraining
    • Atemphysiotherapie
    • Lösung der Verschleimung
 
Jeder Rehabilitand erhält eigene Therapiegeräte, je nach Bedarf zum Beispiel ein Atemübungsgerät, ein Peak-Flow-Gerät oder eine Inhalationshilfe.
Ergänzt wird das Rundum-Programm für die Lunge durch Kraft- und Ausdauertraining. Auch die psychologische Mitbehandlung bei möglichen psychomentalen Beeinträchtigungen nach langem Krankheitsverlauf und Isolation ist ein zentraler Baustein
Die Therapiedauer beträgt bei stationären Rehabilitanden 21 Tage.
Die spezifische pneumologische Post-Corona-Reha bietet MEDIAN in folgenden Rehakliniken an:
    • MEDIAN Klinik Heiligendamm
    • MEDIAN Klinik Flachsheide Bad Salzuflen
    • MEDIAN Klinik Flechtingen
    • MEDIAN Klinik am Burggraben Bad Salzuflen

Häufige Fragen zur Reha nach Corona
Für wen ist eine Reha nach Corona sinnvoll?
Ein Reha-Aufenthalt ist für alle Personen sinnvoll, die mit den Auswirkungen von Covid-19 zu kämpfen haben. Dies gilt sowohl für Betroffene mit körperlichen (Langzeit-)Folgen, als auch für Menschen, die seelisch unter ihrer Erkrankung bzw. den vielfältigen Auswirkungen der globalen Covid-19-Pandemie und der Lockdowns leiden. Für beide Gruppen haben die MEDIAN Kliniken vier unterschiedliche Rehabilitationskonzepte entwickelt – zwei somatische, ein psychosomatisches sowie eines mit dem Schwerpunkt Sucht.
Ab welchem Zeitpunkt ist eine Post-Corona-Rehabilitation möglich?
Abhängig von der Art der Covid-19 Rehabilitation sind unterschiedliche Voraussetzungen nötig, damit unsere Rehakliniken Sie für die Behandlung nach einer Corona-Erkrankung aufnehmen können.
Wie lange dauert eine Reha nach einer Covid-19-Erkrankung?
Die Therapiedauer einer Behandlung nach Covid-19 hängt von der Art der Rehabilitation und den individuellen Voraussetzungen des jeweiligen Patienten ab. Für unsere vier Rehabilitationsarten in Zusammenhang mit Corona ist mit folgenden Aufenthaltsdauern zu rechnen:
    • Spezifische pneumologische Post-Corona-Rehabilitation: bei stationären Rehabilitanden 21 Tage
    • Suchtrehabilitation Covid-19 assoziierter Abhängigkeitserkrankungen: zwischen 12 und 15 Wochen
    • Bei spezifischen psychosomatischen Post-Corona-Rehabilitationen ist sowohl kurzfristig als auch mit einer Latenz von bis zu ca. 3 Jahren zu rechnen.
    • Interdisziplinäre Post-Corona-Rehabilitation: 21 Tage mit der Möglichkeit zur Verlängerung
Was sind die Behandlungsziele einer Post-Corona-Reha?
Die Ziele einer Post-Corona-Reha hängen einerseits von der Art der Corona-Rehabilitation als auch von den individuellen Patientenbedürfnissen ab. Im Mittelpunkt unserer angebotenen Post-Corona-Rehabilitationen stehen psychische oder körperliche Folgeschäden einer Covid-19-Erkrankung sowie psychosomatische Störungen, die durch die Begleiterscheinungen der Covid-19-Pandemie hervorgerufen oder verstärkt wurden.
Die pneumologische Post-Corona-Reha hat zum Ziel, eine Verbesserung der Atemnot sowie eine Stärkung der Lungenfunktion und eine allgemeine Kräftigung und Mobilisierung zu erreichen.
Bei der interdisziplinäre Post-Corona-Reha werden sowohl körperliche als auch seelische Auswirkungen einer Covid-19-Erkrankung behandelt. Sie verfolgt neben der Verbesserung der Atemnot, der Atemmuskelkraft und der pulmonalen Belastbarkeit auch das Ziel psychomentale Beeinträchtigungen und/oder stressinduzierte seelische Folgestörungen der Infektion zu lindern. 
In der psychosomatischen Post-Corona-Reha werden psychosomatische Störungen behandelt, die durch die Begleiterscheinungen der Covid-19-Pandemie ausgelöst oder verstärkt wurden. Dazu gehören psychische Erkrankungen wie Angststörungen, langwierige Trauerreaktionen und Zwangsstörungen. 
Die Sucht-Post-Corona-Rehabilitation widmet sich verschiedenen Abhängigkeitserkrankungen, aufgrund der Covid-19-Pandemie und deren Begleiterscheinungen entwickelt oder verstärkt wurden. Sie verfolgt das Ziel der Suchtmittelabstinenz, beispielsweise der Verzicht auf pathologischen PC-/Internetgebrauch oder pathologisches Glücksspielen.  
Wie beantrage ich eine Reha nach Corona?
Sie haben den Wunsch, eine Reha-Maßnahme in Anspruch zu nehmen, oder Ihr Arzt bzw. Therapeut empfiehlt Ihnen eine Rehaklinik nach Corona? Dann stellen Sie gemeinsam einen Antrag bei Ihrem Kostenträger. Sie haben grundsätzlich einen Anspruch auf eine Reha nach Corona, um Ihre Gesundheit und Erwerbsfähigkeit zu erhalten.
Musterantrag der Gesetzlichen Krankenversicherung für die Rehabilitation nach Covid-19-Erkrankung.
Welche Reha-Angebote gibt es für Menschen, die seelisch unter Pandemie, Lockdown oder einer Covid-19-Erkrankung gelitten haben?
Für Menschen, die unter einer Covid-Erkrankung, der Pandemie oder ihren Folgen psychisch gelitten oder Störungsbilder entwickelt haben, bietet MEDIAN zwei Post-Corona-Rehabilitationen mit den Schwerpunkten Psychosomatik und Sucht an.
Die spezifische psychosomatische Post-Corona-Reha behandelt psychosomatische Beschwerden, wie Angststörungen, depressive Befürchtungen oder Zwangsstörungen durch strenge Hygienevorschriften oder auch Depressionen in Folge traumatischer Erlebnisse, die durch die Covid-19-Pandemie und deren Begleiterscheinungen ausgelöst oder verstärkt wurden.
Die spezifische Sucht-Post-Corona-Reha widmet sich Abhängigkeitserkrankungen, die durch Faktoren wie Einsamkeit, Langeweile, fehlende berufliche Verpflichtungen oder Existenzängste während der Covid-19-Pandemie ausgelöst beziehungsweise gefördert wurden. Dazu zählen Alkoholabhängigkeit, Drogen- und Medikamentensucht sowie der pathologische Gebrauch von PC/Internet und Glücksspiel.
Welche Maßnahmen werden von MEDIAN zur Prävention von Corona-Infektionen in den Kliniken getroffen?
Die Gesundheit unserer Patienten, Mitarbeiter und deren Angehörigen stehen für uns an oberster Stelle. Deswegen hat MEDIAN ein umfassendes Konzept zur Prävention von Corona-Infektionen in den Kliniken entwickelt. Alle Informationen sowie Dokumente zum Download finden Sie auf unserer Seite zu Präventionsmaßnahmen.


FAQ der MEDIAN Unternehmensgruppe zur Rehabilitation
Allgemeine Informationen:
1. Was ist Rehabilitation?
Rehabilitation ist die Wiederherstellung der körperlichen, geistigen und sozialen Fähigkeiten eines Menschen nach einer Erkrankung oder Verletzung. Ziel ist es, die bestmögliche Selbstständigkeit und Lebensqualität im Alltag zu erreichen.
2. Welche Ziele hat die Rehabilitation?
Die Rehabilitation hat verschiedene Ziele, darunter:
    • Verbesserung der körperlichen Funktionen
    • Stärkung der geistigen und emotionalen Gesundheit
    • Erlernen von Kompensationsstrategien
    • Wiedereingliederung in den Alltag
    • Verhinderung von Folgeerkrankungen
3. Welche Arten von Rehabilitation gibt es?
Die MEDIAN Gruppe bietet verschiedene Arten von Rehabilitation an, darunter:
    • Anschlussrehabilitation (AR)
    • Berufsgenossenschaftliche Rehabilitation (BGR)
    • Rentenversicherungsträgerliche Rehabilitation (RV)
    • Stationäre Weiterbehandlung (STW)
    • Ambulante Rehabilitation
    • Kinder- und Jugendrehabilitation
    • Psychosomatische Rehabilitation
    • Onkologische Rehabilitation
    • Neurologische Rehabilitation
    • Orthopädische Rehabilitation
    • Kardiologische Rehabilitation
4. Wie lange dauert eine Rehabilitation?
Die Dauer einer Rehabilitation kann je nach Art der Erkrankung oder Verletzung und den individuellen Bedürfnissen des Patienten variieren. In der Regel dauert eine Rehabilitation zwischen drei und sechs Wochen.
5. Wo findet eine Rehabilitation statt?
Rehabilitationen finden in der Regel in speziellen Rehabilitationseinrichtungen statt. Die MEDIAN Gruppe verfügt über ein bundesweites Netz von mehr als 120 Kliniken und Fachkrankenhäusern.
6. Wer trägt die Kosten für eine Rehabilitation?
Die Kosten für eine Rehabilitation werden in der Regel von den Krankenkassen, den Rentenversicherungsträgern oder den Berufsgenossenschaften übernommen. In einigen Fällen müssen die Patienten die Kosten selbst tragen.
7. Wie kann ich einen Antrag auf Rehabilitation stellen?
Den Antrag auf Rehabilitation stellen Sie bei Ihrem zuständigen Kostenträger. Die MEDIAN Gruppe unterstützt Sie gerne bei der Antragstellung.
8. Was muss ich bei der Antragstellung beachten?
Bei der Antragstellung sollten Sie folgende Unterlagen bereithalten:
    • Ärztlicher Befundbericht
    • Rentenbescheid
    • Krankenkassenkarte
    • Personalausweis
9. Was passiert nach der Antragstellung?
Nach der Antragstellung wird Ihr Kostenträger den Antrag prüfen und entscheiden, ob eine Rehabilitation bewilligt wird.
10. Wie kann ich mich auf die Rehabilitation vorbereiten?
Um die Rehabilitation optimal nutzen zu können, sollten Sie sich gut darauf vorbereiten. Dazu gehört, dass Sie sich über die Ziele der Rehabilitation informieren und sich Gedanken machen, welche Fragen Sie an die Ärzte und Therapeuten haben.
11. Was kann ich während der Rehabilitation erwarten?
Während der Rehabilitation werden Sie von einem Team aus Ärzten, Therapeuten und Pflegekräften betreut. Sie erhalten ein individuelles Behandlungsprogramm, das auf Ihre Bedürfnisse abgestimmt ist.
12. Was passiert nach der Rehabilitation?
Nach der Rehabilitation erhalten Sie einen Abschlussbericht, der Ihre Fortschritte und die erreichten Ziele dokumentiert. Die MEDIAN Gruppe unterstützt Sie gerne bei der Wiedereingliederung in den Alltag.
FAQ zu den einzelnen Arten der Rehabilitation:
Anschlussrehabilitation (AR)
13. Was ist eine Anschlussrehabilitation?
Die Anschlussrehabilitation (AR) schließt direkt an eine Krankenhausbehandlung an und hat zum Ziel, die erreichten Behandlungsergebnisse zu stabilisieren und die Wiedereingliederung in den Alltag zu erleichtern.
14. Wer trägt die Kosten für eine Anschlussrehabilitation?
Die Kosten für eine Anschlussrehabilitation werden in der Regel von den Krankenkassen übernommen.
Berufsgenossenschaftliche Rehabilitation (BGR)
15. Was ist eine berufsgenossenschaftliche Rehabilitation?
Die berufsgenossenschaftliche Rehabilitation (BGR) wird von den Berufsgenossenschaften (BG) getragen und kommt für die Folgen von Arbeitsunfällen und Berufskrankheiten auf.
16. Welche Leistungen umfasst die BGR?
Die BGR umfasst alle Leistungen, die zur Wiederherstellung der Arbeits

Häufige Fragen zum Reha Übergangsgeld:
Wann bekomme ich mein Übergangsgeld nach der Reha?
Übergangsgeld wird über die gesamte Dauer der medizinischen oder beruflichen Rehabilitation ausgezahlt. Dieser Zeitraum beträgt meist 6 Wochen. Das Übergangsgeld wird vom zuständigen Rehabilitationsträger vergütet. Der Patient erhält es nach der abgeschlossenen Reha.

Was versteht man unter Übergangsgeld?
Übergangsgelder sind Leistungen, die bei einer rehabilitativen Behandlung von zuständigen Kostenträgern (Unfallversicherung, Krankenversicherung, Rentenversicherung, etc.) ausbezahlt werden. Sie treten dann ein, wenn die Entgeltfortzahlung auf Seiten des Arbeitgebers im Krankheitsfall beendet wurde.

Wer hat Anspruch auf Übergangsgeld?
Erkrankt ein Arbeitnehmer oder ist dieser in einen (Arbeits-)Unfall verwickelt, der eine langwierige und intensive Betreuung in Form einer Reha benötigt, hat er das Recht Übergangsgeld zu beantragen. Anspruch auf Übergangsgeld besteht generell dann, wenn der Arbeitnehmer unmittelbar vor der Rehabilitation oder vorangegangenen Arbeitsunfähigkeit Arbeitsentgelt erhalten und Rentenkassenbeiträge bezahlt hat.

Wie lange und auf wie viel Übergangsgeld besteht Anspruch?
Patienten in rehabilitativer Behandlung erhalten Übergangsgeld über die gesamte Dauer der behandelnden Maßnahme (maximal 6 Wochen). Leistungen werden allerdings nur für jene Tage rückerstattet, an den der Patient tatsächlich an der Reha-Maßnahme teilgenommen hat. Die Höhe wird auf Basis des letzten Bruttoarbeitsentgelts berechnet und beträgt zwischen 75 und 80 % dieses Betrags.

Wann wird das Übergangsgeld nach der Reha überwiesen?
Das Übergangsgeld wird nach der abgeschlossenen Reha überwiesen. Es kann aber auch 14 Tagen nach dem Ende der Reha-Maßnahmen ein anteiliger Vorschuss beantragt werden.

Wie lange dauert die Bearbeitung von Übergangsgeld?
Die Bearbeitung von Übergangsgeld dauert meistens sechs Wochen. Das Übergangsgeld wird von dem zuständigen Versicherungsträger vergütet.

Wie wird das Übergangsgeld ausgezahlt?
Das Übergangsgeld vom zuständigen Versicherungsträger ausgezahlt und muss beantragt werden. Individuelle Auskunft bieten die Rentenversicherungsträger, Krankenkassen, Unfallversicherungsträger und die Agentur für Arbeit.

Wer zahlt das Übergangsgeld?
Der zuständige Kostenträger zahlt das Übergangsgeld.

Wiedereingliederung nach Reha – Wer zahlt?
Die stufenweise Wiedereingliederung zurück in den Arbeitsalltag wird in Deutschland je nach Umständen von verschiedenen Rehabilitationsträgern übernommen. In Frage kommen die Rentenversicherung, die gesetzliche Krankenversicherung oder die Unfallversicherung des Patienten.
Stufenweise Wiedereingliederung
Das Ziel einer stufenweisen Wiedereingliederung ist es, arbeitsunfähige Arbeitnehmer nach länger andauernder Erkrankung und Rehabilitation wieder Schritt für Schritt in den regulären Arbeitsalltag einzuführen. Der Patient wird nach Einverständnis auf der Seite des Arbeitnehmers somit allmählich wieder an die volle Arbeitsbelastung herangeführt. Die Stufenweise Wiedereingliederung findet meist gleich im Anschluss an eine Rehabilitation statt. Der Patient ist während der Stufenweisen Wiedereingliederung noch krankgeschrieben. Mit Ausnahme von Zusatzvereinbarungen zwischen Arbeitgeber und Arbeitnehmer im Rahmen der Wiedereingliederung erhält der Patient kein Arbeitsentgelt, sondern durch die Rehabilitationsträger bereitgestellte Lohnersatzleistungen.
Bezahlung der Ersatzleistungen
Die Wiedereingliederungskosten nach einer Reha können in Form von Krankengeld, Übergangsgeld oder Verletztengeld vergütet werden. Abhängig davon, ob die Rehabilitation und Wiedereingliederung durch Krankheit, Unfall, Arbeitsunfall oder Berufskrankheit hervorgerufen wurden, tritt je nach Sachlage der entsprechende Träger ein. Obwohl der Arbeitgeber zu keinen Leistungen währen der Wiedereingliederung verpflichtet ist, besteht für ihn die Möglichkeit freiwillig Arbeitsentgelt zu entrichten. Dies kann allerdings zu einer Kürzung der Ersatzleistung führen.

Welche Bescheinigungen brauche ich für die Reha?
Die Antragstellung für eine Reha wird gemeinsam vom Patienten und dem behandelnden Arzt erstellt. Die nötigen Unterlagen sind hierbei eine ärztliche Bescheinigung, ein Arztbericht sowie ein eigenes persönliches Schreiben. Alle Dokumente müssen an den zuständigen Kostenträger geschickt werden.
Arztbescheinigungen und Antragstellung
Dank der neuen, im Jahr 2016 in Kraft gesetzten Reha-Richtlinien ist der Antragsprozess heute um vieles vereinfacht. Statt eines zeitaufwendigen zweistufigen Bescheinigungsverfahrens kann nun jeder Arzt, selbst der zuständige Hausarzt, eine medizinische Reha verordnen. Die Art der Erkrankung und Notwendigkeit der Reha muss im Zuge der Antragstellung zuerst von einem Arzt begründet werden. Neben einer Diagnose und vorgeschlagener Therapiemaßnahmen sollen hier auch die Einschränkungen des Betroffenen im Alltag erklärt werden. Ausführliche Bescheinigungen und Berichte sowie ein detailliertes persönliches Schreiben lohnen sich, da die Wahrscheinlichkeit für eine Genehmigung somit steigt. Die unterschiedlichen Kostenträger bieten online eine Vielzahl an vorgefertigten Formularen an, die schnell und einfach heruntergeladen und angepasst werden können.
Aufnahmebescheinigung der Reha – wer stellt aus?
Die Aufnahmebescheinigung für eine ambulante oder stationäre Reha wird vom zuständigen Rehabilitationsträger ausgestellt. Infrage kommen hier unter anderem die gesetzliche oder private Krankenversicherung, die Rentenversicherung oder die Unfallversicherung.
Wer stellt die Krankenmeldung während der Reha aus?
Während der medizinischen Reha muss keine eigene Krankmeldung ausgestellt werden. Um von der Arbeit freigestellt zu werden, ist es ausreichend, die Bescheinigung des Rehabilitationsträgers dem Arbeitgeber vorzulegen, welche Beginn und voraussichtliche Dauer der Reha enthält. War der Patient vor der Reha arbeitsfähig, muss der Arbeitgeber für maximal sechs Wochen Entgeltfortzahlungen leisten.

Gibt es Rehaeinrichtungen, die eine tierbegleitete Therapie anbieten?
Einige unserer MEDIAN Rehabilitationskliniken bieten eine tiergestützte Therapie an. Unter anderem arbeiten wir bei dieser Art von Behandlung mit (Therapie-)Hunden und Pferden.
Informieren Sie sich dazu gerne auf den Seiten unserer jeweiligen Klinik:
    • MEDIAN Klinik Bad Tennstedt 
    • MEDIAN Klinik Flachsheide Bad Salzuflen 
    • MEDIAN Klinik Flechtingen
    • MEDIAN Klinik Mühlengrund Bad Wildungen 
    • MEDIAN Klinik Schlangenbad 
    • MEDIAN Therapiezentrum Ravensruh

Wer genehmigt die Reha?
Die Antragstellung einer stationären oder ambulanten Reha-Behandlung muss vom zuständigen Kostenträger genehmigt werden. Hierbei kommen verschiedene Träger in Frage, wie zum Beispiel die gesetzliche Krankenversicherung, die Rentenversicherung oder die Unfallversicherung.
Welche Unterlagen werden für die Genehmigung benötigt?
Der Patient sollte dafür sorgen, dass die Unterlagen vollständig beim Kostenträger eintreffen. Ein Reha-Antrag erfordert keine speziellen Kenntnisse und kann zusammen mit einer Checkliste auf den Webseiten der verschiedenen Leistungsträger heruntergeladen oder per Telefon angefragt werden. Außerdem leisten die Träger oft zusätzliche Hilfsstellung beim Ausfüllen des Antrags. Der Patient sollte unter anderem darauf achten, die persönliche Krankengeschichte schriftlich offenzulegen. In Form eines medizinischen Gutachtens wird hier vom Hausarzt begründet, warum die Reha erforderlich ist und welche Ziele die rehabilitative Behandlung verfolgt. Der offizielle Antrag und der ärztliche Befund sollte dann umgehend an den Rehabilitationsträger zugesendet werden.
Wann wird die Reha genehmigt?
Der Kostenträger ist gesetzlich dazu verpflichtet drei Wochen nach Erhalt der Unterlagen über die Bewilligung zu entscheiden und den Patienten zu informieren. Sind die eingelangten Unterlagen vollständig und besteht ein Anspruch auf ambulante oder stationäre Reha, kommt es zu einer Genehmigung des Antrags. Manchmal kommt es hingegen zu einer Antragsablehnung. Eine finale Entscheidung ist dies allerdings nicht, da innerhalb von vier Wochen die Möglichkeit besteht, Widerspruch zu erheben. Für einen Widerspruch muss eine schriftliche Begründung sowie Stellungnahme eines Arztes beim Kostenträger eingereicht werden. Musterschreiben für Widersprüche sind oft online zu finden oder können bei Sozialverbänden oder Stellen für unabhängige Patientenberatung eingeholt werden. In vielen Fällen lohnt sich der Gebrauch des Widerspruchsrechts, da Kostenträger die Rehabilitation bei Anfechtung oftmals doch genehmigen.

Wie lange dauert eine Reha?
MEDIAN ist ein verlässlicher Partner der Rentenversicherungen, der gesetzlichen und privaten Krankenversicherungen, der Unfallversicherungsträger und - nicht zuletzt - der Patienten. Alle MEDIAN Kliniken haben die Zulassung zur Beihilfefähigkeit.
Hauptbelegungsträger sind die Deutsche Rentenversicherung Bund und die Rentenversicherungen der Länder sowie die gesetzlichen Krankenversicherungen.
Der Weg zu uns und damit zu einer wirkungsvollen Behandlung ist ganz einfach: Es gibt klar definierte Schritte für die jeweiligen Indikationen/Behandlungsschwerpunkte.

Wie oft habe ich Anspruch auf eine Reha?
Wenn Sie bereits eine Reha gemacht haben, stellt sich die Frage, wann und wie oft Sie erneut Anspruch auf eine Rehabilitation haben.

In der Regel können Sie nach vier Jahren eine weitere Reha beantragen. Reha-Anträge in kürzeren Zeitabständen haben weniger Aussicht, bewilligt zu werden. Dennoch gibt es Fälle, in denen bereits vor Ablauf der vier Jahre ein Reha-Aufenthalt nötig ist. Dies greift dann, wenn eine besonders große medizinische Erfordernis gegeben ist und eine zeitnahe Behandlung nötig ist, um Ihre Gesundheit und Leistungsfähigkeit zu schützen. Wenn Sie für die gleiche Krankheit zweimal kurz hintereinander Reha beantragen, ist dies meist schwer zu begründen. Wenn es sich aber um verschiedene Erkrankungen handelt, kann das durchaus der Fall sein. Sie könnten etwa letztes Jahr eine orthopädische Reha gemacht haben und in der Zwischenzeit ein psychosomatisches Leiden entwickelt haben, welches dringend behandelt werden muss.
Erneuter Antrag hängt von Erkrankung und Notwendigkeit ab
Wie oft Sie eine Reha machen können, hängt im Einzelfall also vom Krankheitsbild ab, zudem auch von den bisher durchgeführten Maßnahmen, um Sie zu heilen, sowie vom voraussichtlichen Behandlungserfolg eines erneuten Reha-Aufenthalts.
Soll demnach eine Reha öfter hintereinander (nach weniger als vier Jahren) erfolgen, müssen die Notwendigkeit (etwa zum Erhalt der Erwerbsfähigkeit), die Erfolgsaussichten einer langfristigen Verbesserung (positive Rehabilitationsprognose) und das Scheitern anderer Maßnahmen im Antrag sehr gut begründet und mit entsprechenden Nachweisen belegt sein. Ihr Arzt ist der beste Ansprechpartner, Ihnen hierbei zu helfen.

Wer zahlt Krankengeld während der Reha?
Reha-Kosten können landesweit von unterschiedlichen sogenannten Rehabilitationsträgern übernommen werden. In Frage kommen hier meist die gesetzliche Kranken- oder Unfallversicherung, die Rentenversicherung, Sozialämter, Jugendhilfen, die Bundesagentur für Arbeit oder Versorger von Kriegsopfern nach dem BVG.
Welcher Träger ist zuständig?
Die Antworten auf die Fragen „Wer bezahlt das Krankengeld währen der Reha?“ oder „Welche Kostenträger sind für mich zuständig?“ sind von einer Vielzahl an Faktoren abhängig. Kam es während der Arbeit zu einem Unfall, der einen Aufenthalt in einer rehabilitativen Einrichtung erforderlich macht, ist meist die Unfallversicherung des Patienten zuständig. Die Rentenversicherung tritt dann ein, wenn die Erwerbstätigkeit aufgrund einer Erkrankung nicht gewährleistet werden kann. Gesetzliche Krankenversicherungen übernehmen hingegen in der Regel die Kosten für Patienten, die bereits in Rente sind. In Sonderfällen kümmert sich das deutsche Sozialamt, die Bundesagentur für Arbeit, die Jugendhilfe oder Kriegsopferversorgung und Kriegsopferfürsorge um die Übernahme des Krankengeldes während der Reha.
Wie wird über die Zuständigkeit entschieden?
Patienten sind nicht dafür verantwortlich, den auserwählten Träger der Rehakosten ausfindig zu machen. Diese Aufgabe teilen sich die Leistungsträger nach der Antragsstellung untereinander. Der Antrag wird anschließend an den zuständigen Rehabilitationsträger weitergeleitet und verarbeitet. Gesetzlich muss der Kostenträger den Patienten innerhalb von zwei Wochen darüber informieren, welcher Träger die Kosten der Reha übernimmt.

Wie lange dauert ein Reha-Antrag bis zur Bewilligung?
Die positive Entscheidung über einen Reha-Antrag dauert in der Regel drei Wochen. Manchmal wird die Bewilligungsfrist allerdings verlängert, zum Beispiel wenn ein medizinisches Gutachten nötig ist oder wenn der Antrag beim falschen Rehabilitationsträger eingereicht wurde.
Der Weg zur Reha-Bewilligung
Egal, wo der Patient den Reha-Antrag einreicht, ist es die Aufgabe der Rehabilitationsträger zu klären, wer für die Bewilligung und Kostenübernahme zuständig ist. Folglich muss sich der Patient nicht darum sorgen, dass der Antrag an die falsche Stelle gelangt. Im Falle einer falsch adressierten Antragstellung werden die Dokumente an den richtigen Rehabilitationsträger weitergeleitet. Da dieser Schritt zusätzlich Zeit kostet, verlängert die Weiterleitung die Bewilligungsfrist auf Seiten des Kostenträgers um zwei Wochen. Wünscht der Patient eine schnelle Verarbeitung des Antrags wird ihm deshalb nahegelegt, sich vor der Einreichung ausreichend zu informieren und die Unterlagen selbstständig an den zuständigen Leistungsträger zu senden.
Die Bewilligungsfrist
Wie bereits erwähnt, dauert die Bewilligung eines Reha-Antrags in der Regel drei Wochen. Hier ist zu beachten, dass die dreiwöchige Frist nur dann gilt, wenn die beim Reha-Träger eingereichten Unterlagen vollständig sind. Laut § 14 SGB IX des Sozialgesetzbuches muss der Leistungsträger innerhalb von 14 Tagen prüfen, ob er nach dem für ihn geltenden Leistungsgesetz für die Leistung zuständig ist. Ist er nicht zuständig, muss der Antrag unverzüglich an den zuständigen Rehabilitationsträger weitergereicht werden. Hat der Antragstellende die Anfrage an den richtigen Reha-Träger adressiert, muss dieser nicht weitergeleitet werden. In diesem Fall hat der Patient das Recht, innerhalb einer zusätzlichen Woche über den positiven Bescheid informiert zu werden. In manchen Fällen benötigt der Leistungsträger ein ärztliches Gutachten, um eine Entscheidung über die Bewilligung treffen zu können. Wird dieses eingefordert, erhält der Entscheidungsträger weitere zwei Wochen ab Eingang des Gutachtens, um den Bescheid zu bewilligen oder abzulehnen. Die Antragstellung und Bewilligung eines Reha-Antrags ist ein langwieriger Prozess. Durch unvollständige Unterlagen, die Zusendung an den falschen Kostenträger oder durch die Einforderung eines medizinischen Gutachtens können Fristen um Wochen verlängert werden. Soll eine Bewilligung rasch erfolgen, wird dem Patienten deshalb geraten, gut zu planen und alle Dokumente parat zu haben.

Häufige Fragen zur Reha Bewilligung
Wie lange dauert ein Reha-Antrag bis zur Bewilligung?
Der Entscheidungsprozess bis zur Bewilligung eines Reha-Antrags dauert in der Regel drei Wochen. Wird ein medizinisches Gutachten benötigt oder wurde der Antrag beim falschen Rehabilitationsträger eingereicht, kann sich die Bewilligungsfrist verlängern.
Wann meldet sich die Rehaklinik nach der Genehmigung?
Der Leistungsträger muss einen Reha-Antrag innerhalb von 14 Tagen prüfen. Wenn der Reha-Antrag genehmigt wird, meldet sich die Klinik innerhalb einer weiteren Woche beim Patienten, um ihn über die Bewilligung zu informieren.
Wie lange dauert ein Reha-Antrag im Eilverfahren?
Ähnlich wie bei einem üblichen Reha-Antrag ist die Bearbeitungszeit eines Reha-Antrages im Eilverfahren von der Aktenlage abhängig. Werden Anträge unvollständig oder bei dem falschen Rehabilitationsträger eingereicht, kann sich die Bearbeitungszeit verlängern. Ebenso ist es möglich, dass vorab eine ambulante Untersuchung eines Arztes des Kostenträgers erbeten wird. Abhängig von diesen Faktoren dauert ein Reha-Antrag im Eilverfahren zwischen drei bis acht Wochen.
Wie lange ist die Reha-Wartezeit nach der Bewilligung?
Nach der Bewilligung eines Reha-Aufenthaltes kann man mit einer Wartezeit von drei bis acht Wochen bis zum Beginn der Rehabilitation rechnen. Reha-Anträge im Eilverfahren werden bevorzugt und daher zeitnaher eingeladen.

Was ist der Unterschied zwischen Kur und Reha?
Kur und Reha: Im Alltagsgebrauch werden diese beiden Begriffe oft vermischt. Tatsächlich gibt es aber Unterschiede zwischen Reha und Kur.

Grundsätzlich kann man sagen, dass eine Kur bei einem gesunden Menschen ansetzt, der erste Symptome aufweist, während eine Reha für einen bereits erkrankten Menschen gedacht ist. Eine Kur ist also präventiv; es handelt sich um Maßnahmen zur Festigung der Gesundheit. Eine Reha dient dagegen stets der Wiederherstellung der Gesundheit nach einer Erkrankung.
Reha versus Kur: unterschiedliche Behandlungsansätze
Folglich unterscheiden sich Kur und Reha auch durch ihren Aufbau und die Behandlungen. Bei einer Kur stehen häufig Massagen, Moorpackungen, Bäder und Spaziergänge auf dem Programm. Der Wellness-, Urlaubs- und Entspannungscharakter ist entsprechend stark ausgeprägt. Im Rahmen einer Reha, bei der z.B. die Beweglichkeit nach einer OP wiederhergestellt werden soll, ist die aktive Mitarbeit der Patienten gefordert. Die medizinischen Maßnahmen beinhalten Physio- und Sporttherapie, Ergotherapie, Psychotherapie oder auch Trainingseinheiten zu Spezialthemen wie z.B. Stressbewältigung. Zudem wird den Patienten auch für die Zeit nach der Reha wichtiges Wissen mit an die Hand gegeben, um den wiedererlangten Gesundheitszustand zu erhalten und eine erneute Verschlechterung zu vermeiden.

Ein weiterer Unterschied zwischen Reha und Kur betrifft die Kostenübernahme: Die Vorsorgemaßnahmen (nach §111a SGB V) werden nur von den Krankenkassen erbracht oder können als Selbstzahler in Anspruch genommen werden, während eine Reha von allen Kostenträgern bewilligt werden kann.

Die MEDIAN Kliniken sind spezialisiert auf Rehabilitationsmaßnahmen. Dennoch werden in einigen Einrichtungen auch Vorsorgeleistungen angeboten – die Sie als Kur buchen können oder beispielsweise auch Ihre Begleitperson bei einer Reha für sich nutzen kann.

FAQ Mediangruppe - Fragen zu speziellen Indikationen

Wann ist eine Reha bei Depressionen sinnvoll?
Trotz guter Therapiemöglichkeiten ist die Behandlung von Depressionen in einer Rehaklinik manchmal unumgänglich. Eine Rehabilitation bei Depression empfiehlt sich besonders dann, wenn sich der Patient über einen langen Zeitraum in einem intensiven depressiven Zustand befindet und ambulante Therapien zu keiner Besserung beitragen. 
Weitere Anzeichen für den Bedarf an einer Reha-Behandlung
Die Behandlung depressiver Erkrankungen in einer Klinik sollte von jenen Patienten in Erwägung gezogen werden, deren Erkrankung einen klaren negativen Einfluss auf das Alltags-, Familien- und Berufsleben nimmt. Das vermehrte Auftreten und die gesteigerte Intensität von depressiven Phasen führt bei Erkrankten oft dazu, dass ambulante Psychotherapien nicht ausreichend helfen. Unter diesen Umständen sollte auf jeden Fall eine stationäre rehabilitative Behandlung in einer Klinik in Betracht gezogen werden.
Ziele einer rehabilitativen Behandlung
Mithilfe einer klinischen Behandlung können neben der direkten Behandlung einer Depression auch neue Behandlungsmöglichkeiten und Rehabilitationsoptionen erkundet werden. Eine stationäre Reha ist durch ihre Kombination aus Psychotherapie, Sport- und Physiotherapie sowie Sozialberatung für Patienten mit schwerer Erkrankung sehr sinnvoll. Das Ziel der Behandlung ist es, eine stabile psychosoziale und berufliche Leistungsfähigkeit des Patienten aufzubauen und die Chancen für zukünftige Wiedererkrankungen oder Rückfälle möglichst gering zu halten.
Wer übernimmt die Kosten?
Der Kostenträger für die Reha hängt von der beruflichen Situation des Patienten ab. Im Falle, dass der Patient noch erwerbstätig ist, übernimmt meist die Deutsche Rentenversicherung die Kosten für stationäre Reha-Behandlungen von Depressionen. Alternativ kann auch die Krankenkasse als Kostenträger infrage kommen und die Rehabilitation bezahlen.

Was ist eine neurologische Frührehabilitation?
Was ist zu tun, wenn zum Beispiel der eigene Vater einen Schlaganfall erlitten hat und sich schon im Krankenhaus daraus resultierende (schwere) neurologische Schädigungen bemerkbar machen? Um die Chancen für eine Rückkehr in ein selbständiges Leben vollends auszuschöpfen, ist die Aufnahme rehabilitativer Maßnahmen so früh wie möglich zu empfehlen. Hier setzt die neurologische Frührehabilitation an, die noch während der Beatmung mit dem rehabilitativen Programm beginnt.
Phasenmodell der Reha-Behandlung
In vielen Fällen beginnt die Frührehabilitation bereits während des stationären Krankenhausaufenthaltes oder wird entsprechend in einer Einrichtung für Frührehabilitation aufgenommen bzw. fortgeführt. Gekennzeichnet ist eine solche Rehabilitation als „Phase B“ in dem Phasenmodell der neurologischen Rehabilitation, da sie direkt an die Akutphase (Phase A) anschließt. Im Rahmen der neurologischen Frührehabilitation können sieben der 14 neurologischen Abteilungen von MEDIAN Patienten bereits wenige Tage nach dieser Akutphase aus dem Krankenhaus in die Rehabilitationsklinik übernehmen.
Ziele der neurologischen Frührehabilitation
Besonders Menschen mit schwersten Hirnschädigungen sind oftmals nicht in der Lage, an deren vorheriges eigenständiges Leben anzuknüpfen. Um solchen Personen einen möglichst unabhängigen Einstieg in deren Alltag zu ermöglichen, werden sie während der Frührehabilitation intensivmedizinisch betreut. Dabei erfolgt eine permanente Überwachung sowie Stabilisierung des Herzens, der Atmung als auch des Kreislaufs. Durch umfassende rehabilitative Maßnahmen soll das Ziel der Besserung des Bewusstseinszustandes und die Herstellung der aktiven Mitarbeit des Patienten erreicht werden. Dies wird durch die Einrichtung neurologischer Stationen auf Intensivniveau ermöglicht, die auch Patienten versorgen können, welche im überwachungspflichtigen Zustand in die neurologische Rehabilitationsklinik verlegt werden müssen.

Wann ist eine Reha nach Bandscheiben-OP sinnvoll?
Obwohl eine Bandscheibenoperation in der Medizin keine Seltenheit ist, steht die Frage einer klinischen Nachbehandlung meist offen. Experten sind sich hingegen einig, dass eine Reha nach einer Bandscheiben-OP für den Patienten absolut sinnvoll ist, um den Genesungsprozess zu beschleunigen, Schmerzen zu lindern und einen früheren Wiedereintritt in den Alltag ermöglichen.
Bandscheiben-OP – der Ablauf
Ein akuter Bandscheibenvorfall, auch Bandscheibenprolaps genannt, erfordert nicht immer einen operativen Eingriff (konservative Rehabilitation des Bandscheibenvorfalls). Sind die Beschwerden allerdings zu stark, muss in der Regel eine Operation durchgeführt werden, wo das geschädigte Bandscheibengewebe und Teile der betroffenen Bandscheibe entfernt werden. Mit deutschlandweit über 140.000 Bandscheibenoperationen pro Jahr ist der Eingriff bereits sehr fortgeschritten. Er erfordert meist einen nur sehr kurzen Nachaufenthalt des Patienten im Krankenhaus von 3-5 Tagen.
Rehabilitation nach der Bandscheiben-OP
Eine Reha nach eine Bandscheiben OP ist sehr empfehlenswert und kann in einer selbst ausgewählten Rehaklinik durchgeführt werden. Basierend auf den Empfehlungen des Operateurs und dem Befund wird in der Regel ein Plan zur physiotherapeutischen Behandlung (Krankengymnastik) aufgestellt. Der Plan beinhaltet meist physiotherapeutische Übungen und Gerätetrainings mit unter anderem Wassergymnastikübungen und Rückenschulelementen, die den Muskelaufbau nach der OP unterstützen. Im Zuge der Rehabilitation nach einer Bandscheiben-OP erfolgt auch oft eine Ernährungsberatung und psychologische Behandlung.
Ziele der Reha-Behandlung
Die klinische Rehabilitation nach einer Bandscheibenoperation verfolgt eine Vielzahl an körperlichen und psychischen/sozialen Ziele. Körperlich wird an einer Reduktion der Muskelanspannung, der Minimalisierung der Bewegungseinschränkung, der Vermeidung von Fehlhaltungen, dem post-operativen Muskelaufbau und der Verbesserung der Mobilität gearbeitet. Außerdem werden verschiedenste psychische und soziale Ziele wie erhöhtes Selbstvertrauen, höhere Lebensfreude und Lebensqualität und eine erfolgreiche Rückkehr in den Familien-, Freizeit- und Berufsalltag verfolgt.

Wann ist eine Reha nach Bandscheiben-OP sinnvoll?
Obwohl eine Bandscheibenoperation in der Medizin keine Seltenheit ist, steht die Frage einer klinischen Nachbehandlung meist offen. Experten sind sich hingegen einig, dass eine Reha nach einer Bandscheiben-OP für den Patienten absolut sinnvoll ist, um den Genesungsprozess zu beschleunigen, Schmerzen zu lindern und einen früheren Wiedereintritt in den Alltag ermöglichen.
Bandscheiben-OP – der Ablauf
Ein akuter Bandscheibenvorfall, auch Bandscheibenprolaps genannt, erfordert nicht immer einen operativen Eingriff (konservative Rehabilitation des Bandscheibenvorfalls). Sind die Beschwerden allerdings zu stark, muss in der Regel eine Operation durchgeführt werden, wo das geschädigte Bandscheibengewebe und Teile der betroffenen Bandscheibe entfernt werden. Mit deutschlandweit über 140.000 Bandscheibenoperationen pro Jahr ist der Eingriff bereits sehr fortgeschritten. Er erfordert meist einen nur sehr kurzen Nachaufenthalt des Patienten im Krankenhaus von 3-5 Tagen.
Rehabilitation nach der Bandscheiben-OP
Eine Reha nach eine Bandscheiben OP ist sehr empfehlenswert und kann in einer selbst ausgewählten Rehaklinik durchgeführt werden. Basierend auf den Empfehlungen des Operateurs und dem Befund wird in der Regel ein Plan zur physiotherapeutischen Behandlung (Krankengymnastik) aufgestellt. Der Plan beinhaltet meist physiotherapeutische Übungen und Gerätetrainings mit unter anderem Wassergymnastikübungen und Rückenschulelementen, die den Muskelaufbau nach der OP unterstützen. Im Zuge der Rehabilitation nach einer Bandscheiben-OP erfolgt auch oft eine Ernährungsberatung und psychologische Behandlung.
Ziele der Reha-Behandlung
Die klinische Rehabilitation nach einer Bandscheibenoperation verfolgt eine Vielzahl an körperlichen und psychischen/sozialen Ziele. Körperlich wird an einer Reduktion der Muskelanspannung, der Minimalisierung der Bewegungseinschränkung, der Vermeidung von Fehlhaltungen, dem post-operativen Muskelaufbau und der Verbesserung der Mobilität gearbeitet. Außerdem werden verschiedenste psychische und soziale Ziele wie erhöhtes Selbstvertrauen, höhere Lebensfreude und Lebensqualität und eine erfolgreiche Rückkehr in den Familien-, Freizeit- und Berufsalltag verfolgt.

Wie ist der Ablauf einer onkologischen Reha?
#Survivor – Die Nachricht einer Krebsdiagnose ist zweifellos ein sehr großer Schock für jeden Erkrankten. Vor allem die Organe der Lunge, weiblichen Brust, Prostata, aber ebenso auch des Darms sind sehr häufig vom Krebs befallen. Nichtsdestotrotz besteht in den meisten Fällen die Chance auf Heilung. Ist die Akutbehandlung erst einmal abgeschlossen, benötigen eine jährlich zunehmende Anzahl an Patienten eine Nachsorge bzw. Weiterbehandlung, welche ebenso als onkologische Rehabilitation erfolgen können.
Ablauf einer onkologischen Rehabilitation
Bereits zu Anfang der Rehabilitation findet eine medizinische und fachlich onkologische Bestandsaufnahme statt. Auf Basis derer werden gemeinsam mit dem Patienten ein oder mehrere Ziele der onkologischen Reha gesetzt. Um diese zu erreichen, werden dem Patienten im Rahmen der angeordneten Rehabilitation bestimmte Einheiten aktiver Anwendungen verordnet. Hierzu zählen Ergotherapie, Sporttherapie sowie Krankengymnastik. Ziele solcher Anwendungen sind vor allem eine Förderung der Ausdauer, Kraft und Koordination. Doch auch wichtige Informationen zu ihrer Krankheit, deren Behandlung, zu einer anzustrebenden gesundheitsbewussten Lebensweise und einer nachhaltigen Planung, bzw. Änderung des Lebensstils sind von bedeutsamer Wichtigkeit. Aus diesem Grund werden während einer onkologischen Rehabilitationsbehandlung ebenfalls Vorträge und Seminare, als auch Gesprächskreise sowie Einzelgespräche durchgeführt.
Kommt eine onkologische Reha für mich in Betracht?
Grundsätzlich eignet sich eine onkologische Rehabilitation für jede der vielzähligen Krebserkrankungen. Grundsätzlich wird für jeden Patienten, welcher sich für eine onkologische Reha bei einer unserer MEDIAN Kliniken entscheidet, ein individuelles Reha-Programm konstituiert. Dieses bezieht verschiedenste Faktoren mit ein, wie unter anderem das spezifische Krankheitsbild, die daraus resultierenden körperlichen Defizite sowie die eigene häusliche oder gegebenenfalls auch die berufliche und soziale Situation.

Welche Behandlungen umfasst eine Reha nach Herzinfarkt?
Etwa 280.000 Menschen erleiden jährlich einen Herzinfarkt in Deutschland – eine besonders hohe Anzahl. Auch, wenn die Zahl der Todesfälle nach einem solchen Infarkt stetig abnimmt, ist der Herzinfarkt sehr bedrohlich und kann bei zu spätem Handeln zum Tode führen. Deshalb gilt dieser auch weiterhin als Haupttodesursache in Deutschland. Demzufolge ist es umso bedeutsamer, eine kardiologische Rehabilitation als Herzpatient durchzuführen.
Fünf maßgebliche Bausteine
Die kardiologische Rehabilitation besteht insgesamt aus fünf fundamentalen „Bausteinen“: So werden auf eine medizinische Therapie, eine gesunde Ernährung, ein regelmäßiges Training, Entspannungsübungen sowie bestenfalls auf eine stückweise Entwöhnung des Tabakkonsums gesetzt. Die Behandlungspläne einer solchen Rehabilitation vereinen psychotherapeutische Verfahren, körperliche Übungs- und Trainingsbehandlungen, Informationsveranstaltungen und Schulungen sowie Beratung in sozialen Fragen. Auch die Behandlung von Begleiterkrankungen wird angeboten.
Dauer einer kardiologischen Rehabilitation
Im Regelfall beschränkt sich die Dauer einer kardiologischen Rehabilitation auf drei Wochen. Bei einer ausreichenden medizinischen Notwendigkeit ist eine Verlängerung des Aufenthalts in einer Rehabilitationseinrichtung jedoch grundsätzlich möglich. Über eine Verlängerung der Rehabilitation entscheidet grundsätzlich der Kostenträger.
Ziele der Reha-Behandlung
Die verfolgten Ziele einer kardiologischen Reha beziehen sich auf viele verschiedene physische, als auch psychische Aspekte. Das primäre Bestreben ist es, die Förderung einer aktiv-problemorientierten Krankheitsverarbeitung mit Hilfe von Information, Kompetenztraining, Spannungsreduktion sowie eine Verminderung von Angst, Depression und Isolation hervorzurufen.

Wie erkennt man, ob jemand alkoholabhängig ist?
Folgende Indikationen können auf eine Alkoholabhängigkeit hindeuten:
    • Ein starkes Verlangen nach Alkohol.
    • Geringe Kontrolle über das Ausmaß des Konsums.
    • Körperliche Entzugserscheinungen, wenn kein Alkohol konsumiert wird.
    • Steigende Toleranz gegenüber Alkohol und damit einhergehend eine steigende Menge die getrunken wird.
    • Alkohol nimmt eine immer wichtigere Rolle im Alltag ein und seine Begleiterscheinungen, wie seine Beschaffung, nehmen zunehmend Zeit in Anspruch.
    • Alkohol wird wider besseren Wissens seiner schädlichen Folgen (körperlich, psychisch oder sozial) konsumiert.
Alkoholabhängigkeit ist weit verbreitet in Deutschland. Laut dem Bundesministerium für Gesundheit sind etwa 1,9 Millionen Deutsche alkoholabhängig. Dabei wird auch von einer hohen Dunkelziffer ausgegangen. Dementsprechend gelten circa drei Prozent der Erwachsenen als alkoholabhängig. Eine Abhängigkeit entsteht schleichend. Da Alkohol meist in Gesellschaft konsumiert wird und dies als gesellig gilt, ist es oftmals schwierig, den Beginn einer Abhängigkeit festzustellen.
Sofern Sie das Gefühl haben, Ihr Konsum ist ungewöhnlich hoch und Ihnen fällt der Verzicht auf Alkohol sehr schwer, ist es ratsam, sich an eine qualifizierte Beratungsstelle oder einen Arzt zu wenden. Für eine erste Einschätzung können Sie zunächst online einen Kurzfragebogen ausfüllen (z. B. den CAGE-Fragebogen). Auch die Bundeszentrale für gesundheitliche Aufklärung bietet einen Selbsttest an.
Weitere Informationen zur Krankheit und deren Behandlung in einer MEDIAN Rehaklinik finden Sie hier.

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
