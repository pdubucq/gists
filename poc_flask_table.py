from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pd.DataFrame({'bla':[0,2,1], 'blub':[3.4,1.5,6]})
    data.set_index(['bla'], inplace=True)
    data.index.name=None
    return render_template('poc_flask_table.html',tables=[data.to_html(), data.to_html()],
    titles = ['1', '2'])

if __name__ == "__main__":
    app.run(debug=True)