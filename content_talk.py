"""Keep it going, talk about your life, fix it. Each topic: (title, tip, one phrase per line)."""

LIFESAVERS = [
("Buying time", "A short phrase gives you three seconds to think.", """
Let me think.
Good question.
Hmm, let me see.
Give me a second.
That's a good question.
How can I put this?
Well, it's hard to say.
Let me think about that for a moment.
I've never thought about that.
Wait, let me remember.
Oh, that's a tough one.
I'm trying to think of the word.
"""),
("Asking someone to repeat", "Ask without saying sorry three times. One sorry is enough.", """
Sorry, can you repeat that?
Could you say that again, please?
Sorry, I didn't catch that.
Can you speak a little slower, please?
Sorry, what did you say?
Pardon?
Could you say the last part again?
Sorry, it's a little noisy here.
Did you say Tuesday or Thursday?
Can you spell that for me?
One more time, please.
"""),
("Asking for a word", "When a word is missing, describe it or ask for it.", """
How do you say this in English?
What's the word for this?
What do you call the thing you use to open cans?
What does that word mean?
How do you spell it?
How do you pronounce this word?
Is that the right word?
I don't know the word, but it's like a small knife.
It's the place where you buy medicine.
What's another word for that?
Can you write it down for me?
"""),
("Correcting yourself", "Fix it and keep going. People care about the message.", """
What I mean is, I'm busy today.
Sorry, I meant Friday, not Thursday.
Let me say that again.
No, wait. That's not right.
I mean, it was okay, not great.
Let me put it another way.
Actually, it was last week.
Sorry, I said that wrong.
In other words, I need more time.
What I'm trying to say is thank you.
"""),
("When you don't understand", "Say what you understood, then ask about the rest.", """
I'm not sure I understand.
Sorry, I'm a little lost.
What do you mean?
Can you explain that again?
Do you mean today or tomorrow?
Can you give me an example?
So, you want me to wait here?
I understood the first part, but not the second.
Let me see if I got that right.
Can you say it in a different way?
I'm sorry, my English isn't perfect yet.
"""),
("Ending a conversation", "End kindly: a reason, a thank you and a goodbye.", """
Well, it was nice talking to you.
I'm sorry, I have to go.
I don't want to keep you.
Let's catch up soon.
I'll let you go.
Thanks for the chat.
I'll see you around.
Take care.
Have a good one.
Talk to you later.
Say hi to your family for me.
I've got to run, but let's talk soon.
"""),
]

BUILDERS = [
("I'd like to...", "Polite and soft. Perfect for asking, ordering and wishing.", """
I'd like to make an appointment.
I'd like to try this on.
I'd like to order, please.
I'd like to speak to the manager.
I'd like to learn to swim.
I'd like to visit Spain one day.
I'd like to pay with my card.
I'd like to change my reservation.
I'd like to help you.
I'd like a table for two, please.
I'd like to cancel my order.
"""),
("I used to...", "Something you did before, but not now.", """
I used to live in Mexico.
I used to smoke, but I quit.
I used to play soccer every day.
I used to work at a bank.
We used to go to the beach every summer.
She used to be my neighbor.
I used to hate vegetables.
This place used to be a school.
I didn't use to like coffee.
Did you use to live here?
I used to be very shy.
"""),
("I've lived here for...", "Started in the past and still true now. Use for or since.", """
I've lived here for five years.
I've worked here for a long time.
I've known her since high school.
We've been married for ten years.
I've had this car since 2019.
I've been here since eight this morning.
How long have you been in this country?
I've worked as a cook for twelve years.
I've been sick for three days.
I've studied English for two years.
"""),
("I'm thinking about...", "A plan you're not sure about yet. Use a verb with -ing.", """
I'm thinking about moving.
I'm thinking about buying a new car.
We're thinking about having another baby.
I'm thinking about taking a class.
I'm thinking about changing jobs.
I'm thinking about you.
We're thinking about going out tonight.
He's thinking about selling his house.
I'm thinking about getting a dog.
Are you thinking about coming?
"""),
("I'm trying to...", "Something you're working on, or something that's hard.", """
I'm trying to lose weight.
I'm trying to save money.
I'm trying to learn English.
I'm trying to find a parking spot.
I'm trying to call my sister.
I'm trying to sleep more.
I'm trying to fix my bike.
We're trying to find a bigger apartment.
I'm trying to understand.
I'm trying to eat healthy.
Stop. I'm trying to work.
"""),
("It depends on...", "No easy answer? Say what the answer depends on.", """
It depends on the weather.
It depends on the price.
It depends on my schedule.
It depends.
It depends on how I feel.
It depends on what you need.
It depends on the traffic.
Everything depends on the doctor.
It really depends on the person.
It depends on how much time we have.
"""),
("The thing is...", "Use it to explain the real problem, gently.", """
The thing is, I'm really busy.
The thing is, I don't have a car.
The thing is, it's too expensive.
The thing is, I already said yes.
The thing is, we don't have enough time.
The thing is, I've never done this before.
The problem is, the store is closed.
The good thing is, nobody got hurt.
The funny thing is, I knew it.
The best thing is, it's free.
"""),
("I'm not sure if...", "If or whether, then the rest of the sentence.", """
I'm not sure if I can come.
I'm not sure if it's open.
I'm not sure if she knows.
I'm not sure if this is right.
I'm not sure what to do.
I'm not sure where it is.
I'm not sure how to say it.
I'm not sure when he's coming.
I'm not sure it's a good idea.
I don't know if I'll have time.
"""),
]

QUESTIONS = [
("What do you do?", "This question is about your job. Answer with I'm a... or I work...", """
What do you do?
I'm a teacher.
I work in a hospital. I'm a nurse.
I work in construction.
I'm a stay-at-home mom.
I'm retired now.
I'm between jobs right now.
I run my own business.
I'm a student. I study nursing.
I work for a big company, in sales.
I drive for a delivery company.
I'm a cook at a restaurant downtown.
"""),
("Where are you from?", "Say your country or your city. Add one detail.", """
Where are you from?
I'm from Puerto Rico.
I'm from Mexico, from a small town near Puebla.
I was born in Colombia, but I grew up here.
I'm from Venezuela. I've lived here for six years.
Originally, I'm from the Dominican Republic.
I'm from Cuba. My family is still there.
I'm from here.
I'm from the south, near the beach.
My parents are from Peru, but I was born in Texas.
I'm from a big city. It's very busy.
"""),
("Where do you live?", "In + city. On + street. Near + place.", """
Where do you live?
I live in Orlando.
I live near the hospital.
I live in a small apartment downtown.
We live in a quiet neighborhood.
I live with my parents for now.
I live about twenty minutes from here.
We just moved to a new house.
I live on Main Street.
I live in the country. It's very peaceful.
I share an apartment with two friends.
"""),
("What do you do on weekends?", "Use the present simple for habits: I usually..., I always...", """
What do you do on weekends?
I usually relax at home.
I play soccer with my friends.
I spend time with my family.
I clean the house and do the laundry.
We go to the beach when it's sunny.
I go to church on Sunday.
I like to cook a big breakfast.
I sleep late. I'm always tired on Saturday.
I work on weekends, so I'm off on Mondays.
We visit my parents every Sunday.
"""),
("How was your day?", "Give one detail. It keeps the conversation going.", """
How was your day?
It was good, thanks. How about you?
It was long. I'm exhausted.
Pretty busy, but good.
Not bad. Nothing special.
It was great. I got some good news.
Terrible. Everything went wrong.
It went well. I finished early.
It was okay. Work was crazy.
Quiet. I stayed home and rested.
It was a little stressful, but I'm fine.
"""),
("Do you have kids?", "Answer, then ask back: How about you?", """
Do you have kids?
Yes, I have two. A boy and a girl.
Yes, I have a daughter. She's seven.
No, not yet.
No, I don't have kids, but I have a dog.
Yes, three. They keep me busy.
My kids are grown up now.
Yes, a baby boy. He's six months old.
We're expecting our first baby in May.
No, but I have a lot of nieces and nephews.
Yes, two teenagers. Wish me luck.
"""),
("What do you like to do?", "Use like or love + verb with -ing.", """
What do you like to do?
I like reading.
I love cooking for my family.
I like watching soccer.
I enjoy going for walks.
I love music. I play the guitar.
I like going to the movies.
I like spending time outside.
I'm into video games.
I really like traveling.
I don't have much free time, but I like to dance.
"""),
("How long have you lived here?", "Use for with a period of time, since with a start.", """
How long have you lived here?
I've lived here for three years.
Since 2020.
Just a few months.
All my life.
About ten years now.
I moved here when I was a kid.
Not long. I just arrived in June.
Almost five years. Time flies.
Since I got married.
"""),
]

EVERYDAY = [
("Food and restaurants", "Order with I'll have... or Can I get...?", """
A table for four, please.
Can I see the menu?
What do you recommend?
I'll have the chicken, please.
Can I get a glass of water?
No onions, please.
This is delicious.
Can we get the check, please?
Can I get this to go?
I'm allergic to peanuts.
I'm starving. Let's eat.
I'm full. I can't eat another bite.
What are you having?
"""),
("Family and home", "Talk about who lives with you and what you do at home.", """
I live with my wife and two kids.
My mom lives with us.
We have a small house with a yard.
It's my turn to cook tonight.
The kids help with the dishes.
We eat dinner together every night.
My house is always a mess.
We're fixing the roof this month.
My brother is staying with us for a while.
I love Sunday mornings at home.
We just got a new couch.
"""),
("Work", "Talk about your day, your schedule and your coworkers.", """
I have a meeting at ten.
I'm working late tonight.
I got a promotion last month.
I'm on vacation next week.
My boss gave me a raise.
We're short on staff this week.
I'm really busy at work.
I asked for a day off.
I'll send you the email today.
My shift ends at six.
I like my job, but it's hard.
"""),
("Sports", "Play soccer, play basketball. Go running, go swimming.", """
Do you like soccer?
I play soccer on Sundays.
Who's your favorite team?
Did you watch the game last night?
We won three to one.
It was a tie.
I go running every morning.
I'm not very good, but I have fun.
My son plays on a team.
Let's watch the game at my place.
He scored a great goal.
I go swimming twice a week.
"""),
("The weather", "It's + adjective: it's hot, it's cold, it's windy.", """
It's really hot today.
It's freezing outside.
It looks like rain.
It's raining again.
What's the weather like?
It's a beautiful day.
It's very humid.
There's a storm coming.
It's windy. Hold your hat.
I hope it's sunny this weekend.
It's cooler in the evening.
The forecast says rain tomorrow.
"""),
("Your town", "Describe where you live: big, small, quiet, busy.", """
I live in a small town.
It's quiet and very safe.
Everybody knows everybody.
There isn't much to do at night.
There's a nice park near my house.
The beach is fifteen minutes away.
Traffic is terrible in the morning.
It's a great place to raise kids.
The food here is amazing.
There's a big festival every summer.
I love my neighborhood.
"""),
("Shopping", "Ask where things are, try things on, and pay.", """
Excuse me, where can I find the milk?
Do you have this in blue?
I'm just looking, thanks.
Where are the fitting rooms?
It's a little too big.
I'll take it.
Can I return this?
I'd like to return this, please.
Do you have it in stock?
Is this on sale?
Where do I pay?
I need a bag, please.
"""),
("Health and the doctor", "Say how long: I've had a fever since Monday.", """
I don't feel well.
I need to see a doctor.
I'd like to make an appointment, please.
I've had a fever since Monday.
I have a bad cough.
I feel dizzy.
I'm allergic to penicillin.
How often should I take this?
Do I need a prescription?
I think I have the flu.
I'm feeling better, thanks.
I hurt my ankle playing soccer.
I can't sleep at night.
"""),
("Weekend plans", "Going to for plans: I'm going to visit my mom.", """
What are you doing this weekend?
Any plans for the weekend?
I'm going to visit my mom.
We're having a barbecue on Saturday.
I don't have any plans yet.
I'm going to rest. I need it.
Do you want to come with us?
Let's go to the movies.
I'm meeting some friends for dinner.
We might go to the beach.
I have to work on Saturday.
How was your weekend?
"""),
]

STORY = [
("Yesterday I...", "Past simple for finished actions: went, saw, made, had.", """
Yesterday I went to the store.
Yesterday I worked all day.
Last night I watched a movie.
This morning I woke up late.
Last weekend we visited my aunt.
Yesterday I cooked dinner for my family.
Last Friday I went out with friends.
Yesterday I called the doctor.
Two days ago I lost my wallet.
Last year we went to Mexico.
Yesterday I didn't do anything.
"""),
("First, then, after that", "Connectors tell the listener the order. Use them slowly.", """
First, I took a shower.
Then I had breakfast.
After that, I drove to work.
Next, I checked my email.
Then we went to the park.
After lunch, we took a nap.
Before dinner, I went for a walk.
After that, we watched TV.
Later, my brother came over.
At the end of the day, I was exhausted.
Meanwhile, the kids were playing.
"""),
("Suddenly", "Use it for the surprise moment of your story.", """
Suddenly, the lights went out.
Suddenly, it started to rain.
All of a sudden, my phone rang.
Suddenly, I heard a loud noise.
Out of nowhere, a dog ran into the street.
Suddenly, I remembered my keys.
I was walking home when I saw an old friend.
We were eating when the power went out.
I was driving when my car stopped.
Then something strange happened.
"""),
("In the end", "Finish your story with the result.", """
In the end, everything was fine.
In the end, we missed the bus.
Finally, we got home at midnight.
Luckily, nobody got hurt.
In the end, I bought the cheaper one.
At last, the doctor called me.
In the end, it was a great day.
So, that's what happened.
Long story short, I got the job.
Anyway, we had a lot of fun.
"""),
("Irregular verbs: go, see, have, make", "Learn them in pairs: go, went. See, saw. Have, had. Make, made.", """
I went to the beach.
We went home early.
I saw my cousin at the store.
Did you see that?
I had a great time.
We had pizza for dinner.
I made a mistake.
She made a cake for my birthday.
He came to my house.
I got a new phone.
I took the kids to school.
I gave her a present.
"""),
("Irregular verbs: say, tell, think, buy", "Say, said. Tell, told. Think, thought. Buy, bought.", """
She said yes.
He told me the truth.
I thought it was closed.
I bought some bread.
I found my keys under the bed.
We left at seven.
I knew it.
I ate too much.
I drank a lot of water.
I forgot my lunch at home.
I felt sick in the morning.
I slept nine hours.
"""),
("A bad day", "Tell a small problem with a beginning, a middle and an end.", """
I had a terrible day.
First, my alarm didn't go off.
I missed the bus and got to work late.
My boss wasn't happy.
Then I spilled coffee on my shirt.
At lunch, I forgot my wallet.
On the way home, it started to pour.
I got home soaking wet.
But my kids made me dinner.
In the end, it wasn't so bad.
"""),
("A trip", "Where, who, what you did, how it was.", """
Last summer we went to Florida.
We drove for ten hours.
We stayed in a small hotel near the beach.
The weather was perfect.
We swam every day.
We tried a lot of new food.
The kids loved the water park.
One day we got lost.
It was the best vacation ever.
I can't wait to go back.
"""),
]

REACT = [
("Giving your opinion", "Start soft: I think, in my opinion, for me.", """
I think it's a good idea.
In my opinion, it's too expensive.
For me, family comes first.
I feel like it's too late.
If you ask me, it's not worth it.
I believe you're right.
Personally, I prefer the beach.
To be honest, I didn't like it.
I don't think so.
I guess it's okay.
"""),
("Agreeing", "Short and natural. You can agree with two words.", """
I agree.
I totally agree.
You're right.
Exactly.
That's true.
Me too.
Me neither.
Good point.
Same here.
I think so too.
Absolutely.
"""),
("Disagreeing politely", "Soften it first: I see your point, but...", """
I don't agree.
I see your point, but I'm not sure.
I'm not so sure about that.
I see it a little differently.
Maybe, but I think it's too risky.
That's true, but it's expensive.
I don't really agree with that.
Sorry, but I think you're wrong.
I understand, but I don't like it.
Let's agree to disagree.
"""),
("Surprise and interest", "Your voice goes up. It shows you're listening.", """
Really?
No way!
Are you serious?
Wow, that's amazing!
I can't believe it!
That's interesting.
Oh, I didn't know that.
That's crazy!
You're kidding!
Seriously?
That's so cool.
"""),
("Understanding and making sense", "Show the other person that you follow the idea.", """
That makes sense.
I see.
Oh, I get it now.
Got it.
Okay, I understand.
That explains it.
Now I see what you mean.
Fair enough.
I hear you.
That's a good way to put it.
"""),
("When you're not sure", "It's okay not to have an opinion yet.", """
I'm not sure.
Maybe.
I don't know yet.
I'll think about it.
It's hard to say.
I'm not sure about that.
Could be.
I have no idea.
I haven't decided yet.
Let me think about it.
"""),
("Follow-up questions", "One more question shows real interest.", """
What happened next?
And then what?
How did you feel?
Why do you think that happened?
What did you do?
How was it?
Did you like it?
Who did you go with?
Are you going to go back?
Tell me more.
What do you mean by that?
"""),
("Good news and bad news", "Match the feeling: happy for them, or sorry.", """
Congratulations!
That's great news!
I'm so happy for you.
Good for you!
You deserve it.
I'm sorry to hear that.
Oh no, that's terrible.
That's too bad.
I hope everything is okay.
Let me know if you need anything.
That must be hard.
"""),
]

MISTAKES = [
("He, she, it + s", "With he, she and it, the verb ends in -s: she works, it fails.", """
She works at a bank.
He lives in Texas.
My dad watches the news every night.
My son plays soccer.
The store opens at nine.
It fails every time.
She speaks three languages.
He doesn't like fish.
My phone needs a new battery.
Does she know?
My mom calls me every day.
"""),
("Present simple for general facts", "Facts and habits use the present simple, not the past.", """
My daughter walks to school every day.
The bus comes every hour.
Water boils at one hundred degrees.
I always drink coffee in the morning.
The kids go to bed at eight.
This app helps you learn words.
He usually works from home.
The sun rises in the east.
People love this restaurant.
It rains a lot in May.
"""),
("Good and well", "Good describes a thing. Well describes how you do something.", """
My day was very good.
My day went well.
You speak English well.
She's a good cook.
She cooks well.
I'm doing well, thanks.
The food is good here.
The interview went well.
He plays the guitar really well.
It looks good on you.
"""),
("Play soccer", "In the US, football is a different game. Say play soccer.", """
I play soccer on weekends.
Do you play soccer?
My kids play soccer at school.
We practice on Tuesdays.
I like to watch soccer on TV.
He plays basketball after work.
Let's play a game.
Soccer is the most popular sport in the world.
I used to play soccer when I was young.
American football is very different.
"""),
("Actually and currently", "Actually means in fact. Currently means right now.", """
Actually, I'm from Colombia.
I'm actually pretty tired.
Actually, I changed my mind.
I currently work at a hospital.
I'm currently looking for a job.
Right now, I live with my parents.
At the moment, I'm very busy.
It's actually easier than it looks.
He's currently on vacation.
Actually, that's not true.
"""),
("Age: I'm 30 years old", "In English, you are an age. You don't have it.", """
I'm 30 years old.
I'm thirty.
How old are you?
My son is ten years old.
She's almost forty.
He just turned eighteen.
I'm in my thirties.
My grandmother is ninety-two.
How old is your daughter?
We're the same age.
"""),
("I've lived here for one year", "Still true now? Use I've + verb, with for or since.", """
I've lived here for one year.
I've lived here since 2024.
I've worked here for two months.
I've known him since we were kids.
She's been sick since Monday.
We've been together for five years.
I've had this phone for a long time.
How long have you worked there?
I've been waiting for twenty minutes.
I haven't seen her since the summer.
"""),
("One no is enough", "English uses one negative: I don't know anybody.", """
I don't know anybody here.
I don't have anything to do.
I didn't see anyone.
I know nobody here.
There's nothing in the fridge.
I don't want anything, thanks.
He never says anything.
I didn't go anywhere.
Nobody called me.
I don't need any help.
"""),
("Depends on, explain to", "Depends on, not depends of. Explain it to me, not explain me.", """
It depends on you.
It depends on the day.
Can you explain it to me?
Let me explain it to you.
Can you explain how it works?
He explained the problem to us.
I'll explain everything to her later.
Please explain the rules to the kids.
It depends on what time you finish.
It doesn't depend on me.
"""),
("False friends", "Assist = help. Attend = go to. Embarrassed = ashamed. Library = books.", """
I attended the meeting.
I go to the library to borrow books.
I buy books at the bookstore.
Can I help you?
The nurse assisted the doctor.
I was so embarrassed.
She's pregnant.
I realized I was wrong.
I finally carried out my plan.
I'm going to the career fair.
Excuse me, where's the exit?
"""),
("Small words that change everything", "Say the subject: it's raining, not is raining.", """
It's raining.
It's important to rest.
It's easy.
There are many people here.
I'm married.
I'm hungry.
I'm afraid of dogs.
She's right.
I'm in a hurry.
I'm used to it.
"""),
]
