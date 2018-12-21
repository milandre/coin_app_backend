"""User Views.

This file has the views used
for user operations like
login and sign up.
"""

from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from account.models import Account
from .models import Client
from .forms import SignUpForm

# Create your views here.


class SignUpView(generic.CreateView):
    """SignUpView

    CreateView for signup page.
    """

    model = Client
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:login'))

        return super(SignUpView, self).dispatch(request, 
                                                *args, 
                                                **kwargs)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


    def form_valid(self, form):
        """If form is valid, save it and show
        a message.

        Args:
            form (obj): Form object

        Returns:
            A http response with a successful message
        """

        self.object = form.save()

        # Create a user account
        Account.objects.create(client=self.object,
                               currency=form.cleaned_data['currency'])

        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Successful sign up')

        return super(SignUpView, self).form_valid(form)