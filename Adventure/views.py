from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Option, State, StateMachine
class Adventure(View):
    def post(self, request):
        user_input = request.POST["option"].strip()
        print(user_input)
        machine = StateMachine.objects.all()[0]
        userState = State.objects.get(state_name=machine.user_state.state_name)
        this_state = Option.objects.get(current_state=userState, text=user_input)
        after_state = this_state.next_state
        StateMachine.user_state = after_state
        op = after_state.options
        state_list = [after_state.title, after_state.text]
        options = list(op.split(','))
        return JsonResponse(list(state_list + options), safe=False)
    def get(self, request):
        current_state = StateMachine.objects.all();
        if len(current_state) == 0:
            StateMachine.objects.create(user_state=State.objects.first())
        machine = StateMachine.objects.all()[0]
        userState = State.objects.first()
        op = userState.options;
        options = op.split(',')
        return render(request, 'adventure.html', {"state" : userState, "options" : options})
