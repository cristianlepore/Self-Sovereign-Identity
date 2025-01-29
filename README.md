# A Model To Assess Digital Identity Solutions

## Identity management

The internet was built without a trust layer, and digital identity was perceived as a patchwork to address the lack of online trust. From the early days, the design of identity models has been closely intertwined with evolving definitions of identity, with each influencing the other.

Traditional identity leverages cryptographic primitives to authenticate users to their online accounts. The information retrieval is based on the client-server paradigm, which is still today the backbone of the Internet, and ensures the establishment of a secure channel between parties. Once authenticated, identity corresponds to online accounts as *"a set of claims made by one digital subject about itself."*[^cameron]

The rise of online services and accounts has led organizations to develop identity management systems to handle authentication and authorization for various services. However, users often authenticate separately to each service, frequently reusing the same password across multiple accounts.

To streamline the management of identities, organizations deployed Identity Providers (IdPs) capable of orchestrating multiple accounts and granting users access to services within the same organization. Users could now authenticate once to access all services within the organization. In this paradigm, the definition of identity was expanded to encompass attributes from multiple accounts.

Fast forward to the spread of mobile applications, which created a market of services and Identity Providers (IdPs) loosely decoupled across different domains and organizations. In other words, services operated outside the boundaries of traditional IdPs, while classical authentication methods proved inadequate to describe the relationships between users, IdPs, and Service Providers (SPs) across different domains. As a solution, new federated protocols emerged to connect services beyond organizational boundaries, such as Kerberos, SAML, Shibboleth, OAuth, OpenID Connect, and others. A new definition of identity emerged to describe relationships and interactions with others.

The problem of trust online was solved, but at the price of giving up our data to IdPs, who constitute a bottleneck to data control. The IdPs are generally the gatekeepers of the web; big tech that create large chunks of repositories holding citizens' data.

Government concerns about data sovereignty, along with a resurgence of decentralized technology, paved the way for new policies such as the GDPR and the California Consumer Privacy Act. A new approach to identity management emerged, shaping a definition of identity based on principles that encompass individual interactions, relationships, and representation in the digital world. This paradigm, known as Self-Sovereign Identity (SSI), aims to guide the next generation of digital identity systems.

## Research questions

After nearly a decade of experimenting with SSI-related concepts, numerous scholars and working groups have contributed to defining a set of principles for SSI. However, disagreements over the precise list of principles and their vague definitions have created room for speculation. As a result, many identity systems - motivated by the growing demand for identity verification and data sovereignty - could claim adherence to self-sovereignty, with little means to prove otherwise.  

In parallel industries, an artifact to evaluate the state of the art has proven instrumental in clearing the fog of consumer expectations. For example, the food and cosmetic industry implements labeling systems to mark the quality of products. These efforts are based on previous research and nutrient ratings from academics. Evaluation frameworks have also been proposed for open-source projects to help determine whether a consumer product follows the principles of Free and Open Source Software. We will discuss further examples in the [Related Works section](#related-works).  

Past research has summarized the benefits of having an assessment model as follows: 1) designing a competitive profile of the products of interest; 2) validating their effectiveness; and 3) providing prescriptive insights on how to strengthen solutions.[^landrum]  

Confident in these benefits, we aim to strengthen the contribution of a model for assessing the adherence of e-Identity solutions to Self-Sovereign Identity (SSI),[^lepore] by expanding the literature review of past works to include 18 studies over the past 10 years that define SSI and categorize principles.  

We build on the past exercise from [^lepore] by conducting both quantitative and qualitative analyses of SSI principles, enabling us to identify the most widely agreed-upon set of principles compared to previous studies, limited to our literature review. Additionally, our review of past evaluation frameworks, discussed in the [Related Works section](#related-works), supports our decision to adopt the same research questions:

*1. RQ1: What are the principles of Self-Sovereign Identity?*
*2. RQ2: Can we assess any identity system based on these principles?*

[Section 1](definition/Definition.md) combines past works to present widely agreed-upon list of principles for Self-Sovereign Identity and categorize them using an objective method. This addresses RQ1. [Section 2](model/Model.md) introduces a model for assessing e-identity solutions, focusing on the promise of user control over information. The idea is to find an answer for RQ2. Finally, [Section 3](testing/Testing.md) explores the testing phase, where the model is applied to evaluate existing solutions in the field of identity.

## Paper structure

1. [Definition of Self-Sovereign Identity](definition/Definition.md)
2. [Model to assess e-identity solutions](model/Model.md)
3. [Testing](testing/Testing.md)

From here on, we will use the terms 'principle', 'property', and 'criterion' interchangeably to refer to the instance of the principles of SSI. The meaning will be clear to the reader based on the context, and any ambiguity will be addressed as needed. For brevity, we will also frequently abbreviate 'Self-Sovereign Identity' as SSI.

## Related works

Allen was the first to provide a list of principles for SSI in his blog post.[^allen] Since then, subsequent efforts have refined Allen's work by offering complementary lists of principles.[^ferdous][^toip][^toth] Our literature review in [Definition of Self-Sovereign Identity](definition/Definition.md) presents a rationale based on 18 contributions from scholars and working groups published over the past 10 years, which explore the definition and categorization of SSI principles. From this list, we have excluded some of these works because they have failed to describe the methodology behind their literature review, raising concerns about the effectiveness of their analysis.[^dib][^bokkem] Others did not explain how they derived their definitions for the principles, ultimately leading to a high level of subjectivity.[^pava][^omar] We believe that To derive a new list of principles based on past exercises, researchers must clearly explain their data collection process, ensuring that the results of their analysis are fully replicable by others. Conversely, we have considered lists of principles that resulted from community contributions or were derived from previous academic works, such as the study in [^cucko].

Regardig the [Model to assess e-identity solutions](model/Model.md), our literature review revealed only a scattered selection of papers addressing digital identity systems based on the promises of SSI. A comprehensive list of the reviewed literature is provided in [Section 2](model/Model.md). To complement existing works on identity, we explored additional evaluation frameworks from diverse fields, by examining three specific cases: (1) open-source projects, (2) nutrient profiling scales, and (3) the Where-to-be-born Index (formerly the Country Quality-of-Life Index). Although not directly related to digital identity, the purpose of this review is to identify whether a general rule of thumb exists for designing evaluation models.We selected these three cases because they incorporate intangible aspects such as the political impact of software, cultural influences on food and products, and considerations of individual freedom and happiness. However, we acknowledge that other rating systems exist in various domains, such as university rankings, cost of living indices, and more.

*1. FOSS projects*
FOSS (Free and Open Source Software) projects are software initiatives where the source code is made publicly available for anyone to view, use, modify, and distribute.[^fortunato] Over the years, FOSS projects have become synonymous with transparency, collaboration, and community-driven development. Some well-known FOSS projects include Linux distributions, LibreOffice, GIMP, Blender, and VLC. These software projects adhere to the principles of openness, transparency, and community-driven development promoted by FOSS. In parallel, a recent trend has emerged where vendors distribute software for free, while consumers later pay fees to unlock additional functionalities. Many mobile apps operate in this way. Despite being free, and sometimes even open source, some of these software products may not fully adhere to FOSS principles. This can lead to confusion and mislead customers. An evaluation framework helps distinguish between projects that embrace the FOSS philosophy and those that do not.

Empirical studies have evaluated FOSS projects using predefined criteria. These criteria have been applied to assess individual projects,[^foss] with much of the research focusing on converting them into quantitative parameters that can be easily measured. For instance, the OpenMRS project evaluates GitHub projects using metrics such as the number of commits, the number of contributors, and the reliability of contributors. A score-based rubric is then used to assign points to these parameters, which are summed up to obtain an overall score for any given open-source project.[^foss_rubric]

In contrast to the criteria-based approach, other projects determine the suitability of FOSS initiatives by addressing a list of questions to a broader audience. Questions are categorized into three groups: project viability, approachability, and suitability. A qualitative analysis of the responses assigns scores to these categories, thus providing an overall assessment of the project.[^hunter] The majority of contributions focus on the types of questions and their categorizations. For example, an alternative method categorizes questions into critical and non-critical (or secondary) questions.[^heidi][^evaluation_activity]

The OpenBRR (Open Business Readiness Rating) model provides a more fine-grained evaluation by gathering data across ten categories and assessing specific criteria for each category. Each criterion is weighted on a scale from 1 to 5, based on past research studies, and the scores are summed up. The uniqueness of this model lies in its flexibility and adaptability; depending on the intended use of the software, adopters can assign different weights to the categories. Thus, not all categories carry the same weight. In certain scenarios, some categories may be excluded entirely from the final rating, allowing for a tailored evaluation process.

A similar approach is used by the Qualification and Selection of Open Source Software (QSOS),[^evaluating_foss] which calculates a final score through four iterative steps that can be applied with varying levels of detail. In the first step, evaluation criteria are established across three primary axes: functionality, license compliance, and community dynamics. Then, each criterion is assigned a score between 0 and 2, based on responses from candidates participating in a survey. These scores are weighted to reflect the specific context and requirements of the intended software use. Finally, a competitive profile is created by comparing results across multiple candidate projects. A dedicated QSOS tool visualizes the outcomes, often using charts for easier comparison. A popular visualization format is the Kiviat chart, which enables graphical comparisons of evaluation results.

A radically different approach from the aforementioned examples is the OSSpal project,[^Wasserman] which helps companies, government agencies, and other organizations find high-quality free and open-source software that fits their needs. OSSpal operates a publicly available website where users can review projects, and it ranks projects based on individual user reviews.

*2. Nutrient profile models*
Nutrient profiling is the science of classifying foods based on their nutritional composition to promote health and prevent disease.[^scarborough] It is useful in various contexts, including the regulation of food labeling, food advertising, and food vending. Selecting an appropriate evaluation model for food policy decisions is crucial, as different models can lead to varying classifications of the same food. Nutrient profiling can categorize foods into two or more groups based on one or more nutritional characteristics. The following list presents a non-exhaustive selection of nutrient profile models, identified using the meta-search engine Google Scholar with the query: "Survey" AND "nutrient profile model." The objective is not to provide a comprehensive analysis of all methods but to explore how common rating systems address the assessment of food and cosmetic products.

**WXYfm model.** The WXYfm model is the foundation of the European Nutri-Score system, a five-color nutrition label designed to guide consumers in purchasing food and cosmetic products by assigning a letter from A (best) to E (worst) to each product.[^arambepola] The model allocates points and classifies foods and drinks into healthiness categories through a two-step process. In the first step, points are assigned based on the content of unhealthy nutrients, including energy, saturated fats, sugars, and sodium, with each nutrient contributing up to 10 points, based on intake values from the Guideline Daily Amounts.[^rayner] These points are derived from criteria established by the Codex Alimentarius Commission. In the second step, points for beneficial nutrients such as protein, fiber, fruit, and vegetables are summed, and the total score is calculated by subtracting the points of the second group from the first.

**SAIN,LIM model.** The SAIN-LIM nutrient profiling model combines two indicators: the Nutrient Density Score (NDS) and the LIM score, which accounts for disqualifying nutrients (i.e., nutrients to be limited). The SAIN component evaluates five nutrients and calculates the unweighted arithmetic mean of the percentage adequacy based on the WXYfm model. Conversely, the LIM score represents the mean percentage of the maximal recommended values for three nutrients. The results are presented on a two-axis chart, displaying four quadrants to provide a clear indication of a product's healthiness.

*3. Where-to-be-born Index*
The Where-to-be-born Index assesses the most favorable conditions for leading a healthy, secure, and prosperous life in a given country. It combines data from a life-satisfaction survey with measurable quality-of-life parameters. For the survey component, researchers identified eleven statistically significant indicators, with participants responding to a series of statements about their lives using a Likert scale, which is explained in [Section 1](definition/Definition.md). Meanwhile, the measurable parameters are evaluated by assigning weights based on their relative importance.[^khoury] The final scores for each country are computed by combining these weighted factors. Countries with higher scores are considered to provide greater opportunities for a healthy, educated, and prosperous life.

However, the methodology for aggregating scores has been the subject of extensive debate. Common approaches include weighted and unweighted arithmetic means, as used in the City Development Index (CDI), the Environmental Sustainability Index (ESI), and the Environmental Vulnerability Index (EVI). Other indices, such as the Human Development Index (HDI), employ the geometric mean, while the Youth Welfare Index utilizes Data Envelopment Analysis, and Bhutan's Gross National Happiness Index applies the Alkire-Foster method.

### Discussion on the related works

Although different evaluation frameworks operate under varying conditions and contexts, our analysis suggests some shared methodologies across them. First, most studies establish criteria as the foundation for their models and use these criteria to formulate questions. These questions are then converted into parameters for evaluation. For the evaluation of these parameters, some studies employ qualitative analysis, while others rely on quantitative analysis. Qualitative analysis can introduce biases, depending on the type of questions posed, the target audience, and the size of the sample. These factors must be clearly defined at the outset of the research; failure to do so can undermine the results. A quantitative analysis, instead, requires the definition of a precise set of parameters that can be measured, which in some fields can be tricky to figure out. In our research, we opted for a quantitative analysis, using a survey solely to refine our findings. We found the concept of presenting results in a Kiviat chart, as proposed by the QSOS software project, to be extremely valuable in showcasing our results.

## References

[^rayner]: Rayner, Mike, Peter Scarborough, and Carol Williams. "The origin of Guideline Daily Amounts and the Food Standards Agency's guidance on what counts as ‘a lot’and ‘a little’." Public Health Nutrition 7.4 (2004): 549-556.

[^khoury]: Khoury, Alexander. "Jad Chaaban, Alexandra Irani &."

[^merz]:Merz, Benedikt, et al. "Nutri-Score 2023 update." Nature Food 5.2 (2024): 102-110.

[^scarborough]: Scarborough, Peter, et al. "Testing nutrient profile models using data from a survey of nutrition professionals." Public health nutrition 10.4 (2007): 337-345.

[^arambepola]: Arambepola, Carukshi, Peter Scarborough, and Mike Rayner. "Validating a nutrient profile model." Public health nutrition 11.4 (2008): 371-378.

[^yuka_rating]: How are food products rated?, Accessed on 13 January 2025. https://help.yuka.io/l/en/article/ijzgfvi1jq-how-are-food-products-scored

[^yuka]: Make the right choices for your health, accessed on 13 January 2025. https://yuka.io/en/

[^dehinbo]: Dehinbo, Kehinde, Pieter Pretorius, and Johnson Dehinbo. "Strategic analysis towards deriving competitive advantage with the use of FOSS: the case of a South African university." 2012 Ninth International Conference on Information Technology-New Generations. IEEE, 2012.

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^hunter]: Accessed on January 10 2025. https://www.cs.hunter.cuny.edu/~sweiss/course_materials/cs_ossd/assignments/assignment_10_project_evaluation.pdf

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^bokkem]: Van Bokkem, D., Hageman, R., Koning, G., Nguyen, L., & Zarin, N. (2019). Self-sovereign identity solutions: The necessity of blockchain technology. arXiv preprint arXiv:1904.12816.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^fortunato]: Fortunato, Laura, and Mark Galassi. "The case for free and open source software in research and scholarship." Philosophical Transactions of the Royal Society A 379.2197 (2021): 20200079.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[^toth]: Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27. 

[^dib]:Dib, O., & Rababah, B. (2020). Decentralized identity systems: Architecture, challenges, solutions and future directions. Annals of Emerging Technologies in Computing (AETiC), 4(5), 19-40.

[^wikipedia_foss_projects]: Wikipedia FOSS projects, accessed on 10 January 2025. https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities

[^toip]: Trust Over IP Foundation. Principles of self-sovereign identity (ssi). https://trustoverip.org/wp-content/uploads/2021/10/ ToIP-Principles-of-SSI.pdf, 2024. Accessed: 2024-12-24 

[^evaluation_activity]:Project Evaluation Activity V1, accessed on 8th January 2025, http://foss2serve.org/index.php?title=Project_Evaluation_Activity_V1&redirect=no

[^ferdous]: Ferdous, Md Sadek, Farida Chowdhury, and Madini O. Alassafi. "In search of self-sovereign identity leveraging blockchain technology." IEEE access 7 (2019): 103059-103079.

[^foss]: FOSS2Serve. (n.d.). Project Evaluation (Activity). Retrieved January 9, 2025, from http://foss2serve.org/index.php/Project_Evaluation_(Activity)

[^foss_rubric]: Project Evaluation Rubric (Activity), accessed on 8th January 2025, http://foss2serve.org/index.php/Project_Evaluation_Rubric_(Activity) 

[^pava]: Pava-Díaz, Roberto A., Jesús Gil-Ruiz, and Danilo A. López-Sarmiento. "Self-sovereign identity on the blockchain: contextual analysis and quantification of SSI principles implementation." Frontiers in Blockchain 7 (2024): 1443362.

[^bokkem]: Van Bokkem, Dirk, et al. "Self-sovereign identity solutions: The necessity of blockchain technology." arXiv preprint arXiv:1904.12816 (2019).

[^omar]: Dib, Omar, and Baha Rababah. "Decentralized identity systems: Architecture, challenges, solutions and future directions." Annals of Emerging Technologies in Computing (AETiC) 4.5 (2020): 19-40.

[^cucko]:Čučko, Š., Bećirović, Š., Kamišalić, A., Mrdović, S., & Turkanović, M. (2022). Towards the classification of self-sovereign identity properties. IEEE access, 10, 88306-88329.

[^joshi]: Joshi, Ankur, et al. "Likert scale: Explored and explained." British journal of applied science & technology 7.4 (2015): 396-403.

[^microsoft]: Microsoft Forms. https://en.wikipedia.org/wiki/Microsoft_Forms, accessed on January 2nd, 2024.

[^ares]: https://www.ares-conference.eu/edid, accessed on 2nd January, 2024.

[^onion]: The Onion Model of FOSS Development, https://medium.com/@deprasadini/evaluation-of-free-open-source-software-foss-371306d94b1f, accessed on 8th January 2025.

[^foss_project]: I hire people to work on a FOSS project. Here's how I evaluate GitHub profiles, https://ondsel.com/blog/evaluating-github-profile/, accessed on 8th January, 2025.

[^Wasserman]: Wasserman, Anthony I., et al. "OSSpal: finding and evaluating open source software." Open Source Systems: Towards Robust Practices: 13th IFIP WG 2.13 International Conference, OSS 2017, Buenos Aires, Argentina, May 22-23, 2017, Proceedings 13. Springer International Publishing, 2017.

[^evaluating_foss]: Evaluating FOSS, accessed on 12 January 2025. https://jgbarah.gitbooks.io/evaluating-foss-projects/content/evaluation_models.html

[^heidi]: Heidi J.C. Ellis, Michelle Purcell, and Gregory W. Hislop. An approach for evaluating foss projects
for student participation. In Proceedings of the 43rd ACM Technical Symposium on Computer Science
Education, SIGCSE ’12, pages 415–420, New York, NY, USA, 2012. ACM

[^alami]: Alami, Adam, Marisa Leavitt Cohn, and Andrzej Wąisowski. "How do foss communities decide to accept pull requests?." Proceedings of the 24th International Conference on Evaluation and Assessment in Software Engineering. 2020.

[^cameron]: Cameron, K. (2005). The laws of identity. Microsoft Corp, 12, 8-11.

[^landrum]: Landrum, R. E., Turrisi, R., & Harless, C. (1999). University image: the benefits of assessment and modeling. Journal of marketing for Higher Education, 9(1), 53-68.
