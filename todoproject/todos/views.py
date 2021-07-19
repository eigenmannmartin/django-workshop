from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from todos.models import Todo, Collection


def collection(request, id):
    collection = get_object_or_404(Collection, pk=id)

    TodoFormSet = modelformset_factory(Todo,
                                       fields=(
                                           'description',
                                           'done',
                                       ),
                                       can_delete=True,
                                       can_delete_extra=False,
                                       can_order=True,)

    queryset = Todo.objects.filter(collection=collection.pk)

    if request.method == 'POST':
        formset = TodoFormSet(request.POST, request.FILES, queryset=queryset)
        if formset.is_valid():
            for new_todo in formset.save(commit=False):
                new_todo.collection = collection
                new_todo.save()

            for obj in formset.deleted_objects:
              if obj.pk:
                obj.delete()

            formset = TodoFormSet(queryset=queryset)
    else:
        formset = TodoFormSet(queryset=queryset)
    return render(request, 'collection.html', {"formset": formset, "collection": collection })


def index(request):

    CollectionFormSet = modelformset_factory(Collection,
                                       fields=(
                                           'name',
                                       ),
                                       can_delete=True,
                                       can_delete_extra=False,
                                       can_order=False,)

                                      
    queryset = Collection.objects.all()

    if request.method == 'POST':
        formset = CollectionFormSet(request.POST, request.FILES, queryset=queryset)
        if formset.is_valid():
            formset.save()
            for obj in formset.deleted_objects:
              if obj.pk:
                obj.delete()

            formset = CollectionFormSet(queryset=queryset)
    else:
        formset = CollectionFormSet(queryset=queryset)


    return render(request, 'index.html', {"formset": formset})
