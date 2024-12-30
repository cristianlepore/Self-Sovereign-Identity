# A Model To Assess Digital Identity Solutions

The purpose of this work is to extend the contribution of a model for assessing the adherence of e-Identity solutions to Self-Sovereign Identity (SSI) [^lepore] by addressing the following research questions:

*1. RQ1: What are the principles of Self-Sovereign Identity?*
*2. RQ2: Can we use these principles to assess any SSI system?*

[Section 1](#1-self-sovereign-identity) proposes a solid definition of Self-Sovereign Identity and addresses RQ1, while Section 2 leverages this definition to propose a model for assessing e-Identity solutions. Finally, Section 3 delves into a testing stage where the model is tested against existing solutions in the field of identity.

Besides taking inspiration from past exercises that define SSI principles [^allen][^ferdous][^toip][^toth][^cucko], this work departs from past contributions because it is not limited to defining SSI but is instrumental in exploiting a model to assess identity solutions. On the other hand, other SSI-based assessments fail to describe the methodology [^pava] or lack precision in their analysis [^bokkem][^omar].

Additionally, we make our list of principles consistent through interviews with experts participating at the ARES conference 2024.

Hereafter, we use the term principles for SSI interchangeably with the terms property and features. For the sake of clarity, they will all refer to the same concept. We often abbreviate the term Self-Sovereign Identity as SSI.

## 1. Self-Sovereign Identity 

Self-Sovereign Identity (SSI) is a novel approach that aims to provide users with an identity they can control. However, the concept also encompasses additional principles. The first to propose a list of principles extending the original Laws of Identity[^cameron] was Christopher Allen.[^allen]

Allen outlined ten guiding principles for SSI, laying the foundation for its implementation. He stated that the key properties of an SSI system are Existence, Control, Access, Transparency, Persistence, Portability, Interoperability, Consent, Minimalization, and Protection.[^allen]

### 1.1 Backgournd

Figure 1 illustrates the data flow of identity information and key roles within the general SSI model. Data moves from left to right, where issuers provide data to holders, who collect personal information within their wallet components. To access a service, users present a combination of assertions as proof of their identity to a verifier. Roles are not static, and each entity can become an issuer or verifier depending on the context. Sometimes the general model is complemented with a verifiable data registry, such as a blockchain or a registering CA, as depicted on the right-hand side of Figure 1.

The peculiarity of Figure 1 is its depiction of Allen's principles as defined in a classification of SSI properties.[^cucko] On the other hand, the communication flow on the right combines optional information through letters A, B, C, D directly from the Architecture and Reference Framework v1.4.1 of the EUDI Wallet solution.[^ARF] Occasionally, instead of a registering authority, a different type of trust anchor can be used for authentication.

![Allen Principles Schema (Local)](Images/Allen_principles/Allen_principles_schema.png)
*Figure 1: SSI properties mapped within the general SSI process flow.[^allen]*

### 1.2 Related works

Several works by academics and industry experts have redefined and extended Allen's original principles in an attempt to converge on a comprehensive list of principles for SSI. We collected 18 research studies published between 2016 (the year the term 'SSI' was coined) and 2024. Table 1 summarizes their key contributions: each row represents an SSI property, while the columns list the corresponding authors. Differences in naming conventions can be observed across the various authors.

[Click to view the table 1.](https://cristianlepore.github.io/Self-Sovereign-Identity/Tables/Principles.html) *Comparison of identified properties in various sources.*

### 1.3 Analysis

Past tentative to converge to a list of SSI principles demonstrated significant disagreement regarding the properties of SSI. Our contribution departs from previous works[^cucko] as it incorporates a broader literature review (x5 the references of [^cucko]) and a clustering algorithm to achieve consensus on properties and their classification. Based on our literature review, this is the first time this type of exercise has been done in a paper from academia.

Specifically, our study analyzes and classifies 51 properties from 18 works to identify a subset of highly cited principles.Additionally, a questionnaire addresses three key objectives: I) Investigate the identified SSI properties and evaluate their importance. II) Identify the most and least critical properties, including non-repudiable ones. III) Validate the classification and grouping of properties.

Our study gathers insights from experts in the Decentralized and Self-Sovereign Identity Management field, spanning diverse roles and domains, including Computer Security and AI. These experts were interviewed during the ARES Conference 2024, held from July 29 to August 2 in Vienna, Austria.

#### 1.3.1 Methodology

A systematic review offers a structured, comprehensive overview of a research field through the following steps.[^lepore][^badzek][^cushman]

*1. Defining research questions.* We formulated research question RQ1 to explore past works on SSI principles, as introduced in the [introduction](#a-model-to-assess-digital-identity-solutions). To address RQ1 (the focus of [Section 1](#1-self-sovereign-identity)),  we generated the following search strings based on relevant keywords:

- *SSI AND principles*
- *Self-Sovereign Identity AND properties*
- *SSI AND definition*

Keywords were refined to optimize search results and to avoid wildcards (e.g., "SSI" and "Self-Sovereign Identity").[^lepore] Keywords were shuffled to gather more results.

*2. Searching.* The search strings were used to identify articles containing relevant keywords in titles and abstracts across multiple academic databases, including ACM, ArXiv, IEEE Xplore, Scopus, and the meta-search engine of Google Scholar. This process yielded 47 initial results.

*3. Screening.* Abstracts and conclusions were screened to exclude irrelevant results based on inclusion/exclusion criteria such as publication year, originality, and whether they presented a taxonomy of SSI principles. Duplicate results were removed, resulting in 18 articles for SSI. Despite being an emerging topic, the selection represents a significant portion of the literature on SSI principles from 2016 to 2024.

*4. Recording of properties.* The selected articles were analyzed to extract properties and their definitions as presented by the authors. We compiled the results into a table containing the papers and corresponding features of SSI.

*5. Comparison of properties.* Some properties shared similar meanings but had different labels across papers. Properties with identical meanings were combined, while others were eliminated using heuristics.

*6. Clustering.* The identified properties were clustered based on their labels, testing methods such as K-Means, Greedy, and Graph Theory.

*7. Refining.* To validate the selection process and finalize the list of properties (used in the questionnaire), expert interviews were conducted. These discussions reviewed and justified the inclusion or exclusion of specific properties.

*8. Final list.* The final step involved creating a definitive list of properties, accompanied by precise definitions for each.

Steps 1 and 3 are instrumental in reaching the Classification step, which may also serve to raise awareness of past works from the literature. In the following section, we detail the results from steps 4 to 8.

#### 1.3.2 Recording of properties

Table 2 presents the information already provided in [Related Works](#12-related-works), with additional details, whenever possible, about the grouping from each article. Differences in naming conventions can be observed among the various authors. Notably, the 18 works describe a total of 51 properties, some of which convey similar meanings.

[Click to view the table 2.](https://cristianlepore.github.io/Self-Sovereign-Identity/Tables/Principles_classification.html) *Comparison of identified properties and grouping from various sources.*

#### 1.3.3 Comparison of properties.

Differences in naming can be observed between different authors. However, these properties often convey the same meaning. Consequently, the following properties were combined: (i) Existence and Representation, (ii) Ownership and Control, (iii) Access and Availability, (iv) Security and Protection, (v) Privacy and Minimal Disclosure, (vi) Decentralization and Autonomy, (vii) Verifiability and Authenticity, and (viii) Usability and Consistency. On the other hand, the properties Equity and Inclusion, as well as Recoverability, were eliminated. Thus, our rationale is based on previous works that combine these properties to create a classification of SSI principles. Figure 2 illustrates the SSI properties causal loop diagram, which shows the merging of properties across different authors.

![Casual Loop Diagram Properties (Local)](/Images/Casual_loop_diagram/)
*Figure 2: Casual loop diagram of the set of SSI properties, defined by different authors on the left. The final set of properties on the right.*

In particular, we used the same approach described in[^cucko], but we renamed Legacy System with Compliance; we merged Usability, Consistency and Accessibility with Consistency and Usability, while linking Recoverability with Usability. This allows us to have an objective analysis of properties that is based on literature.

Table 3 shows the result of combining properties. From this table we notice a significant difference between the original principles from Allen and the extended 28 principles. About the 80% of authors convey to use the principles from Allen, while less than 8% converge on the remaining 28 principles, with only 5 properties above the 25% of share.

Thus, our rationale to define principles of SSI move forward to select all principles from Table 3 that are cited by 5 or more authors. The final list contains all principles from Allen extended with 5 new principles as depicted in Figure 2, on the right.

[Click to view the table 3.](https://cristianlepore.github.io/Self-Sovereign-Identity/Tables/Principles_semplification_2.html) *Revision of Table 2 after combining principles.*

# References

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^cucko]: Čučko, Špela, et al. "Towards the classification of self-sovereign identity properties." IEEE access 10 (2022): 88306-88329.

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[^toth]: Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27. 

[^toip]: Trust Over IP Foundation. Principles of self-sovereign identity (ssi). https://trustoverip.org/wp-content/uploads/2021/10/ ToIP-Principles-of-SSI.pdf, 2024. Accessed: 2024-12-24 

[^ferdous]: Ferdous, Md Sadek, Farida Chowdhury, and Madini O. Alassafi. "In search of self-sovereign identity leveraging blockchain technology." IEEE access 7 (2019): 103059-103079.

[^pava]: Pava-Díaz, Roberto A., Jesús Gil-Ruiz, and Danilo A. López-Sarmiento. "Self-sovereign identity on the blockchain: contextual analysis and quantification of SSI principles implementation." Frontiers in Blockchain 7 (2024): 1443362.

[^bokkem]: Van Bokkem, Dirk, et al. "Self-sovereign identity solutions: The necessity of blockchain technology." arXiv preprint arXiv:1904.12816 (2019).

[^omar]: Dib, Omar, and Baha Rababah. "Decentralized identity systems: Architecture, challenges, solutions and future directions." Annals of Emerging Technologies in Computing (AETiC) 4.5 (2020): 19-40.
