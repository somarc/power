"""Greene-cited court: figures and the law each one carries.

Alcibiades is one file among many. Dualform plates live under
/media/dualform/{slug}-a.webp and -b.webp when generated.
"""

MEDIA = "https://content.da.live/somarc/power/media"

# slug -> identity. `laws` are the rooms they own in this corpus.
FIGURES = {
    "louis-xiv": {
        "name": "Louis XIV",
        "years": "1638–1715",
        "epithet": "The Sun King",
        "laws": [1, 4, 16, 34, 37, 41],
        "ref": "Hyacinthe Rigaud, coronation portrait, 1701, Louvre (PD-Art).",
        "dossier": (
            "The gravitational body of Greene’s European court. He imprisoned Fouquet "
            "for a party that outshone him, answered ministers with “I shall see,” "
            "withdrew like the sun to raise his price, acted royal until the world "
            "agreed, and turned Versailles into a permanent spectacle. Louis XVI later "
            "died in the dent of those shoes."
        ),
    },
    "fouquet": {
        "name": "Nicolas Fouquet",
        "years": "1615–1680",
        "epithet": "The finance minister who threw the wrong party",
        "laws": [1],
        "ref": "Portrait of Nicolas Fouquet, 17th c., public-domain photograph.",
        "dossier": (
            "Vaux-le-Vicomte, 17 August 1661. Molière, Vatel, fireworks, a château "
            "that made the king look like a guest. Voltaire recorded the fall. "
            "Fouquet spent the rest of his life in Pinerolo. Law 1’s transgression "
            "has a street address."
        ),
    },
    "galileo": {
        "name": "Galileo Galilei",
        "years": "1564–1642",
        "epithet": "The observer who dedicated the sky",
        "laws": [1],
        "ref": "Justus Sustermans, National Maritime Museum (PD-Art).",
        "dossier": (
            "Greene’s observance of Law 1: the moons of Jupiter named for the Medici. "
            "He made Cosimo II feel like the universe had a family crest. The telescope "
            "was the gift; the flattery was the politics."
        ),
    },
    "napoleon": {
        "name": "Napoleon Bonaparte",
        "years": "1769–1821",
        "epithet": "The emperor Talleyrand outlasted",
        "laws": [8, 39, 47],
        "ref": "Jacques-Louis David, The Emperor Napoleon in His Study, 1812 (PD-Art).",
        "dossier": (
            "Greene often lists him as the man who held vast power and still lost the "
            "long game to a courtier. He made Europe come to him, stirred waters, then "
            "walked past the mark into Russia. St. Helena is the reversal of Law 47."
        ),
    },
    "talleyrand": {
        "name": "Charles-Maurice de Talleyrand-Périgord",
        "years": "1754–1838",
        "epithet": "The man who survived every regime",
        "laws": [2, 8, 10, 14, 24, 35],
        "ref": "Portrait of Talleyrand, early 19th c. (PD-Art).",
        "dossier": (
            "Bishop, revolutionary, imperial vice-grand elector, Restoration foreign "
            "minister. Greene’s courtier of courtiers: he used former enemies, made "
            "them come to him, avoided the infected, spied while dining, played the "
            "perfect court, and timed every surrender. Napoleon had the army. "
            "Talleyrand had the next government."
        ),
    },
    "bismarck": {
        "name": "Otto von Bismarck",
        "years": "1815–1898",
        "epithet": "The chancellor who concealed a country",
        "laws": [3, 11, 23, 29, 31],
        "ref": "Photographic portrait of Bismarck (PD).",
        "dossier": (
            "He professed peace while designing Denmark, Austria, and France as "
            "hinges. Concentration, dependency, options, and a last page: a German "
            "empire under Prussia. When the last page was written, he was the only "
            "man who had read it in advance."
        ),
    },
    "elizabeth-i": {
        "name": "Elizabeth I",
        "years": "1533–1603",
        "epithet": "The queen who would not marry the realm away",
        "laws": [20, 43],
        "ref": "Darnley portrait, National Portrait Gallery (PD-Art).",
        "dossier": (
            "Greene’s lesson in non-commitment: suitors as foreign policy, never a "
            "husband as a master. Hearts and minds of a nervous island, held for "
            "forty-five years by refusing to pick a side that would own her."
        ),
    },
    "cesare-borgia": {
        "name": "Cesare Borgia",
        "years": "1475–1507",
        "epithet": "The duke who borrowed a headsman",
        "laws": [5, 15, 26],
        "ref": "Portrait traditionally identified as Cesare Borgia (PD-Art).",
        "dossier": (
            "Machiavelli watched him. Ramiro de Lorqua was left in two pieces in a "
            "Cesena piazza on Christmas morning, 1502 — the deputy’s cruelty blamed, "
            "the duke’s hands washed, the city terrified into order. Reputation, "
            "total crush, clean hands: three laws on one square."
        ),
    },
    "julius-caesar": {
        "name": "Julius Caesar",
        "years": "100–44 BCE",
        "epithet": "The man who recrossed as a different self",
        "laws": [25, 28],
        "ref": "Roman marble portrait bust (PD).",
        "dossier": (
            "Greene wrote the book after rereading a Caesar life and the Rubicon. "
            "Recreate yourself; enter bold. The Ides is the reversal of going past "
            "the mark and of appearing too singular."
        ),
    },
    "richelieu": {
        "name": "Cardinal Richelieu",
        "years": "1585–1642",
        "epithet": "The minister who found the king’s screw",
        "laws": [11, 33],
        "ref": "Philippe de Champaigne, portrait of Richelieu (PD-Art).",
        "dossier": (
            "Louis XIII’s insecurity was a thumbscrew. Richelieu turned it until "
            "the state ran through one red cap. Keep them dependent; know the nerve."
        ),
    },
    "fouche": {
        "name": "Joseph Fouché",
        "years": "1759–1820",
        "epithet": "The police of every France",
        "laws": [26, 35],
        "ref": "Portrait of Joseph Fouché (PD-Art).",
        "dossier": (
            "Terror, Directory, Consulate, Empire, Restoration. Greene’s timing "
            "virtuoso and cleaner of hands: he always had a file, never a flag he "
            "could not take down overnight."
        ),
    },
    "barnum": {
        "name": "P. T. Barnum",
        "years": "1810–1891",
        "epithet": "The man who sold the crowd to itself",
        "laws": [5, 6, 37],
        "ref": "Photographic portrait of P. T. Barnum (PD).",
        "dossier": (
            "Reputation as a circus, attention as inventory, spectacle as the "
            "product. Greene’s American court: if they are looking, you can charge."
        ),
    },
    "edison": {
        "name": "Thomas Edison",
        "years": "1847–1931",
        "epithet": "The name on other people’s nights",
        "laws": [7],
        "ref": "Photographic portrait of Edison (PD).",
        "dossier": (
            "Tesla redesigned the dynamos. The name on the current was Edison’s. "
            "Greene’s Law 7 in a Menlo Park key: labor is hireable; the byline is not."
        ),
    },
    "tesla": {
        "name": "Nikola Tesla",
        "years": "1856–1943",
        "epithet": "The man who did the nights",
        "laws": [7],
        "ref": "Photographic portrait of Tesla (PD).",
        "dossier": (
            "The other pole of Law 7. Eighteen-hour days, a promise of fifty "
            "thousand dollars, a laugh. The work remained. The credit did not."
        ),
    },
    "alcibiades": {
        "name": "Alcibiades",
        "years": "c. 450–404 BCE",
        "epithet": "The man who changed cities",
        "laws": [24, 25, 46, 48],
        "ref": "Capitoline MC 1160, so-called Alcibiades, Marie-Lan Nguyen 2011, CC BY 2.5.",
        "dossier": (
            "Greene’s shapeshifter and the warning against looking too perfect. "
            "Courtier, self-recreation, formlessness — and the envy that kills the "
            "unflawed face. One file in the court, not the court itself."
        ),
    },
    "wu-zetian": {
        "name": "Wu Zetian",
        "years": "624–705",
        "epithet": "The empress who finished the rival",
        "laws": [15],
        "ref": "Later portrait type of Wu Zetian (PD-Art).",
        "dossier": (
            "Greene’s crush-totally: not a wound left to organize. The Tang court "
            "learned what an unfinished enemy costs."
        ),
    },
    "haile-selassie": {
        "name": "Haile Selassie",
        "years": "1892–1975",
        "epithet": "The emperor who struck the shepherds",
        "laws": [3, 42],
        "ref": "Photographic portrait (PD / historic).",
        "dossier": (
            "Concealment and decapitation of rival centers. Greene uses the Ethiopian "
            "court as a modern lesson in removing the person the flock faces."
        ),
    },
    "claudius": {
        "name": "Claudius",
        "years": "10 BCE–54 CE",
        "epithet": "The fool who became emperor",
        "laws": [21],
        "ref": "Roman portrait of Claudius (PD).",
        "dossier": (
            "Seem dumber than the mark. Suetonius and Cassius Dio record the limp "
            "and the stammer that kept him alive until the Praetorians needed a name."
        ),
    },
    "columbus": {
        "name": "Christopher Columbus",
        "years": "1451–1506",
        "epithet": "The man who sold a western Indies",
        "laws": [32, 34],
        "ref": "Posthumous portrait type (PD-Art).",
        "dossier": (
            "Fantasy as capital: a shorter road to spice. Royal carriage as costume. "
            "Greene’s observance of playing to a crown’s dream and walking in as if "
            "already titled."
        ),
    },
    "qin-shi-huang": {
        "name": "Qin Shi Huang",
        "years": "259–210 BCE",
        "epithet": "The first emperor in a fortress of his own making",
        "laws": [18],
        "ref": "Later portrait type (PD-Art).",
        "dossier": (
            "Isolation as transgression: the man who unified China and then could "
            "not hear the courtyard. Greene’s warning against the bunker."
        ),
    },
    "de-gaulle": {
        "name": "Charles de Gaulle",
        "years": "1890–1970",
        "epithet": "The general who left so he could be recalled",
        "laws": [16],
        "ref": "Photographic portrait (PD).",
        "dossier": (
            "Absence as a raise in price. Colombey-les-Deux-Églises was a stage "
            "direction. France came to get him."
        ),
    },
    "rasputin": {
        "name": "Grigori Rasputin",
        "years": "1869–1916",
        "epithet": "The stare that organized a palace",
        "laws": [27],
        "ref": "Photographic portrait (PD).",
        "dossier": (
            "Need to believe, given a body. Greene’s cult: a court already hungry "
            "for a plot, offered a holy man who could stop a boy’s bleeding."
        ),
    },
    "catherine-ii": {
        "name": "Catherine II",
        "years": "1729–1796",
        "epithet": "The empress of apparent ease",
        "laws": [30],
        "ref": "Lampi or Rokotov portrait type (PD-Art).",
        "dossier": (
            "Accomplishments as nature. Coups, code, correspondence with Voltaire — "
            "backstage labor, public wu-wei. Greene’s effortlessness in a St. Petersburg key."
        ),
    },
    "rothschild": {
        "name": "Nathan Rothschild",
        "years": "1777–1836",
        "epithet": "The hinge of the money",
        "laws": [23, 40],
        "ref": "Portrait of Nathan Mayer Rothschild (PD-Art).",
        "dossier": (
            "Concentrate the force; despise the free lunch. Information from Waterloo "
            "as a concentrated bet. Payment as independence."
        ),
    },
}

# Per-law primary case from Greene’s illustrations (titles only; original prose).
LAW_CASES = {
    1: {
        "figure": "fouquet",
        "also": ["louis-xiv", "galileo"],
        "history": (
            "Nicolas Fouquet, Vaux-le-Vicomte, 17 August 1661. Molière on the boards, "
            "Vatel in the kitchens, fireworks over a château that made Louis XIV feel "
            "like a guest in his own kingdom. Voltaire recorded the arc: by morning the "
            "finance minister was ruined; he died in the fortress of Pinerolo. "
            "Greene’s observance sits next to it: Galileo naming Jupiter’s moons for "
            "the Medici so Cosimo II would feel the sky had a family."
        ),
    },
    2: {
        "figure": "talleyrand",
        "also": ["louis-xiv"],
        "history": (
            "Michael III of Byzantium made his companion Basilius Caesar; the friend "
            "murdered him. Greene sets against that the converted enemy — Song Taizu "
            "pouring wine for generals and sending them home rich and watched. "
            "Talleyrand’s entire career is the European version: every former camp "
            "had to keep proving the conversion."
        ),
        "reversal": (
            "An enemy converted too cheaply is still an enemy with a badge. "
            "Basilius proved the friendship was a ladder. The conversion had been useful, not true."
        ),
    },
    3: {
        "figure": "bismarck",
        "also": ["haile-selassie"],
        "history": (
            "Otto von Bismarck professed peace while designing three wars as rungs. "
            "Denmark, Austria, France — each a hinge, none announced as the house. "
            "Haile Selassie, in Greene’s modern court, kept the destination off the "
            "table until the shepherds were already moving."
        ),
    },
    4: {
        "figure": "louis-xiv",
        "also": [],
        "history": (
            "Louis XIV’s ministers would finish their case. He would say, “I shall see,” "
            "and walk away. Weeks later a decision arrived with no extra words attached. "
            "Coriolanus is the transgression: the mouth that could not stop giving "
            "Rome a reason. Plutarch’s Life of Coriolanus is the bill."
        ),
    },
    5: {
        "figure": "barnum",
        "also": ["cesare-borgia"],
        "history": (
            "P. T. Barnum built a name that fought before he entered the room, then "
            "spent a life feeding it. Cesare Borgia used the opposite knife: Ramiro "
            "de Lorqua’s split body in a Cesena square, Christmas 1502, so the duke’s "
            "reputation for order could land on a clean street."
        ),
    },
    6: {
        "figure": "barnum",
        "also": ["louis-xiv"],
        "history": (
            "Barnum again: attention as inventory. Cleopatra’s barge in Plutarch’s "
            "Antony is the classical billboard. Louis XIV’s lever — make the court "
            "look at the sun or look at nothing — is the same physics in ermine."
        ),
    },
    7: {
        "figure": "edison",
        "also": ["tesla"],
        "history": (
            "Nikola Tesla offered to redesign Edison’s dynamos. Edison named a figure. "
            "The nights were Tesla’s; the current kept Edison’s name. Rubens’s studio "
            "is Greene’s older version: many hands, one signature."
        ),
    },
    8: {
        "figure": "napoleon",
        "also": ["talleyrand"],
        "history": (
            "Napoleon made Europe cross his courtyard — treaties at his table, not "
            "theirs. Talleyrand then made Napoleon’s enemies come to a man without "
            "an army. The bait was a future France they could live in."
        ),
    },
    9: {
        "figure": "galileo",
        "also": [],
        "history": (
            "Michelangelo did not win the Sistine by argument; the ceiling ended the "
            "meeting. Greene’s Chinese generals do the same: a finished maneuver "
            "beats a won debate. The stone that cannot be put back is the sentence."
        ),
    },
    10: {
        "figure": "talleyrand",
        "also": [],
        "history": (
            "Lola Montez infected Ludwig I’s court until Bavaria paid. Marie "
            "Antoinette’s circle carried a smell. Talleyrand’s genius was medical: "
            "he left rooms before the luck went rancid. Fouché filed the rest."
        ),
    },
    11: {
        "figure": "richelieu",
        "also": ["bismarck"],
        "history": (
            "Richelieu made Louis XIII’s state unable to run without the red cap. "
            "Bismarck made German princes unable to imagine a map without Prussia. "
            "Kissinger, in Greene’s later rooms, rented the same lease in a century "
            "of telephones."
        ),
    },
    12: {
        "figure": "fouche",
        "also": [],
        "history": (
            "Count Victor Lustig sold the Eiffel Tower to a scrap dealer with one "
            "expensive honesty: a real ministry letterhead, a real lunch. Selective "
            "truth as solvent. Fouché’s files worked the same way — one true name "
            "made ten implications land."
        ),
    },
    13: {
        "figure": "talleyrand",
        "also": [],
        "history": (
            "Castruccio Castracani, in Machiavelli’s life of him, asked no one for "
            "mercy. He offered interest. Greene’s farmer and stork is the fable "
            "version: help that does not pay is not help. Talleyrand never pitched "
            "gratitude. He pitched the next regime’s convenience."
        ),
    },
    14: {
        "figure": "talleyrand",
        "also": ["fouche"],
        "history": (
            "Joseph Duveen dined as a friend of millionaires and left with the "
            "inventory of their walls. Catherine de’ Medici ran a flying squadron. "
            "Talleyrand and Fouché made the dinner the interview."
        ),
    },
    15: {
        "figure": "cesare-borgia",
        "also": ["wu-zetian"],
        "history": (
            "Wu Zetian finished rivals. Xiang Yu left Liu Bang wounded and learned "
            "the cost. Cesare Borgia at Cesena made sure the lesson had no pulse. "
            "The Medici, in Florence, treated half-killed families as future coalitions."
        ),
    },
    16: {
        "figure": "de-gaulle",
        "also": ["louis-xiv"],
        "history": (
            "Charles de Gaulle went to Colombey and let the price of his return rise. "
            "Greta Garbo withdrew until absence was the role. Louis XIV left the "
            "room so the sun could be missed. Presence inflates. Leave while they "
            "still use your name as a verb."
        ),
    },
    17: {
        "figure": "louis-xiv",
        "also": [],
        "history": (
            "Ivan IV made terror a climate no one could schedule. Nixon’s “madman” "
            "briefing was the nuclear-age copy. Unpredictability is a handle you "
            "deny the other side. A readable pattern is already a trap."
        ),
    },
    18: {
        "figure": "qin-shi-huang",
        "also": ["louis-xiv"],
        "history": (
            "Qin Shi Huang unified the realm and then walled himself away from the "
            "street that carries news. Greene’s transgression. Louis XIV’s Versailles "
            "is the observance: keep the knives in the same palace, where you can "
            "hear them being sharpened."
        ),
    },
    19: {
        "figure": "richelieu",
        "also": [],
        "history": (
            "Greene sorts animals: the arrogant, the brute, the chameleon. Offend "
            "the wrong one and the joke becomes policy. Richelieu never mistook "
            "Louis XIII’s pride for a toy. Agis of Sparta, in Plutarch, was the "
            "wrong man for Alcibiades to cuckold — a side file, not the lesson."
        ),
    },
    20: {
        "figure": "elizabeth-i",
        "also": ["talleyrand"],
        "history": (
            "Elizabeth I kept suitors as foreign policy and never handed the realm "
            "to a husband. Kissinger’s shuttle was the same refusal to be owned. "
            "Talleyrand’s exclusive would have been a hostage letter. He did not write it."
        ),
        "reversal": (
            "If you never commit, no one will bleed for you. Elizabeth kept the realm; "
            "a quieter loyalty still has to live somewhere. Keep one you do not advertise."
        ),
    },
    21: {
        "figure": "claudius",
        "also": [],
        "history": (
            "Claudius played the fool until the Praetorians needed an emperor. "
            "Socrates played ignorant until the room taught itself. Greene’s sucker "
            "is a student-shaped hole. Pride loves to lecture. Give it a desk."
        ),
    },
    22: {
        "figure": "talleyrand",
        "also": [],
        "history": (
            "Mao’s Long March is Greene’s modern retreat that became a origin myth. "
            "Talleyrand’s surrenders were board changes, not conversions. Yield, "
            "relocate the war, keep the appetite."
        ),
    },
    23: {
        "figure": "bismarck",
        "also": ["rothschild"],
        "history": (
            "The Rothschilds put the weight on one hinge of information. Bismarck "
            "put it on one map. Napoleon’s opposite was the thin line everywhere. "
            "Greene: a smear of force is a line that breaks everywhere."
        ),
    },
    24: {
        "figure": "talleyrand",
        "also": ["alcibiades"],
        "history": (
            "Castiglione wrote the manual. Gracián sharpened it. Talleyrand wore "
            "every room. Alcibiades is the Greek file: austere in Sparta, luxurious "
            "in Ionia, democratic in the Pnyx. The manners were the message."
        ),
    },
    25: {
        "figure": "julius-caesar",
        "also": ["alcibiades"],
        "history": (
            "Julius Caesar crossed a river and became a different self. Greene "
            "started the book on that life. Alcibiades changed cities; Caesar "
            "changed the calendar of Rome. Recreate the livery. Keep the skull."
        ),
    },
    26: {
        "figure": "cesare-borgia",
        "also": ["fouche"],
        "history": (
            "Ramiro de Lorqua in two pieces; Cesare at mass. Fouché’s police, "
            "never Fouché’s signature on the blade. The act and the name of the "
            "act should not share a last name."
        ),
    },
    27: {
        "figure": "rasputin",
        "also": [],
        "history": (
            "Rasputin organized a palace around a boy’s blood. Francesco Giuseppe "
            "Borri sold alchemical belonging in Greene’s older rooms. Loneliness "
            "will staff itself. Offer a plot."
        ),
    },
    28: {
        "figure": "julius-caesar",
        "also": [],
        "history": (
            "Cortés scuttled the ships. Ivan IV entered as a fact. Pietro Aretino "
            "wrote as if already feared. Caesar at the Rubicon is the clean version: "
            "the first full gesture sets the terms. Hesitation is information you "
            "give away."
        ),
    },
    29: {
        "figure": "bismarck",
        "also": ["napoleon"],
        "history": (
            "Bismarck planned German unification through to the last page — which "
            "wars, which order, which throne. The Sicilian expedition is the missing "
            "last page. Napoleon had openings without ends. St. Helena filed them."
        ),
    },
    30: {
        "figure": "catherine-ii",
        "also": [],
        "history": (
            "Catherine II made coups look like weather. Japanese arts of apparent "
            "ease are Greene’s other pole. Houdini hid the hours. Sweat, displayed, "
            "is a request. Sweat, hidden, is a claim of nature."
        ),
    },
    31: {
        "figure": "bismarck",
        "also": ["richelieu"],
        "history": (
            "Kissinger dealt cards both sides could play. Bismarck offered princes "
            "options that all ran through Prussia. Ivan IV’s doors. Freedom that "
            "chooses among your alternatives is still yours."
        ),
    },
    32: {
        "figure": "columbus",
        "also": [],
        "history": (
            "Columbus sold Ferdinand and Isabella a western Indies they already "
            "half-saw. Cagliostro sold Europe an origin. Alchemists sold the last "
            "metal. Facts compete. Fantasies monopolize."
        ),
    },
    33: {
        "figure": "richelieu",
        "also": [],
        "history": (
            "Richelieu found Louis XIII’s insecurity and turned it until the state "
            "obeyed. Lyndon Johnson’s treatment files were the American thumbscrew. "
            "The Count of Saint-Germain sold people their own hunger back to them."
        ),
    },
    34: {
        "figure": "louis-xiv",
        "also": ["columbus"],
        "history": (
            "Louis XIV wore a sun until Europe used the word. Columbus walked into "
            "courts as if already titled; a later life made him a count. Louis-Philippe "
            "is Greene’s transgression: a king who insisted on being a citizen and "
            "was treated like one."
        ),
    },
    35: {
        "figure": "fouche",
        "also": ["talleyrand"],
        "history": (
            "Joseph Fouché timed every France. Talleyrand timed the same years from "
            "the other chair. The same act is genius on Tuesday. They were never "
            "early and rarely late. The funeral is what happens when you miss the click."
        ),
    },
    36: {
        "figure": "louis-xiv",
        "also": [],
        "history": (
            "The Affair of the Diamond Necklace ate Marie Antoinette’s name whether "
            "she wanted the stones or not. Greene’s disdain: what you cannot have, "
            "stop staring at. Henry VIII’s discarded objects. Looking is the handle."
        ),
    },
    37: {
        "figure": "louis-xiv",
        "also": ["barnum"],
        "history": (
            "Versailles was not a house. It was a sentence the eyes had to live inside. "
            "Barnum sold the same grammar to a democracy. Aztec and Chinese empty-city "
            "spectacles are Greene’s older reels. Dazzle, then pass the law."
        ),
    },
    38: {
        "figure": "talleyrand",
        "also": [],
        "history": (
            "Pausanias stopped behaving like a Spartan in Persia and was ruined for "
            "style. Machiavelli’s lesson: inner heresy, outer manners. Talleyrand "
            "went to mass in every France. The notebook stayed private."
        ),
    },
    39: {
        "figure": "napoleon",
        "also": ["bismarck"],
        "history": (
            "Napoleon clouded the water and pulled. Bismarck stirred German leagues "
            "until a country jumped. Mao’s contradictions. Calm water favors the "
            "established net."
        ),
    },
    40: {
        "figure": "rothschild",
        "also": [],
        "history": (
            "Nathan Rothschild paid. Getty paid. Japanese gift-leashes are Greene’s "
            "other warning. What costs nothing is pricing you. The invoice arrives "
            "as a default."
        ),
    },
    41: {
        "figure": "louis-xiv",
        "also": [],
        "history": (
            "Louis XVI sat in Louis XIV’s dent and was measured in the old units. "
            "Alexander’s successors inherited a shape and became shortages. Greene: "
            "do not fill the outline. Draw another floor."
        ),
    },
    42: {
        "figure": "haile-selassie",
        "also": ["cesare-borgia"],
        "history": (
            "Haile Selassie removed the person the flock faced. Cicero against "
            "Catiline. Mao against a named landlord class. Crowds are held by a "
            "body. Strike the shepherd; watch the grammar fail."
        ),
    },
    43: {
        "figure": "elizabeth-i",
        "also": ["catherine-ii"],
        "history": (
            "Elizabeth held an island by belonging in its story. Cyrus in "
            "Xenophon’s Education. Mao’s mass line. Marie Antoinette failed the "
            "hearts and kept the cake sentence. Force holds a room. Attachment "
            "holds a decade."
        ),
    },
    44: {
        "figure": "talleyrand",
        "also": [],
        "history": (
            "Nixon’s office mirrored enemies until they raged at themselves. "
            "Chinese mirror-warfare in Greene’s older chapters. Talleyrand copied "
            "a room’s manners until the room had no uniqueness left to stand on."
        ),
    },
    45: {
        "figure": "bismarck",
        "also": [],
        "history": (
            "Meiji metered the new. The French Revolution sold the word and "
            "delivered the loss too fast. Gorbachev preached change the furniture "
            "could not survive. Bismarck moved one street of Germany at a time, "
            "then a war, then a throne."
        ),
    },
    46: {
        "figure": "alcibiades",
        "also": [],
        "history": (
            "This is Alcibiades’s room in Greene: the unflawed face that dares a "
            "city to invent a crime. Madame de Pompadour showed a crack people "
            "could forgive. Joe Kennedy advised the useful scar. Perfection is a dare."
        ),
    },
    47: {
        "figure": "napoleon",
        "also": ["julius-caesar"],
        "history": (
            "Cyrus past the mark. Croesus. Pyrrhus. Napoleon into Russia. Caesar’s "
            "Ides as the extra step after the civil war was already won. The room "
            "is yours and you keep talking. Something in the back sits up."
        ),
    },
    48: {
        "figure": "alcibiades",
        "also": ["talleyrand"],
        "history": (
            "Mao’s guerrilla water. T. E. Lawrence. The Mongols. Talleyrand with "
            "no fixed flag. Alcibiades among cities until a night in Phrygia when "
            "he was only a man in a house. Formlessness that sleeps becomes a statue "
            "again — and statues burn."
        ),
    },
}


def plate(slug: str, state: str) -> str:
    return f"{MEDIA}/dualform/{slug}-{state}.webp"


def has_plates(slug: str) -> bool:
    return slug in {
        "alcibiades",
        "louis-xiv",
        "fouquet",
        "talleyrand",
        "elizabeth-i",
        "cesare-borgia",
        "galileo",
        "julius-caesar",
        "napoleon",
        "richelieu",
        "fouche",
    }  # plates generated 2026-09-06; others fall back to court shield
