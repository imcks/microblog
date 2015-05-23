from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models import User


class LoginForm(Form):
	openid = StringField('openid', validators = [DataRequired()])
	remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
	'''重写 Form 的 validate 方法 用于在用户编辑页面防止 nickanme 重复的问题'''
	nickname = StringField('nickname', validators=[DataRequired()])
	about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

	def __init__(self, original_nickname, *args, **kwargs):
		super.__init__(self, *args, **kwargs)
		self.original_nickname = original_nickname

	def validate(self):
		if not Form.validate(self):
			return False
		if self.nickname.data == self.original_nickname:
			return True
		user = User.query.filter_by(nickname = self.nickname.data).first()
		if user != None:
			self.nickname.errors.append('This nickanme is already in user. Please choose another one.')
			return False
		return True
