from back_end.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document = '''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''

    return PrescriptionParser(document)



@pytest.fixture()
def doc_empty():
    return PrescriptionParser('')

@pytest.fixture()
def doc_2_virat():
    doc="""Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times"""

    return PrescriptionParser(doc)



def test_get_name(doc_1_maria,doc_empty,doc_2_virat):
    assert doc_1_maria.get_fieldname('patient_name')=='Marta Sharapova'
    assert doc_empty.get_fieldname('patient_name')==None
    assert doc_2_virat.get_fieldname('patient_name')=='Virat Kohli'


def test_get_address(doc_1_maria,doc_empty,doc_2_virat):
    assert  doc_1_maria.get_fieldname('patient_address')=='9 tennis court, new Russia, DC'
    assert  doc_empty.get_fieldname('patient_address')==None
    assert  doc_2_virat.get_fieldname('patient_address')=='2 cricket blvd, New Delhi'

def test_get_medicine(doc_1_maria,doc_empty,doc_2_virat):
    assert doc_1_maria.get_fieldname('patient_medicine')=='K\n\nPrednisone 20 mg\nLialda 2.4 gram'
    assert doc_empty.get_fieldname('patient_medicine') == None
    assert doc_2_virat.get_fieldname('patient_medicine')=='| Omeprazole 40 mg'

def test_get_direction(doc_1_maria,doc_empty,doc_2_virat):
    assert doc_1_maria.get_fieldname('patient_direction')=='Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert doc_empty.get_fieldname('patient_direction') == None
    assert doc_2_virat.get_fieldname('patient_direction')=='Use two tablets daily for three months'

def test_get_refill(doc_1_maria,doc_empty,doc_2_virat):
    assert doc_1_maria.get_fieldname('patient_refill')=='2'
    assert doc_empty.get_fieldname('patient_refill') == None
    assert doc_2_virat.get_fieldname('patient_refill')=='3'


def test_parse(doc_2_virat,doc_1_maria,doc_empty):
    record1=doc_2_virat.parse()

    assert record1=={

        'patient_name':'Virat Kohli',
        'patient_address':'2 cricket blvd, New Delhi',
        'patient_medicine':'| Omeprazole 40 mg',
        'medicine_directions':'Use two tablets daily for three months',
        'medicine_refill':'3'

    }

    record2=doc_1_maria.parse()

    assert record2=={
        'patient_name': 'Marta Sharapova',
        'patient_address': '9 tennis court, new Russia, DC',
        'patient_medicine': 'K\n\nPrednisone 20 mg\nLialda 2.4 gram',
        'medicine_directions': 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month',
        'medicine_refill':'2'


    }

    record3=doc_empty.parse()

    assert record3=={

        'patient_name':None,
        'patient_address':None,
        'patient_medicine': None,
        'medicine_directions':None,
        'medicine_refill':None

    }








