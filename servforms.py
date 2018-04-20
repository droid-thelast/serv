from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField, IntegerField, SubmitField
from wtforms import validators


class PageContent(FlaskForm):

    """
    Help form for Partners: To be accessed through the partners FAQ pages.
    """
    headline = StringField("Title", [validators.DataRequired("Headline")])
    subhead = StringField("Subheading", [validators.DataRequired("SubHeading")])
    tags = StringField("tags", [validators.DataRequired("tags")])
    # email = TextField("Email", [validators.Required("Email"), validators.email("Enter Correct email")])
    content_id = TextAreaField("Content", [validators.DataRequired("Content")])


class Page(FlaskForm):

    name = StringField("Page name", [validators.DataRequired("Page Name")])


class Faq(FlaskForm):

    topic = StringField("Content", [validators.DataRequired("Topic")])


# class helpForm(FlaskForm):
    
#     """
#     Help form for Partners: To be accessed through the partners FAQ pages.
#     """
#     name = TextField("Name", [validators.Required("Enter Your Name")])
#     tel = TextField("Phone", [validators.Required("Phone Number?")])
#     email = TextField("Email", [validators.Required("Email"), validators.email("Enter Correct email")])
#     location = TextField("Your Locale", [validators.Required("Location")])
#     issue = SelectField('Issue', choices=[('service', 'Service'), ('accident', 'Accident'), \
#       ('registration', 'Registration'), ('availability', 'Availabilty'), ('account', 'Account')])
#     report = TextAreaField('Report')

#     def reset(self):
#         blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
#         self.process(blankData)

# class LoginForm(FlaskForm):
    
#     """
#     Login form for Partners: To be used before editing stuff first.
#     """

#     email = TextField("Email", [validators.Required("Email"), validators.email("Enter Correct email")])
#     password = PasswordField('Password', [validators.DataRequired()])
