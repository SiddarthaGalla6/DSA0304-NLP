sentences={"Doctor prescribed medicine to patient.":{"Subject":"Doctor","Verb":"prescribed","Object":"medicine","Recipient":"patient"},"Patient reported severe headache.":{"Subject":"Patient","Verb":"reported","Object":"headache","Symptom":"severe headache"},"Nurse monitored patient continuously.":{"Subject":"Nurse","Verb":"monitored","Object":"patient","Adverb":"continuously"},"Medicine reduced blood pressure.":{"Subject":"Medicine","Verb":"reduced","Object":"blood pressure"}}
print("1. Syntax and Semantic Roles")
for sentence,roles in sentences.items():
    print("\n",sentence)
    for role,value in roles.items():
        print(role,":",value)
print("\n2. Evaluation of Semantic Roles")
print("Doctor -> Agent: Appropriate")
print("Patient -> Recipient: Appropriate for prescribed medicine.")
print("Headache -> Symptom: Appropriate")
print("Medicine -> Instrument/Cause: Appropriate")
print("Nurse -> Agent: Appropriate")
print("Patient -> Object/Target: Appropriate")
print("\n3. Errors from Incorrect Parsing")
print("Incorrect parsing can assign wrong agents and objects.")
print("It can confuse patients, medicines and symptoms.")
print("It can lead to incorrect medical information extraction.")
print("Such errors may affect clinical decision support.")
print("\n4. Improvements")
print("Use medical-specific NLP models.")
print("Use dependency parsing and semantic role labeling.")
print("Use medical dictionaries and ontologies.")
print("Use context-aware transformer models.")
print("Validate extracted information using medical knowledge bases.")


Output:
1. Syntax and Semantic Roles

 Doctor prescribed medicine to patient.
Subject : Doctor
Verb : prescribed
Object : medicine
Recipient : patient

 Patient reported severe headache.
Subject : Patient
Verb : reported
Object : headache
Symptom : severe headache

 Nurse monitored patient continuously.
Subject : Nurse
Verb : monitored
Object : patient
Adverb : continuously

 Medicine reduced blood pressure.
Subject : Medicine
Verb : reduced
Object : blood pressure

2. Evaluation of Semantic Roles
Doctor -> Agent: Appropriate
Patient -> Recipient: Appropriate for prescribed medicine.
Headache -> Symptom: Appropriate
Medicine -> Instrument/Cause: Appropriate
Nurse -> Agent: Appropriate
Patient -> Object/Target: Appropriate

3. Errors from Incorrect Parsing
Incorrect parsing can assign wrong agents and objects.
It can confuse patients, medicines and symptoms.
It can lead to incorrect medical information extraction.
Such errors may affect clinical decision support.

4. Improvements
Use medical-specific NLP models.
Use dependency parsing and semantic role labeling.
Use medical dictionaries and ontologies.
Use context-aware transformer models.
Validate extracted information using medical knowledge bases.
