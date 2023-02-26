import pytest

from back_end.src.parser_patient_details import PatientDetailsParser

@pytest.fixture()
def doc_1_cathy():
    text='''
    17/12/2020

Patient Medical Record

Patient Information

Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight
9264 Ash Dr 95
New York City, 10005 + tage
United States Height:
190
In Casc of Emergency
LL
a
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
990) 375-4621
(990) Work phone
Genera! Medical History
nnn ae ne
Chicken Pox (Varicella): Measies:
IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):
Migraine
    
    '''
    return PatientDetailsParser(text)


@pytest.fixture()
def doc_2_jerry():
    text='''
    17/12/2020

Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 . Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States ght.
170

In Case of Emergency
meee

Joe Lucas 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone . United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles:

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

_ Yes

List any Medical Problems (asthma, seizures, headaches):
N/A
    '''
    return PatientDetailsParser(text)

def test_name(doc_1_cathy,doc_2_jerry):
    assert doc_1_cathy.get_name()=='Kathy Crawford'
    assert doc_2_jerry.get_name()== 'Jerry Lucas'


def test_number(doc_1_cathy,doc_2_jerry):
    assert  doc_1_cathy.get_number()=='(737) 988-0851'
    assert doc_2_jerry.get_number()=='(279) 920-8204'

def test_vaccination(doc_1_cathy,doc_2_jerry):
    assert doc_1_cathy.get_vaccination()=='No'
    assert doc_2_jerry.get_vaccination()=='Yes'

def test_medical(doc_1_cathy,doc_2_jerry):
    assert doc_1_cathy.get_medical()=='Migraine'
    assert doc_2_jerry.get_medical()=='N/A'