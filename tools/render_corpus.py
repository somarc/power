#!/usr/bin/env python3
"""Render DA HTML for the Power corpus. Original commentary only."""
from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content-staging"
MEDIA = "https://content.da.live/somarc/power/media"

COURTS = [
    ("the-masters-house", "The master's house", "1–8", (1, 8)),
    ("the-mouth", "The mouth", "9–16", (9, 16)),
    ("distance", "Distance", "17–24", (17, 24)),
    ("the-self", "The self", "25–32", (25, 32)),
    ("timing", "Timing", "33–40", (33, 40)),
    ("formlessness", "Formlessness", "41–48", (41, 48)),
]


def L(n, slug, title, sentence, feel, history, now, reversal, point, alc=""):
    return {
        "n": n,
        "slug": slug,
        "title": title,
        "sentence": sentence,
        "feel": feel,
        "history": history,
        "now": now,
        "reversal": reversal,
        "point": point,
        "alc": alc,
    }


LAWS = [
    L(1, "never-outshine-the-master", "Never Outshine the Master",
      "Make the person above you feel larger after you have been in the room.",
      "It is a physical sensation: the air gets thinner when a junior is brighter than the chair. Eyes go to the light. The chair notices the eyes. Tomorrow the light is reassigned.",
      "Plutarch, Life of Alcibiades: the young ward of Pericles was so dazzling in the assembly that older men began to measure the master against the boy. Pericles kept him close and slightly in shadow; the moment the shadow slipped, Athens had two suns and then a civil wound. Thucydides shows the same glare in the Sicilian debate.",
      "November 2023 still teaches 2026: a board that felt outshone by Sam Altman tried to extinguish him and instead extinguished itself. In the 2025–26 lab race, deputies who tweet better than their CEO discover the same physics. Brilliance without a larger chair is a firing offense dressed as merit.",
      "If the master is already weak, hiding your light only delays a coup someone else will run. Sometimes the room needs a new sun. Know which room you are in.",
      "Be the lamp that makes the throne look gold.",
      "Alcibiades could not dim. That is why every city that loved him also had to expel him."),
    L(2, "never-put-too-much-trust-in-friends", "Never Put Too Much Trust in Friends, Learn How to Use Enemies",
      "Friendship assumes the ledger is even; power never is. A converted enemy has to keep proving the conversion.",
      "The friend laughs at your jokes in the same key. The enemy watches your hands. You sleep better with the watcher, once he has signed.",
      "Alcibiades in Sparta, 415–412 BCE: the city that had been his enemy received him as the man who could break Athens. Thucydides has him advising the occupation of Decelea. The Spartans used him until they feared him. Xenophon’s Hellenica records the later turn to Tissaphernes — another former enemy, another proof.",
      "Elon Musk and Sam Altman were co-religionists of OpenAI; the 2024–26 lawsuits are what a friendship looks like after the cap table becomes a battlefield. Meanwhile states that were enemies last decade (India–US tech, Saudi–US AI funds) buy loyalty with invoices, not toasts.",
      "An enemy converted too cheaply is still an enemy with a badge. Alcibiades’s Spartan hosts eventually sent a kill order. The conversion had been useful, not true.",
      "Pay enemies in status. Pay friends in suspicion."),
    L(3, "conceal-your-intentions", "Conceal Your Intentions",
      "If they can narrate your next move, they can price it, block it, or steal it.",
      "The face that explains itself is already being mapped. You feel the mapping as helpful questions.",
      "The mutilation of the Herms, 415 BCE: Athens woke to civic faces smashed and immediately invented a plot with Alcibiades’s name on it. Thucydides VI.27–29. Whether he ordered it or not, the city could see a destination (Sicily, then tyranny) and filled in the road. Visibility of intent was the indictment.",
      "DeepSeek’s 2025 R1 drop worked because the West had a story about who could train frontier models. The story did not include a lab in Hangzhou doing it cheaper. Opacity of method plus sudden presence is still the 2026 pattern in model releases, chip smuggling, and quiet secondary listings.",
      "Total opacity reads as conspiracy. Hide the destination; show a plausible nearer town.",
      "Do not announce the landing beach while the fleet is still in Piraeus."),
    L(4, "always-say-less-than-necessary", "Always Say Less Than Necessary",
      "Words are hostages. The fewer you send out, the fewer can be tortured into meaning you did not choose.",
      "A long answer is a confession that you need to be liked. Silence makes other people write your legend for you, which is cheaper.",
      "Spartan brachylogy is the ancient technology. Plutarch’s Laconic Apophthegms; also Alcibiades’s lisp, which Plutarch says made his speech more persuasive by forcing listeners to lean in. The defect did the work of brevity.",
      "In 2026 product keys and earnings calls, the executives who win are the ones who leave one sentence unsaid. The ones who lose are live on X for forty minutes. The DMA filings against Apple are a museum of sentences that should have been shorter.",
      "If you are already distrusted, silence confirms the charge. Then you must speak once, sharply, and stop.",
      "Leave them leaning."),
    L(5, "so-much-depends-on-reputation", "So Much Depends on Reputation — Guard It with Your Life",
      "Reputation is the army that arrives before you. Once it is broken, you spend the rest of the war explaining.",
      "You feel reputation as the pause before someone contradicts you. When the pause dies, you are already smaller.",
      "Alcibiades’s reputation for impiety after the Herms and the Mysteries (Thucydides VI; Plutarch Alc. 19–22) traveled faster than his ship. He was condemned in absentia. The man was still a general; the name was already a criminal.",
      "Boeing’s 737 MAX and door-plug years are the industrial version: 2024–26 deliveries cannot outrun the name. OpenAI’s “safe AGI” brand took a similar dent in the board crisis and never fully re-inflated. In 2026 a lab’s safety page is often a reputation object, not a control.",
      "Guarding a rotten reputation is embalming. Sometimes you must kill the old name and walk out under a new one (Law 25).",
      "The name lands first. Dress it."),
    L(6, "court-attention-at-all-cost", "Court Attention at All Cost",
      "Power that cannot be seen is not power; it is a hobby. The cost of being watched is lower than the cost of being forgotten.",
      "Attention has a temperature. You walk into a room and the temperature rises, or it does not. If it does not, you are furniture.",
      "Alcibiades’s shield device — Eros with a thunderbolt (Plutarch Alc. 16; Athenaeus) — was a billboard on bronze. He entered Olympia with seven chariots. He made Athens look at him even when Athens wanted to look at Pericles’ ghost.",
      "X in 2025–26 is a court of attention: owners, presidents, and models all feed the same fire. Trevor Noah’s 2026 site (Awwwards SOTD, 3 Sep) is the designed version — a person as the house. The ugly version is a founder live-posting through a crash.",
      "Attention without a next move is a clown. Court it only if you can spend it.",
      "If they are not looking, you are already losing."),
    L(7, "get-others-to-do-the-work", "Get Others to Do the Work for You, but Always Take the Credit",
      "Authorship is a political office. Labor can be hired; the name on the work cannot.",
      "The sting is in the byline. You did the nights. Someone else’s voice reads your nights in a keynote.",
      "The Sicilian expedition was Nicias’s caution and Lamachus’s force and Alcibiades’s persuasion; the assembly heard one name. Thucydides VI. Alcibiades had already left when the name still pulled ships.",
      "2026 AI products are a credit machine: models trained on other people’s writing, wrappers on other people’s models, founders on other people’s papers. NVIDIA takes the credit for every lab’s training run by owning the substrate. The labs take credit for science done by unnamed research engineers.",
      "Stolen credit that everyone can see becomes a revolt. Share just enough names to keep the engine from walking out.",
      "Own the sentence that gets quoted. Let others own the sweat."),
    L(8, "make-other-people-come-to-you", "Make Other People Come to You — Use Bait if Necessary",
      "Whoever travels is already negotiating from the saddle. Make them cross your courtyard.",
      "You feel it in the knees: going to them. Staying put is a throne even if the chair is cheap.",
      "Tissaphernes did not go to Alcibiades; Alcibiades went to Sardis and then made the Persian wait on Greek factions (Thucydides VIII). The satrap held the money. The money made Athens and Sparta come.",
      "Apple’s store, NVIDIA’s CUDA, and the 2025–26 EU DMA fights are all about who must travel. DMA tried to make Apple come to Europe’s courtyard. Apple tried to make developers keep coming to Cupertino. The bait is distribution.",
      "Bait that is too sweet looks like a trap and they send a proxy. The courtyard must feel like their idea.",
      "Be the well. Let the city walk."),
    L(9, "win-through-your-actions", "Win Through Your Actions, Never Through Argument",
      "A won argument is an enemy with better vocabulary. A finished action is a fact they have to live inside.",
      "You can hear a debate ending and nobody’s body has moved. That is not power. Power is the pier that is suddenly theirs.",
      "Alcibiades did not argue Sparta into fortifying Decelea; he showed them the map of Attica and the grain. Thucydides VII.27–28: the fort did the speaking afterward. Athens felt it in empty fields.",
      "Isar Aerospace reached orbit on its second flight in September 2026. That sentence ends more European launch arguments than a white paper. In the lab world, a public eval leaderboard still beats a safety essay.",
      "Action without a frame is noise. Do the thing, then let one picture of the thing travel.",
      "Stop explaining. Move a stone they cannot put back."),
    L(10, "infection-avoid-the-unhappy", "Infection: Avoid the Unhappy and Unlucky",
      "Misery is sticky. Courts read your company as your forecast.",
      "You walk in with someone whose luck has gone rancid and the room’s smile becomes medical.",
      "The men around Nicias in Sicily caught his dread; Thucydides VII is an epidemic of omens. Alcibiades, whatever else he was, refused to sit in a losing atmosphere — he changed cities instead of moods.",
      "FTX’s 2022 collapse still infected crypto reputations into 2025. Founders who kept SBF in the Christmas photo paid in 2026 fundraising. AI labs now quietly distance from the last safety-theater scandal the way banks distanced from 2008 names.",
      "Sometimes the unlucky person is you. Then isolation is not hygiene; it is exile. Find one lucky room and do not bring the old smell.",
      "Do not let their weather become your climate."),
    L(11, "keep-people-dependent", "Learn to Keep People Dependent on You",
      "The indispensable person is not the most loved. They are the only bridge.",
      "Dependency feels like gratitude at first, then like a chain you both pretend is a ribbon.",
      "Alcibiades made three cities need his tongue: Athens for the fleet, Sparta for the Attic wound, Persia for Greek disunity. Each need was a lease, not a gift. When a city learned to sail without him, the lease ended in a dagger (Plutarch Alc. 38–39).",
      "CUDA, AWS, the iPhone WebKit, and frontier-API lock-in are 2026’s leases. NVIDIA’s 2025–26 power is not chips; it is the impossibility of leaving. The EU’s interoperability mandates are an attempt to break Law 11 by statute.",
      "If they cannot leave, they will eventually burn the bridge with you on it. Keep a door they are afraid to use, not a wall.",
      "Be the pass. Not the mountain they can tunnel."),
    L(12, "selective-honesty", "Use Selective Honesty and Generosity to Disarm Your Victim",
      "One true expensive thing makes ten false cheap things land.",
      "The gift that is slightly too good. You feel yourself relaxing, which is the point.",
      "Alcibiades returning to Athens in 407 (Xenophon Hell. 1.4; Plutarch Alc. 32–34) gave the city a procession and a restoration of the Mysteries procession — a public piety that laundered the impiety charge. The honesty was ritual. The operation was power.",
      "Corporate 2026: the open-weights drop, the safety board with one real skeptic, the apology that names a specific date. DeepSeek’s open release disarmed a week of export-control sermons. Selective generosity is now a launch tactic.",
      "If the gift is the whole business, you have no second move. Honesty as a system is a different law (and a different life).",
      "Tell one costly truth. Then collect."),
    L(13, "appeal-to-self-interest", "When Asking for Help, Appeal to People's Self-Interest, Never to Their Mercy or Gratitude",
      "Mercy is a mood. Interest is a structure. Ask the structure.",
      "You hear yourself saying “after all I’ve done” and already know you have lost.",
      "Alcibiades to the Spartans: not “forgive a Greek,” but “here is how you beat Athens.” Thucydides VI.89–92 is a masterclass in interest. To Tissaphernes: not loyalty — a cheaper war.",
      "CHIPS Act money, Saudi and Emirati AI funds, and 2025–26 reindustrialization pitches all speak interest. The failed pitches of the same years are the ones that asked democracies to be grateful for past alliances.",
      "Pure interest without a human face feels like a mugging. Give them a story in which their interest is also their virtue.",
      "Do not ask to be remembered. Ask to be useful to their next win."),
    L(14, "pose-as-a-friend-work-as-a-spy", "Pose as a Friend, Work as a Spy",
      "The information that matters is what people say when they think you are on their side of the table.",
      "You feel the warmth of being included and file it. That filing is the job.",
      "Alcibiades in Sparta ate their mess and learned their factions; in Sardis he learned Tissaphernes’s caution. Thucydides VIII is a spy novel in armor. Friendship was the cover.",
      "2026 product “partnerships,” model-eval sharing, and standard-setting tables are full of friendly spies. TikTok’s data fight with Washington is Law 14 argued in public. So is every lab that sits on a rival’s safety board.",
      "If you are caught, you are not a spy; you are a traitor, which pays worse. Leave a trail that looks like ordinary curiosity.",
      "Sit close. Write it down later."),
    L(15, "crush-your-enemy-totally", "Crush Your Enemy Totally",
      "A wounded rival is a future coalition. Endings must be endings.",
      "Mercy in victory feels noble in the hour and looks naive in the decade.",
      "Athens did not crush Alcibiades; it exiled him. He came back with Spartan advice and Persian money. Plutarch’s end at Melissa is the delayed crush — assassins, a house in flames, a body that could no longer switch cities.",
      "Incomplete tech deaths: OpenAI did not crush Musk; Musk did not crush OpenAI; both spent 2024–26 in court while xAI and Anthropic took oxygen. In geopolitics, an un-ended war is a second war with better drones.",
      "Crushing a symbol makes a martyr. Crush the capacity, not the statue.",
      "If they can still walk, they can still return."),
    L(16, "use-absence", "Use Absence to Increase Respect and Honor",
      "Presence is a currency that inflates. Leave, and the price of your return goes up.",
      "The chair is empty and the meeting is worse. That is the sound of your value.",
      "Alcibiades’s absences were involuntary at first (exile) and then tactical. Athens recalled him because the war without him was uglier than the war with him (Xenophon Hell. 1.4). Absence wrote the invitation.",
      "Founders who never leave Slack become furniture. In 2026 the scarce move is the quiet quarter: a model lab that goes dark, a politician who stops posting, an artist who withholds. Scarcity still prices the return.",
      "Absence when you are already forgotten is just absence. You must be missed, which means you must have been a climate, not a cameo.",
      "Leave while they still use your name as a verb."),
    L(17, "cultivate-unpredictability", "Keep Others in Suspended Terror: Cultivate an Air of Unpredictability",
      "A readable pattern is a handle. If they cannot time you, they cannot trap you.",
      "The stomach drop when a calm person does one sharp thing. That drop is governance.",
      "Alcibiades’s career is a refusal to be timed: Athens, Sparta, Persia, Athens, the Thracian Chersonese. Enemies prepared for the last city and met him in the next. Unpredictability was survival, then a brand, then a cause of death.",
      "Tariff letters, sudden model drops, surprise product sunsets — 2025–26 executive power likes the flinch. Markets price the flinch as volatility and still follow it.",
      "Randomness without a private plan is just chaos, and chaos is predictable in the wrong way. Be illegible outward, metronomic inward.",
      "Let them pack for the wrong war."),
    L(18, "do-not-build-fortresses", "Do Not Build Fortresses to Protect Yourself — Isolation is Dangerous",
      "Walls keep you from hearing the knife being sharpened in the courtyard.",
      "Safety that smells like a bunker. No one brings you the joke, the rumor, the plot.",
      "Alcibiades in the Chersonese built a small power on the margins and died in a house that could be surrounded (Plutarch Alc. 38–39). Isolation made the assassination cheap. Contrast Pericles in the city — hated, but informed.",
      "Billionaire bunkers, remote-only founder cults, and air-gapped labs all rhyme. In 2026 the isolated CEO is the last to know they have already been fired by the culture. Information wants a street.",
      "A fortress is correct when the street is actually on fire. Then come out the moment it is not.",
      "Stay where news can still find you."),
    L(19, "know-who-youre-dealing-with", "Know Who You're Dealing With — Do Not Offend the Wrong Person",
      "Not every ego is a toy. Some are states. Some are patients. Some are both.",
      "The joke that dies in the air. You have misread the animal.",
      "Alcibiades slept with the king of Sparta’s wife, Timaea (Plutarch Alc. 23). He treated Agis as a lesser man. Agis was not. The personal insult became policy. The wrong person had an army.",
      "2026: regulators with long memories, engineers who own a key subsystem, a journalist who is actually a court. Offending “the timeline” is cheap. Offending the one person who signs export licenses is not.",
      "Paranoia about everyone is also a misread. Most people are not the wrong person. Save the caution for the few who can end you.",
      "Learn which pride is armed."),
    L(20, "do-not-commit-to-anyone", "Do Not Commit to Anyone",
      "A public exclusive is a hostage letter you wrote yourself.",
      "The relief of picking a side — and the sound of the other door locking.",
      "Alcibiades’s whole method: never only Athens, never only Sparta, never only Persia. Thucydides VIII: he sells each the fear of the other. Commitment would have made him a citizen again. He preferred to be a weather system.",
      "Non-alignment in 2026 is a business model: cloud credits from two hyperscalers, chips from a gray market, a foundation model that will not swear fealty. Countries practice it as “multi-alignment.” Companies practice it as dual-source.",
      "If you never commit, no one will bleed for you. Alcibiades died without a city. Keep one quiet loyalty you do not advertise.",
      "Be needed by several. Owned by none."),
    L(21, "play-a-sucker", "Play a Sucker to Catch a Sucker — Seem Dumber Than Your Mark",
      "Pride loves to teach. Give it a student and it will hand you the keys while lecturing.",
      "You feel smaller on purpose. They expand. In the expansion is the leak.",
      "Socrates plays ignorant in the dialogues; Alcibiades, in Plato’s Symposium, plays the beautiful drunk who knows exactly what he is doing. The city thought the golden boy was only golden. He was also listening.",
      "DeepSeek’s 2025 story included a “we’re not that big” tone that made Western labs explain, in public, how expensive intelligence was supposed to be. The explanation was the gift. In 2026 procurement meetings, the quietest vendor is often the one who already has the contract language.",
      "If you play dumb too long, they will staff you as dumb. Drop the mask at the moment of signature, not before.",
      "Let them enjoy being smarter. Then file."),
    L(22, "surrender-tactic", "Use the Surrender Tactic: Transform Weakness into Power",
      "Yielding at the right instant makes the other side spend their win. Wins that cost too much are losses.",
      "The strange peace of putting the sword down first. They do not know where to cut.",
      "Alcibiades surrendering to Sparta looked like treason and functioned as a reset: from condemned man to counselor. The surrender was a change of board, not of appetite.",
      "Small AI labs in 2025–26 “surrender” into larger clouds and come out with distribution. Defendants who settle keep the archive closed. Ukraine’s territorial bargaining, endlessly rumored, is this law in blood — yield a map to keep an army.",
      "Surrender that is actually surrender is just losing. You must have a second game ready on the other side of the bow.",
      "Bow. Relocate the war."),
    L(23, "concentrate-your-forces", "Concentrate Your Forces",
      "A thin line everywhere is a line that breaks everywhere. Put the weight on one hinge.",
      "The fatigue of ten fronts. The click of one door giving way.",
      "Sicily was the opposite: Athens split the war. Alcibiades wanted a concentrated strike and then more; Nicias wanted none; the city chose a smear. Thucydides VI–VII is concentration refused, then punished.",
      "xAI’s Colossus build in 2024–25 was a concentration bet: one cluster, one model family, one owner. NVIDIA concentrated the world’s training on a single architecture. 2026 startups that do five products are already ghosts.",
      "Concentration on the wrong hinge is just a louder mistake. Pick the hinge that opens the house, not the one that is fashionable.",
      "One door. All the weight."),
    L(24, "play-the-perfect-courtier", "Play the Perfect Courtier",
      "A court is a climate. The person who can breathe it without drowning runs it.",
      "You taste what the room wants to hear and you serve it warm, never piping, never cold.",
      "Plutarch’s Alcibiades is the courtier as shapeshifter: austere in Sparta, luxurious in Ionia, democratic in Athens. The manners were the message. The message was: I already belong.",
      "Washington, Brussels, Riyadh, and the AI safety dinner circuit in 2026 all have court dress. The perfect courtier today speaks model evals in one room and industrial policy in the next, and does not mix the costumes.",
      "The perfect courtier who never risks a view becomes wallpaper. Belong, then steer.",
      "Wear the room. Do not become it."),
    L(25, "re-create-yourself", "Re-Create Yourself",
      "Identity is a costume you are allowed to take off if you can survive the naked minute.",
      "The old name like a coat you have outgrown. The air on the new skin.",
      "This is Alcibiades’s law. Athenian, Spartan, Persian guest, Athenian again, Thracian warlord. Plato’s Symposium still holds the first costume: the beautiful drunk. Plutarch holds the last: a body in a burning house in Phrygia. Between them, a sequence of selves that kept the same neck.",
      "2026 rebrands: labs that were “safety” becoming “sovereign,” companies that were “open” becoming “enterprise,” politicians who were outsiders becoming the state. The ones who succeed keep one recognizable bone — a voice, a face, a vice — so the new self still casts a shadow.",
      "If you recreate too often, you are formless in the cheap sense (see 48) and no one will follow. Change the livery, not the skull.",
      "Same neck. New city."),
    L(26, "keep-your-hands-clean", "Keep Your Hands Clean",
      "The act and the name of the act should not live on the same person.",
      "You smell iron and it is not on you. That is the design.",
      "The assassins of Alcibiades are a cloud in Plutarch — Spartan order, Persian permission, local hands. No king holds the knife. Clean hands, dirty courtyard.",
      "2026: boards fire CEOs through “independent reviews.” Model labs outsource scraping. States outsource disruption. The DMA’s fines land on a logo, not a minister. Hands stay white; PDFs do the cutting.",
      "If everyone knows whose hands they are, the fiction fails. Either be actually distant or be ready to own the blood.",
      "Have a knife that does not share your last name."),
    L(27, "need-to-believe", "Play on People's Need to Believe to Create a Cultlike Following",
      "Loneliness will organize itself around anyone who offers a plot.",
      "The click of belonging. You did not even have to be right.",
      "Alcibiades’s young followers in Athens treated him as a style of being alive (Plutarch Alc. 16). The Mysteries scandal weaponized that hunger — a private rite, a chosen few. Cult is just court without a building.",
      "AI labs in 2025–26 run on eschatology: scaling laws as scripture, a date for AGI, a caste of the initiated. Fandoms around founders do the same work churches did. The need is older than the stack.",
      "A cult you cannot dissolve will dissolve you. Keep an exit that does not require a schism.",
      "Give them a story that makes their waiting feel like service."),
    L(28, "enter-action-with-boldness", "Enter Action with Boldness",
      "Hesitation is information you give away. The first full gesture sets the terms.",
      "The body commits before the committee. Air moves.",
      "Alcibiades proposing Sicily was boldness; staying to see it through would have been concentration. He was bold in speech, then absent in the act. Boldness without follow-through is a firework.",
      "Isar’s second-flight orbit, September 2026, is boldness with a telemetry trail. So was every lab that shipped a model before the committee finished the red team. The 2026 graveyard is full of “almost ready” decks.",
      "Boldness in a minefield is a smear. Scout, then go in as if you had always been going in.",
      "Arrive as a fact."),
    L(29, "plan-all-the-way-to-the-end", "Plan All the Way to the End",
      "The opening that has no last page is a trap you built for yourself.",
      "Victory morning, no plan for noon. That hollow is how empires leak.",
      "Sicily had a beginning (glory) and no designed end (occupation, supply, politics at home). Thucydides makes the missing last page the tragedy. Alcibiades’s personal plans always had a next city; the expedition did not.",
      "2021’s withdrawals and 2023–26 wars are classrooms of unfinished last pages. Product-wise: a model launch with no eval, no legal, no support, no second training run. 2026 investors now ask for the end-state slide first.",
      "Over-planning the end can freeze the start. Write the last page in pencil. But write it.",
      "Know the last scene before you light the first."),
    L(30, "accomplishments-seem-effortless", "Make Your Accomplishments Seem Effortless",
      "Sweat, displayed, is a request for sympathy. Sweat, hidden, is a claim of nature.",
      "They think you were born like this. That is the spell.",
      "Plutarch insists Alcibiades’s charm felt native — the lisp, the walk, the ease in any mess hall. The labor of becoming all men was backstage. Effortlessness was the product.",
      "Apple’s keynote grammar still dominates 2026 launches: the thing simply appears. The opposite — a founder narrating how hard it was — is a 2010s leftover. Labs that leak their cluster suffering look mortal on purpose, which is sometimes the other spell.",
      "If they think it is nature, they will not pay for the labor. Show just enough craft to invoice.",
      "Bleed in private. Walk out dry."),
    L(31, "control-the-options", "Control the Options: Get Others to Play with the Cards You Deal",
      "Freedom that chooses among your alternatives is still your freedom.",
      "Two doors, both yours. They feel like a person making a choice.",
      "Tissaphernes, coached by Alcibiades, kept both Greek leagues weak by funding just enough of each (Thucydides VIII.46). The options were: a little Sparta, a little Athens. Never a winner. The dealer was Persian.",
      "App stores, cloud committed-use discounts, “open” licenses with claws, and DMA “choice screens” are 2026’s dealt hands. The fight is over who prints the menu. Europe wants to print it. Platforms want to print it. Users think they are hungry, not dealt.",
      "Too few options and they smell the cage. Three is often the humane number: two you can stand, one you can praise them for avoiding.",
      "Print the menu. Let them pick."),
    L(32, "play-to-peoples-fantasies", "Play to People's Fantasies",
      "Facts compete. Fantasies monopolize. Sell the picture they already half-see.",
      "You watch their face leave the room for a better room. You just described the door.",
      "Sicily was a fantasy of empire the assembly already wanted (Thucydides VI.24). Alcibiades did not invent the hunger; he plated it. Nicias served vegetables. Vegetables lost.",
      "AGI as salvation or doom, a return to a past country, a personal superintelligence in a pocket — 2026’s capital still follows pictures. The sober pitch raises a seed. The fantasy raises a campus.",
      "A fantasy you cannot touch in twelve months becomes a religion, then a riot. Promise a picture with a staircase.",
      "Describe the city they already miss."),
    L(33, "discover-each-mans-thumbscrew", "Discover Each Man's Thumbscrew",
      "Everyone has a pressure that turns will into compliance. Find it; do not guess it.",
      "The tiny flinch. There. That is the screw.",
      "Alcibiades read Agis’s pride, Tissaphernes’s caution, the Athenian demos’s hunger for spectacle. Different screws, same hand. Plutarch is a catalog of those pressures.",
      "2026 thumbscrews: a regulator’s legacy, an engineer’s paper, a politician’s primary, a lab’s eval rank, a nation’s chip access. Discovery is diligence. Use is politics. HR software that “scores sentiment” is a clumsy industrial version.",
      "Turn the screw in public and you create a crowd around the victim. Turn it in private and you have a partner.",
      "Do not push the chest. Press the one nerve they think is hidden."),
    L(34, "be-royal-in-your-own-fashion", "Be Royal in Your Own Fashion: Act Like a King to Be Treated Like One",
      "People take the temperature you set. Enter as a petitioner and you will be given a line.",
      "The spine knows before the title does.",
      "Alcibiades on the Olympic circuit performed royalty without a throne: tents, gifts, seven chariots (Plutarch Alc. 11–12). The cities treated the performance as rank. Rank followed the costume more than the office.",
      "Founder-mode in 2025–26 is this law in Allbirds or in a black tee. The royal fashion of the lab is the keynote cadence, the cluster tour, the unhurried pause. Act like a vendor and you get vendor terms.",
      "Costume without delivery is delusion. Be royal in the room you can actually feed.",
      "Set the temperature. They will match it."),
    L(35, "master-the-art-of-timing", "Master the Art of Timing",
      "The same act is genius on Tuesday and suicide on Wednesday. Time is the hidden law inside the others.",
      "The click when the room is ready. Moving then is almost easy. Moving early is a speech. Moving late is a funeral.",
      "Alcibiades’s recall in 407 came when Athens had been starved of luck. Xenophon Hell. 1.4: the timing made a condemned man a savior for a season. He left again before the season turned. He did not time the last night in Phrygia.",
      "F1’s 2026 regulations, model-release windows before a competitor’s keynote, and rate-cut mornings are clocks. The labs that shipped in the DeepSeek shock week looked either prophetic or desperate depending on the hour.",
      "Waiting for a perfect hour is how Nicias died in Sicily. Time the hinge, then accept the weather.",
      "Not whether. When."),
    L(36, "disdain-things-you-cannot-have", "Disdain Things You Cannot Have: Ignoring Them is the Best Revenge",
      "Want, displayed, is a confession of lack. Lack is a handle.",
      "You look away and they become smaller. Looking is what made them large.",
      "After exile, Alcibiades could not have Athens, so he made Athens look like a smaller game than Persia. The disdain was strategy. When he wanted Athens again, the disdain came off like a cloak.",
      "2026: companies that cannot get CUDA pretend they never needed it. Politicians who cannot get a platform pretend the platform is for children. The tell is the second glance.",
      "Disdain that is fake is transparent. If you actually need it, Law 8 (make them come) beats Law 36.",
      "If you cannot hold it, do not stare."),
    L(37, "create-compelling-spectacles", "Create Compelling Spectacles",
      "Most people think with their eyes. Give the eyes a scene and the mind will write a law under it.",
      "The hush. Then the noise. Then the story that was not quite what happened.",
      "The restored Mysteries procession in 407; the Olympic chariots; the very body of Alcibiades walking back into Athens. Plutarch Alc. 32–34. Spectacle laundered a charge the courts had not.",
      "Product keynotes, rocket landings, model demos that talk like a person — 2026 still runs on staged astonishment. Awwwards itself is a spectacle machine for sites. A still that holds when you kill the motion (Hon Tran, Jun 2026) is the adult form.",
      "Spectacle without a next fact is a carnival. Use the hush to pass a law, a price, a surrender.",
      "Make a scene they can still see with their eyes closed."),
    L(38, "think-as-you-like-behave-like-others", "Think as You Like but Behave Like Others",
      "Inner heresy, outer manners. The opposite order gets you killed for style.",
      "You nod in the temple and keep your own map folded.",
      "Alcibiades failed this in Athens (the Mysteries, the Herms — whether guilty or framed, he looked like a man who did not behave like others) and passed it in Sparta (black broth, short hair, obedience as costume). Plutarch makes the contrast the point.",
      "Lab researchers who think the scaling religion is over still cite it in memos. 2026 employees use the company’s pronouns for the roadmap. Inner dissent, outer deck. The ones who tweet the dissent first get the quiet exit.",
      "If outer manners become inner law, you have been converted. Keep one private notebook.",
      "Wear the city’s face. Keep your own eyes."),
    L(39, "stir-up-waters", "Stir Up Waters to Catch Fish",
      "Calm water favors the established net. Mud favors the one who brought a spear.",
      "The meeting that was fine until you asked the one question. Fish rise.",
      "Alcibiades stirring Greek leagues against each other for Tissaphernes (Thucydides VIII) is mud as policy. Confusion was the product. He fished in it for a salary and a future city.",
      "Leaks before a board meeting, a sudden price war, a safety scare two days before a rival’s launch — 2026’s stirred waters. Markets call it volatility and still swim in it. The DMA process itself stirs platforms until concessions jump.",
      "If you cannot see in the mud either, you are just another drowned fish. Stir only a pond you have mapped.",
      "Cloud the water. Then take one clean pull."),
    L(40, "despise-the-free-lunch", "Despise the Free Lunch",
      "What costs nothing is pricing you. Pay, and you choose the terms.",
      "The easy gift. Your hand is already in a posture of thanks, which is a posture of debt.",
      "Persian gold to Greek politicians was never free (Thucydides VIII). Alcibiades both took it and warned others it was a leash. The lunch was a satrapy.",
      "“Free” models, “free” credits, “free” open weights with a license claw, “free” distribution on a platform — 2026’s lunches. The invoice arrives as a default, a ranking, a sudden ToS. Paying NVIDIA is clearer than eating free compute.",
      "Some lunches are strategy (Law 12). Despise the ones that make you polite.",
      "Pay. It keeps your mouth your own."),
    L(41, "avoid-stepping-into-a-great-mans-shoes", "Avoid Stepping into a Great Man's Shoes",
      "A predecessor’s outline will make you look like a shortage. Build a different floor.",
      "The ghost is still sitting. You are standing in his dent.",
      "Alcibiades after Pericles could not be a second Pericles; he became a different animal. Those who tried to be “the next Pericles” vanished into comparison. The shoes were a trap. The new walk was the escape.",
      "Every 2025–26 CEO who took a founder’s chair without moving the furniture is already being measured in the old units. Labs that brand as “the next OpenAI” volunteer for the comparison. The smart successors change the product so the ghost has no room.",
      "If the great man’s system is actually the job, you must wear the shoes and then scuff them in public on purpose.",
      "Do not fill the outline. Draw another."),
    L(42, "strike-the-shepherd", "Strike the Shepherd and the Sheep Will Scatter",
      "Crowds are held by a person, not a paragraph. Remove the person, watch the grammar fail.",
      "The silence after the loud one leaves. Bodies forget how to stand.",
      "Athens striking at Alcibiades (the recall from Sicily, the death sentence) scattered the expedition’s nerve. They thought they were cutting a tumor. They cut the shepherd and the sheep walked into Syracuse’s killing ground. Thucydides VII.",
      "Decapitation as 2026 tactic: take out a founder, a general, a mayor of a platform, a lead maintainer. Open-source projects die when the shepherd burns out. Companies die when the only person who can say no is gone.",
      "Strike a shepherd who is also a martyr and you invent a better shepherd. Prefer co-option (Law 2) when the flock is religious.",
      "Do not argue with the flock. Move the one they face."),
    L(43, "hearts-and-minds", "Work on the Hearts and Minds of Others",
      "Force holds a room. Attachment holds a decade. Get into the story they tell themselves.",
      "They defend you when you are not there. That is the interior victory.",
      "Alcibiades’s gift was making people feel more alive near him (Plato, Symposium; Plutarch). That is hearts. The minds followed because the living felt like a reason. When the feeling soured, the minds wrote charges.",
      "Culture, fandom, internal memos that sound like belonging — 2026 institutions that cannot buy hearts try to buy minds with slides and fail. The labs that keep researchers are the ones that still feel like a cause at 1 a.m.",
      "Hearts without a structure are a mob. Pair this with 11 (dependency) or 27 (belief) or you are just popular.",
      "Win the story they tell in the dark."),
    L(44, "mirror-effect", "Disarm and Infuriate with the Mirror Effect",
      "Copying a person steals their uniqueness, which is often the only thing they were sure of.",
      "They see themselves coming back slightly wrong. Rage, then emptiness.",
      "Alcibiades mirroring Sparta (short hair, broth, laconic air) disarmed a city that expected an Athenian peacock. The copy was a weapon. When he mirrored Persia’s luxury, Sparta saw the earlier copy as a lie.",
      "Clone products, clone models, clone interfaces — 2026’s mirrors. Open-weight copies of closed models infuriate more than they compete. Parody accounts unwind reputations (Law 5) by reflection.",
      "A perfect mirror is a confession you have no form (48). Mirror to enter, then add one scar that is yours.",
      "Hold their face up. Let them flinch first."),
    L(45, "preach-change-reform-slowly", "Preach the Need for Change, but Never Reform Too Much at Once",
      "People love the word new and hate the feeling of loss. Sell the word. Meter the loss.",
      "The cheer for the announcement. The sulk when the furniture moves.",
      "Athens loved Alcibiades’s newness and punished his speed. The Mysteries, the youth, the style — too much reform of manners at once. Slow change would have been Pericles. He could not be slow.",
      "The EU AI Act’s phased duties, Apple’s year-long DMA theater, and “we’re evolving the model family” notes are 2026’s metering. Big-bang reorgs still happen; their obituaries are already written in Glassdoor.",
      "If the house is actually on fire, slow reform is arson by delay. Know whether you are in a court or a blaze.",
      "Promise a new city. Move one street."),
    L(46, "never-appear-too-perfect", "Never Appear Too Perfect",
      "Perfection is a dare. Give them a flaw they can forgive so they do not have to invent a crime.",
      "The relief of seeing you miss. They come closer.",
      "Alcibiades’s vices were public — drink, sex, insolence. They made him human enough to love and prosecutable enough to ruin. Plutarch cannot decide if the flaws were charm or exhibit A. They were both.",
      "2026 brands that present as fully aligned, fully green, fully safe invite forensic campaigns. The ones that admit a scar (a delayed launch, a known eval miss) look adult. Perfection is now a tell of a communications team with too much budget.",
      "A flaw that is actually your operation (cruelty, theft) is not this law. Display a harmless crack, not the fault line.",
      "Show a scar they can touch. Hide the ones that open."),
    L(47, "do-not-go-past-the-mark", "Do Not Go Past the Mark You Aimed For; In Victory, Learn When to Stop",
      "The extra step after the win is where the story turns. Stopping is a skill that feels like death and is life.",
      "The room is already yours and you keep talking. Something in the back of the room sits up.",
      "After Cyzicus and the restoration, Alcibiades could have been the restrained savior. He pushed, raided, made new enemies. The mark had been: return. Past the mark was: remain the weather. Weather gets blamed for storms.",
      "Wars that take the extra province, companies that take the extra vertical, labs that train past the point of a clean story — 2026 is littered with overshoots. The DMA’s maximalists and the platform maximalists both overshoot and feed each other.",
      "Stopping too early is Law 15 failed (the enemy lives). Stopping is not the same as mercy. It is the last accurate shot.",
      "Hit the mark. Put the bow down."),
    L(48, "assume-formlessness", "Assume Formlessness",
      "A shape is a target. Water has no edge for the knife. Be water that still remembers it has a destination.",
      "They reach for you and get climate. You are in the next weather.",
      "This is Alcibiades’s last law and his epitaph. Formless among cities, he survived every form they tried to pin on him — until a night when he was only a man in a house. Plutarch’s fire is what happens when formlessness sleeps. Thucydides never sees that night; he sees the method.",
      "Guerrilla product, gray-zone war, models that are neither open nor closed, companies that are neither labs nor clouds — 2026 power likes the undefined object. DeepSeek was formless to export-control categories for a season. Categories caught up. They always do, unless you move.",
      "Formlessness with no will is drift. Alcibiades had will without a last city. Pair water with a private shore.",
      "Do not be a statue. Do not be mist. Be the sea they cannot hold."),
]


def court_for(n: int) -> tuple[str, str]:
    for slug, title, _span, (a, b) in COURTS:
        if a <= n <= b:
            return slug, title
    return "", ""


def page_shell(main: str) -> str:
    return (
        "<body>\n<header></header>\n<main>\n"
        + main
        + "\n</main>\n<footer></footer>\n</body>\n"
    )


def metadata(title: str, desc: str, image: str) -> str:
    return f"""<div class="metadata">
<div><div>title</div><div>{escape(title)}</div></div>
<div><div>description</div><div>{escape(desc)}</div></div>
<div><div>image</div><div><img src="{image}" alt=""></div></div>
</div>"""


def dualform(eyebrow: str, h1: str, lede: str, a: str, a_alt: str, b: str, b_alt: str, variant: str = "") -> str:
    cls = f' class="dualform-hero {variant}"' if variant else ' class="dualform-hero"'
    return f"""<div{cls}>
<div>
<div>
<p>{escape(eyebrow)}</p>
<h1>{escape(h1)}</h1>
<p>{lede}</p>
</div>
<div>
<p><img src="{a}" alt="{escape(a_alt)}"></p>
<p><img src="{b}" alt="{escape(b_alt)}"></p>
</div>
</div>
</div>"""


def section_meta(*styles: str) -> str:
    return f"""<div class="section-metadata">
<div><div>Style</div><div>{escape(", ".join(styles))}</div></div>
</div>"""


A_HEAD = f"{MEDIA}/dualform/alcibiades-a.webp"
B_HEAD = f"{MEDIA}/dualform/alcibiades-b.webp"
STAMP = "/media/lottie/stamp.json"


def render_index() -> str:
    rows = []
    for law in LAWS:
        href = f"/laws/{law['n']:02d}-{law['slug']}"
        rows.append(
            f"<div><div>{law['n']:02d}</div>"
            f"<div><p><a href=\"{href}\">{escape(law['title'])}</a></p></div>"
            f"<div><p>{escape(law['sentence'])}</p></div></div>"
        )
    court_links = " ".join(
        f'<p><a href="/courts/{slug}">{escape(title)} ({span})</a></p>'
        for slug, title, span, _ in COURTS
    )
    main = f"""<div>
{dualform(
    "Marble · living",
    "You never leave the man.",
    "A personal corpus of the 48 Laws of Power, written as original commentary for 2026. The object is Alcibiades. The laws remap on one neck.",
    A_HEAD,
    "Marble bust of the so-called Alcibiades, Capitoline type, isolated on a wine-black field",
    B_HEAD,
    "The same silhouette living: Alcibiades as a man in a symposium, gold in the hair, eyes open",
)}
{section_meta()}
</div>
<div>
<p>This is not a summary of Robert Greene. It is a court. Forty-eight rooms, six courts, one body. Historical cases sit on Plutarch, Thucydides, Xenophon, and Plato. Present cases sit on the public record of 2025–26 — labs, platforms, states, launches.</p>
<p><strong><a href="/alcibiades">Alcibiades</a></strong> is the house object. If you cover the wordmark you should still know who you are looking at.</p>
{court_links}
<p><em><a href="/laws/">Enter the laws</a></em></p>
{section_meta("wide")}
</div>
<div>
<h2>The 48</h2>
<div class="law-index">
{''.join(rows)}
</div>
{section_meta("wide")}
{metadata("Power — 48 Laws", "A personal Dualform corpus of the 48 Laws of Power, with Alcibiades as the object. Original commentary for 2026.", A_HEAD)}
</div>"""
    return page_shell(main)


def render_alcibiades() -> str:
    main = f"""<div>
{dualform(
    "Athens · Sparta · Persia",
    "Alcibiades",
    "c. 450–404 BCE. Son of Cleinias, of the deme Scambonidae. Ward of Pericles. The neck, Plutarch says, bent a little. The hair, long. The speech, a lisp that made people lean in. Beauty as a political technology.",
    A_HEAD,
    "Marble Alcibiades, substrate — memory, exile, stone",
    B_HEAD,
    "Living Alcibiades, expression — the court, the symposium, the next city",
)}
{section_meta()}
</div>
<div>
<h2>Feel him</h2>
<p>He is not a marble saint and not a villain in a textbook. He is the person in the room who makes everyone else slightly late to themselves. Plato’s Symposium lets him crash a party already in progress, crowned and drunk, and still steal the night from Socrates. That is the sensation: a climate walking in on two feet.</p>
<p>Plutarch says the neck turned in a characteristic way. Athenaeus says he wore the hair long. The Capitoline bust (MC 1160, Palazzo dei Conservatori) is a Roman copy of a late-classical type, traditionally called Alcibiades — an ideal male portrait, not a photograph. We use it because it is the face the West has used for him, and because Dualform needs a lockable silhouette. State A is that stone. State B is the same mass with blood in it.</p>
<h2>The life, as a law</h2>
<p>He grows up in Pericles’ house and cannot help outshining it. He marries Hipparete and humiliates her with courtesans until she leaves (Plutarch Alc. 8). He puts Eros with a thunderbolt on his shield. He enters seven chariots at Olympia. In 415 he talks Athens into Sicily, is accused of mutilating the Herms and profaning the Mysteries, and defects to Sparta rather than stand the trial (Thucydides VI). In Sparta he advises the fort at Decelea and, the story goes, fathers a child on Queen Timaea. When Sparta sours, he goes to Tissaphernes. He sells each Greek league to the Persian as a way to keep both weak. Athens recalls him. He comes home in 407 to a spectacle, restores a procession, wins at sea, then loses the city’s patience. He dies in Phrygia in 404, a house set on fire, arrows in the dark (Plutarch Alc. 38–39). Hadrian later puts marble on the tomb at Melissa.</p>
<p>He embodies Laws 6, 20, 24, 25, 48. He violates 1, 18, 19, 47. The violations kill him. The embodiments make him impossible to forget.</p>
<p>Visual references (likeness, not a claim of portraiture): Capitoline MC 1160, photograph Marie-Lan Nguyen, 2011, CC BY 2.5; the labeled mosaic at Sparta (ΑΛΚΗΒΕΙΑΔΗΣ); the painted tradition of Socrates dragging him from vice (Regnault, Gérôme, Eckersberg) — useful as Victorian fever, not as evidence.</p>
<p><em><a href="/laws/">The 48</a></em></p>
{metadata("Alcibiades", "The house object of this corpus: Alcibiades as Dualform — marble and living, Athens and the next city.", B_HEAD)}
</div>"""
    return page_shell(main)


def render_laws_index() -> str:
    rows = []
    for law in LAWS:
        href = f"/laws/{law['n']:02d}-{law['slug']}"
        rows.append(
            f"<div><div>{law['n']:02d}</div>"
            f"<div><p><a href=\"{href}\">{escape(law['title'])}</a></p></div>"
            f"<div><p>{escape(law['sentence'])}</p></div></div>"
        )
    main = f"""<div>
<h1>The 48</h1>
<p>Six courts. One body. Original commentary — not a digest of Greene. Each law is a room you can stand in.</p>
<div class="law-index">
{''.join(rows)}
</div>
{section_meta("wide")}
{metadata("The 48 Laws", "Index of the 48 Laws of Power as original 2026 commentary, with Alcibiades as the through-line.", A_HEAD)}
</div>"""
    return page_shell(main)


def render_court(slug: str, title: str, span: str, lo: int, hi: int) -> str:
    rows = []
    for law in LAWS:
        if not (lo <= law["n"] <= hi):
            continue
        href = f"/laws/{law['n']:02d}-{law['slug']}"
        rows.append(
            f"<div><div>{law['n']:02d}</div>"
            f"<div><p><a href=\"{href}\">{escape(law['title'])}</a></p></div>"
            f"<div><p>{escape(law['sentence'])}</p></div></div>"
        )
    main = f"""<div>
{dualform(
    f"Court · {span}",
    title,
    "A chapter of one life, not a module in a course.",
    A_HEAD,
    "Alcibiades in marble — the court as memory",
    B_HEAD,
    "Alcibiades living — the court as presence",
    "compact",
)}
{section_meta()}
</div>
<div>
<div class="law-index">
{''.join(rows)}
</div>
<p><a href="/laws/">All 48</a></p>
{section_meta("wide")}
{metadata(title, f"Laws {span} of the Power corpus.", A_HEAD)}
</div>"""
    return page_shell(main)


def render_law(law: dict, prev_l: dict | None, next_l: dict | None) -> str:
    n = law["n"]
    _, court_title = court_for(n)
    num = f"{n:02d}"
    prev_html = (
        f'<p><a href="/laws/{prev_l["n"]:02d}-{prev_l["slug"]}">← {prev_l["n"]:02d} {escape(prev_l["title"])}</a></p>'
        if prev_l else "<p></p>"
    )
    next_html = (
        f'<p><a href="/laws/{next_l["n"]:02d}-{next_l["slug"]}">{next_l["n"]:02d} {escape(next_l["title"])} →</a></p>'
        if next_l else "<p></p>"
    )
    alc = f"<p><em>{escape(law['alc'])}</em></p>" if law.get("alc") else ""
    main = f"""<div>
{dualform(
    f"Law {num} · {court_title}",
    law["title"],
    escape(law["sentence"]),
    A_HEAD,
    "Alcibiades in marble — substrate of the law",
    B_HEAD,
    "Alcibiades living — the law as livery on one body",
    "compact",
)}
{section_meta()}
</div>
<div>
<div class="lottie-accent">
<div>
<div>
<p><a href="{STAMP}">stamp</a></p>
<p>Law {num}</p>
</div>
</div>
</div>
<div class="power-point">
<div>
<div>Power point</div>
<div>{escape(law["point"])}</div>
</div>
</div>
<h2>In the room</h2>
<p>{escape(law["feel"])}</p>
<h2>Then</h2>
<p>{escape(law["history"])}</p>
<h2>Now</h2>
<p>{escape(law["now"])}</p>
<h2>Reversal</h2>
<p>{escape(law["reversal"])}</p>
{alc}
<div class="columns">
<div>
<div>{prev_html}</div>
<div>{next_html}</div>
</div>
</div>
<p><a href="/laws/">The 48</a> · <a href="/alcibiades">Alcibiades</a></p>
{metadata(f"Law {num}: {law['title']}", law["sentence"], B_HEAD)}
</div>"""
    return page_shell(main)


def render_nav() -> str:
    return """<body>
<header></header>
<main>
<div>
<p><a href="/">Power</a></p>
</div>
<div>
<ul>
<li><a href="/">House</a></li>
<li><a href="/alcibiades">Alcibiades</a></li>
<li><a href="/laws/">The 48</a></li>
<li><a href="/courts/the-masters-house">Courts</a></li>
</ul>
</div>
<div></div>
</main>
<footer></footer>
</body>
"""


def render_footer() -> str:
    return """<body>
<header></header>
<main>
<div>
<p>A personal Dualform corpus. Original commentary on the 48 Laws of Power. Alcibiades is the object. 2026.</p>
<p><a href="/alcibiades">The man</a> · <a href="/laws/">The laws</a></p>
</div>
</main>
<footer></footer>
</body>
"""


def write(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print(f"wrote {path.relative_to(OUT)}")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    write(OUT / "index.html", render_index())
    write(OUT / "nav.html", render_nav())
    write(OUT / "footer.html", render_footer())
    write(OUT / "alcibiades.html", render_alcibiades())
    write(OUT / "laws" / "index.html", render_laws_index())
    for slug, title, span, (lo, hi) in COURTS:
        write(OUT / "courts" / f"{slug}.html", render_court(slug, title, span, lo, hi))
    for i, law in enumerate(LAWS):
        prev_l = LAWS[i - 1] if i else None
        next_l = LAWS[i + 1] if i + 1 < len(LAWS) else None
        write(
            OUT / "laws" / f"{law['n']:02d}-{law['slug']}.html",
            render_law(law, prev_l, next_l),
        )
    print(f"done: {1 + 1 + 1 + 1 + 1 + len(COURTS) + len(LAWS)} documents")


if __name__ == "__main__":
    main()
