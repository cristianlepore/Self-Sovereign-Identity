# A Model To Assess Digital Identity Solutions

## History

Traditional identity management relied on cryptographic primitives that allowed users to authenticate themselves to their online accounts. Information retrieval was based on a client-server paradigm, which established secure communication between parties. This paradigm remains prevalent in older systems and in other systems where users need to access to multiple accounts and services, requiring each individual to authenticate separately to each service provider. Despite its simplicity, a more efficient architectural approach involves deploying an Identity Provider (IdP) as an intermediary between users and services. The IdP orchestrates access to services and manages authentication across multiple service providers with a single login.

When services and identity providers are loosely decoupled across different domains, federated identity systems emerge to transcend local boundaries, linking entities across domains. The traditional client-server paradigm with secure channel establishment proved inadequate for this task. To address the challenges of loosely coupled entities, protocols were developed in the late 2000s to extend the client-server paradigm, enabling federation between services and identity providers. First came Kerberos, followed by widely adopted protocols such as SAML, OAuth, and OIDC, which remain in use today.

Since 2016, a new approach to identity management has gained traction, emphasizing principles that include individual interactions, their representation in the world, and how others perceive their identity. This paradigm, known as Self-Sovereign Identity (SSI), serves as a blueprint for the next generation of digital identity systems.

## Research questions

Despite nearly a decade of experimentation with the SSI concept and related technologies, its definition remains elusive. The lack of a clear definition has led to misunderstandings about SSI's role within existing identity models and opened the door to speculation. In many industries, a model to rate the state-of-the-art is instrumental to clear the fog in a specific field of study, and we witnessed the development of methods to evaluate open source projects, classifying the nutritional value of food and cosmetics, as well as to provide indexes for the country quality of life index. Clearing the fog in a narrowed field like Self-Sovereign Identity is important to clarify the quality of identity management systems and to distinguish between effective and flawed implementations of Self-Sovereign Identity. For this purpose, we aim to extend the contribution of a model for assessing the adherence of e-Identity solutions to Self-Sovereign Identity (SSI), previously introduced in [^lepore], by addressing the following research questions:

*1. RQ1: What are the principles of Self-Sovereign Identity?*

*2. RQ2: Can we use these principles to assess any SSI system?*

[Section 1](definition/Definition.md) proposes a definition of Self-Sovereign Identity and addresses RQ1, while [Section 2](model/Model.md) leverages this definition to propose a model for assessing e-identity solutions. Finally, [Section 3](testing/Testing.md) delves into a testing stage where the model is tested against existing solutions in the field of identity.

## Paper structure

1. [Definition of Self-Sovereign Identity](definition/Definition.md)
2. [Model to assess e-identity solutions](model/Model.md)
3. [Testing](testing/Testing.md)

Hereafter, we use the term principles for SSI interchangeably with the terms property and features. For the sake of clarity, they will all refer to the same concept. We often abbreviate the term Self-Sovereign Identity as SSI.

## Related works

This work is inspired by past exercises that define SSI principles[^allen][^ferdous][^toip][^toth]. However, we depart from previous contributions because the scope of our analysis is instrumental in developing a model to assess identity solutions based on the promise of user control over information. While this is not the first contribution aimed at assessing the quality of identity systems, other SSI-based assessments have either failed to describe their methodology[^pava], lacked extensive precision in their analysis[^bokkem], or did not explain how they derived the criteria for their system analysis[^omar]. For this reason, we make it clear that our list of principles is consistent with past exercises from the literature. Furthermore, the exercise we conducted is fully replicable, as we employed an objective method to select properties and categorize them. We exaplained it step-by-step. Finally, a qualitative analysis is conducted through a survey with experts participating in the ARES conference 2024 to refine our results.

Regarding RQ2, struggling to find similar examples in the field of identity, we examined different approaches to address our research questions by analyzing three different examples from (1) open-source projects, (2) nutrient profiling scales, and we studied the (3) Where-to-be-born Index (formerly the Country Quality-of-Life Index). While rating systems exist even in other fields, such as University Ranking or cost of living, we study three examples in the fields of engineering, science, and social indicators of human welfare, because, to some extent, they all include intangible aspects such as the political impacts of software, cultural aspects of food and products, individual freedom, and happiness. At the same time, measuring them requires defining metrics. Hence, our purpose is to understand the rationale that grounds some of the decisions made by designers when developing a rating model. It is not the purpose of this article to describe them deeply; rather, it is about finding a rule of thumb for the concepts that tackle their works.

*1. FOSS projects evaluation*
Wikipedia has a comparison of source code hosting sites at [^wikipedia_foss_projects]. The point is that there are many different places to look for projects. Empirical studies define criteria for the evaluation of FOSS projects and solicits these criteria to forge specific ways to evaluate each project.[^foss] OpenMRS make use of the work in [^foss] to evaluate projects on GitHub. The appropriateness of a project is determined, for the most part, by the answers to a set of important questions.[^hunter] Some of these questions are more important than others in terms of whether the project is a good choice or not. Some researchers in this field have even suggested that the questions that should be asked fall into three categories related to the project: viability, approachability, and suitability,[^heidi] and that some should be tagged as critical whereas others are not as critical and are tagged as secondary. For example, the Project Evaluation Rubric uses a score-based system to evaluate Free and open source projects,[^foss_rubric] while the work in [^evaluation_activity] defines principles and split them into two subclasses: mission critical criteria (primary) and secondary criteria. These criteria are later tested against the evaluation of student participation within the Mifos project. An Onion model for the development of FOSS projects emphasizes the roles and interactions of the community in FOSS.[^onion] Using the Onion model, users have a comprehensive understanding of the community-driven development process. The blog post on[^foss_project] describes methods to evaluate the contribution of developers on free and open code. Finally, Alami [^alami] proposed a qualitative method with experts interviews to define criteria to evaluate weather a pull request should be accepted in an open source projects.

Other attempts to quantitatively evaluate the contribution of open source projects is proposed by the OpenBRR (Open Business Readiness Rating), as an evaluation method that provides an objective manner to assess community-driven projects. The Open BRR offers a way to measure the readiness of a project to be deployed in a business environment. At this regard, the evaluation involves a multi-step process that can be adjusted by the evaluator to adapt the assessment to the specific needs of the organization that wants to deploy the software under study. A quantitative analysis is based on gathering metrics and factual data on ten categories, and in each category, a set of criteria and metrics are proposed. The first step in the process is to select and weight criteria to be use in the evaluation process. In the following step, each criteria is evaluated on its own. Inputs are then weighted and each category is given a rating ranging from 1 to 5. In order to obtain a total score for the functionality criteria, the total weights of the standard functionality items is summed up in W. Then, depending on the final usage the software, adopters may even weight the categories, thus obtaining the overall rating for the project. Then the score for the assessed tool is obtained by adding all the scores, both from the standard and extended functionality. As we may understand, not all categories are weighted equally, or for some scenarios a category may not be considered at all for the final rating.

The Qualification and Selection of Open Source Software (QSOS) is a structured methodology designed to evaluate software projects systematically.[^evaluating_foss] It includes a defined workflow and a suite of tools to facilitate the evaluation process. The QSOS process is divided into four iterative steps, which can be applied with varying levels of granularity.The first step involves defining evaluation criteria across three key axes: functionality, license compliance, and community dynamics. In the second step, projects are evaluated by assigning a score between 0 and 2 to each criterion. These scores are then weighted based on the specific context and requirements for the intended use of the software. The final step is the selection of the most suitable software solution, achieved by comparing the results of multiple candidate projects. The outcomes of the QSOS process can be visualized and compared graphically, with one popular format being a radar chart.

A last example in the field of open source that combines qualitative and quantitative evaluation is given by the OSSpal project,[^Wasserman] which is aimed at helping companies, government agencies, and other organizations find high-quality free and open-source software that meets their needs. Instead of a purely numeric calculated score, OSSpal adds curation of high-quality FOSS projects and individual user reviews of these criteria. OSSpal has an operational, publicly available website where users may search by project name or category and enter ratings and reviews for projects.

*2. Nutrient profile models*
Nutrient profiling, also known as nutritional profiling, is the science of classifying or ranking foods by their nutritional composition in order to promote health and prevent disease.[^scarborough] It is worth in different circumstances, from the regulation of food labelling, food advertising, and vending of foods. The Yuka app is an example of an application that guides consumers in the identification of nutritional values.[^yuka]

The Yuka app relies on a number of nutrient profiling models developed by academics, health organizations, national governments, and the food industry. The selection of a model to use in food policy decisions is important, as different models can lead to different classifications of the same foods. For example, nutrient profiling can divide foods into two or more groups and categorize groups as healthier than others on the basis of one or more nutritional characteristics. The following list is a non-exhaustive set of nutrient profile models gathered from a literature review on Google Scholar with the following search query: "Survey" AND "nutrient profile models." The purpose is not to have a comprehensive analysis of methods, rather to understand how the most common models address the issue of assessing food and cosmetic products.

**WXYfm model.** The WXYfm model allocates points and classifies foods and drinks into healthiness categories. The classification works in several steps. In the first step, it accounts for unhelthy nutrients by summing up points for energy, saturated fats, sugars, and sodium. Each nutrient accounts for a maximum of 10 points, where the threashold is based on the intake of nutrients that an average man and woman should consume during the day, as for the Guideline Daily Amounts.[^rayner] These four nutrients are the key nutrients consumers should consider when looking at the nutrition label, and their rationale is based on heuristics from [^rayner], while points for defining "a lot" and "a little" were derived from the criteria of the Codex Alimentarius Commission. For each nutrient, the WXYfm model sets points as defined in the research work from Rayner [^rayner]. This concludes the first step.

In the second step, points for protein, fibre, fruit, vegetables are summing up. The total score is then computed by subtracting points from iof the second group of nutrients from the first. At this point, the total score is within a category as healthy or less healthy.

The WXYfm model is at the basis of the European Nutri-Score system, a five-colour nutrition label that aims to guide consumers in buying food and cosmetics products by assigning products a rating letter from A (best) to E (worst), with associated colours from green to red.[^arambepola] In turn, the Nutri-Score system underpins the food ranking used by many food rating apps.

**SAIN,LIM model.** The SAIN-LIM nutrient profiling model is based on two indicators: the Nutrient Density Score (NDS), for qualifying nutrients (i.e., positive nutrients), and the LIM score, for disqualifying nutrients (i.e., nutrients to be limited). The SAIN considers five nutrients and calculate the unweighted arithmetic mean of the percentage adequacy based on the French and European nutritional recommendations (the Eurodiet Core Report, 2000); on the other hand, the LIM score is the mean percentage of the maximal recommended values for three nutrients. Results are then presented within a two-axis chart of SAIN and LIM that displays four 'quadrants.' This aims to provide a clear indication of the healthiness of a product.

*3. Where-to-be-born Index*
The Where-to-be-born Index assesses which country offers the most favorable conditions for a healthy, secure, and prosperous life. It combines results from subjective life-satisfaction surveys with objective determinants of quality of life across countries.

For the life satisfaction scores, researchers identified 11 statistically significant indicators. A common method for calculating this index is through the Satisfaction With Life Scale (SWLS), developed by Diener in 1985. In that scale, participants respond to a series of statements about their life using a Likert scale, as described in [Section 1](definition/Definition.md).

The objective part of the index is calculated using various indicators, each assigned a weight based on its importance as rated by users or experts.[^khoury] Scores for each country are then determined by combining these weighted factors.

There is ongoing debate about the best methods to scale, normalize, weight, and aggregate scores for sustainable development indices. These steps are necessary to make different criteria comparable and combine them into a single index. Common methods include using a weighted or unweighted arithmetic mean, as seen in the City Development Index (CDI), the Environmental Sustainability Index (ESI), the Environmental Vulnerability Index (EVI), and the Well-being Index. While equal weights are often used, some indices rely on expert feedback or techniques like principal component analysis. Other methods, such as the geometric mean for the Human Development Index (HDI), Data Envelopment Analysis for the Youth Welfare Index, and the Alkire-Foster method for Bhutan's Gross National Happiness Index, have also been employed.

Countries with higher scores are considered better places to "be born," offering greater opportunities for a healthy, educated, and prosperous life. The index ranks countries based on these scores, highlighting those with the best overall living conditions.

## References

[^rayner]: Rayner, Mike, Peter Scarborough, and Carol Williams. "The origin of Guideline Daily Amounts and the Food Standards Agency's guidance on what counts as ‘a lot’and ‘a little’." Public Health Nutrition 7.4 (2004): 549-556.

[^khoury]: Khoury, Alexander. "Jad Chaaban, Alexandra Irani &."

[^merz]:Merz, Benedikt, et al. "Nutri-Score 2023 update." Nature Food 5.2 (2024): 102-110.

[^scarborough]: Scarborough, Peter, et al. "Testing nutrient profile models using data from a survey of nutrition professionals." Public health nutrition 10.4 (2007): 337-345.

[^arambepola]: Arambepola, Carukshi, Peter Scarborough, and Mike Rayner. "Validating a nutrient profile model." Public health nutrition 11.4 (2008): 371-378.

[^yuka_rating]: How are food products rated?, Accessed on 13 January 2025. https://help.yuka.io/l/en/article/ijzgfvi1jq-how-are-food-products-scored

[^yuka]: Make the right choices for your health, accessed on 13 January 2025. https://yuka.io/en/

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^hunter]: Accessed on January 10 2025. https://www.cs.hunter.cuny.edu/~sweiss/course_materials/cs_ossd/assignments/assignment_10_project_evaluation.pdf

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[^toth]: Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27. 

[^wikipedia_foss_projects]: Wikipedia FOSS projects, accessed on 10 January 2025. https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities

[^toip]: Trust Over IP Foundation. Principles of self-sovereign identity (ssi). https://trustoverip.org/wp-content/uploads/2021/10/ ToIP-Principles-of-SSI.pdf, 2024. Accessed: 2024-12-24 

[^evaluation_activity]:Project Evaluation Activity V1, accessed on 8th January 2025, http://foss2serve.org/index.php?title=Project_Evaluation_Activity_V1&redirect=no

[^ferdous]: Ferdous, Md Sadek, Farida Chowdhury, and Madini O. Alassafi. "In search of self-sovereign identity leveraging blockchain technology." IEEE access 7 (2019): 103059-103079.

[^foss]: FOSS2Serve. (n.d.). Project Evaluation (Activity). Retrieved January 9, 2025, from http://foss2serve.org/index.php/Project_Evaluation_(Activity)

[^foss_rubric]: Project Evaluation Rubric (Activity), accessed on 8th January 2025, http://foss2serve.org/index.php/Project_Evaluation_Rubric_(Activity) 

[^pava]: Pava-Díaz, Roberto A., Jesús Gil-Ruiz, and Danilo A. López-Sarmiento. "Self-sovereign identity on the blockchain: contextual analysis and quantification of SSI principles implementation." Frontiers in Blockchain 7 (2024): 1443362.

[^bokkem]: Van Bokkem, Dirk, et al. "Self-sovereign identity solutions: The necessity of blockchain technology." arXiv preprint arXiv:1904.12816 (2019).

[^omar]: Dib, Omar, and Baha Rababah. "Decentralized identity systems: Architecture, challenges, solutions and future directions." Annals of Emerging Technologies in Computing (AETiC) 4.5 (2020): 19-40.

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