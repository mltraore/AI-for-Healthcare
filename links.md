# Program Resources 
This file compiles curated links shared throughout the course, providing valuable supplementary resources, references, and materials to enrich the learning experience.

## Course 1: Applying AI to 2D Medical Imaging Data
<details> 
  <summary>
      🧠 <b> Course 1: </b> Applying AI to 2D Medical Imaging Data 
  </summary>
<br/> 

course content
course content
</details>

## Course 2: Applying AI to 3D Medical Imaging Data

<details>
  <summary>
      🧠 <b> Lesson 5: </b> Deploying AI Algorithms in Real World Scenarios 
  </summary>

[Nifti file format](https://brainder.org/2012/09/23/the-nifti-file-format/)  
[MRI](https://hsmradyoloji.com/en/mri-mr/?gad=1&gclid=CjwKCAjw5remBhBiEiwAxL2M98idT3fVIwBwHbwZ4A15vHqahnYBzbwlh_6dfyp_VoRMKtUUUn7zcxoCR90QAvD_BwE)  
[MRI](https://www.fieldtriptoolbox.org/faq/coordsys/)  
[NiBabel](https://nipy.org/nibabel/coordinate_systems.html)  
[DICOM REF](https://www.dicomstandard.org/)  
[DICOM REF](https://dicom.innolitics.com/ciods/enhanced-sr/general-study/00080050)  
[DICOM REF](https://clinflows.blog/2022/09/29/dicom-explained-what-is-dicom/#:~:text=The%20DICOM%20Tags%20are%20assigned,uniform%20communication%20protocol%20for%20sharing.)  
[DICOM REF](https://dicom.nema.org/medical/Dicom/2017e/output/chtml/part06/chapter_6.html)  
[DICOM REF](https://www.dicomlibrary.com/dicom/dicom-tags/)  
[DICOM REF](https://www.dicomlibrary.com/dicom/dicom-tags/)  
[DICOM REF](https://www.dicomlibrary.com/dicom/dicom-tags/)  
[Anonymize DICOM data](https://pydicom.github.io/pydicom/stable/auto_examples/metadata_processing/plot_anonymize.html#sphx-glr-auto-examples-metadata-processing-plot-anonymize-py)
</details>

<details>
  <summary>
      🧠 <b> Project: </b>  Quantifying Hippocampus Volume for Alzheimer's Progression
  </summary>

  - [Hippocampus](https://commons.wikimedia.org/wiki/File:Hippocampus_small.gif)  
  - [Seahorse & Hippocampus](https://commons.wikimedia.org/wiki/File:Hippocampus_and_seahorse.JPG)  
  - [Hippocampal volume across age: Nomograms derived from over 19,700 people in UK Biobank](https://www.sciencedirect.com/science/article/pii/S2213158219302542 "According to this paper, 2019, the volume of hippocampus varies in a population, depending on various parameters, within certain boundaries, and it is possible to identify a 'normal' range taking into account age, sex, and brain hemisphere.")  
  - [Medical Decathlon competition](http://medicaldecathlon.com/)  
  - [Emulating PACS: Orthanc server](https://www.orthanc-server.com/download.php)  
  - [Viewing images: OHIF zero-footprint web viewer](https://docs.ohif.org/development/getting-started/)  
  - [DCMTK tools](https://dcmtk.org/en/)  
  - [Project Rubic](https://learn.udacity.com/nanodegrees/nd320/parts/cd0567/lessons/7aaadba1-56c3-45f3-91ab-cec178d320c7/concepts/7aaadba1-56c3-45f3-91ab-cec178d320c7-project-rubric)  
  - [Secondary Capture IODs](http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.8.html "If you want to understand better the generation of valid DICOM, remove everything below
and try writing your own DICOM generation code from scratch.
Refer to this part of the standard to see what are the requirements for the valid
Secondary Capture IOD: http://dicom.nema.org/medical/dicom/2019e/output/html/part03.html#sect_A.8
The Modules table (A.8-1) contains a list of modules with a notice which ones are mandatory (M)
and which ones are conditional (C) and which ones are user-optional (U)
Note that we are building an RGB image which would have three 8-bit samples per pixel
Also note that writing code that generates valid DICOM has a very calming effect
on mind and body :)")  
</details>

<details>
  <summary>
      🧠 <b> Further Resources </b>
  </summary>
  <br/>
  <details>
    <summary>
      🧠 <b> Conferences and professional societies </b>
    </summary>
  
   - [MICCAI Society](http://www.miccai.org/) hosts an annual conference dedicated to medical imaging and related fields, and also hosts a number of challenges. One that has consistently generated good volumetric datasets is called [BRATS](http://braintumorsegmentation.org/)  
   - [Radiological Society of North America](https://www.rsna.org/) is a renowned organization that unifies medical imaging professionals around the globe. In addition to hosting the eponymous largest medical imaging conference in the world it has been turning more attention to AI recently, and hosted interesting medical imaging competitions within its "[AI challenge](https://www.rsna.org/en/education/ai-resources-and-training/ai-image-challenge)" program. Last year's challenged featured a classification problem for CT imaging (although with the focus on 2D methods)  
   - [SIIM](https://siim.org/page/meetings) is a society that focuses on medical imaging informatics and it has recently started running a machine learning sub-conference called C-MIMI.
  </details>

  <details>
    <summary>
      🧠 <b> Academia </b>
    </summary>
    
   - [Center for Clinical Data Science](https://www.ccds.io/) by Parthers Healthcare  
   - [Stanford's AIMI](https://aimi.stanford.edu/)  
   - [National Consortium of Intelligent Medical Imaging](https://www.medsci.ox.ac.uk/research/networks/national-consortium-of-intelligent-medical-imaging), kicked off by the University of Oxford and the UK's National Health Service  
  </details>
    
  <details>
    <summary>
      🧠 <b> Startups </b>
    </summary>
    <br/>
    There are plenty and there will be more. Some choose to pursue a clinical workflow, some focus on the application of particular machine learning techniques and some capitalize on existing clinical footprint and invest in platforms that accelerate others' efforts. Some established players are:
  
   - [Cortechslabs](https://www.cortechslabs.com/) - focuses on quantitative analysis of brain images. Of particular note is the software called [Neuroquant](https://www.cortechslabs.com/products/neuroquant/) which uses deep learning to produce reports with MRI-based volumetric measurements of structures inside the brain that are related to age-related neurodegenerative disorders such as Alzheimer's. Sounds familiar? :)
   - [Mirada Medical](https://mirada-medical.com/) - Oxford-based company that advanced the field of radiation oncology with its deep-learning-based segmentation models.
   - [Arterys](https://www.arterys.com/) - Silicon Valley startup that was the first to obtain an FDA clearance for a deep learning medical imaging suite for oncology.
   - [Enlitic](https://www.enlitic.com/) - San Francisco-based company aiming at diagnostic use cases that accelerate radiologic workflow.
   - [Nuance](https://www.nuance.com/healthcare/diagnostics-solutions/ai-marketplace.html) is a Boston-based company that produces a well-established platform of choice for radiological dictation. Recently the company focused a lot of effort on a marketplace for medical imaging AI solutions where startups that do not quite have Nuance's reach can deploy their software.
   - [Terarecon](https://www.terarecon.com/envoyai/exchange) - similarly to Nuance, this Californian company started in core diagnostic radiology and expanded with an AI marketplace offering branded "EnvoyAI".
    
   </details>
    
  <details>
    <summary>
      🧠 <b> Big Tech </b>
    </summary>
    <br/>
Some big cloud providers are eyeing the space closely, and running their own programs and projects related to medical imaging.
    
   - Microsoft Research has a [project InnerEye](https://www.microsoft.com/en-us/research/project/medical-image-analysis/) that for the past 10+ years has been exploring the use of machine learning for a variety of medical imaging applications. One of the instructors of this course had the honor of spending a significant part of his career as a team member here.
   - Google DeepMind is a group within Google doing some cutting-edge AI research, including [some work on medical imaging](https://deepmind.com/blog/article/ai-uclh-radiotherapy-planning). We can credit them with the contribution to the invention of the U-net which has been prominently featured in this course.
   </details>
   </details>
  
## Course 3: Applying AI to EHR Data 

<details>
  <summary>
      🧠 <b> Lesson 1: </b> Introduction
  </summary>

  - [Health Affairs](https://www.healthaffairs.org/doi/abs/10.1377/hlthaff.2018.05499)  
  - [CMS](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/NationalHealthExpendData/NationalHealthAccountsProjected)  
  - [50 Surprising Statistics Every Healthcare Stakeholder Must Know](https://www.osplabs.com/insights/50-surprising-statistics-every-healthcare-stakeholder-must-know/)  
  - [Apple Healthcare Data](https://www.apple.com/healthcare/health-records/)  
  - [Google Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/projects-datasets-data-stores)  
  - [Google Health](https://health.google/)  
</details>

<details>
  <summary>
      🧠 <b> Lesson 2: </b> EHR Data Security and Analysis
  </summary>

  - [Value of Medical Data on the Dark web](https://www.experian.com/blogs/ask-experian/heres-how-much-your-personal-information-is-selling-for-on-the-dark-web/)  
  - [Hacker Hone their Techniques](https://www.healthcareitnews.com/news/healthcare-data-big-risk-hackers-innovate-and-hone-their-techniques)  
  - [Examples from U.S. HIPAA fines](https://www.federalregister.gov/documents/2019/04/30/2019-08530/notification-of-enforcement-discretion-regarding-hipaa-civil-money-penalties)  
  - [HIPAA](https://www.hhs.gov/hipaa/index.html)  
  - [HITECH](https://www.hhs.gov/hipaa/for-professionals/special-topics/hitech-act-enforcement-interim-final-rule/index.html)  
  - [GDPR](https://gdpr-info.eu/)  
  - [DPA](https://www.gov.uk/data-protection)  
  - [PHI](https://www.hhs.gov/answers/hipaa/what-is-phi/index.html)  
  - [Covered Entites](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html)  
  - [Sample Business Associate Agreement](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html)  
  - [Business Associate Guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html)  
  - [De-Identification Rationale](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html#rationale)  
  - [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)  
  - [What is Exploratory Data Analysis](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)  
  - [EDA in Python](https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce)  
  - [Get started with TensorFlow Data Validation](https://www.tensorflow.org/tfx/data_validation/get_started)  
  - [Imputation Methods](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)  
  - [Advanced Imputation Methods](https://www.sciencedirect.com/science/article/pii/S2352914819302783)  
  - [Z-Score](https://www.statisticshowto.com/probability-and-statistics/z-score/)  
  - [Reducing Dimensionality](https://en.wikipedia.org/wiki/Dimensionality_reduction)  
  - [Demographic Analysis](https://www.sciencedirect.com/topics/computer-science/demographic-data)  

</details>


<details>
  <summary>
      🧠 <b>   Lesson 3: </b> EHR Code Sets
  </summary>

  - [IDC10-CM Sepsis Codes](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A30-A49/A41-/A41)  
  - [CDC's Rationale](https://www.cdc.gov/nchs/icd/icd10cm_pcs_background.htm)  
  - [Code Structure](https://library.ahima.org/doc?oid=106177#.Xm70u5NKhQI)  
  - [Coding Guidelines](https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2019-ICD10-Coding-Guidelines-.pdf)  
  - [2020 ICD-10CM Codes - Query all codes](https://www.icd10data.com/ICD10CM/)  
  - [CDC ICD10-CM Lookup Tool](https://icd10cmtool.cdc.gov/?fy=FY2019)  
  - [Coronavirus ICD Code Announcement](https://www.cdc.gov/nchs/data/icd/Announcement-New-ICD-code-for-coronavirus-2-20-2020.pdf)  
  - [Primary, Principal, and Secondary Diagnosis Codes](https://acdis.org/articles/qa-primary-principal-and-secondary-diagnoses-1)  
  - [PCS Procedure Code System](https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2014-pcs-procedure-coding-system.pdf)  
  - [Medicare Coding](https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2016-PCS-Slides.pdf)  
  - [Understanding CPT Codes](https://www.verywellhealth.com/what-are-cpt-codes-2614950#:~:text=Current%20Procedural%20Terminology%20(CPT)%20codes,%2C%20surgical%2C%20and%20diagnostic%20services.)  
  - [CMS.gov Database Download for CPT Codes](https://www.cms.gov/medicare-coverage-database/search.aspx?error=Please%20use%20the%20new%20MCD%20Search%20to%20find%20your%20document.&from=~/overview-and-quick-search.aspx&npage=/medicare-coverage-database/downloads/downloadable-databases.aspx)  
  - [CMS.gov HCPCS Codes Information](https://www.cms.gov/Medicare/Coding/MedHCPCSGenInfo)  
  - [HCPCS Wikipedia](https://en.wikipedia.org/wiki/Healthcare_Common_Procedure_Coding_System)  
  - [NDC LOOKUP](https://ndclist.com/)  
  - [RXNorm Overview](https://www.nlm.nih.gov/research/umls/rxnorm/overview.html)  
  - [CCS website](https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp#download)  
  - [MS-DRG](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/AcuteInpatientPPS/MS-DRG-Classifications-and-Software)  
  - [SNOMED CT](https://www.snomed.org/five-step-briefing)  
  - [Graph Convolutional Transformer](https://arxiv.org/pdf/1906.04716.pdf)  
  - [Transformer Architecture](https://arxiv.org/abs/1706.03762)  
  - [Graph Convolutional Transformer - Github Code](https://github.com/Google-Health/records-research/tree/master/graph-convolutional-transformer)  
  - [Graph Convolutional Transformer - EHR Data](https://eicu-crd.mit.edu/about/eicu/)  

</details>


<details>
  <summary>
      🧠 <b>   Lesson 4: </b> EHR Transformations & Feature Engineering
  </summary>

  - [Encounter Definitions](https://www.hl7.org/fhir/encounter-definitions.html)  
  - [Google's Nature Paper-Logitudinal EHR Data Representation](https://www.nature.com/articles/s41746-018-0029-1)  
  - [Google's Patent- EHRs Data Management Systems and Methods](https://patents.google.com/patent/US20160042124)  
  - [FHIR Overview](https://www.hl7.org/fhir/overview.html)  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  

</details>

<details>
  <summary>
      🧠 <b>   Lesson 5: </b> Building, Evaluating and Interpreting Models
  </summary>

  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()


</details>


<details>
  <summary>
      🧠 <b>   Project: </b>  Patient Selection for Diabetes Drug Testing
  </summary>

  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  

</details>

## Course 4: Applying AI to Wearable Device Data

<details>
  <summary>
        🧠 <b>   Lesson 1: </b> Introduction to Wearable Data
  </summary>

  - [Hillsborough teen: Apple Watch saved my life](https://www.abcactionnews.com/news/region-hillsborough/hillsborough-teen-apple-watch-saved-my-life)  
  - [5 examples of popular wearable devices in healthcare](https://www.businessinsider.com/5-examples-wearable-healthcare-devices-2021-5)  
  - [Precision-Recall](https://commons.wikimedia.org/wiki/File:Precisionrecall.svg)  
  - [Digital health](https://en.wikipedia.org/wiki/Digital_health)  
  - [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)  
  - [Framingham Heart Study](https://en.wikipedia.org/wiki/Framingham_Heart_Study)  
  - [Apple Heart Study: Assessment of Wristwatch-Based Photoplethysmography to Identify Cardiac Arrhythmias](https://classic.clinicaltrials.gov/ct2/show/NCT03335800)  
  - [Apple Heart Study: Large-scale assessment of a smartwatch to identify atrial fibrillation](https://www.nejm.org/doi/full/10.1056/NEJMoa1901183)  
  - [Apple Heart Study Response: Watched by Apple](https://www.nejm.org/doi/full/10.1056/NEJMe1913980)  
  - [Framingham Study: Atrial fibrillation as an independent risk factor for stroke: the Framingham Study](https://www.ahajournals.org/doi/10.1161/01.STR.22.8.983)  
  - [Wearable Health: Health Wearables: Ensuring Fairness, Preventing Discrimination, and Promoting Equity in an Emerging Internet-of-Things Environment](https://louisville.edu/mobileelsi/wgm-3/wgm-3-background-materials/health-wearables-insuring-fairness-preventing-discrimination-and-promoting-equality-in-an-emerging-internet-of-things-enviromnent_kathryn-montgomery-et-al/)
  - [Pipfile Example](https://github.com/udacity/nd320-c4-wearable-data-starter/blob/master/Pipfile)
  - [Pipenv: Python Dev Workflow for Humans](https://pipenv-fork.readthedocs.io/en/latest/index.html)
  - [Spyder IDE](https://docs.spyder-ide.org/current/index.html)

</details>

<details>
  <summary>
        🧠 <b>   Lesson 2: </b> Intro to Digital Sampling & Signal Processing
  </summary>

  - [Sampling Signal Processing](https://en.wikipedia.org/wiki/Sampling_%28signal_processing%29)  
  - [PhysioNet: The Research Resource for Complex Physiologic Signals](https://physionet.org/)  
  - [European ST-T Database: ECG dataset along with R wave peak annotations](https://physionet.org/content/edb/1.0.0/)  
  - [Interpolation](https://en.wikipedia.org/wiki/Interpolation)  
  - [Linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation)  
  - [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)  
  - [3Blue1Brown - Animated Maths](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)  
  - [But what is the Fourier Transform? A visual introduction](https://www.youtube.com/watch?v=spUNpyF58BY)  
  - [Short-Time Fourier Transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)  
  - [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)  
  - [Matplotlib Spectrogram](https://linuxhint.com/matplotlib-spectogram/)  
  - [Wavelet Transform](https://users.rowan.edu/~polikar/WTpart1.html)  
  - [The more general uncertainty principle, regarding Fourier transforms](https://www.youtube.com/watch?v=MBnnXbOM5S4)
  - [Harmonic](https://en.wikipedia.org/wiki/Harmonic) 
  - [What are harmonics? Exploring the fabric of music](https://splice.com/blog/what-are-harmonics/?utm_term=&campaignid=20329853011&adgroupid=148615476697&adid=664393838102)  
  - [Why Don't All Instruments Sound The Same?](https://www.youtube.com/watch?v=Q8ITu0EASL4)  
  - [Music And Measure Theory](https://www.youtube.com/watch?v=cyW5z-M2yzw)  

</details>

<details>
  <summary>
        🧠 <b>   Lesson 3: </b> Introduction to Sensors
  </summary>

  - [Piezoelectric Accelerometers](https://blog.endaq.com/piezoelectric-accelerometers-how-they-work-and-where-to-buy)  
  - [Activity/Posture Recognition using Wearable Sensors Placed on Different Body Locations](https://pdfs.semanticscholar.org/b8ac/6f5f1a3362f83aef7c75b0b75ab09e17a3c1.pdf)  
  - [Gait Cycle Segmentation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4732099/)  
  - [Gait Cycle Segmentation Using an Ankle Based Accelerometer](https://eudl.eu/pdf/10.4108/icst.pervasivehealth.2011.246061)  
  - [How changes in the gait cycle can be learned behavior? In this case, from prior KGB training.](https://www.bmj.com/content/351/bmj.h6141)  
  - [Monitoring of Heart Rate from Photoplethysmographic Signals Using a Samsung Galaxy Note8 in Underwater Environments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6651860/)  
  - [Photoplethysmogram](https://en.wikipedia.org/wiki/Photoplethysmogram)  
  - [Photoplethysmography-Based Biomedical Signal Processing](https://www.semanticscholar.org/paper/Photoplethysmography-Based-Biomedical-Signal-Sch%C3%A4ck/c1d1318d4fa8c8c02b1eaae2ca50c16532b53e15?p2df)  
  - [Electrocardiography](https://en.wikipedia.org/wiki/Electrocardiography)  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
</details>

<details>
  <summary>
        🧠 <b>   Lesson 4: </b> Activity Classification
  </summary>

  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  

</details>

<details>
  <summary>
        🧠 <b>   Lesson 5: </b> ECG Signal Processing
  </summary>

  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  

</details>

<details>
  <summary>
        🧠 <b>   Project: </b> Motion Compensated Pulse Rate Estimation
  </summary>

  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  
  - []()  

</details>

## Miscellaneous

<details>
  <summary>
        🧠 <b>   Resources </b> 
  </summary>

  - [PyTorch and Monai for AI Healthcare Imaging](https://www.youtube.com/watch?v=M3ZWfamWrBM&t=10153s&ab_channel=freeCodeCamp.org)
  - [Using PyTorch Visualization Utilities in Inference Pipeline](https://debuggercafe.com/using-pytorch-visualization-utilities-in-inference-pipeline/)
  - [Git & GitHub](https://www.youtube.com/playlist?list=PLWKjhJtqVAbkFiqHnNaxpOPhh9tSWMXIF)  
  - [Efficient PyTorch — Supercharging Training Pipeline](https://towardsdatascience.com/efficient-pytorch-supercharging-training-pipeline-19a26265adae)  
  - [DICOM Training](https://dcmtk.org/en/services/dicom-training/)  
  - [Getting started with OHIF](https://docs.ohif.org/development/getting-started/)  
  - [[Info Need]: Can you share MONAI-like library in TensorFlow/Keras?](https://discuss.tensorflow.org/t/info-need-can-you-share-monai-like-library-in-tensorflow-keras/7976/1)  
  - [An Introduction to Biomedical Image Analysis with TensorFlow and DLTK](https://blog.tensorflow.org/2018/07/an-introduction-to-biomedical-image-analysis-tensorflow-dltk.html)  
  - [MIScnn: Medical Image Segmentation with Convolutional Neural Networks](https://github.com/frankkramer-lab/MIScnn)  
  - [pynetdicom Tutorial: python package for DICOM networking](https://pydicom.github.io/pynetdicom/stable/tutorials/index.html)  
  - []()
  - []()
  - []()
  - []() 
  - []()
  - []()
  - []()
  - []()
  - []()
  - []()
  - []()
  - []() 
</details>
