i3systems_assignment
==============================

Case Study for i3systems interview process

## Problem Statement
> Identify the medical packages given the medical description containing details of past history, illness, diagnosis, etc.

## Data
Sample Data - 4999 rows & 3 fields.
* **Sample** - Procedures or reports for a particular case whether some procedure has happened for a case.
* **Medical Description** - Contains details about illness, diagnosis, discharge summary, procedures, etc.
* **Package** - There are 40 packages in all. Surgery is the most frequent class (1088) & Hospice is the least frequent class (6).

### Target Variables
#### CARDIOVASCULAR
Relating to the circulatory system, which comprises the heart and blood vessels. Cardiovascular diseases are conditions that affect the heart and blood vessels and include arteriosclerosis, coronary artery disease, heart valve disease, arrhythmia, heart failure, hypertension, orthostatic hypotension, shock, endocarditis, diseases of the aorta and its branches, disorders of the peripheral vascular system, and congenital heart disease.

#### ORTHOPEDIC
Concerned with the correction or prevention of deformities, disorders, or injuries of the skeleton and associated structures (such as tendons and ligaments)

#### RADIOLOGY
Dealing with X-rays and other high-energy radiation, especially the use of such radiation for the diagnosis and treatment of disease.

#### GASTROENTROLOGY
The branch of medicine which deals with disorders of the stomach and intestines.

#### NEUROLOGY
The branch of medicine or biology that deals with the anatomy, functions, and organic disorders of nerves and the nervous system.

#### SOAP Note
SOAP note – an acronym for *Subjective, Objective, Assessment and Plan* – is the most common method of documentation used by providers to input notes into patients' medical records.

#### GYNECOLOGY
The branch of physiology and medicine which deals with the functions and diseases specific to women and girls, especially those affecting the reproductive system.

#### UROLOGY
Urology is a part of health care that deals with diseases of the male and female urinary tract (kidneys, ureters, bladder and urethra). It also deals with the male organs that are able to make babies (penis, testes, scrotum, prostate, etc.).

#### DISCHARGE SUMMARY
Hospital discharge summaries serve as the primary documents communicating a patient's care plan to the post-hospital care team. Often, the discharge summary is the only form of communication that accompanies the patient to the next setting of care.

#### Otolaryngology
An otolaryngologist is often called an ear, nose, and throat doctor, or an ENT for short.

#### NEUROSURGERY
Surgery performed on the nervous system, especially the brain and spinal cord.

#### ONCOLOGY
The study and treatment of tumours.

#### OPTHALOMOLOGY
The branch of medicine concerned with the study and treatment of disorders and diseases of the eye.

#### NEPHROLOGY
The branch of medicine that deals with the physiology and diseases of the kidneys.

#### PEDIATRICS
Paediatrics is the area of medicine that is concerned with the treatment of children's illnesses.

#### PAIN MANAGEMENT
Pain management, pain medicine, pain control or algiatry, is a branch of medicine that uses an interdisciplinary approach for easing the suffering and improving the quality of life of those living with chronic pain.

#### PSYCHIATRY
The study and treatment of mental illness, emotional disturbance, and abnormal behaviour.

#### PODIATRY
The treatment of the feet and their ailments

#### DERMATOLOGY
Dermatology is the science that is concerned with the diagnosis and treatment of diseases of the skin, hair and nails.

#### COSMETIC / PLASTIC SURGERY
The process of reconstructing or repairing parts of the body by the transfer of tissue, either in the treatment of injury or for cosmetic reasons.

#### DENTISTRY
The treatment of diseases and other conditions that affect the teeth and gums, especially the repair and extraction of teeth and the insertion of artificial ones.

#### PHSYICAL MEDICINE - REHAB
Physical medicine and rehabilitation, also known as physiatry, is a branch of medicine that aims to enhance and restore functional ability and quality of life to people with physical impairments or disabilities.

#### SLEEP MEDICINE
Sleep medicine is a medical specialty or subspecialty devoted to the diagnosis and therapy of sleep disturbances and disorders.

#### ENDOCRINOLOGY
The branch of physiology and medicine concerned with endocrine glands and hormones.

#### BARIATRICS
The branch of medicine that deals with the study and treatment of obesity.

#### CHIROPRATIC
A system of complementary medicine based on the diagnosis and manipulative treatment of misalignments of the joints, especially those of the spinal column, which are believed to cause other disorders by affecting the nerves, muscles, and organs.

#### RHEUMATOLOGY
The study of rheumatism, arthritis, and other disorders of the joints, muscles, and ligaments.

#### AUTOPSY
Postmortem

#### HOSPICE
Hospice care is a type of health care that focuses on the palliation of a terminally ill patient's pain and symptoms and attending to their emotional and spiritual needs at the end of life.

### Possibly Overlapping Categories
* **NEUROSURGERY** could be confused with SURGERY & NEUROLOGY fields
* **OPTHALOMOLOGY** can be part of ENT
* **NEPHROLOGY** deals with kidneys & so does UROLOGY
* **PAIN MANAGEMENT** could have an overlap of multiple categories
* **CHIROPRATIC** could be confused with Neurology
* **RHEUMATOLOGY** - Deals with joints & muscles, which could overlap with many above fields

## Evaluation
### Accuracy
Accuracy is the number of correct classifications divided by total number of samples

### Matthews Correlation Coeffecient
The Matthews correlation coefficient (MCC) is used as a measure of the quality of binary and multiclass classifications. It takes into account true and false positives and negatives and is generally regarded as a balanced measure which can be used even if the classes are of very different sizes.
Ranges between -1 and +1.  A coefficient of +1 represents a perfect prediction, 0 an average random prediction and -1 an inverse prediction

## Getting Started
All the experiments are run on `python 3.8.0`.

1. Clone the repository
2. If you do not have python3.8 installed. Run the below steps for easy installation using [asdf](https://asdf-vm.com/). *asdf* allows us to manage multiple runtime versions such for different languages such as `nvm`, `rbenv`, `pyenv`, etc using a CLI tool
	* Install asdf using this [guide](https://asdf-vm.com/#/core-manage-asdf-vm?id=install)
	* Now install `python3.8.0`
	```bash
	asdf plugin add python
	asdf install python 3.8.0
	asdf local python 3.8.0	# sets python3.8 as interpreter for the project
	```
	* Check the set python version
	```bash
	asdf current python
	```
3. Install poetry. [Poetry](https://python-poetry.org/docs/) is a python dependency management & packaging tool. Allows us to declare project libraries dependency & manage them
	```bash
	asdf plugin add poetry
	asdf install poetry latest # current 1.0.10; might need sudo
	asdf local poetry 1.0.10
	```
4. Install all dependencies
	```bash
	poetry install
	```

## Running
To train a model & generate *submission file* -

```bash
poetry run python main.py
```
To choose between multiple models, change *model_name* in `config` to one of the following -
* `bert-base-uncased`
* `distilbert-base-uncased`
* `roberta-base`

## General
* Managing Python version: `asdf`
* Python dependancy/project management: `poetry`
* Data/model versioning/management: `dvc`
* Auto-linting: `black`

## Next Steps
* Use some pooling strategy over the final embeddings
* AdamWeightDecay weight warmup
* BlueBERT
* BioMed-RoBERTa-base
