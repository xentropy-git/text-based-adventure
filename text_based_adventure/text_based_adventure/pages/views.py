# pages/views.py
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ActionForm
from django.shortcuts import redirect
from ..data.rooms import STORY_ROOMS


class HomeView(TemplateView):
    template_name = "home.jinja"


class ProfileView(TemplateView):
    template_name = "profile.jinja"


class StoryRoomView(LoginRequiredMixin, TemplateView):
    template_name = "story.jinja"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = kwargs.get("room_id")
        room_id_int = int(room_id)
        room = STORY_ROOMS.get(room_id)
        if room is None:
            raise Http404("Story room not found")
        form = ActionForm()
        context.update(
            {
                "room": room,
                "form": form,
            }
        )

        return context

    def post(self, request, *args, **kwargs):
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data["action"]
            # Process the action here (e.g., log it or modify the story)
            print(f"User action: {action}")

            if action:
                # Process the action here (e.g., log it or modify the story)
                room = STORY_ROOMS.get(kwargs.get("room_id"))
                print(f"User action: {action}")
                for choice in room["actions"]:
                    if choice["action"] == action:
                        room_id = choice["next_room"]
                        return redirect("story_room", room_id=room_id)
        return self.get(request, *args, **kwargs)
