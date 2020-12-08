from flask import Flask,render_template,request
from newsapi import NewsApiClient
 
 
app = Flask(__name__)
 
yourAPIKEY = '07552fb216424e1fa30c9d09af2e427e'
 
newsapi = NewsApiClient(api_key=yourAPIKEY)
 
 
#print(top_headlines['articles'])
 
#head_lines=[]
 
#for news in top_headlines['articles']:
 #   head_lines.append(news['title'])
 
 
@app.route('/')
def home():
    #news =head_lines
    return render_template('index.html',news='')
 
@app.route('/results/',methods=['POST']) 
def get_results():
    keyword = request.form['keyword']  #getting input from user
 
    news = newsapi.get_everything(q=keyword,
                                     #sources='googlenews,the-verge',#optional and you can change
									 #category: "general",
                                     language='pt'
                                     )
    #print(news['articles'])
    return render_template('index.html',news=news['articles'])
 
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
