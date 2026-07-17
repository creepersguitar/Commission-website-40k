from ai.Overseer.studio_ai import StudioAI
from ai.The_Herald.customer_ai import CustomerAI


# Create council members
herald = CustomerAI()
overseer = StudioAI()


# Herald gathers customer request
commission = herald.process()


# Herald summarises request
summary = herald.summarise(commission)

print("\n--- Herald Summary ---")
print(summary)


# Overseer evaluates commission
studio_response = overseer.evaluate_commission(commission)


# Combine council response
def combine(customer_request, studio_response):
    return f"""
===== Council Decision =====

Customer: {customer_request['customer']}
Army: {customer_request['army']}
Models: {customer_request['models']}
Paint Level: {customer_request['paint_level']}
Deadline: {customer_request['deadline']}

Overseer Decision:
{studio_response['status']}

Reason:
{studio_response.get('reason', 'No reason provided')}

Estimated Time:
{studio_response.get('estimated_time', 'Unknown')}

Difficulty:
{studio_response.get('difficulty', 'Unknown')}
"""


final_answer = combine(commission, studio_response)


print("\n--- Council Decision ---")
print(final_answer)