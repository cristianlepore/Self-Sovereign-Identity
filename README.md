# A Model To Assess Digital Identity Solutions

The purpose of this work is to extend the contribution of a model for assessing the adherence of e-Identity solutions to Self-Sovereign Identity (SSI) [^lepore] by addressing the following research questions:

*1. RQ1: What are the principles of Self-Sovereign Identity?*

*2. RQ2: Can we use these principles to assess any SSI system?*

[Section 1](definition/Definition.md) proposes a definition of Self-Sovereign Identity and addresses RQ1, while [Section 2](model/Model.md) leverages this definition to propose a model for assessing e-identity solutions. Finally, [Section 3](testing/Testing.md) delves into a testing stage where the model is tested against existing solutions in the field of identity.

Besides taking inspiration from past exercises that define SSI principles,[^allen][^ferdous][^toip][^toth] this work departs from past contributions because it is not limited to defining SSI but is instrumental in exploiting a model to assess identity solutions. On the other hand, other SSI-based assessments fail to describe the methodology[^pava] or lack precision in their analysis.[^bokkem][^omar] Additionally, we make our list of principles consistent through a questionnaire with experts participating at the ARES conference 2024.

Hereafter, we use the term principles for SSI interchangeably with the terms property and features. For the sake of clarity, they will all refer to the same concept. We often abbreviate the term Self-Sovereign Identity as SSI.

## Related works

We explored diffrent ways to lift answers for our research questions looking at similar exercises in the field of software projects, food ranking and index of quality of life. We took three examples to ground our work. The first was a method to evaluate Free and Open-Source  Software (FOSS) projects.

*Empirical studies on FOSS evaluation.* 
Several empirical studies have examined the evolution of FOSS systems, providing valuable insights into their growth patterns and development dynamics. The work in[^foss] defines general criteria and then solicits these criteria to forge specific ways to evaluate each project. OpenMRS provides a good example for evaluating each criterion for projects on GitHub. Projects on other forges will require different approaches to evaluate many of the criteria. Similarly, the Project Evaluation Rubric uses a score-based system to the same criteria to evaluate Free and open source projects.[^foss_rubric] In a similar way, the[^evaluation_activity] walks through of an evaluation of the Mifos project defining mission critical criteria (primary) and secondary criteria for evaluation, in order to for a project to be considered suitable for student participation.

The Onion model provides a structured view of the FOSS development community, emphasizing the roles and interactions within the community.[^onion] The evaluation of Free and Open Source Software (FOSS) using the Onion model provides a comprehensive understanding of the community-driven development process. The blog on[^foss_project] describes methods to evaluate the contribution of developers on free and open code.

Quantitative evaluation is proposed in OpenBRR (Open Business Readiness Rating) as an evaluation method proposed with the goal to provide an objective manner to assess community-driven projects, offering a way to measure the readiness of a project to be deployed in a business environment. The OpenBRR involves a multi-step evaluation process, that can be adjusted by the evaluator to adapt the assessment to the specific needs of the organization that wants to deploy the software under study. it is based on gathering metrics and factual data on ten categories. For each category, a set of criteria and metrics are proposed. These inputs are then weighted and each of the above introduced categories are given a rating that ranges from 1 to 5. Then, depending on the final usage the software will be given, adopters may weight these categories, obtaining an overall rating of the project. Hence, not all categories are weighted equally, and for some scenarios a category may not be considered at all for the final rating (in that case, its weight factor would be 0%). The first step in the process is to select and weigh the criteria to be use in the evaluation process. In the following step, each criteria is evaluated on its own. In order to obtain a total score for the functionality criteria, the total weights of the standard functionality items is summed up in W. Then the score for the assessed tool is obtained by adding all the scores, both from the standard and extended functionality, as T. Depending on the completeness of T related to W (in percentage), a final rating score is provided, using the cutoff values.



## Table of Contents

1. [Definition of Self-Sovereign Identity](definition/Definition.md)
2. [Model to assess e-identity solutions](model/Model.md)
3. [Testing](testing/Testing.md)

## References

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[^toth]: Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27. 

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