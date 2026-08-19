Pseudocode:
FUNCTION classify_utterance(utterance, speaker):
    IF speaker == user AND has_modal_request_pattern AND is_question: RETURN Request
    ELSE IF is_question: RETURN Question
    ELSE IF speaker == user: RETURN Inform
    ELSE IF is_acknowledgement: RETURN Confirmation
    ELSE IF speaker == agent AND indicates_completed_task: RETURN Action
    ELSE: RETURN fallback_classifier(utterance)


Python Code:
python
def classify_utterance(utterance, speaker):
    text = utterance.lower().strip()
    if speaker == "user" and ("can you" in text or "could you" in text) and text.endswith("?"):
        return "Request"
    if text.endswith("?"):
        return "Question"
    if speaker == "user":
        return "Inform"
    if "sure" in text:
        return "Confirmation"
    if speaker == "agent" and ("has been" in text or "booked" in text):
        return "Action"
    return "Inform"
conversation = [
    ("user", "Can you book a train ticket for me?"),
    ("agent", "Sure, where would you like to travel?"),
    ("user", "I want to go to Chennai."),
    ("agent", "Your ticket has been booked.")
]
print("Dialogue-Act Sequence:")
slots = {}
for speaker, utterance in conversation:
    act = classify_utterance(utterance, speaker)
    print(f"  [{speaker.title():5}] {utterance!r:42} -> {act}")
    if act == "Inform" and "chennai" in utterance.lower():
        slots["destination"] = "Chennai"
print("\nUpdated Intent Frame:")
print("  intent = 'book_train_ticket'")
for k, v in slots.items():
    print(f"  {k} = '{v}'")
print("  status = 'booked'")


Output:
Dialogue-Act Sequence:
  [User ] 'Can you book a train ticket for me?'      -> Request
  [Agent] 'Sure, where would you like to travel?'    -> Question
  [User ] 'I want to go to Chennai.'                 -> Inform
  [Agent] 'Your ticket has been booked.'              -> Action
Updated Intent Frame:
  intent = 'book_train_ticket'
  destination = 'Chennai'
  status = 'booked'
