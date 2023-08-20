from flask import Flask
from flask import request 
from flask import render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def GetQuery():
    if request.method == "POST":
    
        WordLength = request.form.get("WordLength")
        if WordLength == '':
            WordLength = '0'
        WordContains = request.form.get('WordContains').lower()
        WordBegins = request.form.get('WordBegins').lower()
        WordEnds = request.form.get('WordEnds').lower()

        CleanWords = set()
        Query = set()

        with open('Words.txt','r') as RawWords:
            for EachWord in RawWords:
                CleanWords.add(EachWord[:-1])
                
        for EachWord in CleanWords:
            if len(EachWord) == int(WordLength) and WordContains in EachWord and EachWord[:len(WordBegins)] == WordBegins  and EachWord[len(EachWord)-len(WordEnds):] == WordEnds:
                Query.add(EachWord)

        if len(Query) > 0:
            return render_template("Findings.html",Words=Query)
        elif len(Query) == 0:
            return render_template('Error.html')
            
        #return render_template('Findings.html',tell=WordEnds)
    return render_template("Query.html")

if __name__ == "__main__":
  app.run()
