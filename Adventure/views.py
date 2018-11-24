from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Option, State, StateMachine
class Adventure(View):
    def post(self, request):
        #Get the input from the POST request
        user_input = request.POST["option"].strip()
        machine = StateMachine.objects.all()[0]
        #Get the current state
        userState = State.objects.get(state_name=machine.user_state.state_name)
        #Get the current state options
        this_state = Option.objects.get(current_state=userState, text=user_input)
        #Find the next tate
        after_state = this_state.next_state
        #Set the next state in the state machine
        StateMachine.user_state = after_state
        setattr(machine, "user_state", after_state)
        #Get the next state options and next state and send it through a JSONResponse
        op = after_state.options
        state_list = [after_state.title, after_state.text]
        options = list(op.split(','))
        return JsonResponse(state_list + options, safe=False)
    def get(self, request):
        #Get the current state
        current_state = StateMachine.objects.all();
        if len(current_state) == 0:
            # If no statemachine exists, create one.
            StateMachine.objects.create(user_state=State.objects.first())
        #Get the state machine, find the current state, get the options and render it on first request.
        machine = StateMachine.objects.all()[0]
        userState = machine.user_state
        op = userState.options
        options = op.split(',')
        return render(request, 'adventure.html', {"state" : userState, "options" : options})
