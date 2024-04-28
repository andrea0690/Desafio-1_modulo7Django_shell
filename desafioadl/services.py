from django.http import Http404
from django.shortcuts import get_object_or_404
from desafioadl.models import SubTarea, Tarea

def recupera_tareas_y_sub_tareas(id):
    try:
        tarea = get_object_or_404(Tarea, id=id)
        sub_tareas = SubTarea.objects.filter(tarea_id = tarea)
        return {
            'id': id,
            'descripcion': tarea.descripcion,
            "subtareas": [{"id": sub_tarea.id, "descripcion": sub_tarea.descripcion} for sub_tarea in sub_tareas]
        }
    except Http404:
        return f"No se encontró la tarea con ID {id}"

def crear_nueva_tarea(desc: str):
    tarea = Tarea(descripcion = desc)
    tarea.save()
    imprimir_en_pantalla()
    return tarea

def crear_sub_tarea(tarea: Tarea, descripcion: str):
    subtarea = SubTarea(descripcion = descripcion, tarea_id = tarea)
    subtarea.save()
    return imprimir_en_pantalla()

def elimina_tarea(tarea_id):
    try:
        tarea = get_object_or_404(Tarea, id=tarea_id)
        tarea.eliminada = True
        tarea.save()
        return imprimir_en_pantalla()
    except Http404:
        return f"No se encontró la tarea con ID {tarea_id}"

def elimina_sub_tarea(sub_tarea_id):
    try:
        sub_tarea = get_object_or_404(SubTarea, id=sub_tarea_id)
        sub_tarea.eliminada = True
        sub_tarea.save()
        return imprimir_en_pantalla()
    except Http404:
        return f"No se encontró la subtarea con ID {sub_tarea_id}"

def imprimir_en_pantalla():
    tareas = Tarea.objects.filter(eliminada= False).all()
    for tarea in tareas:
        print(f'[{tarea.id}] {tarea.descripcion}')
        subtareas = SubTarea.objects.filter(tarea_id = tarea, eliminada = False)
        for subtarea in subtareas:
            print(f'    [{subtarea.id}] {subtarea.descripcion}')
