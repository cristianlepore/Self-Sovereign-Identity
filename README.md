# A Model To Assess Digital Identity Solutions

The purpose of this work is to extend the original contribution of a model for assessing the adherence of e-Identity solutions to Self-Sovereign Identity (SSI) [^lepore] by addressing the following research questions:

1. *RQ1: What are the principles of Self-Sovereign Identity?*
2. *RQ2: Can we assess any SSI system based on these principles?*

[Section 1](#1-self-sovereign-identity) addresses RQ1 and provides a comprehensive definition of Self-Sovereign Identity, while Section 2 introduces the model for assessing e-Identity solutions.

## 1. Self-Sovereign Identity 

Self-Sovereign Identity (SSI) represents a new concept to manage digital identities, aiming to empower individuals by giving them control over their identity information.[^lepore] SSI is defined as a list of principles that extends the  original Laws of Identity.[^cameron]

### 1. Defintion of Self-Sovereign Identity

Allen has proposed ten guiding principles of the SSI, laying out the foundation for implementation of the concept, stating that the key properties of the SSI system are *Existence, Control, Access, Transparency, Persistence, Portability, Interoperability, Consent, Minimalization, and Protection*.[^allen]

#### 1.1 Related works

The schema below illustrates the data processing flow and the key roles within the general SSI model. It builds upon previous studies from the literature and incorporates the authentication process between users and verifiers (Relying Parties), as outlined in the Architecture and Reference Framework v1.4.1 of the EUDI Wallet.[^cucko][^ARF]

The left side of the schema lacks specific details regarding wallet instances and stages, while the right side depicts the data flow associated with the request and presentation of assertions. The principles *Transparency* and *Persistence* are outside the schema,[^cucko] while the communication identified by letters A,B,C,D are optional for many solutions.

![Allen Principles Schema (Local)](Images/Allen_principles/Allen_principles_schema.png)
*Figure 1: SSI properties mapped within the general SSI process flow.[^allen]*

#### 1.2 Analysis

Several works by academics and industry experts have redefined and extended the original principles of Self-Sovereign Identity (SSI). Unlike earlier studies that primarily utilized, critiqued, or extended Allen’s principles, our research analyzed and classified 51 properties identified in 18 works from the literature. Using heuristics, we converged on a shared set of properties and organized them based on prior grouping exercises described in the literature. To achieve this, we tested three clustering methods: Greedy, K-Means, and Graph Theory. This process resulted in a subset of highly relevant properties and an objective clustering of principles.

We further refined the properties and conducted a questionnaire to address three key objectives I) Investigate the identified SSI properties and evaluate their importance. II) Identify the most and least critical properties, including non-repudiable ones. III) Validate the classification and grouping of properties. Our study gathered insights from experts in Decentralized and Self-Sovereign Identity Management across diverse roles and domains, including Computer Security and AI. These experts were interviewed during the ARES conference 2024, held from July 29 to August 2, 2024 in Vienna, Austria.

##### 1.2.1 Methodology

A systematic review offers a structured, comprehensive overview of a research field through the following steps.[^lepore][^badzek][^cushman]

*1. Defining research questions.* We formulated research question RQ1, as introduced in the [introduction](#a-model-to-assess-digital-identity-solutions). To address *RQ1* (the focus of [Section 1](#1-self-sovereign-identity)), we generated the following search strings based on relevant keywords:

- *SSI AND principles*
- *Self-Sovereign Identity AND properties*
- *SSI AND definition*

Keywords were refined to optimize search results, and wildcards were avoided for clarity (e.g., "SSI" and "Self-Sovereign Identity").[^lepore]

*2. Searching.* The search strings were used to identify articles containing relevant keywords in titles and abstracts across multiple academic databases, including ACM, ArXiv, IEEE Xplore, Scopus, and meta-search engines like Google Scholar. This yielded 250 initial results.

*3. Screening.* Abstracts and conclusions were screened to exclude irrelevant results based on inclusion/exclusion criteria such as subject relevance (SSI), publication year, originality, and proofs-of-concept. Duplicate results were removed, resulting in 47 articles selected for full review. These articles specifically addressed SSI principles. Despite being an emerging topic, the selection represents a significant portion of the literature from 2016 to 2024.

*4. Classification.* The selected articles were analyzed to extract properties and their definitions as presented by the authors. This process identified 18 papers containing a total of 51 distinct properties of SSI.

*5. Data extraction.* Among the 51 properties, many shared similar meanings but were labeled differently across papers. Properties with identical names and definitions were grouped, while heuristics were applied to identify the most commonly cited properties. Only those referenced in at least 30% of the papers were retained as final candidates.

*6. Refining.* The identified properties were clustered based on their labels using a clustering algorithm, such as K-Means, to group related concepts systematically.

*7. Eliminating and finalizing properties.* To validate the selection process and finalize the list of properties (used in the questionnaire), expert interviews were conducted. These discussions reviewed and justified the inclusion or exclusion of specific properties.

*8. Designing.* The final step involved creating a definitive list of properties, accompanied by precise definitions for each.

##### 1.2.2 Results

Table 1 shows the results of the analysis, including the similarities and differences in naming between defined sets of properties. Each Table row represents one property according to the similarity of the collected definitions, while differences in naming can be observed between different authors.

[Click to view the table 1.](https://cristianlepore.github.io/Self-Sovereign-Identity/Tables/Principles.html) *Comparison of identified properties in various sources.*

[Click to view the table 2.](https://cristianlepore.github.io/Self-Sovereign-Identity/Tables/Principles_classification.html)*Comparison of identified properties and correspondiing taxonomy from various sources.*

# References

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^cucko]: Čučko, Špela, et al. "Towards the classification of self-sovereign identity properties." IEEE access 10 (2022): 88306-88329.

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[16] Stokkink, Quinten, and Johan Pouwelse. "Deployment of a blockchain-based self-sovereign identity." 2018 IEEE international conference on Internet of Things (iThings) and IEEE green computing and communications (GreenCom) and IEEE cyber, physical and social computing (CPSCom) and IEEE smart data (SmartData). IEEE, 2018.

[17] Čučko, Špela, et al. "Towards the classification of self-sovereign identity properties." IEEE access 10 (2022): 88306-88329.
