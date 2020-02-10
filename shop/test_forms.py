from django.test import TestCase
from .forms import ReviewForm


class TestReviewForms(TestCase):
    def test_user_can_leave_review(self):
        form = ReviewForm({'headline': 'The best armor',
                                     'rating': '5',
                                     'review_text': 'The bestest armor I ever did try.'
        })
        self.assertTrue(form.is_valid())
