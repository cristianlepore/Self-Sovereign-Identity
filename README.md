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

With respect to RQ1, this work is inspired by past exercises that define SSI principles[^allen][^ferdous][^toip][^toth]. However, we depart from previous contributions because the scope of our analysis is instrumental in developing a model to assess identity solutions based on the promise of user control over information. While this is not the first contribution aimed at assessing the quality of identity systems, other SSI-based assessments have either failed to describe their methodology[^pava], lacked extensive precision in their analysis[^bokkem], or did not explain how they derived the criteria for system analysis[^omar]. We make it clear that our list of principles is consistent with past exercises from the literature. Furthermore, the exercise we conducted is fully replicable, as we employed an objective method to select properties and categorize them. Additionally, a survey was conducted among experts participating in the ARES conference 2024 to refine our results.

Regarding RQ2, we examined different approaches to address our research questions by analyzing three examples from distinct fields: (1) open-source projects, (2) nutrient profiling, and (3) country Quality-of-Life index. While rating systems exist in other fields, for example University Ranking, we study three examples in the field of software engineering, science, and social indicators of human welfare. We chose these three because all of them may, to some extent, include intangibles aspects such as political impacts of software, culturale aspects of food and products, individual freedom, etc. While measuring them is tricky, some of these aspects deserve to be considered of left off when defining a rating system. In our case, we aim to learn the rationale that ground some of the decition taken by designers when developing a rating model. It is not the purpose of this article to describe them deeply, rather we enlist some of the concepts that ground their work.

*1. FOSS projects evaluation*
Wikipedia has a comparison of source code hosting sites at [^wikipedia_foss_projects]. The point is that there are many different places to look for projects. Empirical studies define criteria for the evaluation of FOSS projects and solicits these criteria to forge specific ways to evaluate each project.[^foss] OpenMRS make use of the work in [^foss] to evaluate projects on GitHub. The appropriateness of a project is determined, for the most part, by the answers to a set of important questions.[^hunter] Some of these questions are more important than others in terms of whether the project is a good choice or not. Some researchers in this field have even suggested that the questions that should be asked fall into three categories related to the project: viability, approachability, and suitability,[^heidi] and that some should be tagged as critical whereas others are not as critical and are tagged as secondary. For example, the Project Evaluation Rubric uses a score-based system to evaluate Free and open source projects,[^foss_rubric] while the work in [^evaluation_activity] defines principles and split them into two subclasses: mission critical criteria (primary) and secondary criteria. These criteria are later tested against the evaluation of student participation within the Mifos project. An Onion model for the development of FOSS projects emphasizes the roles and interactions of the community in FOSS.[^onion] Using the Onion model, users have a comprehensive understanding of the community-driven development process. The blog post on[^foss_project] describes methods to evaluate the contribution of developers on free and open code. Finally, Alami [^alami] proposed a qualitative method with experts interviews to define criteria to evaluate weather a pull request should be accepted in an open source projects.

Other attempts to quantitatively evaluate the contribution of open source projects is proposed by the OpenBRR (Open Business Readiness Rating), as an evaluation method that provides an objective manner to assess community-driven projects. The Open BRR offers a way to measure the readiness of a project to be deployed in a business environment. At this regard, the evaluation involves a multi-step process that can be adjusted by the evaluator to adapt the assessment to the specific needs of the organization that wants to deploy the software under study. A quantitative analysis is based on gathering metrics and factual data on ten categories, and in each category, a set of criteria and metrics are proposed. The first step in the process is to select and weight criteria to be use in the evaluation process. In the following step, each criteria is evaluated on its own. Inputs are then weighted and each category is given a rating ranging from 1 to 5. In order to obtain a total score for the functionality criteria, the total weights of the standard functionality items is summed up in W. Then, depending on the final usage the software, adopters may even weight the categories, thus obtaining the overall rating for the project. Then the score for the assessed tool is obtained by adding all the scores, both from the standard and extended functionality. As we may understand, not all categories are weighted equally, or for some scenarios a category may not be considered at all for the final rating.

The Qualification and Selection of Open Source Software (QSOS) is a structured methodology designed to evaluate software projects systematically.[^evaluating_foss] It includes a defined workflow and a suite of tools to facilitate the evaluation process. The QSOS process is divided into four iterative steps, which can be applied with varying levels of granularity.The first step involves defining evaluation criteria across three key axes: functionality, license compliance, and community dynamics. In the second step, projects are evaluated by assigning a score between 0 and 2 to each criterion. These scores are then weighted based on the specific context and requirements for the intended use of the software. The final step is the selection of the most suitable software solution, achieved by comparing the results of multiple candidate projects. The outcomes of the QSOS process can be visualized and compared graphically, with one popular format being a radar chart.

A last example in the field of open source that combines qualitative and quantitative evaluation is given by the OSSpal project,[^Wasserman] which is aimed at helping companies, government agencies, and other organizations find high-quality free and open-source software that meets their needs. Instead of a purely numeric calculated score, OSSpal adds curation of high-quality FOSS projects and individual user reviews of these criteria. OSSpal has an operational, publicly available website where users may search by project name or category and enter ratings and reviews for projects.

*2. Nutrient profile models*
Nutrient profiling, also nutritional profiling, is the science of classifying or ranking foods by their nutritional composition in order to promote health and prevent disease.[^scarborough] It can be used in a range of different circumstances including the regulation of food labelling, food advertising and vending of foods. A common use of nutrient profiling is in the creation of nutritional rating systems to help consumers identify nutritious food in a simple manner. The Yuka app is an example of application that guides consumers in the identitfication of nutritional values.[^yuka]

A variety of nutrient profile models have been developed by academics, health organizations, national governments and the food industry. The development or selection of a model to use in food policy decisions is important, as different models can lead to different classifications of the same foods. Some of these methods serve to ground nutritional score systems like the Nutri-Score adopted in many European countries.[^merz] Although their predictive validity in relation to chronic disease has yet to be demonstrated, they constitute valid examples about the design and testing of food classification. 

Nutrient profile models can categorise foods in a variety of ways. One way is to divide foods into two or more groups and to categorise groups as healthier than others on the basis of one or more nutritional characteristics of the foods. Another approach is to rank foods from the most healthy to least healthy, again using one or more nutritional characteristics of the food. The following list is a non-exhaustive set of nutrient profile models gathered from a literature review from google scholar by searching for: "Survey" AND "nutrient profile models." The purpose is not to have a comprehensive analysis of methods, rather to understand how the most common models address the issue to assess food and cosmetics products.

**WXYfm model.** The model first allocates points on the basis of the nutritional content per 100g of the food or drink. Foods and drinks are then classified into healthiness categories.

In the first step, "A" points are calculated by summing up points for energy, saturated fats, sugars, and sodium. A maximum of 10 points can be scored for each nutrient and the individual nutrient thresholds are derived from the Guideline Daily Amounts.[^rayner] The Guideline Daily Amount is based on the intake of nutrient that an avarage man and woman has to take during the day. The reason of the previous four nutrients is because these were the main nutrients that consumers should focus on when looking at the nutrition label (despite the EU directive provides a longer format for nutrition labelling). The paper in [^rayner] provides the rationale for some of the heuristics and decisions taken when defining the threashold for nutrients. They also based these facts on the Food Advisory Committee, the UK government agency for food advisory. They also defined a numeric cut points for a lot and a little. A source of figures was the criteria for nutrition claims that had been developed by the FAC or were being developed by the Codex Alimentarius Commission. At this point, the WXYfm model sets points for threashold deined in [^rayner].

In the second step of the WXYfm model, "C" points are calculated by summing up points for protein non-starch polysaccharide (NSP) fibre, fruit, vegetable and nuts. This time, a maximum of 5 points can be scored for each nutrient/food component. The total score is computed by subtracting scores from A and C, and then based on the final score, a food or drink is categorized as healthy or less healthy.

Finally, the WXYfm model is at the base of the Nutri-Score system, a five-colour nutrition label that aims to guide consumers in the buying of food and cosmetics products by assigning products a rating letter from A (best) to E (worst), with associated colors from green to red.[^arambepola] In turn, the Nutru-score system grounds the food ranking of the Yuka app.[^yuka_rating]

**SAIN,LIM model.** The SAIN,LIM nutrient profiling model is based on two indicators: the Nutrient Density Score (NDS), for qualifying nutrients (i.e. positive nutrients), and the LIM score, for disqualifying nutrients (i.e. the nutrient to be limited). Thresholds instead are defined for each of these sub-indicators to define four healthiness categories. On the one hand, the SAIN score is an un-weighted arithmetic mean of the percentage adequacy for five positive nutrients, on the other hand, the LIM score is the mean percentage of the maximal recommended values for three nutrients. In both cases, the percentage of adequacy is based on French and European (the Eurodiet Core Report, 2000) nutritional recommendations. Results are then rendered within a two axis chart of SAIN and LIM that display four 'quadrants.'

Although further nutrient models exist, they all ground on past research exercises to determine the threashold for food or the points to assign. In corner cases, these works are based on surveys of experts to tune values.

*3. Quality of life index*
Have you ever asked yourself which country is the best, and what parameter to use when ranking countries.


## References

[^rayner]: Rayner, Mike, Peter Scarborough, and Carol Williams. "The origin of Guideline Daily Amounts and the Food Standards Agency's guidance on what counts as ‘a lot’and ‘a little’." Public Health Nutrition 7.4 (2004): 549-556.

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