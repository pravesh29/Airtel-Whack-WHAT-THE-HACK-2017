# About the competition
This Chat bot was built during a 24 hour Hackathon at Airtel (India's leading network subscriber). I built a chatbot for self-care and customer experience theme. As organizations continue to automate their sales and customer service functions in order to reduce costs without degrading the customer experience, chatbots and other intuitive dialog systems are becoming more popular.

# How the idea shaped up
I initially came up with a question answering driven Customer experience system (as I had an assumption we'll have some data available from Airtel). Twitter Feedback eventually helped us to shape some conversation stories and I could define conversation flow with a bot and also perform intention detection. It's still not perfect or something to be directly used in production. But this is a very good start and is very scalable. The bot trains on the principle of "learn by doing", we need to give more and more conversation flows to define different ways a user can come up with a statement and then model its workflow.
Airtel WHack - #WhatTheHack

The chatbot data has been made by the tweets from the last 20 days that customer have tweeted on @airtel_presence handle

For now the bot supports only single statement dialogs.

# Tools and resources used in this implementation are
1. Python - Flask (for web app) and SocketIO (for websockets)
2. Wit.ai - Open source Platform to automate the conversation stories in chatbots. I've also used its Python wrapper(pywit)
3. Natural Language Processing techniques to normalise, standardise and process texts
4. Twitter Feed of @airtel_presence for conversation ideas.

# ====================================Pending issues===============================
The conversation flow has very few data points. It uses Hidden markov models internally to predict
the actions leveraging the Context free grammars. Due to this at times the bot does not function as we suppose it to.

The replies might vary in different interactions.


#======================================================Stories Used======================================================

##----------------Greeting story-----------------
USER: introduce yourself ex: hi i am Hugh Jackman, Hi this is Moritz
BOT: welcomes you and ask for any assistance you need ex:hi pravesh how can i assist you


##--------------Internet not working story----------------
USER: complains about data issue for e.g. my net not working, my data plan not working, my internet not working, data
not working etc..
BOT: asks for your plan
USER: reply his/her plan ie postpaid or prepaid
BOT: on the basis of answer bot ask different type of question so that the customer problem can be verified easily


##--------------Find my bill Story-----------------------
USER: ask query for bill for e.g where can i find my bill e.g. How can i find bill, find bill
BOT: tells user to dial *141# and ask is there anything else it can do
USER: reply by saying yes or no
BOT: if yes – ask user for timing when available to schedule a call
          If no  - give greeting –end
		  
##---------------Bill charges Story----------------------
USER: tells bot that he/she has been charged high for bill e.g. Why i m charged with high bill, charged high bill
BOT: uses a sample json file users.json (This can be replaced by anyexisting api and passed) to make decisions for
possible reasons for bill increase. In case the phone number
is not from the users.json file. Bot returns : Not an Airtel Number (Telephone numbers available are ) 

USER: gives his/her phone no. e.g. 123456789
BOT: get bill details


##---------------Porting (mnp) Story---------------------
USER: asks how to port his/her phone no. from other services to airtel e.g. port to airtel
BOT: gives user the instruction to follow for porting and welcomes user to aitel family
Else:
USER: asks for porting his/her airtel no.  e.g. port my airtel no. to jio
BOT: apologise to let him go and ask a personal call to resolve the issue of customer if possible


##---------------Competition comparision Story----------------
USER: asks the bot why he/she should choose airtel over any other services e.g. why should i choose airtel over reliance jio,
why should i choose airtel
BOT: give user the survey result taken in india showing that it has better data speed and connecticity than other company
and give a url link to view it