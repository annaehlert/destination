from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .forms import AddDestinationForm
from uberr.models import Client, Destination
from .forms import AddClientForm


class MainPageView(View):
    def get(self, request):
        return render(request, "general.html")


# endpoint for getting info about specific user
class ClientInfoView(View):
    def get(self, request, client_id):
        profile = Client.objects.get(id=client_id)

        number_of_orders = Destination.objects.filter(client=client_id).count()
        list_of_orders = Destination.objects.filter(client=client_id)
        ctx = {
            "client": profile,
            "number_of_orders": number_of_orders,
            "list_of_orders": list_of_orders
        }
        return render(request, "details.html", ctx)


# endpoint for adding client to database
class AddClientView(View):

    def get(self, request):
        form = AddClientForm()
        return render(request, "add_client.html",
                      {"form": form}
                      )

    def post(self, request):
        form = AddClientForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'Klient nie został dodany, spróbuj jeszcze raz')
            return render(request, "add_client.html",
                          {"form": form}
                          )
        client = Client.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'])
        messages.add_message(request, messages.SUCCESS, 'Klient został dodany')
        return redirect(reverse('client-profile', kwargs={"client_id": client.id}))


# endpoint for adding orders to database
class DestinationView(View):
    def get(self, request):
        form = AddDestinationForm()
        return render(request, "add_order.html",
                      {"form": form}
                      )

    def post(self, request):
        form = AddDestinationForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'WYSTĄPIŁ BŁĄD! Zamówienie nie zostało dodane, spróbuj jeszcze raz')
            return render(request, "add_order.html", {
                "form": form
            })
        client = form.cleaned_data['client']
        Destination.objects.create(
            address=form.cleaned_data['address'],
            order_date=form.cleaned_data['order_date'],
            client=client)
        client_id = client.id
        messages.add_message(request, messages.SUCCESS, 'Zamówienie zostało dodane')
        return redirect(reverse('client-profile', kwargs={"client_id": client_id}))
