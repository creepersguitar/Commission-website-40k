from ai_module import customer_ai, studio_ai, combine

customer_request = customer_ai.process()

studio_response = studio_ai.evaluate(customer_request)

final_answer = combine(customer_request, studio_response)