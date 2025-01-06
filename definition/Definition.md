# 1. Self-Sovereign Identity 

Self-Sovereign Identity (SSI) is a novel approach that aims to provide users with an identity they can control. However, the concept also encompasses additional principles. The first to propose a list of principles extending the original Laws of Identity[^cameron] was Christopher Allen.[^allen]

Allen outlined ten guiding principles for SSI, laying the foundation for its implementation. He stated that the key properties of an SSI system are Existence, Control, Access, Transparency, Persistence, Portability, Interoperability, Consent, Minimalization, and Protection.[^allen]

## 1.1 Backgournd

Figure 1 illustrates the data flow of identity information and key roles within the general SSI model. Data moves from left to right, where issuers provide data to holders, who collect personal information within their wallet components. To access a service, users present a combination of assertions as proof of their identity to a verifier. Roles are not static, and each entity can become an issuer or verifier depending on the context. Sometimes the general model is complemented with a verifiable data registry, such as a blockchain or a registering CA, as depicted on the right-hand side of Figure 1.

The peculiarity of Figure 1 is its depiction of Allen's principles as defined in a classification of SSI properties[^toip]. On the other hand, the communication flow on the right combines optional information through letters A, B, C, D directly from the Architecture and Reference Framework v1.4.1 of the EUDI Wallet solution.[^ARF] Occasionally, instead of a registering authority, a different type of trust anchor can be used for authentication.

![Allen Principles Schema (Local)](/definition/images/allen_principles/Allen_principles_schema.png)
*Figure 1: SSI properties mapped within the general SSI process flow.[^allen]*

## 1.2 Related works

Several works by academics and industry experts have redefined and extended Allen's original principles in an attempt to converge on a comprehensive list of principles for SSI. We collected 18 research studies published between 2016 (the year the term 'SSI' was coined) and 2024.

## 1.3 Analysis

Past tentative to converge to a list of SSI principles demonstrated significant disagreement regarding the properties of SSI. Our contribution departs from previous works as it incorporates a broader literature review and a clustering algorithm to achieve consensus on properties and their classification. Based on our literature review, this is the first time this type of exercise has been done in a paper from academia.

Specifically, our study analyzes and classifies 52 properties from 18 works to identify a subset of highly cited principles.Additionally, a questionnaire addresses three key objectives: I) Investigate the identified SSI properties and evaluate their importance. II) Identify the most and least critical properties, including non-repudiable ones. III) Validate the classification and grouping of properties.

Our study gathers insights from experts in the Decentralized and Self-Sovereign Identity Management field, spanning diverse roles and domains, including Computer Security and AI. These experts were questioned during the ARES Conference 2024, held from July 29 to August 2 in Vienna, Austria.

### 1.3.1 Methodology

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

*8. Expert validation.* To validate the selection process and finalize the list of properties used in the questionnaire. These discussions reviewed and justified the inclusion or exclusion of specific properties.

*9. Final list.* The final step involved creating a definitive list of properties, accompanied by precise definitions for each.

Steps 1 and 3 are instrumental in reaching the Classification step, which may also serve to raise awareness of past works from the literature. In the following section, we detail the results from steps 4 to 8.

### 1.3.2 Recording of properties

Table 1 summarizes their key contributions: each row represents an SSI property, while the columns list the corresponding authors. Differences in naming conventions can be observed across the various authors. Notably, the 18 works describe a total of 52 properties, some of which convey similar meanings.

[Click to view the table 1.](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/tables/principles/Principles1.html) *Comparison of identified properties in various sources.*

### 1.3.3 Comparison of properties.

Differences in naming can be observed between different authors. However, these properties often convey the same meaning. Consequently, the following properties were combined: (i) Existence and Representation, (ii) Ownership and Control, (iii) Access and Availability, (iv) Security and Protection, (v) Privacy and Minimal Disclosure, (vi) Decentralization and Autonomy, (vii) Verifiability and Authenticity, and (viii) Usability and Consistency. On the other hand, the properties Equity and Inclusion, as well as Recoverability, were eliminated. Thus, our rationale is based on previous works that combine these properties to create a classification of SSI principles. Figure 2 illustrates the SSI properties causal loop diagram, which shows the merging of properties across different authors.

![Casual Loop Diagram Properties (Local)](/definition/images/casual_loop_diagram/Casual_loop_diagram.png)
*Figure 2: Casual loop diagram of the set of SSI properties, defined by different authors on the left. The final set of properties on the right.*

In particular, we renamed Legacy System with Compliance; we merged Usability, Consistency and Accessibility with Consistency and Usability, while linking Recoverability with Usability. This allows us to have an objective analysis of properties that is based on literature.

Table 2 shows the result of combining properties. From this table we notice a significant difference between the original principles from Allen and the extended 24 principles. The 80% of authors adopt the principles from Allen; on avarage, they share 8 principles of the 10 from the original definition of SSI. Situation slightly change among the remaining 24 extending principles, shared by less than 10% of authors.

[Click to view the table 2.](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/tables/principles_semplification/Principles_semplification2.html) *Comparison of identified properties grouping from various sources*

| **Category**                          | **Adoption Rate** | **Details**                                      |
|---------------------------------------|-------------------|-------------------------------------------------|
| Authors adopting Allen's principles   | 80%               | Share an average of 8 out of 10 SSI principles. |
| Extended principles (24 total)        | < 10%             | Less than 10% of authors share these principles.  |

Thus, our rationale to define a final set of principles of SSI move forward to select all principles from Table 2 that are cited by 5 or more authors. The final list contains all principles from Allen extended with 5 new principles as depicted in Figure 2, on the right.

[Click to view the table 3.](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/tables/principles_semplification/Principles_semplification1.html) *Comparison of identified properties grouping from various sources and final list of properties.*

### 1.3.4 Clustering

Other than extending Allen's principles of SSI, some works provide a taxonomy of their properties, offering insights into the definition itself. In Table 4, we extend the information previously given in Table 1, detailing each principle in the first column after using the causal loop diagram in Figure 2. Similar to the principles, differences in the naming of the taxonomy can also be observed among various authors.

[Click to view the table 4.](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/tables/principles_classification/Principles_classification1) *The taxonomy of principles provided by various authors.*

Thus, unlike the combination of principles, we cannot rely on past literature contributions to provide our taxonomy. Indeed, all works base their taxonomization of principles on their own interpretations. To avoid subjectivity, we decided to use a clustering technique to base our grouping on what has already been done by other authors. We tested three main methods: 

1) Greedy, which iteratively selects the local optimal solution, meaning that for a given category, it minimizes the distance between the categories. Despite its simplicity, the Greedy algorithm does not always guarantee a globally optimal solution. In cases where some principles have categories with the same number of instances, it is crucial to minimize the distance between clusters by considering multiple categories.

2) K-Means, which minimizes intra-cluster distance.

3) Finally, we used a graph representation to visually verify the results.

Results are reported within different sheets of the excel file located in: https://cristianlepore.github.io/Self-Sovereign-Identity/definition/tables/principles_classification/Summary.xlsx

The three methods lead to the same conslusion. We authomatize the process through the following [python program](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/program/Compute_K-Means.py).

- The program reads data from a CSV file 
`data = pd.read_csv(file_path)`
- Fills black cells with zeroes 
`cleaned_data = numerical_columns.fillna(0)`
- Applies the K-Means clustering 
`kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)` with a pre-established value `K=5`
For reproducibility of results, we used the same seed to calculate the starting centroid through `random_state=42`
- Save results. `print(f"Clustering completed! Results saved in: {output_file}")`

We tested several combinations of parameter K (number of clusters) and eventually settled on `K=5`. This value of K ensures a fair number of elements in each cluster. Figure 3 shows the final result. The group's name is based on literature.

![Final list of principles and clustering (Local)](/definition/images/Final_list_principles/Final_list_properties.png)
*Figure 3: The final set of principles and its grouping.*

### 1.3.5 Refining principles

The final set of 15 properties and their definitions can be found below. The definitions come from the combination of the 18 works from the literature. However, we shorten the definitions as much as possible, maintaining their essence for the questionnaire.

| Property | Definition |
|----------|----------|
| Existence and Representation | Entities and individuals must be able to prove their existence through the assertion of attributes to services. Additionally, individuals should be able to create as many identities as they wish.[^lepore] | 
| Consent | Entities must explicitly agree to the collection, use, and sharing of their identity data, including opt-in and opt-out options for consent. | 
| Ownership and Control | Entities can directly manage their identity, including control and negotiation of attributes from the agent/wallet to the service provider.[^cameron] | 
| Security and Protection | Entities should be protected by the use of the most cutting-edge technology. Identity should be secured and protected against suppression or invalidation of the list of attributes, IdPs, and SPs. | 
| Persistence | Individuals' identities must persist as long as the users wish, remaining valid over that period regardless of the identity provider.[^allen] Hence, individuals may present the same attributes from multiple sources.[^allen] |
| Privacy and Minimal Disclosure | The privacy of entities should be guaranteed by the use of protocols for the selective disclosure and data minimization of attributes. | 
| Access and Availability | Entities must have unrestricted access to the list of identity providers and service providers. | 
| Transparency | Policies, rules, protocols, and algorithms to manage the ecosystem members must be transparent. |
| Portability | Allowing users to carry and use their digital identity across multiple platforms and contexts. Attributes can be transported to other ecosystems. |
| Interoperability | Entities must be able to interoperate across domains and not be limited to a specific domain. | 
| Cost | The mechanisms for creating, maintaining, and sustaining the system should have minimal costs. | 
| Standard | An e-identity system must use globally recognized standards. | 
| Decentralization and Autonomy | Entities should have autonomy over their identity data without relying on any third party. | 
| Verifiability and Authenticity | Entities should be able to reliably verify users' identities and must provide proof of the authenticity of their personal data. |
| Usability and Consistency | Agents and other identity components should be easy to use, and their information should be delivered through rules, policies, and best practices that align across jurisdictions for system consistency. | 

### 1.3.6 Expert validation

To further validate our results, we conducted a survey on the proposed principles, targeting experts in the field of decentralized identity and Self-Sovereign Identity (SSI). The experts were approached in person during the ARES Conference 2024, held from July 29 to August 2, 2024. The survey aimed to gain a broader understanding of the perception of the SSI concept (Part 1) and its associated properties (Part 2). Specifically, the objective was to assess whether the identified properties, along with their naming and definitions, aligned with the opinions of the respondents. Additionally, the survey sought to determine the perceived level of importance of these properties, identifying the most and least critical ones. Moreover, by gathering expert insights, we aimed to uncover any additional concerns, inconsistencies, misunderstandings, or properties that might have been overlooked in our analysis.

**Methodology**

The ARES Conference hosted the International Workshop on Emerging Digital Identities[^ares]. Participants in the room were invited to answer a list of 37 questions divided into two sections. The first 20 questions aimed to gather insights into the field of decentralized identity. The second list of questions focused on evaluating the properties defined in [Section 1.3.5](#135-refining-principles). The questionnaire was provided on a voluntary basis to participants in the room, while a digital version of the same questions was accessible via a QR code for those who preferred to respond electronically. The online version, created using Microsoft Forms[^microsoft], was available throughout the entire duration of the conference, from July 29 to August 2, 2024.

**Questionnaire structure**

The first part of the questionnaire aimed to familiarize participants with the candidates' knowledge of identity. In the second part, the questions were designed to validate the SSI properties, following the order of the 15 proposed principles. While similar contributions often required respondents to invest significant time reviewing definitions alongside the list of principles for evaluation, we recognized that the time spent completing the questionnaire was an active component of the survey and could affect the overall response rate. To minimize the time burden on respondents and reduce dropout rates, we shortened the questionnaire's completion time. This was achieved by creating a single question for each principle and embedding the principle's definition directly within the question, maintaining respondent awareness throughout the process. [Appendix A](#appendix-a) contains a sample of the questionnaire related to the principles of Self.

Each question was designed to measure the perceived importance of each property using a Likert scale with the following items: (i) Irrelevant, (ii) Slightly Relevant (Unnecessary), (iii) Moderately Relevant (Useful), (iv) Relevant (Desirable), and (v) Very Relevant (Mandatory).[^joshi] These questions also aimed to evaluate whether our definitions in [Section 1.3.5](#135-refining-principles) were appropriate. Respondents were given the opportunity to express their agreement with the proposed definitions.

**Partecipants**

We broadcasted the survey among participants of the International Workshop on Emerging Digital Identities at the ARES Conference 2024.[^ares] The workshop track lasted the entire morning, and we collected results at the end of the session. The questionnaire was distributed anonymously to experts in the room, including participants from academia and industry. A total of 27 participants responded to the survey and completed it in full. Although all respondents chose to remain anonymous, we collected their responses and analyzed the results. For those who completed the survey online, the average completion time was 11.48 minutes, with the fastest completion recorded at 10.27 minutes and the slowest at 15.02 minutes. Of the respondents, 15 (more than 50%) reported having an identity wallet on their mobile device. While we did not track participants' job positions, roles, or affiliations, we know they were interested in identity-related topics. Despite the high number of respondents with identity wallets, 56% indicated they do not use them to present certificates digitally. Additionally, 48% of respondents believed that governments should fund the design of identity wallets, and 59% agreed that governments should also cover the deployment of the ecosystem of services and infrastructure surrounding identity wallets. Furthermore, 37% of respondents agreed that identity wallets provide a more secure means of authentication with services, where authentication is generally performed using biometrics such as fingerprinting and facial recognition. Finally, the majority of respondents expressed a preference for paying for an identity wallet rather than receiving advertisements. A detailed list of the questions and answers from this first set of the survey is available in [Appendix B](#appendix-b).

**Limitations**

The study was limited to the 15 properties included in the questionnaire, as presented in Section III-A, and to the classifications outlined in [Section 1.3.5](#135-refining-principles). Another limitation was the number of respondents (27) who participated in the questionnaire. A larger sample size would enhance the validity of the results and improve the potential for generalization. However, as the field of SSI is still emerging, our focus was on engaging true experts in the domain. We intentionally refrained from broadening the scope of participants to increase the number of respondents. Nevertheless, further discussion and research will be necessary to refine and solidify the definitions, ensuring they are both robust and comprehensive.

**Results and discusison**

Table 5 shows the results of respondend related to the 15 proposed properties and their ranking based on the avarage and the standard deviation.

[Click to view the table 5.](https://cristianlepore.github.io/Self-Sovereign-Identity/definition/survey/part2/Survey.html) *Ranking of identified properties.*

The figure below shows a breakdown of the votes for each property.

![Level of importance](survey/part2/LevelOfImportance.png)

The most and least important properties, as well as their intersection, is presented below.

![Important properties](survey/part2/ImportantProperties.png)

### 1.3.7 Final list

The definitions presented in [Section 1.3.5](#135-refining-principles) were abbreviated as much as possible intentionally, due to their use in the questionnaire. In this Section, we want to enhance them in accordance with the results of the respondents, as we obtained valuable insights from experts in the fields of IdM and SSI, expressing their concerns and possible misunderstandings of an individual property. Below you can find the corretion of properties that have either (i) obtained an avarage level below 3.75 with a high Standard Deviation, or (ii) Have required additional discussion reflecting the obtained results, while other properties are omitted intentionally.  Changes are bold, while the parts that need to be removed are crossed out.

In particular, many of the properties that achieved a low ranking were simplified, and their content narrowed to include a single concept (e.g., Access and Availability, Security and Protection). This does not come with a loss of specificity but rather with a simplified definition. Whenever necessary, we split the property into two properties.

| Property | Definition | Classification |
|----------|----------|----------|
| Existence ~~and Representation~~ | **Entities must have an independent existence.** They should be able to create as many identities **as required** and must be able to prove their existence through the assertion of attributes to services. | Controllability |
| ~~Ownership and~~ Control | **Entities must control their digital identity and corresponding personal data.** They can directly manage their attributes, including control the negotiation of attributes from the agent/wallet to the service provider. | Controllability |
| Consent | Entities must give deliberate consent for the collection, use, and share of identity data. Additionally, they should be able to ~~opt-in and~~ opt-out for consent **at a later date**. | Controllability |
| Persistence | ~~Individuals'~~ Identity must persist as long as the users wish, remaining valid over that period regardless of the identity provider. **To achieve this, individuals must be able to self assert attributes as well as receive attributes potentially from multiple sources.** | Security |
| Security ~~and protection~~ | Entities should be protected by the use of the most cutting-edge technology against suppression or invalidation of the list of attributes, as well as identity providers and service providers. | Security |
| Privacy **protection**~~and Minimal Disclosure~~ | The privacy of entities should be protected through the use of **technique that allow to minimize the disclosure of personal information**. | Security |
| Access ~~and Availability~~ | Entities must have unrestricted access to the list of identity providers and service providers. **They must be able to retrieve information about those entities.** | Mobility |
| Transparency | **The identity system, algorithms,** policies, rules, and protocols to manage the ecosystem members must be **free, open-soure, well-known, and independent of any specific architecture**. | Sustainability | 
| Portability | **Identity must be portable.** Users must be able to carry and use their digital identity across multiple platforms and multiple jurisdictions. Attributes and architectures must be transportable to other domains and ecosystems. | Sustainability | 
| Interoperability | Entities must be able to interoperate across domains and not be limited to a specific domain. **Idnetities must be widely usable.** | Sustainability | 
| Cost | **Entities must be able to performe crucial operation without cost barriers.** Mechanisms for creating, maintaining, and sustaining the system should have minimal or no costs. | Sustainability | 
| Standard | An e-identity system must use globally recognized standards. | Sustainability |
| ~~Decentralization and~~ Autonomy | Entities should have autonomy over their identity data without relying on any third party. **They must be the only one being resposible for all operations about their identity.** | Usability | 
| Verifiability ~~and Authenticity~~ | Entities should be able to reliably verify users' identities and must provide proof of the authenticity of their personal data. | Usability |

## Appendix A

A copy of the survey given to respondents at the International Workshop on Emerging Digital Identities at ARES 2024.[^ares]

![Survey part 2](survey/part2/Survey.png)

## Appendix B

Results of the first part of the Survey.

![Survey results (Local)](survey/part1/Results.png)

## References

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[^toth]: Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27. 

[^toip]: Trust Over IP Foundation. Principles of self-sovereign identity (ssi). https://trustoverip.org/wp-content/uploads/2021/10/ ToIP-Principles-of-SSI.pdf, 2024. Accessed: 2024-12-24 

[^ferdous]: Ferdous, Md Sadek, Farida Chowdhury, and Madini O. Alassafi. "In search of self-sovereign identity leveraging blockchain technology." IEEE access 7 (2019): 103059-103079.

[^pava]: Pava-Díaz, Roberto A., Jesús Gil-Ruiz, and Danilo A. López-Sarmiento. "Self-sovereign identity on the blockchain: contextual analysis and quantification of SSI principles implementation." Frontiers in Blockchain 7 (2024): 1443362.

[^bokkem]: Van Bokkem, Dirk, et al. "Self-sovereign identity solutions: The necessity of blockchain technology." arXiv preprint arXiv:1904.12816 (2019).

[^omar]: Dib, Omar, and Baha Rababah. "Decentralized identity systems: Architecture, challenges, solutions and future directions." Annals of Emerging Technologies in Computing (AETiC) 4.5 (2020): 19-40.

[^joshi]: Joshi, Ankur, et al. "Likert scale: Explored and explained." British journal of applied science & technology 7.4 (2015): 396-403.

[^microsoft]: Microsoft Forms. https://en.wikipedia.org/wiki/Microsoft_Forms, accessed on January 2nd, 2024.

[^ares]: https://www.ares-conference.eu/edid, accessed on 2nd January, 2024.
