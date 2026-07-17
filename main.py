from ai.Overseer.studio_ai import StudioAI
from ai.The_Herald.customer_ai import CustomerAI

customer_ai_instance = CustomerAI()
customer_request = customer_ai_instance.process()

studio_ai_instance = StudioAI()
studio_response = studio_ai_instance.evaluate_commission(customer_request)

def combine(customer_request, studio_response):
    return {
        "customer": customer_request,
        "studio": studio_response
    }


final_answer = combine(customer_request, studio_response)



studio = StudioAI()

request = {
    "model": "Custodian Guard",
    "difficulty": "medium",
    "hours": 10
}

result = studio.evaluate_commission(request)

print(result)