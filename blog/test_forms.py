from django.test import TestCase
from .forms import CommentForm


# class TestCommentForm(TestCase):

#     def test_form_is_valid(self):
#         # A valid comment should pass
#         form = CommentForm({'body': 'This is a great post'})
#         self.assertTrue(form.is_valid(), msg="Form is invalid")

#     def test_form_is_invalid(self):
#         # An empty comment should fail
#         form = CommentForm({'body': ''})
#         self.assertFalse(form.is_valid(), msg="Form is valid")
