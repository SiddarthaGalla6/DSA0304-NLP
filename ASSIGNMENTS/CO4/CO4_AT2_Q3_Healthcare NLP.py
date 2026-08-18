import re
sentence="The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai."
tokens=re.findall(r'\b[\w-]+\b',sentence.lower())
features={"subject":"doctor","number":"singular","verb":"recommends","verb_number":"singular","object":["starting medication","scheduling a follow-up visit"],"location":"Chennai","time":"last week"}
medical_frames={"review":{"subject":"doctor","object":"patient","time":"last week"},"recommend":{"subject":"doctor","action":"treatment"},"start":{"action":"medication"},"schedule":{"action":"follow-up visit","location":"Chennai"}}
print("HEALTHCARE NLP ARCHITECTURE")
architecture=["Input Layer","Medical Tokenization","CFG Syntactic Parser","PCFG Ambiguity Resolution","Feature Structure Agreement","Medical Sub-Categorization","Earley Parsing","Semantic Role Extraction","Structured Output"]
for i,layer in enumerate(architecture,1):
    print(i,"->",layer)
print("\nSTEP-BY-STEP WORKFLOW")
workflow={"1":"Receive medical report","2":"Tokenize and normalize sentence","3":"Build syntactic structure using CFG","4":"Use PCFG to select the most probable parse","5":"Check subject-verb agreement using feature structures","6":"Apply medical verb sub-categorization frames","7":"Extract medical entities and actions","8":"Generate structured clinical information"}
for step,description in workflow.items():
    print(step,description)
print("\nTOKENS")
print(tokens)
print("\nFEATURE STRUCTURE")
for key,value in features.items():
    print(key,":",value)
print("\nSUB-CATEGORIZATION FRAMES")
for verb,frame in medical_frames.items():
    print(verb,":",frame)
print("\nSTRUCTURED OUTPUT")
output={"Diagnosis":"Not explicitly stated","Doctor":"doctor","Reviewed Patient":"patient","Review Time":"last week","Treatment":"starting medication","Follow-Up":"scheduling a follow-up visit","Location":"Chennai"}
for key,value in output.items():
    print(key,":",value)
print("\nREAL-TIME AND SCALABILITY")
methods=["Use Earley parsing for partial and efficient parsing","Use PCFG probabilities learned from medical corpora","Use feature structures for agreement validation","Use medical sub-categorization dictionaries","Use parallel processing for multiple reports","Use caching for repeated medical expressions","Use domain-specific NLP models for higher accuracy"]
for method in methods:
    print("-",method)


Output:
HEALTHCARE NLP ARCHITECTURE
1 -> Input Layer
2 -> Medical Tokenization
3 -> CFG Syntactic Parser
4 -> PCFG Ambiguity Resolution
5 -> Feature Structure Agreement
6 -> Medical Sub-Categorization
7 -> Earley Parsing
8 -> Semantic Role Extraction
9 -> Structured Output

STEP-BY-STEP WORKFLOW
1 Receive medical report
2 Tokenize and normalize sentence
3 Build syntactic structure using CFG
4 Use PCFG to select the most probable parse
5 Check subject-verb agreement using feature structures
6 Apply medical verb sub-categorization frames
7 Extract medical entities and actions
8 Generate structured clinical information

TOKENS
['the', 'doctor', 'who', 'reviewed', 'the', 'patient', 'last', 'week', 'recommends', 'starting', 'medication', 'and', 'scheduling', 'a', 'follow-up', 'visit', 'in', 'chennai']

FEATURE STRUCTURE
subject : doctor
number : singular
verb : recommends
verb_number : singular
object : ['starting medication', 'scheduling a follow-up visit']
location : Chennai
time : last week

SUB-CATEGORIZATION FRAMES
review : {'subject': 'doctor', 'object': 'patient', 'time': 'last week'}
recommend : {'subject': 'doctor', 'action': 'treatment'}
start : {'action': 'medication'}
schedule : {'action': 'follow-up visit', 'location': 'Chennai'}

STRUCTURED OUTPUT
Diagnosis : Not explicitly stated
Doctor : doctor
Reviewed Patient : patient
Review Time : last week
Treatment : starting medication
Follow-Up : scheduling a follow-up visit
Location : Chennai

REAL-TIME AND SCALABILITY
- Use Earley parsing for partial and efficient parsing
- Use PCFG probabilities learned from medical corpora
- Use feature structures for agreement validation
- Use medical sub-categorization dictionaries
- Use parallel processing for multiple reports
- Use caching for repeated medical expressions
- Use domain-specific NLP models for higher accuracy
