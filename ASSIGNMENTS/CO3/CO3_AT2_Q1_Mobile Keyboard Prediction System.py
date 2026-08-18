import math
c_data=3
c_data_science=3
c_science=3
c_science_is=2
c_science_drives=1
c_science_drives_innovation=1
p_science_data=c_data_science/c_data
print("CASE STUDY 1: Smart Mobile Keyboard Prediction System")
print("1. MLE P(science|data) =",round(p_science_data,3))
print("Interpretation: High probability makes science a strong next-word prediction after data.")
p_is=c_science_is/c_science
p_drives=c_science_drives/c_science
p_improves=0
print("\n2. Backoff for unseen sequence data science improves")
print("Trigram P(improves|data science) = 0")
print("Bigram P(improves|science) = 0")
print("Unigram P(improves) = 0")
print("Backoff probability = 0")
print("Interpretation: Backoff checks lower-order models when higher-order sequences are unseen.")
l1=0.5
l2=0.3
l3=0.2
p_tri=c_science_drives_innovation/c_science_drives
p_big=c_science_is/c_science
p_uni=c_science_is/12
p_inter=l1*p_tri+l2*p_big+l3*p_uni
print("\n3. Deleted Interpolation for data science is")
print("Trigram probability =",round(p_big,3))
print("Bigram probability =",round(p_big,3))
print("Unigram probability =",round(p_uni,3))
print("Interpolated probability =",round(p_inter,3))
print("Interpretation: Interpolation combines higher and lower order probabilities.")
p1=0.66
p2=0.33
entropy=-(p1*math.log2(p1)+p2*math.log2(p2))
print("\n4. Entropy")
print("Entropy =",round(entropy,3),"bits")
print("Interpretation: Lower entropy means higher prediction confidence.")


Output:
CASE STUDY 1: Smart Mobile Keyboard Prediction System
1. MLE P(science|data) = 1.0
Interpretation: High probability makes science a strong next-word prediction after data.

2. Backoff for unseen sequence data science improves
Trigram P(improves|data science) = 0
Bigram P(improves|science) = 0
Unigram P(improves) = 0
Backoff probability = 0
Interpretation: Backoff checks lower-order models when higher-order sequences are unseen.

3. Deleted Interpolation for data science is
Trigram probability = 0.667
Bigram probability = 0.667
Unigram probability = 0.167
Interpolated probability = 0.567
Interpretation: Interpolation combines higher and lower order probabilities.

4. Entropy
Entropy = 0.917 bits
Interpretation: Lower entropy means higher prediction confidence.
