from django.http import JsonResponse

def add(request):
    try:
        num1 = int(request.GET.get("num1", 0))
        num2 = int(request.GET.get("num2", 0))
        result = num1 + num2
    except:
        return JsonResponse({"error": "invalid input"}, status=400)
    return JsonResponse({
    "result": result
})