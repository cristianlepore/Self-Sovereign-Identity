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

1. [Definition of Self-Sovereign Identity](definition/Definition.md) [togliere la survey, e mettere i veri risultati.]
2. [Model to assess e-identity solutions](model/Model.md)
3. [Testing](testing/Testing.md)

Hereafter, we use the term principles for SSI interchangeably with the terms property and features. For the sake of clarity, they will all refer to the same concept. We often abbreviate the term Self-Sovereign Identity as SSI.

## Related works

This work is inspired by past exercises that define SSI principles[^allen][^ferdous][^toip][^toth]. However, we depart from previous contributions because the scope of our analysis is to use these principles to develop a model for assessing identity solutions based on the promise of user control over information. In contrast, other SSI-based assessments have either failed to describe their methodology[^pava], lacked extensive precision in their analysis[^bokkem], or did not explain how they derived the criteria for their system analysis[^omar]. To avoid similar shortcomings, our exercise is fully replicable, as we employed a quantitative method to select properties and a clustering technique to categorize principles. The quantitative analysis is then complemented by a qualitative analysis through a survey of experts participating in the ARES conference 2024 to refine our results.

At the same time, we have found only a handful of papers assessing digital identity systems based on SSI. We discussed them later. For the moment, to broaden our perspective, we examined how evaluation systems have been designed in divergent fields of study by analyzing three different examples: (1) open-source projects, (2) nutrient profiling scales, and (3) the Where-to-be-born Index (formerly the Country Quality-of-Life Index). The following review is not by any means comprehensive, and other rating systems exist in fields as diverse as university rankings, cost of living indices, and more. Although these are not directly relevant to digital identity, these systems all deal with a mix of qualitative and quantitative data analysis. Indeed, they include intangible aspects such as the political impacts of software, cultural aspects of food and products, individual freedom, and happiness. These are the types of concepts we aim to include in our SSI assessment model. Hence, our purpose for this literature review is to understand the rationale that grounds some of the decisions made by designers when creating a rating model. Simultaneously, we aim to determine if a rule of thumb exists for defining evaluation models.

*1. FOSS projects evaluation*
FOSS (Free and Open Source Software) projects are software initiatives where the source code is made publicly available for anyone to view, use, modify, and distribute.[^fortunato] Over the years, FOSS projects have become synonymous with projects that prioritize transparency, collaboration, and community-driven development. Some of the FOSS principles align with our SSI-derived properties. Notable examples of FOSS projects that follow these principles include Linux distributions, LibreOffice, GIMP, Blender, and VLC. Beyond these projects, there is a market of other free software vendors distributed online that do not respect the principles of community-driven development, openness, and transparency promoted by FOSS. Users could, therefore, be misled by the use of such software tools. It is crucial to establish a way to help users and protect software providers by distinguishing between projects that genuinely embrace the FOSS philosophy and those that do not.

Previous empirical studies have evaluated FOSS (Free and Open Source Software) projects using predefined criteria. These criteria were applied to assess individual projects.[^foss] However, much of this research focused on converting these criteria into measurable parameters. For instance, the OpenMRS project evaluates GitHub projects using metrics like the number of commits, the number of contributors, the reliability of contributors, and similar factors. A score-based rubric is then used to assign points to these parameters and calculate an overall score for a given open-source project.[^foss_rubric]

In contrast to this criteria-based approach, some projects prefer to determine the suitability of a GitHub project by using a set of questions addressed to a wide audience. Responses to these questions are assessed qualitatively.[^hunter] To organize this method, some researchers have suggested categorizing questions into three groups: project viability, approachability, and suitability. Scores for these categories provide an overall assessment of the GitHub project. A related but slightly different method was proposed by [^heidi], which categorized questions into two types: critical and non-critical (or secondary). Similarly, the work of [^evaluation_activity] proposed dividing evaluation principles (not questions) into two subclasses—mission-critical criteria (primary) and secondary criteria—each with its own set of associated questions.

The OpenBRR (Open Business Readiness Rating) proposes a more flexible method for evaluating projects. This method relies on gathering metrics and data across ten categories. Within each category, specific criteria and metrics are assessed. The evaluation process begins with selecting and weighting the criteria to be used. Weights are based on past research studies. In the next step, the criteria are evaluated, and a score for each category is obtained. Each category is then assigned a rating on a scale from 1 to 5. To calculate the total score, the weighted scores for standard and extended functionality items are summed. The flexibility of this model lies in its adaptability; depending on the intended use of the software, adopters can assign different weights to the categories. The overall project rating is derived by combining scores from both standard and extended functionality, along with the weighted categories. Importantly, not all categories carry the same weight. In certain scenarios, some categories may be excluded entirely from the final rating, allowing for a tailored evaluation process.

The Qualification and Selection of Open Source Software (QSOS) provides a structured and systematic approach to evaluating Free and Open Source Software (FOSS).[^evaluating_foss] QSOS calculates a final score through four iterative steps, which can be applied with varying levels of detail.
1. Defining Evaluation Criteria: In the first step, evaluation criteria are established across three primary axes: functionality, license compliance, and community dynamics.
2. Scoring: In the second step, each criterion is assigned a score between 0 and 2, based on responses from candidates participating in a survey.
3. Weighting: These scores are then weighted to reflect the specific context and requirements of the intended software use. Weights are project-dependent.
4. Selecting the Best Option: Finally, QSOS facilitates the selection of the most suitable software solution by comparing results across multiple candidate projects.

A dedicated QSOS tool visualizes the outcomes, often using charts for easier comparison. A popular visualization format is the Kiviat chart, which enables graphical comparisons of the evaluation results.

Another final example in the field of FOSS is the OSSpal project,[^Wasserman] which helps companies, government agencies, and other organizations find high-quality free and open-source software that suits their needs. Rather than relying solely on a numeric score, OSSpal incorporates curated selections of high-quality FOSS projects based on individual user reviews based on specific criteria. OSSpal operates a publicly available website where users can search by project name or category, and contribute ratings and reviews for projects.

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

*Discussion.*
After a detailed analysis of these three approaches to designing evaluation models, irrespective of the qualitative or quantitative methods proposed, we observed some shared methodologies across all of them. First, most works establish criteria to form the foundation of their models. Subsequently, research questions are formulated for each criterion, which then lead to the definition of parameters to be evaluated. There is some flexibility in combining qualitative and quantitative methods. Some works introduce qualitative methods following quantitative analyses, while others rely heavily on one of the two. However, qualitative analyses based on surveys to derive new concepts can introduce biases, depending on the type of questions asked, the audience targeted, and the sample examined. These are critical factors that should be explicitly addressed at the outset of any research; failure to do so can result in biased outcomes. After reviewing some of the existing literature, we decided to adopt a quantitative analysis approach, using surveys solely to refine our results. We further borrow the idea of rendering results on a Kiviat chart as proposed by the QSOS software project. Given that our chosen sample is smaller than those in other studies—partly because identity is still an emerging field of research—we consider the results of our survey only as a means to refine our conclusions. We discuss our model deeply in [Section 2](model/Model.md).

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

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^fortunato]: Fortunato, Laura, and Mark Galassi. "The case for free and open source software in research and scholarship." Philosophical Transactions of the Royal Society A 379.2197 (2021): 20200079.

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