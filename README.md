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

![Allen Principles Schema (Local)](/Definition/Images/Allen_principles/Allen_principles_schema.png)
*Figure 1: SSI properties mapped within the general SSI process flow.[^allen]*

### 1.2 Related works

Several works by academics and industry experts have redefined and extended Allen's original principles in an attempt to converge on a comprehensive list of principles for SSI. We collected 18 research studies published between 2016 (the year the term 'SSI' was coined) and 2024.

### 1.3 Analysis

Past tentative to converge to a list of SSI principles demonstrated significant disagreement regarding the properties of SSI. Our contribution departs from previous works[^cucko] as it incorporates a broader literature review (x5 the references of [^cucko]) and a clustering algorithm to achieve consensus on properties and their classification. Based on our literature review, this is the first time this type of exercise has been done in a paper from academia.

Specifically, our study analyzes and classifies 52 properties from 18 works to identify a subset of highly cited principles.Additionally, a questionnaire addresses three key objectives: I) Investigate the identified SSI properties and evaluate their importance. II) Identify the most and least critical properties, including non-repudiable ones. III) Validate the classification and grouping of properties.

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

*7. Refining principles.* We provide the table with the list of principles and corresponding definition. We shorten the definition as much as possible, while trying to keep their essence.

*8. Expert validation.* To validate the selection process and finalize the list of properties (used in the questionnaire), expert interviews were conducted. These discussions reviewed and justified the inclusion or exclusion of specific properties.

*9. Final list.* The final step involved creating a definitive list of properties, accompanied by precise definitions for each.

Steps 1 and 3 are instrumental in reaching the Classification step, which may also serve to raise awareness of past works from the literature. In the following section, we detail the results from steps 4 to 8.

#### 1.3.2 Recording of properties

Table 1 summarizes their key contributions: each row represents an SSI property, while the columns list the corresponding authors. Differences in naming conventions can be observed across the various authors. Notably, the 18 works describe a total of 52 properties, some of which convey similar meanings.

[Click to view the table 1.](https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Tables/Principles/Principles1.html) *Comparison of identified properties in various sources.*

#### 1.3.3 Comparison of properties.

Differences in naming can be observed between different authors. However, these properties often convey the same meaning. Consequently, the following properties were combined: (i) Existence and Representation, (ii) Ownership and Control, (iii) Access and Availability, (iv) Security and Protection, (v) Privacy and Minimal Disclosure, (vi) Decentralization and Autonomy, (vii) Verifiability and Authenticity, and (viii) Usability and Consistency. On the other hand, the properties Equity and Inclusion, as well as Recoverability, were eliminated. Thus, our rationale is based on previous works that combine these properties to create a classification of SSI principles. Figure 2 illustrates the SSI properties causal loop diagram, which shows the merging of properties across different authors.

![Casual Loop Diagram Properties (Local)](/Definition/Images/Casual_loop_diagram/Casual_loop_diagram.png)
*Figure 2: Casual loop diagram of the set of SSI properties, defined by different authors on the left. The final set of properties on the right.*

In particular, we used the same approach described in[^cucko], but we renamed Legacy System with Compliance; we merged Usability, Consistency and Accessibility with Consistency and Usability, while linking Recoverability with Usability. This allows us to have an objective analysis of properties that is based on literature.

Table 2 shows the result of combining properties. From this table we notice a significant difference between the original principles from Allen and the extended 24 principles. The 80% of authors adopt the principles from Allen; on avarage, they share 8 principles of the 10 from the original definition of SSI. Situation slightly change among the remaining 24 extending principles, shared by less than 10% of authors.

[Click to view the table 2.](https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Tables/Principles_semplification/Principles_semplification2.html) *Comparison of identified properties grouping from various sources*

| **Category**                          | **Adoption Rate** | **Details**                                      |
|---------------------------------------|-------------------|-------------------------------------------------|
| Authors adopting Allen's principles   | 80%               | Share an average of 8 out of 10 SSI principles. |
| Extended principles (24 total)        | < 10%             | Less than 10% of authors share these principles.  |

Thus, our rationale to define a final set of principles of SSI move forward to select all principles from Table 2 that are cited by 5 or more authors. The final list contains all principles from Allen extended with 5 new principles as depicted in Figure 2, on the right.

[Click to view the table 3.](https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Tables/Principles_semplification/Principles_semplification1.html) *Comparison of identified properties grouping from various sources and final list of properties.*

#### 1.3.4 Clustering

Other than extending Allen's principles of SSI, some works provide a taxonomy of their properties, offering insights into the definition itself. In Table 4, we extend the information previously given in Table 1, detailing each principle in the first column after using the causal loop diagram in Figure 2. Similar to the principles, differences in the naming of the taxonomy can also be observed among various authors.

[Click to view the table 4.](https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Tables/Principles_classification/Principles_classification1) *The taxonomy of principles provided by various authors.*

Thus, unlike the combination of principles, we cannot rely on past literature contributions to provide our taxonomy. Indeed, all works base their taxonomization of principles on their own interpretations. To avoid subjectivity, we decided to use a clustering technique to base our grouping on what has already been done by other authors. We tested three main methods: 

1) Greedy, which iteratively selects the local optimal solution, meaning that for a given category, it minimizes the distance between the categories. Despite its simplicity, the Greedy algorithm does not always guarantee a globally optimal solution. In cases where some principles have categories with the same number of instances, it is crucial to minimize the distance between clusters by considering multiple categories.

2) K-Means, which minimizes intra-cluster distance.

3) Finally, we used a graph representation to visually verify the results.

Results are reported within different sheets of the excel file located in: https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Tables/Principles_classification/Summary.xlsx

The three methods lead to the same conslusion. We authomatize the process through the following [python program](https://cristianlepore.github.io/Self-Sovereign-Identity/Definition/Program/Compute_K-Means.py).

- The program reads data from a CSV file 
`data = pd.read_csv(file_path)`
- Fills black cells with zeroes 
`cleaned_data = numerical_columns.fillna(0)`
- Applies the K-Means clustering 
`kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)`
For reproducibility of results, we used the same seed to calculate the starting centroid through `random_state=42`
- Save results. `print(f"Clustering completed! Results saved in: {output_file}")`

We tested several combinations of parameter KK (number of clusters) and eventually settled on K=5K=5. This value of KK ensures a fair number of elements in each cluster. Figure 3 shows the final result. The group's name is based on literature.

![Final list of principles and clustering (Local)](/Definition/Images/Final_list_principles/Final_list_properties.png)
*Figure 3: The final set of principles and its grouping.*

#### 1.3.5 Refining principles

The final set of 15 properties and their definitions can be found in Table 5. The definitions come from the combination of the 18 works from the literature. However, we shorten the definitions as much as possible, maintaining their essence for the questionnaire.

| Property | Definition |
|----------|----------|
| Existence and representation   | The ability to establish and recognize an independent existence through the assertion of attributes to services as proof of their identity. Additionally, individuals should be able to creare as many identities as required presenting attributes to service providers.[^lepore] |
| Consent  | It is the permission individuals give to collect, use, and share their data. Ensuring the user’s explicit consent for the usage of their identity data, including opt-in and opt-out mechanisms. |
| Ownership and control   | Ensuring users can directly manage their identity, including negotiating their attributes from the agent/wallet.[^cameron] |
| Persistence    | An identity must persist and being valid over time. Individuals may present the same attributes from multiple sources.[^allen] |
| Privacy and minimal disclosure    |  Individuals should be able to protect their provicy through selective disclosure and data minimization.[^cucko] |
| Security and protection    |  Identity should be secured and protected against suppression or invalidation of the list of attributes, IdPs and SPs by any central authority.  |
| Decentralization and autonomy    | Entities should have autonomy of their identity data without relying on any third party. |
| Usability and consistency    | Agents and other identity components should be easy to use and their information should be consistent among different domains. Aligning rules, policies, practices across jurisdictions or systems for consistency. |
| Verifiability and authenticity    |  Entities should be able to reliably verify their identities and must provide proof of the authenticity of their personal data.[^cucko] |
| Access and availability   | Entities must have unrestricted access to the list of identity providers and service providers. |
| Cost   | The mechanisms for creating, maintaining, and sustain the system should have a minimal cost. |
| Interoperability   | Entities must be as widely usable available as possible and not limited to a specific domain. |
| Portability   | Allowing users to carry and use their digital identity across multiple platforms and contexts. Attributes can be transported to other ecosystems. |
| Standard   | An e-identity system must use globally recognized standards. |
| Transparency | Policies, rules, protocols and algorithms to manage the ecosystem members must be transparent. Open policies and rules; transparent algorithms to manage ecosystem members. |

#### 1.3.6 Expert validation



## References

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
