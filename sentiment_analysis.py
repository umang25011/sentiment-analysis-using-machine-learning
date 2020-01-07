root_path="" #folder path

#LOAD THE MODELS
import joblib

logistic_model=joblib.load(root_path+"logistic_model.pkl",'r+') #enter file
svc_model=joblib.load(root_path+"svc_model.pkl",'r+')
text_to_vector=joblib.load(root_path+"text_to_vector.pkl",'r+')

#get the data in this list..either form file or direct strings
text_for_analysis=[]

from clean_data import clean_data #clean_data file 

text_for_analysis=clean_data(text_for_analysis)

text_for_analysis_vector=text_to_vector.transform(text_for_analysis)
logistic_answer=logistic_model.predict(text_for_analysis_vector)
svc_answer=svc_model.predict(text_for_analysis_vector)

print("logistic prediction :", logistic_answer, " svc prediction :",svc_answer )

positive_feedback=0
negative_feedback=0

#to count both type of feedback
for ans in svc_answer:
        if ans==0:
            negative_feedback+=1
        else:
            positive_feedback+=1

print("negative_feedback = ",negative_feedback ,"positive_feedback = ",positive_feedback )
         
