from flask import Flask , render_template, request ,redirect
from textblob import TextBlob ,Word , Blobber

app = Flask(__name__)

@app.route('/' ,methods=["POST","GET"])
def main():
	if request.method == 'GET' :
		return render_template('movie_review.html')

@app.route('/analysis',methods=["POST","GET"])
def analysis():
	if request.method == 'POST' :
		name = request.form['name']
		print(name)

		review = request.form['review']
		blob = TextBlob(review)
		score = blob.sentiment.polarity
		if score > 0:
			if score > 1:
				star = "your review of the movie is ⭐⭐⭐⭐⭐"
				opinion = "Wow this seems like a great movie to watch 🍿"
			else:
				star = "your review of the movie is ⭐⭐⭐⭐"
				opinion = "Wow this seems like a very good movie to watch 🍿"

		if score == 0:
			star = "your review of the movie is ⭐⭐⭐"
			opinion = "This seems like a not too bad of a movie to watch 🍿"

		if score < 0 :
			if score < -1:
				star = "your review of the movie is ⭐⭐"
				opinion = "This seems like a not good movie to watch 🍿"
			else:
				star = "your review of the movie is ⭐"
				opinion = "I'm sorry you had to watch it"

		return render_template('results.html',name=name,star=star,opinion=opinion)


@app.route('/feedback',methods=["POST","GET"])
def feedback():
	if request.method == 'POST' :
		feedback = request.form['feedback']
		blob = TextBlob(feedback)
		score = blob.sentiment.polarity

		if score > 0:
			if score > 1:
				results = "Our analysis was very accurate 😄"
				thanks = "Thank you for your feedback ✅"
			else:
				results = "Our analysis was accurate 😊"
				thanks = "Thank you for your feedback ✅"

		if score == 0:
			results = "Our analysis was not very accurate 😔"
			thanks = "Thank you for your feedback ✅"

		if score < 0 :
			if score < -1:
				results = "Our analysis was not accurate 😞"
				thanks = "Thank you for your feedback  ✅"
			else:
				results = "Our analysis was not accurate at all 😓"
				thanks = "Thank you for your feedback ✅"

		return render_template('feedback.html',feedback=feedback,thanks=thanks,results=results)


		
if __name__ == '__main__': 
	app.run(debug=True) 
