from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Animal
from .forms import AnimalForm
from rest_framework import viewsets
from .serializer import AnimalSerializer
from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly

class AnimalListView(View):
    def get(self, request):
        animals = Animal.objects.filter(shelter=request.user.profile.shelter)
        return render(request, 'animal_list.html', {'animals': animals})

class AnimalEditView(View):
    def get(self, request, pk):
        animal = Animal.objects.get(pk=pk)
        form = AnimalForm(instance=animal)
        return render(request, 'animal_form.html', {'form': form})

    def post(self, request, pk):
        animal = Animal.objects.get(pk=pk)
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
        else:
            return render(request, 'animal_form.html', {'form': form})

class AnimalDeleteView(View):
    def post(self, request, pk):
        animal = Animal.objects.get(pk=pk)
        animal.delete()
        return redirect('animal_list')

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    context = {'animal': animal}
    return render(request, 'animal_detail.html', context)

class AnimalViewSet(viewsets.ModelViewSet):
    """
    API-конечная точка, которая предоставляет CRUD-операции на объектах Animal.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
