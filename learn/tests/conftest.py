import pytest
from starlette.testclient import TestClient

from main import get_app


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def sample_text():
    return """

I am sitting in the middle seat of the third row of a minivan. A heap of purses crowd my feet. Elbows and knees jab my sides. We are gridlocked on I-285 during Atlanta evening rush hour in a crawl-pause rhythm, our progress as tedious as arranging the frames of a stop motion animation film. The nose of our van points southeast to Savannah, the historic coastal town Union Army General Sherman spared during the Civil War. When raindrops the size of nickels smack our windshield, the hazard lights on surrounding vehicles blink on like garlands of bulbs on a Christmas tree.

“Hey,” my friend in the second row calls, craning her neck to make eye contact. “Do you want chai?”

I lean forward. The seatbelt catches my breastbone. “You want to make a stop already? We’ll never get there at this rate.”

“No, no,” says the driver, my neighbor from up the street. “We brought a thermos. And cups.”

I am incredulous, not only because my friends thought to pack chai on a four-hour road trip, but because, judging by the way the rest of my friends continue their chatter, I am the only person who finds it odd.

It’s no wonder. Among our seven passengers, six have immigrated to the U.S. from South Asia. They sip chai from morning to night. Percolating pots of fresh ginger, full fat milk and cardamom serve as background music in their homes.

I am the only one of us born and raised in the States, the only one who considers bagged tea to be actual tea, the one who stubbornly refuses to wear saris to celebrate South Asian holidays, the clueless audience for conversations rattled off in Hindi, a language I don’t understand.

I am the interpreter of academic monograms like S.A.T. and A.P., the friend who suggests they not worry so much about their kids’ grades or test scores, the beloved Aunty who sticks up for their children whenever a parental rule interferes with their enjoyment of authentically American childhoods.

Steam from the chai forms a layer of film on my face. I inhale its aroma, hopeful it will ease the dull ache in my gut, the sinking feeling my friends probably can’t decipher because they grew up in countries where their brown skin and names did not summarily mark them as outsiders. Not even these ladies, my closest friends, know that I harbor a deep-seated fear of small American cities and towns.

Like the one we’re headed to.

* * *

It is the winter of 1990, just after the U.S. begins bombing a Saddam Hussein-led Iraq for invading Kuwait in Operation Desert Storm. I am seventeen years old. Famished, I pull into a Wendy’s parking lot after a long day of school and play rehearsal. I jump out of the car, throw open the glass door to the restaurant.

A long line snakes through chain rails. The stench of oil-drenched French fries wafts through the air. I take my place at the end, extract a five-dollar-bill from my pocket.

Two men get in line behind, contemplate their orders. One has a voice that’s raspy and thick. A smoker with a cold. His friend chuckles lightly between phrases. They settle on cheeseburgers. Chili. Two large fries.

The dozen people ahead of me page through magazines, run fingers through beards, adjust baseball caps. A woman with long hair cradles a bald baby. A stream of drool leaks from her pouty lips.

I tap the face of my gold-tinted Timex. I’m running late. I could ditch the dining room for the drive-though, but the last time I tried that tactic it backfired.

“Hey, you been watching the news? Crazy shit, huh?”

It’s one of the men behind me, addressing his companion. The one who wants the chili.

His buddy cackles. A response pours out of him, as if he’s had it bottled up all day and now that it’s been uncapped, he can release it into the ether. Hope those bastards in Eh-RACK get what they deserve, blow SAD-um away, take out the whole damn country. God damned Ragheads are taking over the world.

My back rounds with an audible sigh. I think to myself, Suh-DAHM Hussein is the president of Ir-RAHK, not Eh-RACK. He doesn’t wear a turban. Not everyone east of the Mediterranean Sea does.

One of the men, the raspy one, has apparently read my mind. He moves closer. His shadow eclipses mine. His hot, tobacco-tinged breath seeps over the collar of my dress. “We need to drive the sand niggers out of this country, too.”

His voice is low, quiet. Each syllable erupts with spittle. I imagine it sticking to the back of my hair like discarded chewing gum.

“They don’t belong here. They should go back to where they came from.”

I shut my eyes. The force of my held breath presses against my ribs. My mind floods with everything I ever learned about self-defense, and two years’ worth of expensive tae kwon do lessons: Stab their eyeballs out with your keys kick them in the groin smack their ears with your flattened palms yell “Fire” “Don’t touch me!” round-house kick to the neck piss your underwear vomit in his face.

I try to figure out what might work here, in this public space, when these men have yet to lay a hand on me.

My saddle oxfords inch forward. The shoes behind me echo in tandem.

“Muslims… Arabs… illegal alien bastards…”

The thumping in my eardrums drowns out the prepositions and verbs.

All I have to do is leave. All I have to do is lift my leaden feet, place one in front of the other, dart toward the exit. But if they follow me out, I will be alone with them in the parking lot. No one will hear my screams over the music flowing from the dining room’s speakers, the calling out of order numbers, the tantrumming toddler in the booth.

A young woman with a blond bob smacks her gum, flips open a compact to check her lipstick. She’s waiting at the counter to pick up her meal. I stare hard at her profile, will her to look at me, to engage me in a conversation about the weather. Anything. She’s oblivious. Or maybe she knows exactly what’s happening, but just doesn’t give a damn.

“Can I help you?”

It’s the visored woman behind the register, addressing me, the first person in line. She keeps her eyes on the buttons, bobs her head to a silent rhythm. I scan the overhead menu, a menu I probably have memorized. Suddenly I don’t know why I’m here, what I want to eat.

My mind has become a string of ellipses, a blinking cursor on a blank screen.

Impatience settles between her eyebrows. Her long, fuchsia nails tap the side of the register. I want to signal her about the two men terrorizing me. I think of bank tellers held up by robbers, how in the movies they slide their fingers ever so slightly under the lip of the counter to push a panic button. I wish I had one of those.

My order comes to me. “One baked potato, to go, please.”

I want a frosty, too. I always get a frosty. But I’m too afraid to tack it onto my order. The machine’s slow expulsion of thick chocolate will take too much time. The baked potatoes sit under warming lights, like baby chicks in an incubator. In mere seconds a gloved hand can caress the oval-shaped aluminum pod like a silver football and hurl it into a bag.

I thrust money in the cashier’s direction. She takes her time counting out bills in my palm. Coins shoot out the side of the register like pinballs. I slide further down the counter. My fingers run along its edge, as if it’s base in a game of tag.

The two men step up to place their orders. I catch a glimpse of them in my periphery. One has light-brown hair, too-thick sideburns. The other strokes his sculpted goatee. They have soft, clean faces, pressed clothes. They are young. Nothing like the caricatures I’d imagined.

I would never have pegged them as racists in a line-up.

At the counter, their demeanors transform. Their voices assume a relaxed, friendly, tone. They’ve turned their hatred off like a faucet.

“Yes, Ma’am,” one of them responds, when the cashier reads back the order.

Did I imagine their cruelty? If I am the only witness, did it really happen?

My aggressors begin their perp walk alongside the counter, rattle off stats for their favorite basketball team.

A woman wearing a headset calls my number, hands me a paper bag. It crinkles loudly in my grasp. I bolt past the condiments, the soda dispenser, around the trashcans, throw open the glass door.

I don’t look back.

My hand shakes so badly I can’t slide my key into the keyhole. When it finally complies, I dive into the driver’s seat, slam the door shut, turn the ignition, hit the stick shift into reverse. I speed around the drive-through line until the parking lot spits me back onto the main road. My hands grip the steering wheel so tightly it indents my palms.

I glance in the rearview mirror.

I think of all the things I should have said to those men: I was born in Michigan, have lived in Tennessee for seven years. I’m not Iraqi or Arab or Muslim but even if I were, I don’t deserve your hatred. I’m a harmless teenager who loves Def Leppard and Coca Cola and Johns Hughes films.

A few miles away, I pull into a gas station, open the paper bag, tear into the spoon’s plastic sheath. My stomach growls. But when I unwrap the foil, the brown, leathery skin and white buttered flesh initiate my gag reflex. I stuff everything back inside the bag, jump out of the car, hurl it into the nearest trashcan. It hits the bottom with a hollow thud, like a stone.

* * *

When you are brown in America, there’s no such thing as exculpatory evidence. You are an aberration, a foreigner from a foreign land, no matter your American citizenship, no matter if every home you’ve ever lived in was built on American soil. Every disparaging comment about terrorism is directed to you. Every illegal border crossing implicates you.

Your great American privilege comes with severe limitations.

As I grew older, I would remember to keep my hands visible at all times in chic department stores in the elite suburbs of St. Louis, to stifle the flow of tears post-9/11, in the Philadelphia International Airport during security checks so humiliating and exhaustive I’d miss flights, to remain calm while waiting to cast a vote in a presidential election amid racist remarks fired off like a round of bullets, to shrink myself in overwhelmingly white spaces, to be both present and disappear, like dust in the wind.

Despite my American birth, I am not any more tied to this land than my foreign-born father is. I have inherited his immigrant status, like a dominant gene. It will underlie my identity narrative, no matter how many legal documents verify my nationality, no matter how many times I testify that I belong.

No matter who stands behind me in line.

* * *

The weather in Savannah refuses to cooperate. Sheets of rain soak through our jackets, smudge the lenses of our glasses, drench our shoes. We seek refuge in a red touring trolley reminiscent of the one in Mr. Rogers’ Neighborhood. As we step into its belly, I survey the tourists poring over guidebooks, tapping their phones. I worry one of them will mutter something derogatory about this group of seven brown women whose mere presence seems to have doubled the minority population of this historic district.

They ignore us.

Relieved, I settle into a bench seat, rest my forehead against a misty window, shift my attention to the landscape, the elegance of the low country, in the way Spanish moss swathes live oak branches like a much-beloved quilt.

* * *

The rain trickles to echoes in gutters. The sun elbows its way through the last gray clouds. Our silhouettes weave between Corinthian columns of grand estate homes, traverse through Savannah’s famous squares. The soles of our shoes meet colonial cobblestones laid well before any of our family trees branched into America.

We convene for lunch at Clary’s, the infamous diner featured as a gossip hub in John Berendt’s book Midnight in the Garden of Good and Evil. At the table, our hands cradle mugs of coffee to warm damp bones. We slurp down French onion soup, sink teeth into buttermilk biscuits as fluffy as clouds. When we’ve licked our plates clean, we ask the server to take our photo, gather to one side of the table, and squeeze together to fit in the frame.
The pose triggers the memory: I am standing in line at Wendy’s, hot breath at my neck, stress crushing my chest. Twenty years later, not even the shelter of dear friends, the festive tone of a cocktail-infused weekend, can protect me from this trauma. It has imbedded itself in my psyche, has reared its ugly head without warning or apology, even in moments, like this one, of levity.
This is its legacy.
I have wondered over the years about those men, where they are today. I wonder if they understand what they stole from me, how their slurs vibrate in the tympanic membrane of my eardrum in perpetuity. I wonder, in the intervening years, if they have changed. And then I read an article about the current state of racial hatred in the U.S., in the world, and I feel certain they have not.
Outside of Clary’s, evidence of the weekend’s storms linger in shallow puddles and tree branches thick with beads of saturation. My phone’s storage space diminishes as photos supplant bytes. Here we are, clinking wine glasses over dinner, there we are, posing in front of The Cathedral of Saint John the Baptist, perusing t-shirts at River Street Market, feigning fear on a ghost tour.
When it’s time to leave, to resume our lives, reunite with our families, I crawl back into the third row, middle seat, rest my weary head on the shoulder of another. Our van, due northwest on I-16, departs the city, bisects the low lands of the coastal plain, toward Atlanta, through the state we all call home.
    """
