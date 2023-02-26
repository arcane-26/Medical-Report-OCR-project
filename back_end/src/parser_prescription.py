import re

from back_end.src.parser_generic import medical_doc_parser

class PrescriptionParser(medical_doc_parser):

    def __init__(self,text):
        medical_doc_parser.__init__(self,text)




    def parse(self):
        return {
            'patient_name':self.get_fieldname('patient_name'),
            'patient_address':self.get_fieldname('patient_address'),
            'patient_medicine':self.get_fieldname('patient_medicine'),
            'medicine_directions':self.get_fieldname('patient_direction'),
            'medicine_refill':self.get_fieldname('patient_refill')
        }


    def get_fieldname(self,field):


        pattern_dict={
            'patient_name':{'pattern':"Name:(.*)Date",'flags':0 },
            'patient_address':{'pattern':"Address:(.*)\n", 'flags':0 },
            'patient_medicine':{'pattern':"Address:[^\n]*(.*)Directions", 'flags':re.DOTALL },
            'patient_direction': {'pattern':"Directions:\s+(.*)\s+Refill", 'flags': re.DOTALL},
            'patient_refill':{'pattern':"Refill:\s(\d+)\stimes",'flags':0}


        }

        pattern_object=pattern_dict.get(field)
        if pattern_object:
            match = re.findall(pattern_object['pattern'], self.text,flags=pattern_object['flags'])
            if len(match) > 0:
                return match[0].strip()





# if __name__=='__main__':
#
#     doc='''Dr John Smith, M.D
# 2 Non-Important Street,
# New York, Phone (000)-111-2222
#
# Name: Marta Sharapova Date: 5/11/2022
#
# Address: 9 tennis court, new Russia, DC
#
# K
#
# Prednisone 20 mg
# Lialda 2.4 gram
#
# Directions:
#
# Prednisone, Taper 5 mg every 3 days,
# Finish in 2.5 weeks a
# Lialda - take 2 pill everyday for 1 month
#
# Refill: 2 times'''
#     pp=PrescriptionParser(doc)
#
#     data=pp.parse()
#     print(data)
