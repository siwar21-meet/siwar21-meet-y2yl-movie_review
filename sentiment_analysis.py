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
				star = "your review of the movie is 5 stars"
				opinion = "Wow this seems like a great movie to watch!"
			else:
				star = "your review of the movie is 4 stars"
				opinion = "Wow this seems like a very good movie to watch!"

		if score == 0:
			star = "your review of the movie is 3 stars"
			opinion = "This seems like a not too bad of a movie to watch!"

		if score < 0 :
			if score < -1:
				star = "your review of the movie is 2 stars"
				opinion = "This sees like a not good movie to watch!"
			else:
				star = "your review of the movie is 1 star"
				opinion = "This seems like a bad movie to watch!"

		return render_template('results.html',name=name,star=star,opinion=opinion)
		
if __name__ == '__main__': 
	app.run(debug=True) 
