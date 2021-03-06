from django.test import TestCase, Client
from django.template import loader
from django.urls import resolve


#base templates
templates = [
	"base.html",
]

#player templates
templates += [
	"player/"+name for name in [
		"register.html",
		"registration_confirmation.html",
		"request_char.html",
		"request_char_confirmation.html",
		"register_char_confirmation.html",
		"register_char_error.html",
		"login.html",
		"logged_out.html",
		"password_change_form.html",
		"password_change_done.html",
		"password_reset.html",
		"password_reset_complete.html",
		"password_reset_confirm.html",
		"password_reset_done.html",
		"profile.html",
	]
]

#base urls
urls = [
]

#player urls
urls += [
	"/player/"+name for name in [
		"register/",
		#"register_char",
		"login",
		"logout",
		"password_change",
		"password_change_done",
		"password_reset",
		"password_reset_done",
		#"reset",
		"password_reset_complete",
	"profile",
	]
]


class TestTemplates(TestCase):
	def test_compile(self):
		for template_name in templates:
			template = loader.get_template(template_name)
			template.render()


class Check_url_access(TestCase):

	@classmethod
	def setUpClass(self):
		super(Check_url_access, self).setUpClass()
		self.client = Client()

	def test_urlsResolve(self):
		for u in urls:
			resolve(u)

	def test_eachURLReturnsStatusCodeBetween100and300s(self):
		for u in urls:
			response = self.client.get(u)
			self.assertIn( response.status_code, [200, 302], "On a dataless get request, URL '"+u+"' does not return status code 200 or 302")
