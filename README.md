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

[Table 1](#table-1) shows the results of the analysis, including the similarities and differences in naming between defined sets of properties. Each Table row represents one property according to the similarity of the collected definitions, while differences in naming can be observed between different authors.

<a id="table-1"></a>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabella SSI</title>
    <style>
        table {
            font-size: 5px;
            border-collapse: collapse;
            width: 100%;
            table-layout: fixed;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
            text-align: left;
            width: 100px;
        }
        th {
            background-color: #d4f7d4;
            font-weight: bold;
        }
        td:first-child, th:first-child {
            position: sticky;
            left: 0;
            background-color: #d4f7d4;
            z-index: 1;
        }
        tr:nth-child(even) td:not(:first-child) {
            background-color: #f0f0f0;
        }
        tbody tr td:first-child {
            font-weight: bold;
        }
        td.check {
        background-color: #FFDAB9 !important;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Principles</th>
                <th>Tobin and Reed [1]</a></th>
                <th>Andrieu et al. [2]</th>
                <th>Ferdous et al. [3]</th>
                <th>Mühle et al. [4]</th>
                <th>Gilani et al. [5]</th>
                <th>Naik and Jenkins [6]</th>
                <th>Sheldrake [7]</th>
                <th>Toth and Kalman [8]</th>
                <th>eSSIF-Lab [9]</th>
                <th>ToIP [10]</th>
                <th>Sovrin [11]</th>
                <th>BkThDVr [12]</th>
                <th>Glöckler et al. [13]</th>
                <th>Pava-Díaz et al. [14]</th>
                <th>Satybaldy et al. [15]</th>
                <th>Stokkink and Pouwelse [16]</th>
                <th>Čučko et al. [17]</th>
                <th>Allen [18]</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Existence</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Control</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td> 
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Access</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Transparency</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Persistence</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Portability</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Interoperability</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Consent</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Protection</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Minimization</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td class="check">✔</td>
            </tr>
            <tr>
                <td>Self-generatable and independent</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Opt-in</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Opt-out</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Recoverable</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Simple</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Non-repudiatable</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Reliable</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Equivalent</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Autonomy</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Ownership</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Single Source</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Choosability</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Standard</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Cost</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Availability</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Disclosure</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Validity</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Freedom Information</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Participation</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Auditability</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Compliance</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Integrity</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Security</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Effectiveness</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Efficiency</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Manageability</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Privacy</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Trust</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Usability</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Identity Assurance</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Verification</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td class="check">✔</td>
                <td></td>
            </tr>
            <tr>
                <td>Counterfait Prevention</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Scalable</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Representation</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Equity and Inclusion</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Consistency</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Delegation</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Decentralization</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Identity Verification</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Secure Identity Transfer</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Secure Transactions</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="check">✔</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
</body>
</html>

*Table 1. Comparison of identified properties in various sources.*

[View the live HTML file](https://github.com/cristianlepore/Self-Sovereign-Identity/blob/main/Tables/Complete_table_SSI.html)

# References

[^lepore]: Lepore, Cristian, et al. "A Model For Assessing The Adherence of E-Identity Solutions To Self-Sovereign Identity." World Conference on Information Systems and Technologies. Cham: Springer Nature Switzerland, 2024.

[^cameron]: Cameron, Kim. "The laws of identity." Microsoft Corp 12 (2005): 8-11.

[^allen]: Allen, Christopher. "The path to self-sovereign identity." Life with Alacrity (2016).

[^cucko]: Čučko, Špela, et al. "Towards the classification of self-sovereign identity properties." IEEE access 10 (2022): 88306-88329.

[^ARF]: EUDI Wallet. Architecture and Rererence Framework v 1.4.1 https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/ Accessed on December 28, 2024.

[^badzek]: Badzek, Laurie, et al. "Ethical, legal, and social issues in the translation of genomics into health care." Journal of Nursing Scholarship 45.1 (2013): 15-24.

[^cushman]: Cushman, Reid, et al. "Ethical, legal and social issues for personal health records and applications." Journal of biomedical informatics 43.5 (2010): S51-S55.

[4] Mühle, Alexander, et al. "A survey on essential components of a self-sovereign identity." Computer Science Review 30 (2018): 80-86.

[6] Naik, Nitin, and Paul Jenkins. "Self-sovereign identity specifications: Govern your identity through your digital wallet using blockchain technology." 2020 8th IEEE International Conference on Mobile Cloud Computing, Services, and Engineering (MobileCloud). IEEE, 2020.

[8] Toth, Kalman C., and Alan Anderson-Priddy. "Self-sovereign digital identity: A paradigm shift for identity." IEEE Security & Privacy 17.3 (2019): 17-27.

[15] Satybaldy, Abylay, Mariusz Nowostawski, and Jørgen Ellingsen. "Self-sovereign identity systems: Evaluation framework." Privacy and Identity Management. Data for Better Living: AI and Privacy: 14th IFIP WG 9.2, 9.6/11.7, 11.6/SIG 9.2. 2 International Summer School, Windisch, Switzerland, August 19–23, 2019, Revised Selected Papers 14 (2020): 447-461.

[16] Stokkink, Quinten, and Johan Pouwelse. "Deployment of a blockchain-based self-sovereign identity." 2018 IEEE international conference on Internet of Things (iThings) and IEEE green computing and communications (GreenCom) and IEEE cyber, physical and social computing (CPSCom) and IEEE smart data (SmartData). IEEE, 2018.

[17] Čučko, Špela, et al. "Towards the classification of self-sovereign identity properties." IEEE access 10 (2022): 88306-88329.
