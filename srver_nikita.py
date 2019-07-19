class StartForm(FlaskForm):
	text = TextAreaField('name')
	submit = SubmitField('start')

class BetForm(FlaskForm):
    bet = NumberField('bet')
    submit = SubmitField('make')

@app.route('/')
@app.route("/start")
def start():
	form = StartFrom()
	
	if form.validate_on_submit():
        '''
            make user_id and associate with name
        '''
        user_id = 0
		return redirect("auction/" + str(user_id))
	else:
		return render_template("start.html") 


@app.route('/auction/<int:user_id>')
def auction(user_id):
    try:
        user = getUserById(user_id)
        auction = getAuction()
        return render_template('auction.html', auction = auction)
    except:
        return redirect('/')
   
