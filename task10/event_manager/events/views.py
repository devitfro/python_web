from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, ParticipantForm
from django.forms import formset_factory
from .models import Event, Participant

def create_event(request):
    ParticipantFormSet = formset_factory(ParticipantForm, extra=1)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        participant_formset = ParticipantFormSet(request.POST)

        if event_form.is_valid() and participant_formset.is_valid():
            event = event_form.save()
            for form in participant_formset:
                email = form.cleaned_data.get('email')
                if email:
                    Participant.objects.create(event=event, email=email)
            return redirect('event_detail', event_id=event.id)
    else:
        event_form = EventForm()
        participant_formset = ParticipantFormSet()

    return render(request, 'events/create_event.html', {
        'event_form': event_form,
        'participant_formset': participant_formset,
    })

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})