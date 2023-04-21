import json
import pandas as pd
def main():
    ###
    # txt_data: import txt file
    # data: data which form txt data to json data
    # filter_data: data after filter to put them into csv file
    # ###
    data=[]
    filter_data=[]
    #open txt data file
    with open('data.txt', 'r') as f2:
        txt_data = f2.read()
    #split data base on '}{'
    txt_data=txt_data.split("}{")
    #pfizer	moderna	astrazeneca	janssen	verocell
    pfizer=0
    #Tranform data from txt to json and collect each kind of data we need.
    for x in range(len(txt_data)):
        # Add
        txt_data[x]="{"+txt_data[x]+"}"
        # printing converted dictionary
        object=json.loads(txt_data[x])
        data.append(object)

        hashtags=''
        if len(object['entities']['hashtags']) > 0:
            for tag in object['entities']['hashtags']:
                hashtags += tag['text'] + ";"

        # pfizer	moderna	    astrazeneca	    janssen	    verocell
        # Data base:[time, id, text, url, retweet, pfizer vaccine, moderna vaccine, astrazeneca vaccine, janssen vaccine, verocell vaccine,
        #                                            user_screen_name, retweeted_screen_name, creator,creator description,hashtags, language, timestamps_ms]
        if 'retweeted_status' in object.keys():
            filter_data.append([object['created_at'], object['id'], object['text'], "https://" in object['text'], True,
                                'pfizer' in hashtags, 'moderna' in hashtags, 'astrazeneca' in hashtags,
                                'janssen' in hashtags, 'verocell' in hashtags,
                                object['user']['screen_name'], object['retweeted_status']['user']['screen_name'],
                                object['retweeted_status']['user']['screen_name'], object['retweeted_status']['user']['description'],
                                hashtags, object['lang'], object['timestamp_ms']])
        else:
            filter_data.append([object['created_at'], object['id'], object['text'], "https://" in object['text'], False,
                                'pfizer' in hashtags, 'moderna' in hashtags, 'astrazeneca' in hashtags,
                                'janssen' in hashtags, 'verocell' in hashtags,
                                object['user']['screen_name'], 'NaN',
                                object['user']['screen_name'], object['user']['description'],
                                hashtags, object['lang'], object['timestamp_ms']])

    csv_data = pd.DataFrame(filter_data, columns=['time', 'id', 'text', 'url', 'retweet','pfizer', 'moderna', 'astrazeneca', 'janssen', 'verocell',
                                                  'user_screen_name', 'retweeted_screen_name', 'creator', 'creator_description', 'hashtags', 'language', 'timestamps_ms'])
    csv_data.to_csv('data.csv', index=False)
if __name__ == "__main__":
    main()