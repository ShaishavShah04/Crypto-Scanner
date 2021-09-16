# **Crypto-Scanner**
----
## Technologies Used:
----
### **CCXT** Module (*Python*)
- This was used to connect to the Binance Exchange to fetch the data.
- This was also used to fetch ticker info
- In order to avoid over-using the API (which could ban you), I decided to fetch the info for all the tickers at once, instead of fetching them for individual sort-listed cryptos.

### **Pandas** Module (*Python*)
- Pandas made this entire project much less time-taking then I thought. This was one of the key reasons I chose Python to do this project.
- Pandas was used to process the dataframe and check the conditions.

### **Twilio** Module (*Python*) (*Not Free*)
- This module was used to send the messages to my phone.
- Cost: ~$5/month to send a message hourly for everyday of the month. More cost if your messages are longer


### **AWS** (*Not Free*)
- EC2 Instance to host script (Ubuntu 18.04)
- Used Cron to schedule running the scripts and clearing the 'already alerted' symbols.
- I'm using the free tier, but make sure to not cross the instance's free tier limits.

---- 
## What is this project?
----
This project is intended to alert you when a coin (crypto) meets certain defined criteria. The hope is to get these alerts to save you time from constantly staring at the charts!

This crypto scanner relies fully on technical analysis, not any fundamentals have been incorporated yet.

<img src="media\Alert_examples.PNG" alt="drawing" height="400"/>
<img src="media\Perfect_Alert.PNG" alt="drawing" height="400"/>

----
## Whats next for this project:
----

Similar to this, I have another peice of code that takes a symbol and generates buy and sell signals. The upcoming plan is to have a common Database that keeps all the coins to watch. This database can be accessed to generate buy and sell signals. 