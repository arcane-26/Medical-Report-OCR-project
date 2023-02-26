import re


from back_end.src.parser_generic import medical_doc_parser

class PatientDetailsParser(medical_doc_parser):
    def __init__(self,text):
        medical_doc_parser.__init__(self,text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_patient_phone_number(),
            'medical_problems': self.get_medical_problems(),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination()
        }

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_patient_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]

    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_hepatitis_b_vaccination(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_medical_problems(self):
        pattern = 'List any Medical Problems .*?:(.*)Name of Insurance Company'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()












# if __name__=='__main__':
#     text_1 = '''
#         17/12/2020
#
#     Patient Medical Record
#
#     Patient Information
#
#     Birth Date
#     Kathy Crawford May 6 1972
#     (737) 988-0851 Weight
#     9264 Ash Dr 95
#     New York City, 10005 + tage
#     United States Height:
#     190
#     In Casc of Emergency
#     LL
#     a
#     Simeone Crawford 9266 Ash Dr
#     New York City, New York, 10005
#     Home phone United States
#     990) 375-4621
#     (990) Work phone
#     Genera! Medical History
#     nnn ae ne
#     Chicken Pox (Varicella): Measies:
#     IMMUNE IMMUNE
#
#     Have you had the Hepatitis B vaccination?
#
#     No
#
#     List any Medical Problems (asthma, seizures, headaches):
#     Migraine
#
#         '''
#
#     text_2 = '''
#         17/12/2020
#
#     Patient Medical Record
#
#     Patient Information Birth Date
#
#     Jerry Lucas May 2 1998
#
#     (279) 920-8204 . Weight:
#
#     4218 Wheeler Ridge Dr 57
#
#     Buffalo, New York, 14201 Height:
#
#     United States ght.
#     170
#
#     In Case of Emergency
#     meee
#
#     Joe Lucas 4218 Wheeler Ridge Dr
#     Buffalo, New York, 14201
#     Home phone . United States
#     Work phone
#
#     General Medical History
#
#     Chicken Pox (Varicelia): Measles:
#
#     IMMUNE NOT IMMUNE
#
#     Have you had the Hepatitis B vaccination?
#
#     _ Yes
#
#     List any Medical Problems (asthma, seizures, headaches):
#     N/A
#         '''
#     pd_1=PatientDetailsParser(text_1)
#     pd_2=PatientDetailsParser(text_2)
#     print(pd_1.parse())
#     print(pd_2.parse())
