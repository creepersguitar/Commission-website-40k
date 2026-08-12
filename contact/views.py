import os
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def submit_commission(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )

    try:
        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        commission_type = data.get("commission_type")
        game_system = data.get("game_system")
        project = data.get("project")
        number_of_miniatures = data.get("number_of_miniatures")
        deadline = data.get("deadline")

        send_mail(
            subject=f"New Commission Request from {name}",
            message=f"""
New commission request

Customer: {name}
Email: {email}

Commission Type: {commission_type}
Game System: {game_system}

Number of Miniatures: {number_of_miniatures}

Desired Completion Date: {deadline}

Project Details:
{project}
""",
            from_email=None,
            recipient_list=[os.environ.get("EMAIL_HOST_USER")],
        )

        return JsonResponse(
            {"success": True},
            status=200
        )

    except Exception as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )