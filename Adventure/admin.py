from django.contrib import admin

# Register your models here.
from .models import State, StateMachine, Option
admin.site.register(Option)
admin.site.register(State)
admin.site.register(StateMachine)