import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


def to_dict(e):
    """Turn an Employee row into a plain dictionary so it can become JSON."""
    return {
        "id": e.id,
        "name": e.name,
        "email": e.email,
        "role": e.role,
        "created_at": e.created_at.isoformat(),
    }


def read_fields(request):
    """Read name/email/role from the JSON body. Returns None if any is missing."""
    data = json.loads(request.body or "{}")
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    role = str(data.get("role", "")).strip()
    if not (name and email and role):
        return None
    return name, email, role


@csrf_exempt
def employee_list(request):
    if request.method == "GET":                      # GET /employees
        employees = Employee.objects.order_by("id")
        return JsonResponse([to_dict(e) for e in employees], safe=False)

    if request.method == "POST":                     # POST /employees
        fields = read_fields(request)
        if fields is None:
            return JsonResponse({"error": "name, email and role are required"}, status=400)
        e = Employee.objects.create(name=fields[0], email=fields[1], role=fields[2])
        return JsonResponse(to_dict(e), status=201)

    return JsonResponse({"error": "method not allowed"}, status=405)


@csrf_exempt
def employee_detail(request, id):
    try:
        e = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)

    if request.method == "PUT":                      # PUT /employees/{id}
        fields = read_fields(request)
        if fields is None:
            return JsonResponse({"error": "name, email and role are required"}, status=400)
        e.name, e.email, e.role = fields
        e.save()
        return JsonResponse(to_dict(e))

    if request.method == "DELETE":                   # DELETE /employees/{id}
        e.delete()
        return JsonResponse({"deleted": id})

    return JsonResponse({"error": "method not allowed"}, status=405)
