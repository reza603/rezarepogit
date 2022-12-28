from django.shortcuts import render, get_object_or_404,redirect




def show(request):

    return render(request, 'calander/Timetable.html')