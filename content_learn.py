"""Learn the basics. Each topic: (title, tip, one phrase per line).
Contractions show the full form, then the short form: "I am tired. -> I'm tired." (they never go through contract())."""

CONTRACTIONS = [
("I'm, you're, he's, she's, it's, we're, they're", "Be + subject: the verb gets shorter and joins the word before it.", """
I am tired. -> I'm tired.
I am at home. -> I'm at home.
You are right. -> You're right.
You are very kind. -> You're very kind.
He is my brother. -> He's my brother.
She is a nurse. -> She's a nurse.
It is cold today. -> It's cold today.
It is late. -> It's late.
We are ready. -> We're ready.
We are on our way. -> We're on our way.
They are my neighbors. -> They're my neighbors.
They are at work. -> They're at work.
"""),
("don't, doesn't, didn't", "Do + not. Use doesn't with he, she and it.", """
I do not know. -> I don't know.
I do not like coffee. -> I don't like coffee.
We do not have time. -> We don't have time.
They do not live here. -> They don't live here.
He does not work on Sundays. -> He doesn't work on Sundays.
She does not eat meat. -> She doesn't eat meat.
It does not matter. -> It doesn't matter.
I did not see it. -> I didn't see it.
We did not go out. -> We didn't go out.
She did not call me. -> She didn't call me.
Do not worry. -> Don't worry.
Did you not hear me? -> Didn't you hear me?
"""),
("isn't, aren't, wasn't, weren't", "Be + not. For I, say I'm not. Nobody says I amn't.", """
It is not far. -> It isn't far.
This is not my car. -> This isn't my car.
The store is not open yet. -> The store isn't open yet.
They are not here. -> They aren't here.
The kids are not hungry. -> The kids aren't hungry.
I am not sure. -> I'm not sure.
It was not easy. -> It wasn't easy.
He was not at home. -> He wasn't at home.
The food was not bad. -> The food wasn't bad.
We were not ready. -> We weren't ready.
They were not happy. -> They weren't happy.
You were not there. -> You weren't there.
"""),
("can't, couldn't, won't, wouldn't, shouldn't", "Won't is the short form of will not. It sounds like 'wont'.", """
I cannot find my keys. -> I can't find my keys.
She cannot come today. -> She can't come today.
I could not sleep last night. -> I couldn't sleep last night.
We could not find a parking spot. -> We couldn't find a parking spot.
I will not be late. -> I won't be late.
It will not take long. -> It won't take long.
He would not listen to me. -> He wouldn't listen to me.
I would not do that. -> I wouldn't do that.
You should not drive so fast. -> You shouldn't drive so fast.
We should not wait any longer. -> We shouldn't wait any longer.
The door will not open. -> The door won't open.
"""),
("I'll, you'll, we'll", "Will + verb for the future and for quick decisions: I'll get it!", """
I will call you later. -> I'll call you later.
I will be there at six. -> I'll be there at six.
I will have a coffee, please. -> I'll have a coffee, please.
You will love this place. -> You'll love this place.
You will see. -> You'll see.
We will talk tomorrow. -> We'll talk tomorrow.
We will be back soon. -> We'll be back soon.
She will help you. -> She'll help you.
He will be fine. -> He'll be fine.
They will arrive tonight. -> They'll arrive tonight.
It will be okay. -> It'll be okay.
"""),
("I've, you've, we've", "Have + past participle: I've been, I've seen, I've had.", """
I have been here before. -> I've been here before.
I have seen that movie. -> I've seen that movie.
I have had a long day. -> I've had a long day.
I have finished my work. -> I've finished my work.
You have been very helpful. -> You've been very helpful.
You have changed a lot. -> You've changed a lot.
We have met before. -> We've met before.
We have lived here for two years. -> We've lived here for two years.
They have already left. -> They've already left.
She has never been to New York. -> She's never been to New York.
He has lost his phone. -> He's lost his phone.
"""),
("I'd = I would or I had", "I'd like means I would like. I'd better means I had better.", """
I would like a glass of water. -> I'd like a glass of water.
I would like to go home. -> I'd like to go home.
I would love to come. -> I'd love to come.
I would rather stay in. -> I'd rather stay in.
We would like to order now. -> We'd like to order now.
She would like some help. -> She'd like some help.
I had better go now. -> I'd better go now.
You had better hurry. -> You'd better hurry.
We had better leave early. -> We'd better leave early.
I had never seen snow before. -> I'd never seen snow before.
If I were you, I would wait. -> If I were you, I'd wait.
"""),
("let's, that's, there's, what's, here's, who's", "Very common at the start of a sentence. Use them all day.", """
Let us go. -> Let's go.
Let us eat something. -> Let's eat something.
That is great. -> That's great.
That is not what I meant. -> That's not what I meant.
There is a problem. -> There's a problem.
There is a pharmacy on the corner. -> There's a pharmacy on the corner.
What is your name? -> What's your name?
What is wrong? -> What's wrong?
Here is your change. -> Here's your change.
Here is my number. -> Here's my number.
Who is that man? -> Who's that man?
Who is coming tonight? -> Who's coming tonight?
"""),
("The confusing ones", "Same sound, different meaning. It's = it is, but its = belongs to it.", """
It is raining. -> It's raining.
The dog wants its toy.
You are late. -> You're late.
Is this your bag?
They are friends. -> They're friends.
That's their house.
Put it over there.
He is tired. -> He's tired.
He has been busy. -> He's been busy.
She is from Texas. -> She's from Texas.
She has got two kids. -> She's got two kids.
"""),
("gonna, wanna, gotta, kinda", "Spoken English only. Say them, but don't write them in an email.", """
I am going to call her. -> I'm gonna call her.
We are going to be late. -> We're gonna be late.
It is going to rain. -> It's gonna rain.
I want to go home. -> I wanna go home.
Do you want to eat? -> Do you wanna eat?
I have got to go. -> I've gotta go.
You have got to try this. -> You've gotta try this.
We have got to leave now. -> We've gotta leave now.
I am kind of tired. -> I'm kinda tired.
It is kind of cold. -> It's kinda cold.
I sort of like it. -> I sorta like it.
"""),
]

VOCAB = [
("Feelings and emotions", "Say how you feel with I'm or I feel.", """
I'm really happy today.
I'm so tired after work.
I feel a little nervous.
I'm worried about my mom.
The kids are excited about the trip.
I'm bored. There's nothing to do.
I get frustrated in traffic.
I'm proud of my son.
I'm sad that you're leaving.
She's angry with me.
I'm a little stressed this week.
I feel much better now.
Don't be scared. It's okay.
I'm surprised to see you here.
"""),
("Body parts", "At the doctor: my + body part + hurts.", """
My back hurts.
I have a headache.
My throat is sore.
I have a stomachache.
My knee hurts when I walk.
I hurt my hand at work.
My eyes are tired.
I have a pain in my chest.
My feet are killing me.
I cut my finger.
My shoulder is stiff.
I have a toothache.
My ears hurt on the plane.
"""),
("Days of the week", "On + day: on Monday. Every Friday. Next Tuesday.", """
I work on Monday.
See you on Wednesday.
We play soccer every Saturday.
I'm off on Fridays.
What are you doing on Sunday?
The store is closed on Sundays.
I have a meeting next Tuesday.
I saw her last Thursday.
The weekend starts on Friday night.
Mondays are always busy.
Can we meet on Thursday instead?
I go to the gym three days a week.
"""),
("Months of the year", "In + month: in March. On + date: on March fifth.", """
My birthday is in July.
We're going on vacation in August.
It's very hot in June.
School starts in September.
I moved here in January.
It gets cold in December.
My son was born in April.
We got married in May.
The rainy season starts in October.
I'll see you in February.
Is your birthday in March?
November is my favorite month.
"""),
("Seasons and holidays", "In the summer, in the winter. On Christmas Day. At Christmas.", """
I love the summer.
It snows a lot in the winter.
The leaves change color in the fall.
Spring is my favorite season.
What do you do for Christmas?
We spend Thanksgiving with my family.
Happy New Year!
Merry Christmas to you and your family.
We go to the beach every summer.
Are you doing anything for Easter?
We celebrate with a big dinner.
Happy birthday! How old are you today?
"""),
("Telling the time", "At + time: at seven thirty. In the morning, at night.", """
What time is it?
It's seven thirty.
It's a quarter past nine.
It's half past six.
It's a quarter to five.
It's almost noon.
I get up at six in the morning.
I go to bed at eleven at night.
The movie starts at eight.
I'll be there in ten minutes.
We're open from nine to five.
Do you have the time?
It's a little after three.
"""),
("Dates and years", "Say dates with ordinals: November fifth, not November five.", """
What's the date today?
Today is November fifth.
My birthday is on May third.
I was born in 1990.
We moved here in 2018.
The party is on the twenty-first.
I'll be back on the first of June.
The deadline is next Friday, the twelfth.
It happened two years ago.
We met in the summer of 2015.
The baby is due in March.
It's the second time this week.
"""),
("Prices and money", "How much is it? How much are they? Use is for one thing.", """
How much is it?
How much are these shoes?
It's twenty dollars.
That's too expensive.
It's on sale today.
Do you take credit cards?
Can I pay in cash?
Do you have change for a twenty?
Here's your receipt.
I need to save money.
That's a good deal.
Can I get a discount?
I'll pay for dinner tonight.
It costs about fifty dollars.
"""),
("Family members", "My mom, my dad, my wife, my husband, my kids.", """
This is my wife.
My husband works at the hospital.
I have two kids, a boy and a girl.
My older brother lives in Florida.
My younger sister is still in school.
My parents are retired.
My grandmother is ninety years old.
I have a lot of cousins.
My aunt and uncle live near us.
My son is five years old.
My daughter just started college.
My in-laws are visiting this weekend.
I'm an only child.
"""),
("Colors and describing things", "The describing word goes before the thing: a big house.", """
I have a blue car.
I'm looking for a black jacket.
It's a big house with a small yard.
This phone is cheap, but it's good.
That's really expensive.
The room is clean and quiet.
The coffee is too hot.
These shoes are very comfortable.
It's a little old, but it works.
I like the red one.
The new store is huge.
The street is dark at night.
It's heavy. Can you help me?
"""),
("Rooms and things at home", "In the kitchen, in the bedroom, on the table.", """
The keys are on the kitchen table.
The kids are in their bedroom.
I'm in the living room.
Can you turn off the light?
The bathroom is down the hall.
I left my phone on the couch.
The fridge is almost empty.
Please close the window. It's cold.
The towels are in the closet.
I need to wash the dishes.
We're painting the garage.
Turn on the TV, please.
There's a lot of noise upstairs.
"""),
("Clothes", "Put on your jacket. Take off your shoes. Wear a hat.", """
I need a new pair of jeans.
Put on your jacket. It's cold.
Please take off your shoes.
I'm wearing a white shirt.
These pants are too tight.
Do you have this in a smaller size?
Can I try it on?
I like your shoes.
I always wear a hat in the sun.
My socks are wet.
She looks great in that dress.
I need a warm coat for the winter.
"""),
("Places in town", "At the bank, at the pharmacy, at the supermarket.", """
Is there a bank near here?
I need to go to the pharmacy.
I'm at the supermarket right now.
The gas station is on the corner.
Let's meet at the coffee shop.
The post office closes at five.
I'm going to the hospital to see my uncle.
The kids are at school.
Is the library open today?
There's a nice park downtown.
I'll drop you off at the bus stop.
The mall is always crowded on weekends.
Where's the nearest restroom?
"""),
("Jobs and work", "I work as a teacher. I work at a hospital. I work in sales.", """
I work as a teacher.
I work at a hospital.
She's a nurse.
He's an engineer.
I work from home three days a week.
I start work at eight.
I'm looking for a new job.
My boss is very nice.
I have a lot of work this week.
I work the night shift.
I'm off today.
My coworkers are great.
I got a new job last month.
"""),
("Question words", "Who for people, where for places, when for time, why for reasons.", """
Who is that?
What do you need?
Where do you work?
When does the store open?
Why are you late?
How are you doing?
How much does it cost?
How long does it take?
How often do you go to the gym?
Which one do you want?
Whose phone is this?
How many kids do you have?
How far is the airport?
"""),
("In, on, at", "In May, in the morning. On Monday, on the table. At night, at home.", """
I was born in May.
We go out in the evening.
See you on Monday.
The cup is on the table.
I'm at home now.
I work at night.
She lives in a small town.
Meet me at the entrance.
The party is on Saturday night.
I'll call you in an hour.
The picture is on the wall.
I'm at work until five.
We arrived in Miami on Friday.
"""),
("Everyday verbs: get, take, make, do, have, go", "These six verbs do most of the work in English.", """
I get up at six.
I'll get some milk on the way home.
Take your time.
I take the bus to work.
Can you take a picture of us?
I'll make some coffee.
Don't make noise. The baby is sleeping.
I need to do the laundry.
Can you do me a favor?
Let's have lunch together.
I have a question.
We go out on Fridays.
I'm going to bed.
It takes twenty minutes to get there.
"""),
]
