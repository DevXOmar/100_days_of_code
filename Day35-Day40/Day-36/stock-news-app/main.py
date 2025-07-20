import requests
import datetime as dt
from twilio.rest import Client

now = dt.datetime.now()
day = now.day
month = now.month
year = now.year

date_today = f"{year}-{month}-{day}"
date_yesterday = f"{year}-{month}-{day-1}"


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


#Stocks API
params1={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":""
}
call_alphavantage = requests.get(url = "https://www.alphavantage.co/query",params= params1)
stock_data = call_alphavantage.json()
# print(stock_data)

Date_latest_open = stock_data["Meta Data"]["3. Last Refreshed"]
day_today = int(Date_latest_open.split("-")[2])
prev_latest_open = f"{Date_latest_open.split("-")[0]}-{Date_latest_open.split("-")[1]}-{day_today-1}"
# print(Date_latest_open)
# print(prev_latest_open)

closing_price_dayTminus1 = float(stock_data["Time Series (Daily)"][Date_latest_open]["4. close"])
closing_price_dayTminus2 = float(stock_data["Time Series (Daily)"][prev_latest_open]["4. close"])
perc_diff = ((closing_price_dayTminus1-closing_price_dayTminus2)/closing_price_dayTminus2)*100
# print(closing_price_dayTminus1)
# print(closing_price_dayTminus2)
pos_perc_diff = abs(perc_diff)
# print(perc_diff)


#News API
def get_news():
    params2 = {
        "q":STOCK,
        "from":date_yesterday,
        "to":date_today,
        "sortBy":"popularity",
        "apiKey": ""
    }
    call_news_api = requests.get(url = "https://newsapi.org/v2/everything",params = params2)
    news_data = call_news_api.json()

    top_3_articles = news_data["articles"][0:3]
    data_3_articles = []
    for x in top_3_articles:
        title = x["title"]
        brief = x["description"]
        dict1 = {"Headline":title,"Brief":brief}
        data_3_articles.append(dict1)
    return data_3_articles


def send_message():
    #Twilio API
    account_sid = ""
    auth_token = ""
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = final_message,
        from_ = "",
        to = "",
    )
    print(message.sid)


## Main
if pos_perc_diff > 2:
    article_data = get_news()
    if perc_diff > 0:
        symbol  = "🔺"
    else:
        symbol = "🔻"

    Heading = f"{STOCK}: {symbol}{pos_perc_diff:.2f}%"
    # print(Heading)
    txt = [f"Headline: {x["Headline"]}\nBrief: {x["Brief"]}" for x in article_data]
    news_body = "\n\n".join(txt)##.
    final_message = f"{Heading}\n\n{news_body}"

    top_article = article_data[0]
    finale_message = f"{Heading}\nHeadline: {top_article["Headline"]}"

    send_message()




